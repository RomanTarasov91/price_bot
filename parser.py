from time import sleep

from selenium import webdriver
# Импортируем классы для Chrome. Если у вас другой браузер - измените импорт.
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Если у вас установлен другой браузер - импортируйте нужный драйвер.
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import IEDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.opera import OperaDriverManager

# DJANGO_URL = 'http://158.160.172.156/'
# TEST_URL = 'https://ozon.ru/t/rRw3MDq'
# TEST_URL = 'https://twentysix.ru/blog/stuff/143819.html'
TEST_URL = 'https://admarginem.ru/product/teoriya-kino-kratkij-putevoditel/'
# TEST_URL = 'https://www.ozon.ru/product/zen-and-the-art-of-motorcycle-maintenance-dzen-i-iskusstvo-obsluzhivaniya-mototsiklov-kniga-na-1639529508/?utm_campaign=productpage_link&utm_medium=share_button&utm_source=smm'
# USERNAME = 'somany'
# PASSWORD = 'somany123'
PAUSE_DURATION_SECONDS = 2


def parse_price(admarginem_url):
    # Проверка и установка (или обновление) драйвера для Chrome через DriverManager.
    service = Service(executable_path=ChromeDriverManager().install())
    # Запуск веб-драйвера для Chrome.
    driver = webdriver.Chrome(service=service)

    # Открытие страницы по заданному адресу.
    driver.get(admarginem_url)
    # Развёртывание окна на полный экран.
    driver.maximize_window()
    # Здесь и далее паузы, чтобы рассмотреть происходящее.
    sleep(PAUSE_DURATION_SECONDS)

    driver.save_screenshot('screenshot.png')
    sleep(PAUSE_DURATION_SECONDS)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    pr = soup.find(class_='woocommerce-Price-amount amount')
    # json_script = soup.find('script', type='application/ld+json')

    price_text = pr.get_text(strip=True)
    # Удалить символ валюты и пробелы, если нужно
    price_value = price_text.split()[0]  # Получить первое слово
    print(price_value)

    # print(pr)

    # # Поиск первого поста на странице по классу.
    # first_post = driver.find_element(By.CLASS_NAME, 'card-text')
    # # Вывод текста найденного элемента в терминал.
    # print(first_post.text)
    # Закрытие веб-драйвера.
    driver.quit()

    return price_value