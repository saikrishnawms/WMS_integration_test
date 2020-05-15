import unittest
from selenium import webdriver
import time
from pathlib import Path
import wheel

class MyTestCase(unittest.TestCase):

    def test_create_new_user_with_G4(self):
        path = "/usr/bin/chromedriver"
        driver = webdriver.Chrome(executable_path=path)
        driver.get("http://test.saikrishnacoldstorage.in/lot")
        driver.find_element_by_name("name").send_keys("Nishi")
        driver.find_element_by_name("fatherName").send_keys("Shrivastava")
        driver.find_element_by_name("address").send_keys("Bartiningelle")
        driver.find_element_by_name("phoneNumber").send_keys("8380083195")
        driver.find_element_by_name("numberOfBags").send_keys(100)
        driver.find_element_by_name("averageWeight").send_keys(50)
        driver.find_element_by_name("numberOfEmptyBagsGiven").send_keys(9)
        driver.find_element_by_xpath("/html/body/div/div/div/form/div/div[9]/fieldset/div/label[1]/span[1]/span[1]/input").click()
        driver.find_element_by_name("palledariPaid").click()
        driver.find_element_by_name("comments").send_keys("test")
        driver.find_element_by_class_name("MuiButton-label").click()
        driver.close()
        driver.quit()


    def test_create_new_user_with_Gola(test_navigate_into_Url):
        path = "/usr/bin/chromedriver"
        driver = webdriver.Chrome(executable_path=path)
        driver.get("http://test.saikrishnacoldstorage.in/lot")
        driver.find_element_by_name("name").send_keys("Nishi")
        driver.find_element_by_name("fatherName").send_keys("Shrivastava")
        driver.find_element_by_name("address").send_keys("Bartiningelle")
        driver.find_element_by_name("phoneNumber").send_keys("8380083195")
        driver.find_element_by_name("numberOfBags").send_keys(100)
        driver.find_element_by_name("averageWeight").send_keys(50)
        driver.find_element_by_name("numberOfEmptyBagsGiven").send_keys(9)
        driver.find_element_by_xpath("/html/body/div/div/div/form/div/div[9]/fieldset/div/label[2]/span[1]/span[1]/input").click()
        driver.find_element_by_xpath("/html/body/div/div/div/form/div/div[10]/fieldset/div/label[2]/span[1]").click()
        driver.find_element_by_name("comments").send_keys("test")
        driver.implicitly_wait(20)
        driver.find_element_by_class_name("MuiButton-label").click()
        driver.close()
        driver.quit()


    def test_create_new_user_with_other(self):
        path = "/usr/bin/chromedriver"
        driver = webdriver.Chrome(executable_path=path)
        driver.get("http://test.saikrishnacoldstorage.in/lot")
        driver.find_element_by_name("name").send_keys("Nishi")
        driver.find_element_by_name("fatherName").send_keys("Shrivastava")
        driver.find_element_by_name("address").send_keys("Bartiningelle")
        driver.find_element_by_name("phoneNumber").send_keys("8380083195")
        driver.find_element_by_name("numberOfBags").send_keys(100)
        driver.find_element_by_name("averageWeight").send_keys(50)
        driver.find_element_by_name("numberOfEmptyBagsGiven").send_keys(9)
        driver.find_element_by_xpath("/html/body/div/div/div/form/div/div[9]/fieldset/div/label[3]/span[1]").click()
        driver.find_element_by_xpath("/html/body/div/div/div/form/div/div[10]/fieldset/div/label[2]/span[1]").click()
        driver.find_element_by_name("comments").send_keys("test")
        driver.implicitly_wait(20)
        driver.find_element_by_class_name("MuiButton-label").click()
        driver.close()
        driver.quit()



    def test_title(self):
        path = "/usr/bin/chromedriver"
        driver = webdriver.Chrome(executable_path=path)
        driver.get("http://test.saikrishnacoldstorage.in/lot")
        assert 'React App' == driver.title
        driver.close()


    def test_with_print(self):
        path = "/usr/bin/chromedriver"
        driver = webdriver.Chrome(executable_path=path)
        driver = webdriver.Chrome(executable_path="/Users/anubhavsrivastava/IdeaProjects/wms-app/chromedriver")
        driver.get("http://test.saikrishnacoldstorage.in/showLot/5")
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[13]/button").click()
        driver.close()



    def test_with_result(self):
        path = "/usr/bin/chromedriver"
        driver = webdriver.Chrome(executable_path=path)
        driver.get("http://test.saikrishnacoldstorage.in/showLot/5")
        averageWeight = driver.find_element_by_xpath("/html/body/div/div/div/div/div[8]")
        print(averageWeight.text)
        assert "5050 KG" in averageWeight.text
        lotNumber = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]")
        print(lotNumber.text)
        assert "5 / 100" in lotNumber.text
        driver.close()
        driver.quit()



if __name__ == '__main__':
    unittest.main()
