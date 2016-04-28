from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        
        #User wants to find NO3 estimates for different rain and
        #temp scenarios so goes to check out the Waterborne web-app
        self.browser.get("http://localhost:8000")
        
        #First thing the User sees is a login page
        self.assertIn("User:", self.browser.title)
        self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main(warnings="ignore")

