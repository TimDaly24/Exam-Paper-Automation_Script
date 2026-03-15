import os
from playwright.sync_api import sync_playwright

st = input("eYYYY1 or mYYYY2: ")

material_type = st[0]
if(material_type == "e"):
    material_type = "exampapers"
else:
    material_type = "markingschemes"

year = st[1:5]
paper = st[5]


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set True to hide browser
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    page.goto("https://www.examinations.ie/exammaterialarchive/")
    print("Page loaded")

    # Here we accept the terms and conditions
    page.wait_for_selector('input[type="checkbox"]')
    page.check('#MaterialArchive__noTable__cbv__AgreeCheck')



    # First select the button for select type
    page.wait_for_selector('select[name = "MaterialArchive__noTable__sbv__ViewType"]')
    page.select_option('select[name="MaterialArchive__noTable__sbv__ViewType"]', value = material_type)# Select material type, Papers/ Marking schemes

    # Select year
    page.wait_for_selector('select[name = "MaterialArchive__noTable__sbv__YearSelect"]')
    page.select_option('select[name="MaterialArchive__noTable__sbv__YearSelect"]', value = year)


    # Choose Examnination 
    page.wait_for_selector('select[name = "MaterialArchive__noTable__sbv__ExaminationSelect"]')
    page.select_option('select[name="MaterialArchive__noTable__sbv__ExaminationSelect"]', value = "lc")


    # Choose Subject 
    page.wait_for_selector('select[name = "MaterialArchive__noTable__sbv__SubjectSelect"]')
    page.select_option('select[name="MaterialArchive__noTable__sbv__SubjectSelect"]', value = "3")

    
    if (material_type == "e"):
        if (paper == "1"):
            paper_name = "Paper One / Higher Level (EV)"
            page.wait_for_selector("text=Click Here")
            page.locator("tr", has_text=paper_name).locator("a:has-text('Click Here')").first.click()

        else:
            paper_name = "Paper Two / Higher Level (EV)"
            page.wait_for_selector("text=Click Here")
            page.locator("tr", has_text=paper_name).locator("a:has-text('Click Here')").nth(2).click()
    else:
        paper_name = "Higher Level (EV)"
        page.wait_for_selector("text=Click Here")
        page.locator("tr", has_text=paper_name).locator("a:has-text('Click Here')").first.click()

    
    # Keep the browser open indefinitely so you can view the new tab
    print("Browser and tab will stay open. Press Ctrl+C to exit manually.")
    import time
    while True:
        time.sleep(1)  # just wait indefinitely




