import pytest
from pytest import fixture
from requests import Session
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api.endpoints import Airports, Distance
from config import URL
from pages.login_page import LoginPage
from pages.profile_page import InventoryPage


@pytest.fixture
def get_chrome_options():
    options = Options()
    return options

@pytest.fixture
def get_web_driver(get_chrome_options):
    driver = webdriver.Chrome(
        options=get_chrome_options,
        service=Service(
            ChromeDriverManager().install()
        )
    )
    return driver

@pytest.fixture
def login_page(get_web_driver):
    get_web_driver.get(URL.BASE_URL)
    yield LoginPage(get_web_driver)
    get_web_driver.quit()

@pytest.fixture
def profile_page(get_web_driver):
    get_web_driver.get(URL.BASE_URL)
    return InventoryPage(get_web_driver)


@fixture(scope='session')
def create_session():
    return Session()


@fixture(scope='session')
def airports(create_session):
    return Airports(session=create_session, endpoint=f"{URL.BASE_API_URL}/airports")

@fixture(scope='session')
def distance(create_session):
    def _create_distance(payload):
        return Distance(session=create_session, endpoint=f"{URL.BASE_API_URL}/airports/distance", distance_data=payload)
    return _create_distance