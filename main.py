from selenium import webdriver


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
                inputs.send_keys('83986030106')
            elif inputs.get_attribute('value') == 'Male':
                inputs.click()



        self.chrome.find_element_by_id('checkbox1').click()
        self.chrome.find_element_by_id('checkbox2').click()
        self.chrome.find_element_by_id('checkbox3').click()

        # language
        self.chrome.find_element_by_class_name('ui-autocomplete-multiselect').click()
        self.chrome.find_element_by_link_text('Portuguese').click()
        # clica de nv no sexo pra fechar a aba do option
        self.chrome.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').click()

    # esse da pra fazer como vc disse eu acho
    # skills
    # for skills in self.chrome.find_elements_by_tag_name('select'):
    #     if skills.get_attribute('ng-ng-model')=='Skill':
    #         skills.click()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('http://demo.automationtesting.in/Register.html')
    chrome.inserirDados()
