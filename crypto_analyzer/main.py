import sys
import json
from models import init_db, get_session, User, AnalysisHistory, hash_password, check_password
from services import get_crypto_data, analyze_with_mistral


def register_user(): #регистрация нового пользователя
    try:
        session = get_session()

        username = input("Введите логин: ").strip()
        password = input("Введите пароль: ").strip()

        if not username or not password:
            print("Логин и пароль не должны быть пустыми.")
            session.close()
            return

        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            print("Такой пользователь уже существует.")
            session.close()
            return

        user = User(username=username, password_hash=hash_password(password))
        session.add(user)
        session.commit()
        session.close()

        print("Регистрация успешна.")
    except Exception as e:
        print(f"Ошибка регистрации: {e}")


def login_user(): #авторизация пользователя

    try:
        session = get_session()

        username = input("Введите логин: ").strip()
        password = input("Введите пароль: ").strip()

        user = session.query(User).filter_by(username=username).first()

        if not user or not check_password(password, user.password_hash):
            print("Неверный логин или пароль.")
            session.close()
            return None

        session.expunge(user)
        session.close()

        print(f"Вы вошли как {username}.")
        return user
    except Exception as e:
        print(f"Ошибка входа: {e}")
        return None


def analyze_crypto(user): #основная функция для анализа криптовалюты
    try:
        crypto_options = {
            '1': 'bitcoin',
            '2': 'ethereum',
            '3': 'binancecoin',
            '4': 'cardano',
            '5': 'solana'
        }

        print("\nВыберите криптовалюту:")
        for key, value in crypto_options.items():
            print(f"{key}. {value.capitalize()}")

        choice = input("\nВаш выбор (ID): ").strip()
        crypto_id = crypto_options.get(choice, 'bitcoin')

        user_question = input("\nДополнительный вопрос (или Enter): ").strip()

        print("\nПолучаю данные с CoinGecko...")
        crypto_data = get_crypto_data(crypto_id)

        if not crypto_data:
            print("Не удалось получить данные. Проверьте интернет.")
            return

        print("Отправляю в Mistral AI...")
        ai_result = analyze_with_mistral(crypto_id, crypto_data, user_question)

        print("\n===== РЕЗУЛЬТАТ =====")
        print(ai_result)
        print("=====================\n")

        if ai_result.startswith("Не удалось") or ai_result.startswith("Ключ Mistral API не указан"):
            print("Запрос не сохранен.")
            return

        # сохранение в базу данных
        session = get_session()
        history = AnalysisHistory(
            user_id=user.id,
            crypto_symbol=crypto_id,
            crypto_data=json.dumps(crypto_data, ensure_ascii=False),
            ai_result=ai_result
        )
        session.add(history)
        session.commit()
        history_id = history.id  # получаем id запроса еще до закрытия сессии
        session.close()

        print(f"Сохранено в историю (ID: {history_id})")
    except Exception as e:
        print(f"Ошибка анализа: {e}")


def show_history(user): #история запросов пользователя
    try:
        session = get_session()

        records = (
            session.query(AnalysisHistory)
            .filter_by(user_id=user.id)
            .order_by(AnalysisHistory.created_at.desc())
            .all()
        )

        if not records:
            print("История пуста.")
            session.close()
            return

        print("\n===== ИСТОРИЯ =====")
        for record in records:
            print(f"Дата: {record.created_at}")
            print(f"Криптовалюта: {record.crypto_symbol}")
            print(f"Ответ: {record.ai_result[:500]}...")
            print("-------------------")
        print("===================\n")

        session.close()
    except Exception as e:
        print(f"Ошибка истории: {e}")


def user_menu(user): #самое основное меню
    while True:
        print("\n1. Анализировать криптовалюту")
        print("2. Посмотреть историю")
        print("3. Выйти из аккаунта")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            analyze_crypto(user)
        elif choice == "2":
            show_history(user)
        elif choice == "3":
            break
        else:
            print("Нет такого пункта меню.")


def main(): #главная функция
    print("=== CryptoAnalyzer ===")

    try:
        init_db()  # само создание таблиц в базе данных
        print("БД инициализирована")
    except Exception as error:
        print(f"Не удалось подключиться к БД: {error}")
        return

    while True:
        print("\n=== CryptoAnalyzer ===")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            user = login_user()
            if user:
                user_menu(user)
        elif choice == "3":
            print("Программа завершена.")
            break
        else:
            print("Нет такого пункта меню.")


if __name__ == "__main__":
    main()
