import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://mineuser:hello32U!@localhost:5432/mydatabase?options=-csearch_path=my_schema")
    SECRET_KEY = os.getenv("SECRET_KEY", "ea83ed9de25f56fcfc21969e934a11b03c4278f75f63daf95ba064f9c0bf044a")
    CACHE_TIMEOUT = int(os.getenv("CACHE_TIMEOUT", 300))  # in seconds
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

config = Config()