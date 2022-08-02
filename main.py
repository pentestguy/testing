from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy_ip_port = "localhost:8081"

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

ser_obj=Service("D:\drivers\chromedriver.exe")

driver = webdriver.Chrome(service=ser_obj, desired_capabilities=capabilities)

driver.get("http://demo.testfire.net/login.jsp")
driver.find_element(By.ID,"uid").send_keys("admin")
driver.find_element(By.ID,"passw").send_keys("admin")
driver.find_element(By.NAME, "btnSubmit").click()

act_title=driver.title
exp_title="Altoro Mutual"

if act_title==exp_title:
    print("Login Test passed")
else:
    print("Login Test Failed")

driver.close()
