#!/usr/bin/env python

import finance
from finance import leumi_card

browser, vault = finance.start()

secret = vault.read("secret/leumicard")
leumi_card.login(browser, secret)

months = [
    "201510",
    "201511",
    "201512",
    "201601",
    "201602",
]

for month in months:
    leumi_card.fetch_month(browser, month)

# Wait for downloads to complete
import time
time.sleep(10)
