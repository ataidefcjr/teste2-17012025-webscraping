# WebScraping usando Selenium 

Este é um projeto de teste para o estágio em uma empresa de energia, que utiliza Selenium para navegar em um site de datasets, realizar login, aplicar filtros e fazer download de informações sobre cursos. O script simula interações humanas como cliques, preenchimento de campos e a aplicação de filtros.


### Estrutura do Projeto
* bot_brasil_io.py: O script principal que realiza as operações de web scraping.
* .env: Arquivo de configuração com o nome de usuário e senha para login.

### Como Usar

##### Baixar o ChromeDriver
O ChromeDriver é necessário para controlar o navegador Google Chrome com o Selenium.

Baixe o ChromeDriver:

Vá até o site oficial do ChromeDriver.
Selecione a versão do ChromeDriver que corresponde à versão do seu Google Chrome. Se você tiver o Chrome versão 116.x, baixe o ChromeDriver 116.x.x.

##### Configurar o arquivo .env:

O conteúdo do arquivo deve ser o seguinte:

USERNAME=seu_usuario
PASSWORD=sua_senha

Neste teste ja deixei previamente configurado com minhas credenciais.

### Rodar o script:

Para rodar o script, execute o seguinte comando:

```sh
pip install -r requirements.txt
python bot_brasil_io.py

```

#### Interação com o script:

O script realizará o login no site e navegará até a página de datasets.
Será solicitado ao usuário que selecione filtros (universidade, campus, curso, grau e turno).
Após a aplicação dos filtros, o script tentará fazer o download do dataset.

Saída:

O script exibirá mensagens de sucesso ou erro conforme a execução.
O download será realizado para a pasta `downloads` na raiz do script python.


_____

<p style="text-align:center" dir="auto">
  <a href="#desafio1">Teste 2</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

<h2 id="desafio1" style="text-align:center;border-bottom:none">Teste 2</h2>

Neste teste, você precisa desenvolver uma aplicação para coletar dados do site <a href="https://brasil.io/home/" target="_blank">brasil.io</a>. Seguem as etapas que sua aplicação deve obrigatoriamente seguir ao ser executada:

1) Iniciar pela URL https://brasil.io/home/, simulando sempre a interação de um usuário real.
2) Realizar o login no site antes de qualquer consulta ou extração de dados.
3) Acessar o dataset “Cursos e notas de corte do PROUNI 2018” para os cursos.
4) Filtre pela Universidade, informada como entrada da aplicação.
5) Filtre pelo Nome do Campus, também informado como entrada da aplicação.
6) Filtre pelo Curso, informado como entrada da aplicação.
7) Filtre pelo Turno, informado como entrada da aplicação.
8) Filtre pelo Grau, informado como entrada da aplicação.
9) Baixe o arquivo CSV resultante do filtro.
10) Mova o arquivo CSV baixado para o diretório downloads/ na raiz da aplicação. Se esse diretório não existir, a aplicação deve criá-lo automaticamente.

### Requisitos dos Desafios:
1) Utilize a linguagem Python para desenvolver a solução.
2) No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3) Faça um fork do repositório.
4) A entrega deve ser realizada por meio de um pull request para o repositório original.
5) Envie seus commits para o GitHub faltando 5 minutos para o prazo final do teste. Não faça antes, pois você pode expor informações do seu teste para os demais participantes.
6) Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste.
7) A entrega deve ser realizada dentro do prazo estabelecido.
