As a teammember 
I want to know how to do a sprint retrospective
So that I know how the team evaluates its work

Scenario:
1. Navigate to https://lejonmanen.github.io/agile-helper/
2. Verify that page title is Agile helper
3. Click the button "End the sprint by evaluating your work in Sprint retrospective"
4. Verify a text block with heading "Sprint retrospective" displays
5. Verify that the text 1. What should we start doing?" displays
6. Click the button "The sprint is complete"

# Buttons are implicitly tested that they exist
# In step 5, we check that some expected text displays. Not all text is verified, meaning that the test is more robust.
# (Downside is that not all text is verified.. pros and cons)