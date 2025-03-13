""" Story: Som en användare,
 vill jag se mötet "sprint planning" som utspelar sig första dagen på en sprint,
så att jag vet vad jag ska göra på mötet.

Scenario:
1. Navigera till webbsidan https://lejonmanen.github.io/agile-helper/
2. Klicka på knappen med texten "First"
3. Klicka på knappen vars text innehåller "Sprint planning"
4. Kontrollera att ett <dialog> element visas på sidan, som innehåller en rubrik med texten "Sprint planning"
"""

from playwright.sync_api import Page, expect, sync_playwright
import re

from pytest_playwright.pytest_playwright import browser

def test_view_sprint_planning(page: Page):
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    first_button.click()

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(sp_button).to_be_visible()

#    page.pause()
    # Klicka på den
    sp_button.click()

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(sp_heading).to_be_visible()

