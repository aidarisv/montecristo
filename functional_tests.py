from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  
    #Жил был Вася, работающий аналитиком в какой-то компании. 
    #Однажды Вася захотел прокачаться в когорном анализе.
    #Он решил войти в Гугл, и ввести запрос - Когорный анализ 
    #И кликнул по одной из ссылок.


    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_home_page_title(self):  
        # В браузере Васи открылся сайт {по адресу ...},
        # В заголовке сайта Вася прочел - "Сайт Айдара Исенова",

        self.browser.get('http://localhost:8000')
       
        self.assertIn('Сайт Айдара Исенова', self.browser.title)  
        # self.fail('Finish the test!')  

    def test_home_page_header(self):
        # В шапке сайта написано "Айдар Исенов",

        browser = self.browser.get('http://localhost:8000')
        header = browser.find_elements_by_tag_name('h1')[0]
        self.assertIn('Айдар Исенов', header)



if __name__ == '__main__':  
    unittest.main()



''' 
    А под шапкой расположен блог со статьями,
    
    У каждоый статьи есть заголовок и один абзац текста
    Вася кликнул по заголовку и у него открылась страница с полный текстом статьи
    Прочитав статью Вася кликнул по тексту "Айдар Исенов" в шапке сайта
    И попал обратно на главную страницу.
'''