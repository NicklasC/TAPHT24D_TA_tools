""" Story: Som en användare,
 vill jag se instruktioner för mötet "sprint retrospective"
så att jag förstår vad meningen med mötet är.

Scenario:
1. Navigera till webbsidan https://lejonmanen.github.io/agile-helper/
2. Klicka på knappen med texten "First"
3. Klicka på knappen vars text innehåller "Start off the sprint with sprint planning"
4. Kontrollera att en <dialog> element visas på sidan, som innehåller en rubrik med texten "Sprint planning"
5. Klicka på knappen "OK we're done. Start the sprint!"
6. Kontrollera att knappen "Start over" visas.
"""

from playwright.sync_api import Page, expect, sync_playwright
import re

def test_view_sprint_retrospective(page: Page):

    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Klicka på button "First"
    locator = page.get_by_role("button")

    last_button = locator.get_by_text("Last")
    last_button.click()

    # Hitta button med texten "Sprint planning"
    sprint_retrospective_button = page.get_by_role("button").get_by_text(re.compile("Sprint retrospective"))
    expect(sprint_retrospective_button).to_be_visible()

    #    page.pause()
    # Klicka på den
    sprint_retrospective_button.click()

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint retrospective")
    expect(sp_heading).to_be_visible()

    sprint_is_complete_button = page.get_by_role("button").get_by_text("The sprint is complete")
    expect(sprint_is_complete_button).to_be_visible()
    sprint_is_complete_button.click()

    page.pause()
    locator = page.get_by_role("button")
    start_over = locator.get_by_text("Start over")
    expect(start_over).to_be_visible()
    start_over.click()

    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    expect(first_button).to_be_visible()
