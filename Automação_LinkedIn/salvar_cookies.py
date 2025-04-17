import pickle
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
print("⏳ Faça login manualmente (30s)...")
sleep(30)

with open("cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("✅ Cookies salvos!")
driver.quit()