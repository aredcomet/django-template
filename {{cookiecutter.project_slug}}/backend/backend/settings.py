from .base import *  # noqa

INSTALLED_APPS = INSTALLED_APPS + [
    "django_extensions",
    "drf_generators",
]

LOG_DIR = BASE_DIR.joinpath("logs")
if not LOG_DIR.exists():
    os.mkdir(f"{LOG_DIR}")

# USE WHILE DEVELOPING
FILE_LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        "idealog": {"format": "%(asctime)s %(name)-30s %(levelname)-8s %(message)s"},
    },
    "handlers": {
        "default": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR.joinpath("logfile.log"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "standard",
        },
        "request_handler": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR.joinpath("django_request.log"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "standard",
        },
        "sql_query": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR.joinpath("sql_queries.log"),
            "maxBytes": 1024 * 1024 * 5,  # 5 MB,
            "backupCount": 5,
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {"handlers": ["default"], "level": "DEBUG", "propagate": True},
        "session": {"handlers": ["default"], "level": "DEBUG", "propagate": True},
        "sqlalchemy.engine": {
            "handlers": ["sql_query"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["request_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django.db": {"handlers": ["sql_query"], "level": "DEBUG", "propagate": False},
    },
}

LOGGING = FILE_LOGGING
