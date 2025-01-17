from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import random
import time

def load_env():
    """
    Carrega os dados do arquivo .env
    """
    with open (".env", 'r') as file:
        for line in file:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1) 
                os.environ[key] = value
    if not os.getenv("USERNAME") or not os.getenv("PASSWORD"):
        print("Usuario e/ou Senha não informados, encerrando.")
        exit()

def time_randomizer():
    """
    Faz uma pequena pausa aleatória entre 2 e 4 segundos, simulando uma interação humana.
    """
    time.sleep(random.randint(2, 4))
    return


def start_navigation():
    """
    Inicia a naveção usando Selenium e retorna o driver.
    """
    options = webdriver.ChromeOptions()

    current_directory = os.path.abspath(os.getcwd())
    download_directory = os.path.join(current_directory, "downloads")
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    preferences = {
        "download.default_directory": download_directory,  # Caminho onde o arquivo será salvo
        "download.prompt_for_download": False,  # Desativa o prompt de confirmação de download
        "directory_upgrade": True
    }

    options.add_experimental_option("prefs", preferences)


    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1024, 768)
    driver.get('https://brasil.io/home/')
    time_randomizer()
    return driver


def login(driver):
    """
    Faz o login no site, usando os dados obtidos de .env
    """
    sua_conta_button = driver.find_element(By.CLASS_NAME, "dropdown-trigger")
    sua_conta_button.click()
    time_randomizer()
    login_button = driver.find_element(By.XPATH, '//a[@href="/auth/login/"]')
    login_button.click()
    time_randomizer()
    user_name = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    login_input = driver.find_element(By.ID, "id_username")
    login_input.send_keys(user_name)
    password_input = driver.find_element(By.ID, "id_password")
    password_input.send_keys(password)
    login_form = driver.find_element(By.TAG_NAME, "form")
    login_form.submit()
    time_randomizer()

def navigate_to_cursos(driver):
    """
    Faz a navegação até a página de dataset solicitada.
    """
    dados_button = driver.find_element(By.XPATH, '//a[contains(text(), "Dados")]')
    dados_button.click()
    time_randomizer()
    datasets_button = driver.find_element(By.XPATH, '//a[@href="/datasets/"]')
    datasets_button.click()
    time_randomizer()
    search_box = driver.find_element(By.XPATH, '//input[@name="search"]')
    search_box.send_keys("PROUNI 2018")
    buscar_button = driver.find_element(By.XPATH, '//button[contains(text(), "Buscar")]')
    buscar_button.click()
    time_randomizer()
    titulo_dataset = driver.find_element(By.XPATH, '//h3[contains(text(), "PROUNI 2018")]')
    titulo_dataset.click()
    time_randomizer()
    cursos_link = driver.find_element(By.XPATH, '//a[b[contains(text(), "cursos")]]')
    cursos_link.click()
    time_randomizer()

def selection_input(element, limit):
    """
    Recebe um elemento select e printa para o usuário selecionar as opções desse elemento
    """
    select = Select(element)
    dict = {}

    for index, option in enumerate(select.options):
        dict[index] = {"value":option.get_attribute("value")}
        print(f"{index}. {option.get_attribute("value")}")
        if index >= limit:
            break
    
    selected = int(input("Escolha uma opção: "))

    return dict[selected]['value']

def filter_values(driver):
    """
    Passa todos os inputs a serem filtrados pela função selection_input
    """
    inputs = driver.find_elements(By.CSS_SELECTOR, '.input-field.col.s6')
    time_randomizer()

    # UNIVERSIDADE
    try: 
        universidade_selection = inputs[3].find_element(By.TAG_NAME, 'select')
        universidade_selecionada = selection_input(universidade_selection, 30)
        drop_box = inputs[3].find_element(By.TAG_NAME, 'input')
        drop_box.click()
        time_randomizer()
        universidade_lista = inputs[3].find_element(By.XPATH, f'//li[contains(span/text(), "{universidade_selecionada}")]')
        universidade_lista.click()
    except:
        print("Não foi possível filtrar por universidade, continuando.")
    
    # NOME DO CAMPUS
    try: 
        campus_selection = inputs[4].find_element(By.TAG_NAME, 'input')
        campus_selection.send_keys(input("Digite o nome do Campus: "))
    except:
        print("Não foi possível filtrar por campus, continuando.")    
    
    # NOME DO CURSO
    try: 
        time_randomizer()
        curso_selection = inputs[5].find_element(By.TAG_NAME, 'select')
        curso_selecionado = selection_input(curso_selection, 20)
        drop_box = inputs[5].find_element(By.TAG_NAME, 'input')
        drop_box.click()
        time_randomizer()
        curso_lista = inputs[5].find_element(By.XPATH, f'//li[contains(span/text(), "{curso_selecionado}")]')
        curso_lista.click()
    except:
        print("Não foi possível filtrar por curso, continuando.")

    # GRAU
    try: 
        time_randomizer()
        grau_selection = inputs[6].find_element(By.TAG_NAME, 'select')
        grau_selecionado = selection_input(grau_selection, 10)
        drop_box = inputs[6].find_element(By.TAG_NAME, 'input')
        drop_box.click()
        time_randomizer()
        grau_lista = inputs[6].find_element(By.XPATH, f'//li[contains(span/text(), "{grau_selecionado}")]')
        grau_lista.click()
    except:
        print("Não foi possível filtrar por grau, continuando.")

    # TURNO
    try: 
        time_randomizer()
        turno_selection = inputs[7].find_element(By.TAG_NAME, 'select')
        turno_selecionado = selection_input(turno_selection, 10)
        drop_box = inputs[7].find_element(By.TAG_NAME, 'input')
        drop_box.click()
        time_randomizer()
        turno_lista = inputs[7].find_element(By.XPATH, f'//li[contains(span/text(), "{turno_selecionado}")]')
        turno_lista.click()
    except:
        print("Não foi possível filtrar por turno, continuando.")



def download_results(driver):
    time_randomizer()
    filtrar_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    filtrar_button.click()
    time_randomizer()
   
    #Finaliza se não houver resultados
    try: 
        driver.find_element(By.CLASS_NAME, 'dataTables_empty')
        print("Nenhum resultado, encerrando o programa...")
        exit()
    except:
        pass
    try: 
        download_button = driver.find_element(By.XPATH, '//a[contains(text(), "Baixar resultado")]')
        download_button.click()
        print("Download salvo com sucesso")
    except:
        print("Não foi possível baixar o arquivo, encerrando...")

def main():
    driver = start_navigation()
    print("Iniciando")
    login(driver)
    print("Logado")
    navigate_to_cursos(driver)
    print("Entrando na página cursos")
    filter_values(driver)
    download_results(driver)
    print("Finalizado interação do bot")


if __name__ == '__main__':
    load_env()
    main()
