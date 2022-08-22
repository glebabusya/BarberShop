from os import environ


if environ.get("BUILD_TYPE") == "DEV":
    from .develop import *
elif environ.get("BUILD_TYPE") == "PROD":
    from .production import *
else:
    print("Unknown settings, develop installed")
    from .develop import *
