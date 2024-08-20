# Kyokushin Karate (Site)

Site de uma escola de karate kyokushin fictícia.

## Tecnologias

Para esse projeto, foram utilizadas as seguintes tecnologias: HTML, CSS, JavaScript, Python, Flask e MySQL.

## Índice
- [Instalação](#instalação)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação do Ambiente Virtual](#instalação-do-ambiente-virtual)
  - [Instalação de Dependências](#instalação-de-dependências)
  - [Configuração do Projeto](#configuração-do-projeto)
- [Uso e Funcionalidades](#uso-e-funcionalidades)
- [Imagens](#imagens)
- [Licença](#licença)
- [Contato](#contato)

## Instalação

### Pré-requisitos
Certifique-se de que as seguintes ferramentas estão instaladas no seu sistema:
- Python (versão 3.10 ou superior)
- MySQL

### Instalação do Ambiente Virtual
É importante criar um ambiente virtual para evitar qualquer tipo de conflito de outras bibliotecas ou módulos que já estejam instalados no seu computador.

Para criar um ambiente virtual, use o seguinte comando no seu terminal:
```bash
python -m venv nome_do_ambiente
```
Após a criação do ambiente virtual, será necessário ativá-lo:

## Windows
```bash
nome_do_ambiente\Scripts\activate
```
## macOS e Linux
```bash
source nome_do_ambiente/bin/activate
```
## Instalação de Dependências
Na pasta do projeto, existe um arquivo chamado requirements.txt. Nele, estão todas as bibliotecas necessárias para o projeto funcionar. Para instalá-las, execute o comando:
```bash
pip install -r requirements.txt
```
## Configuração do Projeto
Edite o arquivo config.py para ajustar as variáveis user e password com as credenciais do seu MySQL. Depois, importe o arquivo da tabela MySQL do projeto para o seu banco de dados.

## Uso e Funcionalidades
O site possui uma barra de navegação com acesso a cada seção. A página de cadastro permite que você preencha e envie dados diretamente para o MySQL.<br>
O contato na barra de navegação do site leva a pessoa para o footer no qual possui as informações de contato e redes sociais.  

## Imagens
Segue abaixo as imagens do projeto.<br>
Obs: As capturas das imagens foram feitas pela extensão do google chrome chamada GoFullPage. Essa extensão tira prints da tela e depois junta tudo em uma imagem só e por isso a imagem de fundo do site aparece repetida, mas o background no código está como "background-attachment: fixed;".<br>
Mesmo tentando outra abordagem como deixar scroll, ainda deu problema, mas isso não é um fator que irá prejudicar a apresentação do projeto, pois isso é problema apenas na captura de tela e não no site. Caso saiba de alguma forma de resolver isso, pode entrar em contato comigo.<br>
Para ver as imagens maiores, apenas clique na imagem que deseja ver.
<div align="center"><img width="400" height="400" src="/imagens_readme/imagem1.png"> <img width="400" height="400" src="/imagens_readme/imagem2.png"> <img width="400" height="400" src="/imagens_readme/imagem3.png"> <img width="400" height="400" src="/imagens_readme/imagem4.png"></div>

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato
LinkedIn: https://www.linkedin.com/in/luciano-nobrega-dev<br>
Email: lucianonobregadev@gmail.com
