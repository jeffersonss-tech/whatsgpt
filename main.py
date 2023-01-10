from os import system
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("user-data-dir=C:\\Users\\jeffe\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://web.whatsapp.com/')


def enviar_mensagem( mensagem):
    '''chat = driver.find_element(By.XPATH , f"//span[@title='{numero}']")
    chat.click()'''
    while True:
        try:
            firstChat = driver.find_element(By.XPATH, f'//*[@id="pane-side"]/div/div/div/div/div/div/div/div[1]/div/div')
            firstChat.click()
            break
        except Exception as e:
            print('error!', e)
            sleep(1)
            pass
            
    while True:
        try:
            campo_mensagem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            campo_mensagem.send_keys(mensagem)
            break
        except Exception    as e:
            print('error!',e)
            sleep(1)
    botao_enviar = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
    botao_enviar.click()
    print(f"Mensagem enviada para ")
    
    
def obtermensagem():
    while True:
        try:
            global mensagem
            mensagem =  driver.find_element(By.CLASS_NAME, 'Hy9nV').text
            break
        except Exception as e:
            print('error!', e)
            sleep(1)
            pass
        
def arquivarChat():
    while True:
        try:       
            click3pontos = driver.find_element(By.XPATH, f'//*[@id="main"]/header/div[3]/div/div[2]/div/div/span')
            click3pontos.click()
            sleep(1)
            clickApagar= driver.find_element(By.XPATH, '//*[@id="app"]/div/span[4]/div/ul/div/div/li[7]/div')
            clickApagar.click()
            sleep(1)
            clickConfirmar = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]')
            clickConfirmar.click()
            break
        except Exception as e:
            print('Error!', e)
            sleep(1)



while True:
        obtermensagem()
        enviar_mensagem('"O sucesso não é a chave da felicidade. A felicidade é a chave do sucesso. Se você ama o que está fazendo, terá sucesso." - Albert Schweitzer')
        arquivarChat()
        #input(f'mensagem:{mensagem}')
        sleep(2)
        system('cls')
        
        