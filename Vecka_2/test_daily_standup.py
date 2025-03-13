""" Story: Som en användare,
 vill jag se instruktioner för mötet "daily standup"
så att jag förstår vad meningen med mötet är.

Scenario:
1. Navigera till webbsidan https://lejonmanen.github.io/agile-helper/
2. Klicka på knappen med texten "First"
3. Klicka på knappen vars text innehåller "Start every day with Daily standup"
4. Kontrollera att ett <dialog> element visas på sidan, som innehåller en rubrik med texten "Daily standup"
5. Klicka på knappen "Start the standup: 10 minutes"
6. Vänta 2 sekunder
7. Bekräfta att time left börjar med siffran 9.
"""
import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button", name="First").click()
    page.get_by_role("button", name="Start every day with Daily").click()
    page.get_by_role("heading", name="Daily standup").click()
    page.get_by_role("button", name="Start the standup: 10 minutes").click()

    time.sleep(3)
    text = page.locator("span.framed").text_content()
    assert(text.startswith("9"))
    print("Visad text: ", text)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
