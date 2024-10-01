import os
import environ
from pathlib import Path

PATH_DIR = Path(__file__).resolve().parent.parent.parent
PATH_DIR = os.path.join(PATH_DIR, '.env.dev')
env = environ.Env()
environ.Env.read_env(PATH_DIR)

DB_POSTGRES_HOST = env('DB_POSTGRES_HOST')
DB_POSTGRES_NAME = env('DB_POSTGRES_NAME')
DB_POSTGRES_USER = env('DB_POSTGRES_USER')
DB_POSTGRES_PASSWORD = env('DB_POSTGRES_PASSWORD')
DB_POSTGRES_PORT = env('DB_POSTGRES_PORT')


if None in [DB_POSTGRES_HOST, DB_POSTGRES_NAME, DB_POSTGRES_USER, DB_POSTGRES_PASSWORD, DB_POSTGRES_PORT]:
    raise Exception('Settings vars is not OS ENV')