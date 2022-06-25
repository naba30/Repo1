from selenium import webdriver
driver=webdriver.chrome("C:\\Users\\user\\OneDrive\\Desktop\\python\\chromedriver.exe")
driver.get("https:\\automationstepbystep.com")
print(driver.title)


