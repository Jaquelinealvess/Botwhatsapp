from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Bom dia!! Passando para desejar um ótimo dia e informar que se você antecipar o pedido do mês que vem, eu posso conseguir um ótimo desconto. \n Clique aqui para maiores informações 'www.google.com'"
        self.grupos = ["Vendas", "Vendas2", "Vendas3"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <span dir="auto" title="Vendas" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Vendas</span>
        # <div tabindex="-1" class="p3_M1">
        # <span data-testid="send" data-icon="send" class="">
        print('teste')
        self.driver.get('https://web.whatsapp.com/')
        # enquanto não encontrar a tela carregada que corresponde o login
        while len(self.driver.find_elements_by_id("side")) < 1:
            time.sleep(1)

        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()
