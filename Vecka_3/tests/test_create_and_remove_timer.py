from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page, expect, sync_playwright

def test_add_and_remove_timer(page: Page):
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    first_button.click()

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(sp_button).to_be_visible()
