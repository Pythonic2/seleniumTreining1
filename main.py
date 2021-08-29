from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#ng-model FirstName
class FireAuto:
    def __init__(self):
        
        self.options = webdriver.FirefoxOptions()
        self.navegador = webdriver.Firefox(
           
            options=self.options
        )
    def acessa(self,site):
      self.navegador.get(site)
    def inserirDados(self):
      
      for inputs in self.navegador.find_elements_by_tag_name('input'):
        if inputs.get_attribute('ng-model') == 'FirstName':
          inputs.send_keys('Igor')
        elif inputs.get_attribute('ng-model') == 'LastName':
          inputs.send_keys('Marinho')
          self.navegador.find_element_by_tag_name('textarea').send_keys('Rua 1')
        elif inputs.get_attribute('ng-model') == 'EmailAdress':
          inputs.send_keys('igormarinhosilva@gmail.com')
          #Phone
        elif inputs.get_attribute('ng-model') == 'Phone':
          inputs.send_keys('83986030106')
        elif inputs.get_attribute('value') == 'Male':
          inputs.click()

if __name__ == '__main__':
  navegador = FireAuto()
  navegador.acessa('http://demo.automationtesting.in/Register.html')
  navegador.inserirDados()
  