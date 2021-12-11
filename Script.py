from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


username = input ("Enter username:  ")
password = getpass("Enter password:  ")


driver = webdriver.Chrome("C:\\Users\\Alex\\Desktop\\SeleniumHomeTask\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

def add_WorkShiftName(NewShiftName):
   
    NewShiftName = input("Input your New ShiftName: ")
    NewShiftName_txt = driver.find_element_by_id("workShift_name")
    NewShiftName_txt.send_keys(NewShiftName)


def selectWorkHours():
   WFrom = Select(driver.find_element_by_id("workShift_workHours_from"))
   WFrom.select_by_visible_text('06:00')
   
   WTo = Select(driver.find_element_by_id("workShift_workHours_to"))
   WTo.select_by_visible_text('18:00')



class EmpSelect():
    def add_Emps(self):
       employees = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/table/tbody/tr[2]/td[1]/select")
       SomeEmployees = Select(employees)
       
       SomeEmployees.select_by_index(1)
       btnSq5 = driver.find_element_by_id("btnAssignEmployee")
       btnSq5.click()
 
       SomeEmployees.select_by_index(5)
       btnSq6 = driver.find_element_by_id("btnAssignEmployee")
       btnSq6.click()
 
       SomeEmployees.select_by_index(15)
       btnSq7 = driver.find_element_by_id("btnAssignEmployee")
       btnSq7.click()

def CheckBoxPass():
    driver.find_element_by_id("ohrmList_chkSelectAll").click()
    time.sleep(5)

    Del = driver.find_element_by_id("btnDelete")
    Del.click()
    
    time.sleep(5)

    Dialog = driver.find_element_by_id("dialogDeleteBtn")
    Dialog.click()

    time.sleep(5)
 
       


username_txt = driver.find_element_by_id("txtUsername")
username_txt.send_keys(username)

password_txt = driver.find_element_by_id("txtPassword")
password_txt.send_keys(password)

login_button = driver.find_element_by_id("btnLogin")
login_button.submit()

link = driver.find_element_by_link_text("Admin")
link.click()

Job = driver.find_element_by_id("menu_admin_Job")
Job.click()

WShift = driver.find_element_by_id("menu_admin_workShift")


actions = ActionChains(driver)
actions.click(WShift)
actions.perform()

Add_button = driver.find_element_by_id("btnAdd")
Add_button.click()

time.sleep(10)

add_WorkShiftName(NewShiftName = 'ShiftName1')

time.sleep(5)

selectWorkHours()

time.sleep(10)

Semployees = EmpSelect()
Semployees.add_Emps()

time.sleep(5)

save_button = driver.find_element_by_id("btnSave")
save_button.click()
    

time.sleep(5)

CheckBoxPass()

time.sleep(3)

