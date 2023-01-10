from os import system
from time import sleep

import openai
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("user-data-dir=C:\\Users\\jeffe\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://web.whatsapp.com/')


openai.api_key = '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'


def enviar_mensagem( mensagem):
    '''chat = driver.find_element(By.XPATH , f"//span[@title='{numero}']")
    chat.click()'''
    while True:
        try:
            print('enviando msg...')
            firstChat = driver.find_element(By.XPATH, f'//*[@id="pane-side"]/div/div/div/div/div/div/div/div[1]/div/div')
            firstChat.click()
            break
        except Exception as e:
            print('erro na função enviar mensagem ')
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
            pass
            
    while True:
        try:
            
            botao_enviar = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
            botao_enviar.click()
            break
        except Exception as e:
            print(e)
            sleep(1)
            
    print(f"Mensagem enviada")
    
    
def obtermensagem():
    while True:
        try:
            global mensagem
            mensagem =  driver.find_element(By.CLASS_NAME, 'Hy9nV').text
            break
        except Exception as e:
            system('cls')
            print('aguardando mensagem...')
            sleep(5)
            pass
    
    
    #inteligencia artificial
    print('obtendo resposta da ia') 
    prompt = mensagem
    completion = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            temperature=0.5,
            )
            
    global response
    response = completion.choices[0].text
    print(response)
        
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
            pass


while True:
        obtermensagem()
        enviar_mensagem(response)
        arquivarChat()
        #input(f'mensagem:{mensagem}')
        sleep(2)
        system('cls')
        
        