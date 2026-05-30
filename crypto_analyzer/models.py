import os
import hashlib
import secrets
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

load_dotenv()

# используем sqlite, данные будут в файле crypto_analyzer.db
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///crypto_analyzer.db")

# создание движка для базы данных
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def hash_password(password: str) -> str: #хэширование пароля для безопасности
    # Генерируем случайную соль (16 байт в hex формате)
    salt = secrets.token_hex(16)
    # Хешируем соль + пароль через SHA256
    password_hash = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    # Возвращаем соль$хеш
    return salt + "$" + password_hash


def check_password(password: str, password_hash: str) -> bool: #проверка правильности пароля по хэшу
    try:
        # разделяем строку на соль и хэш
        salt, saved_hash = password_hash.split("$", 1)
    except ValueError:
        return False

    # хэшируем тот же пароль с солью
    current_hash = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    # Сравниваем с сохраненным хешем
    return current_hash == saved_hash


class User(Base): #модель пользователя в базе данных
    __tablename__ = "users"

    # id юзера (первичный ключ)
    id = Column(Integer, primary_key=True)
    # имя юзера (уникальное)
    username = Column(String(100), unique=True, nullable=False)
    # хэшированный пароль
    password_hash = Column(String(200), nullable=False)

    # связь с историей анализов
    analyses = relationship("AnalysisHistory", back_populates="user")


class AnalysisHistory(Base): #модель истории запросов или анализов
    __tablename__ = "analysis_history"

    # id записи (первичный ключ)
    id = Column(Integer, primary_key=True)
    # id пользователя (внешний ключ)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # символ криптовалюты (bitcoin, ethereum и т.д.)
    crypto_symbol = Column(String(20), nullable=False)
    # данные полученные с CoinGecko API (в json)
    crypto_data = Column(Text, nullable=False)
    # ответ от мистраля
    ai_result = Column(Text, nullable=False)
    # дата создания запроса
    created_at = Column(DateTime, default=datetime.now)

    # связь с пользователем
    user = relationship("User", back_populates="analyses")


def init_db() -> None: #создание таблиц базы данных если их нет
    Base.metadata.create_all(engine)


def get_session(): #создание сесси для работы с базой данных
    return SessionLocal()
