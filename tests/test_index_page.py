import time

import pytest
import pages


class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.main_page.open_main_page(page)
        print(str(pages.main_page.get_title_main(page)))
        time.sleep(10)



