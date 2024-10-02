import pytest
import pages


class TestFooter:

    def test_main_search_button_must_have_the_text_google_search(self, page):
        pages.index_page.open_index_page(page)


