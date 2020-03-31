import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def check_button_display(browser):
    browser.get(link)    
    time.sleep(30)
    def exist():
        try:
            browser.find_element_by_class_name("btn-add-to-basket")
        except:
            return False        
        return True
        
    assert exist(), 'Button does not exist'
    
