from config.settings.base import *

DEBUG = False
ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS").split(",")]

if "DATABASE_URL" in os.environ:
    DATABASES["default"] = os.getenv("DB_URL")
