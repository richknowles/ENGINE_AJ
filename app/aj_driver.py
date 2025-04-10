from undetected_chromedriver import Chrome, ChromeOptions

def get_driver():
    options = ChromeOptions()
    options.add_argument('--user-data-dir=./user_data')
    options.add_argument('--profile-directory=Default')
    driver = Chrome(options=options)
    driver.get("https://web.whatsapp.com")
    return driver
