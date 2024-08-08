from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://www.demoblaze.com/index.html")
time.sleep(5)

data = [
    {
        "Username":"DenisChasipantaITSQMET1",
        "Password": "Denis",
    }
]

informacion =[
    {
        "Nombre":"Denis Chasipanta",
        "Pais": "Ecuador",
        "Ciudad": "Quito",
        "TarjetaCredito": "4000123456789010",
        "Mes":"Agosto",
        "Año":"2024"
    }
]

#LOGUEARSE
'''login = driver.find_element(By.XPATH,'//*[@id="login2"]')
login.click()
time.sleep(1)

for item in data:
    campoUsername= driver.find_element(By.XPATH,"//*[@id='loginusername']")
    campoUsername.send_keys(item["Username"])
    campoPassword= driver.find_element(By.XPATH,"//*[@id='loginpassword']")
    campoPassword.send_keys(item["Password"])
    boton = driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]")
    boton.click()
    time.sleep(5)'''

#INGRESAR PRODUCTO N°1

Producto1Escojido = driver.find_element(By.XPATH,"//*[@id='tbodyid']/div[1]/div/div/h4/a")
Producto1Escojido.click()
time.sleep(1)
'''AgregarCarrito = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/a')
AgregarCarrito.click()
alert = driver.switch_to.alert 
alert.accept()
time.sleep(2)'''
Regresar = driver.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[1]/a")
Regresar.click()
time.sleep(1)

#INGRESAR PRODUCTO N°2

Producto2Escojido = driver.find_element(By.XPATH,"//*[@id='tbodyid']/div[7]/div/div/h4/a")
Producto2Escojido.click()
time.sleep(1)
'''AgregarCarrito = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/a')
AgregarCarrito.click()
alert = driver.switch_to.alert 
alert.accept()
time.sleep(2)'''
Regresar = driver.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[1]/a")
Regresar.click()
time.sleep(1)
CarritoCompras = driver.find_element(By.XPATH, '//*[@id="cartur"]')
CarritoCompras.click()
time.sleep(1)
Comprar = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
Comprar.click()
time.sleep(1)
for item in informacion:
    campoNombre= driver.find_element(By.XPATH,"//*[@id='name']")
    campoNombre.send_keys(item["Nombre"])
    campoPais= driver.find_element(By.XPATH,"//*[@id='country']")
    campoPais.send_keys(item["Pais"])
    campoCiudad= driver.find_element(By.XPATH,"//*[@id='city']")
    campoCiudad.send_keys(item["Ciudad"])
    campoTarjetaCredito= driver.find_element(By.XPATH,"//*[@id='card']")
    campoTarjetaCredito.send_keys(item["TarjetaCredito"])
    campoMes= driver.find_element(By.XPATH,"//*[@id='month']")
    campoMes.send_keys(item["Mes"])
    campoAño= driver.find_element(By.XPATH,"//*[@id='year']")
    campoAño.send_keys(item["Año"])
    botonCompras = driver.find_element(By.XPATH,'//*[@id="orderModal"]/div/div/div[3]/button[2]')
    botonCompras.click()
    time.sleep(5)
    alert = driver.switch_to.alert 
    alert.accept()

#CERRAR LA PÁGINA
driver.close()

