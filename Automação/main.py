from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

i = 0

service = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=service)

navegador.get('https://web.whatsapp.com/')

time.sleep(35)

mensagem = "Bom dia:). Teste de automação com Selenium !"

lista_contatos=["Eu Mesmo","Eu", "My Darling Teacher Totoro", "Tio Bolinho","Projeto Nossa Casita"]

qtd_contatos = len(lista_contatos)

for i in range(qtd_contatos):

    navegador.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
    time.sleep(1)
    navegador.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(lista_contatos[i])
    time.sleep(1)
    navegador.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
    time.sleep(1)
    navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(mensagem)
    time.sleep(1)
    navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    time.sleep(2)

time.sleep(10000)
