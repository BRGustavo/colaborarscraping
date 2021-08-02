from playwright.sync_api import sync_playwright
import re
from bs4 import BeautifulSoup
import os
from time import sleep


class NavegarColaborar:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.__password = password
        self.browser = None
        self.current_page = None
        self.playwright = sync_playwright().start()
        self.list_data = list()
        self.logged = False
        self.app = None

    @property
    def password(self):
        return ':P'

    def start_login(self):

        self.browser = self.playwright.chromium.launch()
        self.current_page = self.browser.new_page()
        self.current_page.goto(self.url)
        self.current_page.fill('#username', self.username)
        self.current_page.fill('#password', self.__password)
        self.clicar('text=Entrar')
        self.clicar('text=Entrar')

        if "login_error" not in self.current_page.url and self.current_page.url != self.url:
            self.logged = True
            return True
        else:
            self.close_page()
            return False

    def get_all_colaborar_info(self, ):
        if self.logged:
            materias_url = self.selectall('.pda .atividadeNome')

            lista_urls = list()
            for materia in materias_url:
                lista_urls.append(materia.get_attribute('href'))

            for ir_url in lista_urls:
                self.current_page.goto(f"{self.url}{ir_url}")
                materia_titulo = self.current_page.text_content('h2').strip()
                materia_titulo = re.sub(r'\([0-9]{1,100}\)', ' ', materia_titulo)
                materia_titulo = materia_titulo.strip()


                quadro_atividade = self.current_page.query_selector_all('.timeline-panel')
                self.wait_page(100)
                for info_quadro in quadro_atividade:
                    titulo_atividade = info_quadro.query_selector('.timeline-title').query_selector('small')\
                        .text_content().strip()
                    titulo_atividade = self.personalizar_atividade(materia_titulo, titulo_atividade)

                    periodo = info_quadro.query_selector('.text-muted').text_content().strip()

                    if 'Data da Prova' in periodo:
                        periodo = info_quadro.query_selector_all('.text-muted')[1].text_content().strip()

                    inicio_periodo, fim_periodo = self.date(periodo)
                    self.list_data.append({'Materia': materia_titulo, 'Atividade': titulo_atividade,
                                           'Inicio': inicio_periodo, 'Fim': fim_periodo})


    def clicar(self, item):
        self.wait_page(2)
        self.current_page.click(item)
        self.wait_page(10)

    def selectall(self, seletor):
        self.wait_page(100)
        lista = self.current_page.query_selector_all(seletor)
        self.wait_page(10)
        return lista

    def wait_page(self, time):
        self.current_page.wait_for_timeout(time)

    def close_page(self):
        self.current_page.close()
        self.playwright.stop()

    def date(self, periodo):
        values = re.findall(r'[0-9]{1,4}.[0-9]{1,4}.[0-9]{1,4}', periodo.strip())
        return values

    def personalizar_atividade(self, titulo_materia, atividade):
        titulo_materia = " - "+titulo_materia
        valor = atividade
        valor = valor.replace("Cw", "Conteúdo Web - ")
        valor = valor.replace("Aap", "Atividade - Aap")
        valor = valor.replace("Adg", "Atividade - Adg")
        valor = valor.replace("Leitura", "Livro Leitura ")
        valor = valor.replace(titulo_materia, "")
        return valor

    def transformar_html(self):
        HTML_File = open("config/index.html", 'r', encoding="utf-8")
        arquivo = HTML_File.read()
        HTML_File.close()

        objeto = BeautifulSoup(arquivo, "html.parser")
        finder = objeto.prettify()
        finder = finder.replace("lista_data=", f"lista_data = {self.list_data}")
        with open("./config/pag_teste.html", 'w', encoding="utf-8") as nova_pagina:
            nova_pagina.write(finder)
        sleep(10)

        self.current_page.goto(f"file://{os.getcwd()}/config/pag_teste.html")
        self.current_page.pdf(path="arquivo.pdf", prefer_css_page_size=True, display_header_footer=True,
                              print_background=True)
        os.remove("./config/pag_teste.html")

