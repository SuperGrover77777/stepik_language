import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_on_the_site_contains_the_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    checking_the_button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert checking_the_button, "button not found"
