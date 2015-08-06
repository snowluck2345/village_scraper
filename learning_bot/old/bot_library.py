


def login():
    browser.driver.maximize_window()
    # Visit URL
    url = "https://www.tribalwars.net"
    browser.visit(url)
    browser.fill('user', 'dschreib')
    browser.fill('password', 'oblivion')

    time.sleep(random.random())
    # Find and click the 'search' button
    #button = browser.find_by_id('js_login_button')
    # Interact with elements
    #button.click()

    
    browser.execute_script("javascript:document.querySelector('.button_middle').click()")

    time.sleep(random.random())

    os.system("screencapture screen.jpg")

    time.sleep(random.random())

    browser.find_by_css('.world_button_active').mouse_over()
    browser.find_by_css('.world_button_active').click()


def captcha_check():
    if browser.is_text_present('splinter.readthedocs.org'):
        captcha = raw_input()
        browser.fill('code', captcha)
        print('\a')