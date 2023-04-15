import os

import environ

from .django import BASE_DIR

env = environ.Env()

DATABASES = {
    "default": env.db(
        "DATABASE_URL", default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}"
    )
}
