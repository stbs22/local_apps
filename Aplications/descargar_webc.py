from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request

URL = "https://webc.uai.cl/login/index.php"
path = "chromedriver"

usuario = "eshernandez@alumnos.uai.cl"
contraseña = '7Tofilijones20193804%;Parangari'

driver = webdriver.Chrome(path)
driver.set_window_size(1366,768)

try:
  
  driver.get(URL)
  time.sleep(1.5)

  driver.find_element(By.XPATH, value="//*[@id=\"username\"]").send_keys(usuario)
  driver.find_element(By.XPATH, value="//*[@id=\"password\"]").send_keys(contraseña)
  
  while(True):
    try:
      driver.find_element(By.XPATH, value="//*[@id=\"loginbtn\"]").click()
      break
    except Exception:
      continue
  
  print("Sesión iniciada")
  videoURL = ""
  num = 1
  while(True):

    input("Presione enter para registrar")
    nombre = "ECO_Clase_"+str(num)+".mp4"

    try:
      videoURL = driver.find_element(By.TAG_NAME, value="source").get_attribute("src")
      print("encontrado:\n"+str(videoURL)+"\nA nombre de: "+nombre)
      urllib.request.urlretrieve(videoURL, nombre)
      print("descargado")
      num = num + 1
      continue
    except Exception as e:
      print("Bad: "+str(e))
      print("Numero Actual: "+str(num))

  driver.close()

except Exception as e:

    print("Algo salió Mal:\n",e)

    driver.close()
