""" Story: Som en användare,
 vill jag se instruktioner för mötet "sprint review"
så att jag förstår vad meningen med mötet är.

Scenario:
1. Navigera till webbsidan https://lejonmanen.github.io/agile-helper/
2. Klicka på knappen med texten "Last"
3. Klicka på knappen vars text innehåller "End the sprint by evaluating your work in sprint review"
4. Kontrollera att en <dialog> element visas på sidan, som innehåller en rubrik med texten "Sprint review"
5. Klicka på knappen "OK we're done. Onwards to retrospective!"
6. Kontrollera att knappen "Start over" visas.
"""

from playwright.sync_api import Page, expect, sync_playwright
import re

def test_sprint_review(page: Page):

    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Klicka på button "First"
    locator = page.get_by_role("button")

    last_button = locator.get_by_text("Last")
    last_button.click()

    #page.pause()
    # Hitta button med texten "Sprint planning"
    sprint_planning_button = page.get_by_role("button").get_by_text(re.compile("Present your work to the"))
    expect(sprint_planning_button).to_be_visible()

    #    page.pause()
    # Klicka på den
    sprint_planning_button.click()

    # Finns rubriken "Sprint review"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint review")
    expect(sp_heading).to_be_visible()

    sprint_is_complete_button = page.get_by_role("button").get_by_text("OK we're done. Onwards to retrospective!")
    expect(sprint_is_complete_button).to_be_visible()
    sprint_is_complete_button.click()

    # page.pause()
    locator = page.get_by_role("button")
    start_over = locator.get_by_text("Start over")
    expect(start_over).to_be_visible()
    start_over.click()

    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    expect(first_button).to_be_visible()
