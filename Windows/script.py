## Importations
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,WebDriverException
import time
import os

## Variables
DELAY = 6
URL = "https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=fr-fr"

# Creation des options pour le driver
options = Options()
options.add_argument("user-data-dir="+os.getcwd()+"\\User Data")
# options.add_argument('--headless')

# Creation du driver
driver = webdriver.Chrome(chrome_options=options, executable_path="chromedriver.exe")

# Rediriger url du driver
driver.get(URL)

# Chargement de la page
time.sleep(DELAY)

# Recuperation du WebElement (recompense du jour) a cliquer
webelement = ui.WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".components-home-assets-__sign-content_---active---36unD3")))

# click sur le webelement
webelement.click()

# Chargement de la recuperation
time.sleep(DELAY)

# Fermeture du driver
driver.close()
