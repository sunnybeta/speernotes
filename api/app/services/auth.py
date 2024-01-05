import datetime
from datetime import timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from ..config.auth import SECRET, EXP, ALGORITHM
from ..config.logger import logger
from ..exceptions import Unauthorized
from ..models.user import UserModel
from ..models.user_pass import UserPass
from ..schemas.auth import LoginForm, SignupForm, Token, AuthSignupResponse
from ..services.servicemixin import ServiceMixin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService(ServiceMixin):

    def __init__(self, db: Session):
        self.__db = db

    @classmethod
    def hash(cls, password: str):
        return pwd_context.hash(password)

    @classmethod
    def verify(cls, plain: str, hashed: str):
        return pwd_context.verify(plain, hashed)

    @classmethod
    def encode(cls, data: dict, delta: timedelta | None = None) -> str:
        if delta:
            expire = datetime.datetime.now(datetime.UTC) + delta
        else:
            expire = datetime.datetime.now(datetime.UTC) + timedelta(minutes=EXP)
        data.update({'exp':expire})
        encoded_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)
        return encoded_token

    @classmethod
    def decode(cls, token: str) -> Token:
        try:
            decoded_token = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
            return Token(**decoded_token)
        except JWTError:
            raise Unauthorized

    def login(self, login_form: LoginForm):
        user = (
            self.__db.query(
                UserModel.id,
                UserModel.username,
                UserModel.email,
                UserPass.salt,
                UserPass.password,
            )
            .filter(or_(UserModel.username == login_form.user, UserModel.email == login_form.user))
            .outerjoin(UserPass, UserModel.id == UserPass.user_id)
            .first()
        )
        if not user:
            return None
        if self.verify(user.salt + login_form.password, user.password):
            data = Token(id=user.id, username=user.username, email=user.email)
            return self.encode(data.model_dump())

    def signup(self, signup_form: SignupForm):
         # Create User Data
        user_id = self.generate_id(prefix="usr")
        user = UserModel(id=user_id, username=signup_form.username, email=signup_form.email)
        
        # Create UserPass Data
        salt = self.generate_id("salt")
        hash = AuthService.hash(salt + signup_form.password)
        user_pass = UserPass(user_id=user_id, salt=salt, password=hash)

        # Write Object
        try:
            self.__db.add(user)
            self.__db.add(user_pass)
            self.__db.commit()
            data = Token(
                id=user_id,
                username=signup_form.username,
                email=signup_form.email,
            )
            token_str = self.encode(data.model_dump())
            return AuthSignupResponse(**data.model_dump(), token=token_str)
        except IntegrityError as e:
            self.__db.rollback()
            logger.error(e._sql_message())
            return None
        except Exception as e:
            self.__db.rollback()
            logger.error(repr(e))
            return None
