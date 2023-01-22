import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver="/Users/Islam/OneDrive/Desktop/chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://www.amazon.eg/?&tag=egtxabkgode-21&ref=pd_sl_7p2aq4fe2v_e&adgrpid=123528178741&hvpone=&hvptwo=&hvadid=542971874049&hvpos=&hvnetw=g&hvrand=2138165328266447413&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1028886&hvtargid=kwd-10573980&hydadcr=334_2546792&gclid=CjwKCAiA2rOeBhAsEiwA2Pl7Q1HXPmKt7RVPYe-GueGLWxE9yluY76jpiPth5RWZdJYfMSQGQ7SkDRoCV4QQAvD_BwE&language=en_AE")

search=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
search.send_keys("keybord")

search_button=driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
search_button.click()
time.sleep(5)

keybord=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div[1]/span/a/div/img')
keybord.click()
time.sleep(5)

addcart=driver.find_element(By.XPATH,'//*[@id="add-to-cart-button"]')
addcart.click()
time.sleep(5)

search_again=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
search_again.send_keys("mouse")

button=driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
button.click()
time.sleep(5)

mouse=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div[1]/span/a/div/img')
mouse.click()
time.sleep(5)

add_to_cart=driver.find_element(By.XPATH,'//*[@id="add-to-cart-button"]')
add_to_cart.click()
time.sleep(5)

last_search=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
last_search.send_keys("gaming pad")

b=driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
b.click()
time.sleep(5)

pad=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div[1]/span/a/div/img')
pad.click()
time.sleep(5)

cart=driver.find_element(By.XPATH,'//*[@id="add-to-cart-button"]')
cart.click()
time.sleep(5)

cart_button=driver.find_element(By.XPATH,'//*[@id="nav-cart-text-container"]')
cart_button.click()
time.sleep(10)