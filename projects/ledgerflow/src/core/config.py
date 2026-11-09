from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    app_name : str = "LedgerFlow"
    debug : bool = False

settings = Settings()