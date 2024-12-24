from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uuid
from datetime import datetime, timedelta
from typing import List, Optional
import random
app = FastAPI(
    title="Authentication",
    root_path="/api-gateway/authentication-service",
    swagger_ui_parameters={"openapiUrl": "/api-gateway/authentication-service/openapi.json"}
)


# Mock Data (фейковая база данных)
fake_users_db = {
    uuid.uuid4(): {
        "email": "user@example.com",
        "username": "user1",
        "keycloak_id": uuid.uuid4(),
        "last_login": None,
        "status": "active"
    }
}

fake_roles_db = {
    uuid.uuid4(): {
        "name": "admin",
        "description": "Administrator role",
        "keycloak_role_id": uuid.uuid4()
    },
    uuid.uuid4(): {
        "name": "user",
        "description": "Regular user role",
        "keycloak_role_id": uuid.uuid4()
    },
    uuid.uuid4(): {
        "name": "manager",
        "description": "Manager role",
        "keycloak_role_id": uuid.uuid4()
    }
}

fake_user_roles_db = {
    uuid.uuid4(): uuid.uuid4()  # user_id -> role_id
}

fake_groups_db = {
    uuid.uuid4(): {
        "name": "group1",
        "keycloak_group_id": uuid.uuid4()
    }
}

fake_user_groups_db = {
    uuid.uuid4(): uuid.uuid4()  # user_id -> group_id
}

fake_sessions_db = {}


# Pydantic Models
class AuthRequest(BaseModel):
    token: str


class User(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)  # id генерируется автоматически
    email: str
    username: str
    last_login: Optional[datetime] = None
    status: str

    class Config:
        orm_mode = True


class Role(BaseModel):
    name: str
    description: str


class Session(BaseModel):
    user_id: uuid.UUID
    keycloak_session_id: uuid.UUID
    expires_at: datetime


# Вспомогательные функции
def verify_token(token: str) -> uuid.UUID:
    # Здесь обычно будет проверка с Keycloak API, но мы возвращаем mock ID
    if token == "valid-token":
        return list(fake_users_db.keys())[0]  # возвращаем ID первого пользователя из фейковой базы
    raise HTTPException(status_code=401, detail="Invalid token")


def get_user_by_id(user_id: uuid.UUID) -> User:
    user = fake_users_db.get(user_id)
    if user:
        return User(**user)  # Использование Pydantic для преобразования
    raise HTTPException(status_code=404, detail="User not found")


def get_random_role() -> Role:
    # Выбираем случайную роль
    role_id = random.choice(list(fake_roles_db.keys()))  # Выбираем случайный ID роли
    role = fake_roles_db[role_id]
    return Role(**role)


def create_session(user_id: uuid.UUID) -> Session:
    session_id = uuid.uuid4()
    expires_at = datetime.utcnow() + timedelta(hours=1)
    session = Session(user_id=user_id, keycloak_session_id=session_id, expires_at=expires_at)
    fake_sessions_db[session_id] = session
    return session


# Ручка для аутентификации
@app.post("/authenticate")
async def authenticate(auth_request: AuthRequest):
    user_id = verify_token(auth_request.token)  # Проверяем токен
    user = get_user_by_id(user_id)  # Получаем пользователя по ID
    role = get_random_role()  # Выбираем случайную роль для пользователя
    session = create_session(user_id)  # Создаем сессию для пользователя

    return {
        "user": user,
        "role": role,  # Возвращаем случайную роль
        "session": session
    }


# Для тестирования
@app.get("/users/{user_id}")
async def get_user(user_id: uuid.UUID):
    return get_user_by_id(user_id)
