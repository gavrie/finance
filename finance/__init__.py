import logging
import os

import hvac
from selenium import webdriver

def start():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

    logging.info("Connecting to Vault...")
    vault = hvac.Client(url='http://localhost:8200')
    vault.token = os.environ["VAULT_TOKEN"]

    logging.info("Starting browser...")
    #  browser = webdriver.PhantomJS()
    browser = webdriver.Chrome()

    return browser, vault
