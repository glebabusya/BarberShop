import os
from dotenv import load_dotenv

load_dotenv()

if os.getenv("BUILD_TYPE") == "DEV":
    from .develop import *
elif os.getenv("BUILD_TYPE") == "PROD":
    from .production import *
else:
    print("Unknown settings, develop installed")
    from .develop import *
