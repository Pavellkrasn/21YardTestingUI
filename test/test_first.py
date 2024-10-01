import re


import pytest
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://dev.21yard.com/")

    # Expect a title "to contain" a substring.
    expect(page.get_by_role("heading", name="Сервис поиска строительных подрядчиков")).to_be_visible()
    expect(page.get_by_role("button", name="Начать сейчас"))


    #Секция актуальные заявки
    expect(page.get_by_role("heading", name="Актуальные заявки"))
    expect(page.get_by_role("button", name="Поиск по городам"))
    expect(page.get_by_role("button", name="Поиск по видам работ"))
    expect(page.get_by_role("button", name="Поиск по регионам"))
    expect(page.get_by_role("button", name="Поиск по регионам"))
    expect(page.get_by_role("article", name=".flex flex-col w-full h-full"))

    # Находим элементы в секции заявки
    list_of_applications = page.locator(".flex.flex-col.w-full.rounded-16.bg-white").all()
    assert len(list_of_applications) == 10


def test_has_head(page:Page):
    page.goto("https://dev.21yard.com/")
    expect(page.locator("Поиск по регионам"))
    locator = page.locator("Поиск по регионам")
    locator.click()
    expect(page.get_by_role("heading", name="Поиск по городам"))



    # expect(page.get_by_role("paragraph", name="Более 5000 подрядчиков готовы откликнуться на Вашу заявку"))
    # page.get_by_role("button", name="Я подрядчик").click()
    # expect(page.get_by_role("heading", name="Ищите коммерческие строительные заказы по всей России")).to_be_visible()
    # expect(page.get_by_role("paragraph", name="Помощь в заключении договора и поддержка на всех стадиях реализации проекта"))


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
