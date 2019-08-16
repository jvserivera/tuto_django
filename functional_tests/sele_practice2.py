import unittest, os
from selenium import webdriver


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new G.Chrome session
        # dir = os.path.dirname(__file__)

        chrome_driver_path = "C:/Users/JRM3998/PycharmProjects/tuto_django/Drivers/chromedriver.exe"
        inst.driver = webdriver.Chrome(chrome_driver_path)
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get("http://www.google.com/")
        inst.driver.title

    def testa_search_by_text(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("Selenium Webdriver interview questions")
        self.search_field.submit()
        lists = self.driver.find_elements_by_class_name("r")
        self.assertEqual(15, len(lists))

    def testb_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        # enter search keyword and submit
        self.search_field.clear()
        self.search_field.send_keys("Python class")
        self.search_field.submit()
        # get the list of elements which are displayed after the search
        # currently on result page using find_elements_by_class_name method
        list_new = self.driver.find_elements_by_class_name("r")
        self.assertEqual(14, len(list_new))

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
