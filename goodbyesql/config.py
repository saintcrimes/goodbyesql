from typing import Any, Optional
from pydantic_settings import BaseSettings
from typing import List, Annotated, Any
from goodbyesql.registry import get_session
from pydantic import EmailStr

class GoodbyeSQLConfig(BaseSettings):
    user_model: Any
    username_field: str = Optional
    email: EmailStr = Optional

    

