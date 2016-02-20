# vim: set fileencoding=utf-8 :

import logging

def login(browser, secret):
    logging.debug("Logging in...")
    browser.get("https://online.leumi-card.co.il/Registred/Transactions/ChargesDeals.aspx")

    username = browser.find_element_by_id("PlaceHolderMain_CardHoldersLogin1_txtUserName")
    password = browser.find_element_by_id("PlaceHolderMain_CardHoldersLogin1_txtPassword")

    username.send_keys(secret['data']['username'])
    password.send_keys(secret['data']['password'])

    browser.find_element_by_id("PlaceHolderMain_CardHoldersLogin1_btnLogin").click()

    # Ensure any banner pages are skipped
    browser.get("https://online.leumi-card.co.il/Registred/Transactions/ChargesDeals.aspx")

def fetch_month(browser, month):
    # TODO: Use a standard date value for month and convert to required format here.
    # TODO: Select a user-supplied card name (optional?)

    logging.debug("Getting transactions for month %s", month)
    # Filter by month
    # label = "חודש חיוב"
    label = u'\u05d7\u05d5\u05d3\u05e9 \u05d7\u05d9\u05d5\u05d1'
    browser.find_element_by_xpath(u'//*[@id="PlaceHolderMain_CD_CardsFilter1_ctl02_ddlActionType"]'+
        u'/option[text()="{0}"]'.format(label)).click()

    # Get relevant month
    browser.find_element_by_xpath(u'//*[@id="PlaceHolderMain_CD_CardsFilter1_ctl02_ddlMonthCharge"]'+
        u'/option[@value="{0}"]'.format(month)).click()

    # Show transactions for that month
    browser.find_element_by_id("PlaceHolderMain_CD_CardsFilter1_btnShow").click()

    # Download "Excel" file
    logging.debug("Downloading file")
    browser.find_element_by_id("PlaceHolderMain_CD_rptMain_tbl1_0_lvTransactions_0_btnExcel_0").click()

    # TODO: Download by hijacking the session and passing it to requests?
    # http://www.lshift.net/blog/2012/06/11/downloading-files-with-webdriver/
    # TODO: Find some way to rename this to xxxx-YYYY-MM.xls

    #  time.sleep(10) # Wait for download to complete
    logging.debug("Done")
