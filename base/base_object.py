import urllib.parse

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BaseObject:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def _is_visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))

    def _is_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(locator))

    def _is_not_clickable(self, locator: tuple[str, str]) -> bool:
        try:
            self.wait.until_not(ec.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def _is_present(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.presence_of_element_located(locator))

    def _is_not_visible(self, locator: tuple[str, str]):
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def click(self,locator: tuple[str, str], is_present=True) -> None:
        if is_present:
            self._is_clickable(locator).click()
        else:
            self._is_present(locator).click()

    def find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def send_keys(self, locator: tuple[str, str], value: str, is_visible=True) -> None:
        if is_visible:
            self._is_visible(locator).send_keys(value)
        else:
            self._is_present(locator).send_keys(value)

    def get_text(self, locator:tuple[str, str]) -> str:
        return self._is_visible(locator).text
