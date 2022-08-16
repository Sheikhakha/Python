from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("headless")
s = Service("D:\\Selenium\\driver\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chromeOptions)

driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.implicitly_wait(10)
print(driver.title)
driver.find_element(by=By.CSS_SELECTOR, value="a[href*='shop']").click()
products = driver.find_elements(by=By.CSS_SELECTOR, value="div[class*='h-100']")

for product in products:
    productNames = product.find_element(by=By.CSS_SELECTOR, value="div h4 a").text
    if productNames == 'iphone X':
        product.find_element(by=By.CSS_SELECTOR, value="div button").click()

checkoutButton = driver.find_element(by=By.CSS_SELECTOR, value="a[class*='btn-primary']")
driver.execute_script("arguments[0].click();", checkoutButton)
productCheckout = driver.find_element(by=By.CSS_SELECTOR, value="h4[class='media-heading'] a").text

assert "iphone X" == productCheckout

driver.find_element(by=By.CSS_SELECTOR, value="button[class*='btn-success']").click()
driver.find_element(by=By.ID, value='country').send_keys('ind')
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element(by=By.LINK_TEXT, value='India').click()
driver.find_element(by=By.XPATH, value='//body/app-root[1]/app-shop[1]/div[1]/app-checkout[1]/div[1]/div[2]/label[1]').click()
driver.find_element(by=By.CSS_SELECTOR, value="input[class*='btn']").click()

driver.get_screenshot_as_file("protocommercetest.png")
alertMessage = driver.find_element(by=By.CSS_SELECTOR, value="div[class*='alert']").text

assert "Success!" in alertMessage

driver.quit()









