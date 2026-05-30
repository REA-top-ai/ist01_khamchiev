import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

COINGECKO_API = "https://api.coingecko.com/api/v3"


def get_crypto_data(crypto_id: str, days: int = 30) -> list:
    #Получаем данные о криптовалюте с CoinGecko API
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }
    headers = {
        "User-Agent": "CryptoAnalyzerStudentProject/1.0"
    }

    try:
        response = requests.get(
            f"{COINGECKO_API}/coins/{crypto_id}/market_chart",
            params=params,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        prices = data.get("prices", [])
        volumes = data.get("total_volumes", [])

        recent_prices = prices[-7:]
        recent_volumes = volumes[-7:]

        result = []
        for i, (timestamp, price) in enumerate(recent_prices):
            date = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')
            result.append({
                "date": date,
                "price": price,
                "volume": recent_volumes[i][1] if i < len(recent_volumes) else 0
            })

        return result

    except Exception:
        return []


def build_prompt(crypto_id: str, crypto_data: list, user_question: str = "") -> str:
    #Формируем промт для Mistral
    data_text = json.dumps(crypto_data, ensure_ascii=False, indent=2)

    return f"""
Ты - эксперт по криптовалютам.
Проанализируй данные о {crypto_id.upper()}.

Вот данные из CoinGecko API за последние 7 дней:
{data_text}

{user_question if user_question else "Проанализируй и дай прогноз."}

Ответ на русском языке:
1. Текущая ситуация
2. Тренд цены
3. Рекомендации
4. Риски
Пиши кратко и понятно.
"""


def analyze_with_mistral(crypto_id: str, crypto_data: list, user_question: str = "") -> str:
    #Отправляем данные в Mistral AI через HTTP
    api_key = os.getenv("MISTRAL_API_KEY", "")

    if not api_key or api_key == "YOUR_MISTRAL_KEY":
        return "Ключ Mistral API не указан. Добавьте MISTRAL_API_KEY в файл .env."

    prompt = build_prompt(crypto_id, crypto_data, user_question)

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "system", "content": "Ты - эксперт по криптовалютам."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        result = response.json()
        return result['choices'][0]['message']['content']

    except Exception as e:
        return f"Ошибка: {str(e)}"
