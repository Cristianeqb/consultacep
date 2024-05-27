# consultacep

# código em Python utilizando a biblioteca requests para fazer a consulta de um CEP usando a API do ViaCEP.



Constrói a URL para a consulta do CEP.

Faz uma requisição GET à API do ViaCEP.

Converte a resposta para um dicionário Python.

Verifica se o CEP é válido (a API retorna um campo 'erro' se o CEP não for encontrado).

Retorna os dados do endereço ou uma mensagem de erro caso o CEP não seja encontrado.

# Passo da Esteira CI/CD

criado arquivo Python para a consulta de CEP:consulta_cep.py
Contém a função consulta_cep que faz a consulta do CEP.

criado dependências:requirements.txt
Este arquivo deve listar todas as dependências do projeto

criado arquivo de teste para verificar o funcionamento da consulta de CEP:test_consulta_cep.py
Contém testes unitários utilizando a biblioteca unittest para verificar a funcionalidade da consulta de CEP.
test_cep_valido verifica se um CEP válido retorna os dados esperados.
test_cep_invalido verifica se um CEP inválido retorna None.

Configurado o Github Actions:.github/workflows/ci.yml
Configura o GitHub Actions para rodar a esteira de CI.
Especifica que a esteira deve ser acionada em push ou pull request na branch main.
Define um job chamado build que roda em um ambiente ubuntu-latest.
Realiza checkout do código, configura o Python, instala dependências e executa os testes.

Realizado Teste unitário

Criado arquivo para teste de integração: test_integration.py
Contém o teste de integração que verifica a resposta real da API ViaCEP

Configurado o GitHub Actions: github/workflows/ci-cd.yml
Configura o GitHub Actions para rodar a esteira de CI/CD
build-and-test: Job para instalar dependências, rodar testes unitários e de integração.
deploy: Job para deploy, que depende da conclusão bem-sucedida do job build-and-test.
