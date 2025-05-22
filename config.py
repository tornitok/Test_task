import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()


class Secrets:
    USER_NAME: Final[str] = os.getenv('STANDART_USER')
    PASSWORD: Final[str] = os.getenv('PASSWORD')
    TOKEN: Final[str] = os.getenv('TOKEN')

class URL:
    BASE_URL = 'https://www.saucedemo.com/'
    BASE_API_URL = 'https://airportgap.com/api/'
