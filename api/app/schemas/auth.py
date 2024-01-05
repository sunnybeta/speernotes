from pydantic import BaseModel, ConfigDict, EmailStr, SecretStr


class LoginForm(BaseModel):
    user: str # Email or Password
    password: str


class SignupForm(BaseModel):
    username: str
    email: EmailStr
    password: str


class Token(BaseModel):
    id: str
    username: str
    email: str


class AuthSignupResponse(BaseModel):
    id: str
    username: str
    email: str
    token: str
