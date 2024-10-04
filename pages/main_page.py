from idlelib.macosx import overrideRootMenu

from playwright.sync_api import Page
import config
from pages.Utils import BasePage


class MainPage(BasePage):


    _BUTTON_REGISTRATION_HEADLESS = "a[href='/registration'][type='button'][class*='md:!hidden']"
    _BUTTON_LOGIN_HEADLESS = "a[href='/login/'][type='button'][class*='md:!hidden']"
    _BUTTON_HEADLESS_MENU = "button[aria-haspopup='menu']"


    _MENU_ITEM_APPLICATIONS = "a[role='menuitem'][href='/applications']"
    _MENU_ITEM_MY_APPLICATIONS = "a[role='menuitem'][href='/myApplications/active']"
    _MENU_ITEM_TARIFFS = "a[role='menuitem'][href='/tariffs/responseApplication']"
    _MENU_ITEM_TEMPLATES = "a[role='menuitem'][href='/documents/templates']"
    _MENU_ITEM_HELP = "a[role='menuitem'][href='https://t.me/manager21yard']"

    _WRAPPER_HEADLESS_MENU ="#headlessui-portal-root"


    _TITLE_MAIN = "//h1[contains(@class,'sm:text-center')]"
    _TITLE_PARTNER_SECTOR = "//h2[contains(@class,'md:mb-4')]"

    _LIST_OF_COMPANIES_PARTNERS_LOGO = "//body/div/div/section/section/div/div[3]/div[1]/div"
    _LIST_OF_COMPANIES_PARTNERS_DOCUMENT = "//div//div//div//div//div[2]//div[1]//img"
    _LIST_OF_REGISTRATION_AND_APPLICATION_BUTTONS_ON_MAIN_PAGE = ("//a[contains(.//text(), 'Начать сейчас') "
                                                                  "or contains(.//text(), 'Попробовать сейчас')]")

    _LIST_OF_REGISTRATION_BUTTONS_ON_MAIN_PAGE = "a[href='/registration'][type='button']:not(.md\:\!hidden)"
    _LIST_OF_APPLICATIONS_BUTTONS_ON_MAIN_PAGE = "a[href='/applications'][type='button']"


    def navigate(self, url: str):
        pass

    def is_loaded(self) -> bool:
        pass

    def get_title(self) -> str:
        pass

    def close(self):
        pass

    def press(self):
        pass



    def open_main_page(self, page: Page) -> None:  # noqa
        page.goto(config.url.DOMAIN)

    def press_registration(self, page: Page):
        page.locator(self._BUTTON_REGISTRATION).click()

    def press_login(self, page: Page):
        page.locator(self._BUTTON_LOGIN).click()

    def press_headless_menu(self, page: Page):
        page.locator(self._BUTTON_HEADLESS_MENU).click()

    def get_title_main(self, page: Page) -> None:
        return page.locator(self._TITLE_MAIN).text_content()



