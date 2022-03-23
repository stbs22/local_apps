from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

def encontrar(driver):

  gimansio = driver.find_element_by_id("ctl00_ContentPlaceHolder1_wucReservas_GrdReservas_ctl00__6") #5

  try:

    #Hacer click en reservar  (clase : btn-Reservar)
    Reserva = gimansio.find_element_by_class_name("btn-Reservar")

    print("yessss")
    
    Reserva.click()
    
    boolean = False

  except Exception as e: 
    
    print("no",end="")

    boolean = True


  return boolean

URL = "https://pregrado.uai.cl/WebPages/Deporte/Reservas.aspx"
path = "chromedriver"

usuario = "eshernandez@alumnos.uai.cl"
contraseña = '6Tofilijones20193804%;'

driver = webdriver.Chrome(path)

#driver = webdriver.Chrome(ChromeDriverManager().install())

try:
  
  driver.get(URL)
  time.sleep(1)
  
  #Login
  driver.find_element_by_xpath('//*[@id="wucLogin1_tUsnNm"]').send_keys(usuario)
  driver.find_element_by_xpath('//*[@id="tUsrPaswd"]').send_keys(contraseña)
  driver.find_element_by_xpath('//*[@id="wucLogin1_LoginButton"]').click()

  time.sleep(1)
  driver.get(URL)
  
  while ( encontrar(driver) ):
   driver.refresh()

  # clases = list( driver.find_elements_by_class_name('rgRow') + driver.find_elements_by_class_name('rgAltRow'))
  # time.sleep(1)
  # deportes = []
  
  # for i in clases:

  #   lista = i.text.split(" ")

  #   deportes.append(lista[0])
  #   deportes = list( set(deportes) )

  #   print(lista[0] + ' ' + lista[len(i.text.split(" ")) - 1] )

  #   print('------------')

  # print(deportes)
  
  input()
  time.sleep(3)
  driver.close()

except Exception as e:

    print("Algo salió Mal:\n",e)

    driver.close()
