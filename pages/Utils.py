from abc import ABC, abstractmethod
from typing import Optional

from playwright.sync_api import Page

from config import Url


class BasePage(ABC):
    def __init__(self, page: Page,url:Url):
        self.page = page
        self.base_url = url


    @abstractmethod
    def navigate(self, url: Optional[str]):
        """Navigate to the specified URL"""
        self.page.goto(self.base_url.DOMAIN+url)

    @abstractmethod
    def is_loaded(self) -> bool:
        """Check if the page is fully loaded"""
        pass

    @abstractmethod
    def get_title(self) -> str:
        """Get the title of the current page"""
        pass

    @abstractmethod
    def press(self, locator: str):
        self.page.locator(locator).click()

    @abstractmethod
    def close(self):
        """Close the current page"""
        pass
