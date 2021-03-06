from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# ng-model FirstName

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('user-data-dir= C:/Users/igor/Documents/GitHub/seleniumTreining1/Perfil')

        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)
        self.chrome.maximize_window()
    #
    def inserirDados(self):
        for inputs in self.chrome.find_elements_by_tag_name('input'):
            if inputs.get_attribute('ng-model') == 'FirstName':
                inputs.send_keys('Igor')
            elif inputs.get_attribute('ng-model') == 'LastName':
                inputs.send_keys('Marinho')
                self.chrome.find_element_by_tag_name('textarea').send_keys('Rua 1')
            elif inputs.get_attribute('ng-model') == 'EmailAdress':
                inputs.send_keys('igormarinhosilva@gmail.com')
            # Phone
            elif inputs.get_attribute('ng-model') == 'Phone':
                inputs.send_keys('8386030106')
            elif inputs.get_attribute('value') == 'Male':
                inputs.click()


    def check(self):
        self.chrome.find_element_by_id('checkbox1').click()
        self.chrome.find_element_by_id('checkbox2').click()
        self.chrome.find_element_by_id('checkbox3').click()

        # language
        self.chrome.find_element_by_class_name('ui-autocomplete-multiselect').click()
        self.chrome.find_element_by_link_text('Portuguese').click()
        # clica de nv no sexo pra fechar a aba do option
        self.chrome.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').click()

        # skills

    def skills(self):
        for skills in self.chrome.find_elements_by_tag_name('option'):
            if skills.get_attribute('value')=='Python':
                skills.click()

        # COUNTRY

    def paises(self):

        for country in self.chrome.find_elements_by_tag_name('option'):
            if country.get_attribute('value') == 'Brazil':
                country.click()

        procurarPaises = self.chrome.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span/span[2]')
        procurarPaises.click()
        campoPesquisa = self.chrome.find_element_by_class_name('select2-search__field')
        campoPesquisa.click()
        campoPesquisa.send_keys('Sout',Keys.ENTER)

    def idade(self):
        #ano nascimento
        ano = self.chrome.find_element_by_id('yearbox')
        ano.click()
        ano.send_keys('1996',Keys.ENTER)


        # mes
        mes = self.chrome.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[11]/div[2]/select')
        mes.click()
        mes.send_keys('jul',Keys.ENTER)

        # dia

        dia = self.chrome.find_element_by_id('daybox')
        dia.click()
        dia.send_keys('29',Keys.ENTER)

    def login(self):
        # # senha
        password = self.chrome.find_element_by_id('firstpassword')
        password.click()
        password.send_keys('37192541aaSS@')
        #
        # # confirmasenha
        password = self.chrome.find_element_by_id('secondpassword')
        password.click()
        password.send_keys('37192541aaSS@')

    def uparfoto(self):

        # upload foto
        for input in self.chrome.find_elements_by_id('imagesrc'):
            if input.get_attribute('type')=='file':
                input.send_keys('C:/Users/igor/Documents/GitHub/seleniumTreining1/python.jfif')
        self.chrome.find_element_by_id('submitbtn').click()
        sleep(2)
        self.chrome.find_element_by_link_text('WebTable').click()
    def quite(self):
        self.chrome.quit()

    def executatdo(self):
        chrome.inserirDados()
        chrome.check()
        chrome.skills()
        chrome.paises()
        chrome.idade()
        chrome.login()
        chrome.uparfoto()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('http://demo.automationtesting.in/Register.html')
    chrome.executatdo()

