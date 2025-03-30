import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.gp.se/")
    page.get_by_role("button", name="Godkänn alla").click()
    page.get_by_role("link", name="Västsverige•Över 40 i storbrå").click()
    page.get_by_test_id("article-headline_heading").get_by_text("Storbråk i Halmstad – flera").click()

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     test_run(playwright)