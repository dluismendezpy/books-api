from decouple import config

SERVER_PORT: int = config("SERVER_PORT", default=8000, cast=int)
TEMPLATES_DIR: str = "templates"
