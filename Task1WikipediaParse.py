from selenium import webdriver
 
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(executable_path=r'.\geckodriver.exe', options=options)

driver.get("https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту")

class AnimalsList():
     def __init__(self):
         self.list = dict()
         
     def addLitera(self, _litera):
         if (_litera in self.list) == False:
             self.list[_litera] = []
             
     def addAnimal(self, _litera, _name):
         self.list[_litera].append(_name)
         
     def printAllAnimalsCount(self):
         for i in self.list.keys():
             print(str(i) + ": " + str(len(self.list[i])))
             
animals_list = AnimalsList()
print("-----------------------------------------------------------------------------------------------------------")
litera = -1
pages = 0
#for i in range(10): # цикл по страницам
while litera != 'A':
    categories = driver.find_element_by_css_selector('.mw-category')
    categoty_group = driver.find_elements_by_class_name('mw-category-group')
    for j in range(len(categoty_group)): # цикл по группам внутри страницы
        elements = categoty_group[j].find_elements_by_tag_name('li')
        litera = str(categoty_group[j].find_element_by_tag_name('h3').text)
        if litera == 'A':
            break
        animals_list.addLitera(litera)
        for k in range(len(elements)): # цикл по названиям животных
            animals_list.addAnimal(litera, elements[k].text)
            print("Page: " + str(pages) + " Category: " + str(j) + " Animal: " + str(k))
    next_page_link = driver.find_element_by_link_text('Следующая страница')
    next_page_link.click()
    pages += 1
    print("-----------------------------------------------------------------------------------------------------------")    

animals_list.printAllAnimalsCount()
driver.quit()


