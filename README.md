# Colaborar EAD webscraping
O código acima tem por objetivo principal a criação de uma tabela informativa que apresenta dados disponíveis no painel
do aluno da faculdade UNOPAR. No arquivo são descritos as atividades do semestre atual e sua data de inicio e fim.
O programa visa facilitar o processo de programação do aluno, tendo como ação principal a organização de forma visual das
atividades que devem ser realizadas e em qual período estará disponível podendo ser transformado em um documento físico.

## Video demonstrativo
Clique na imagem abaixo para visualizar o video
[![Watch the video](https://i.ytimg.com/an_webp/o0sKw_8Qr8k/mqdefault_6s.webp?du=3000&sqp=CN3um4gG&rs=AOn4CLDrRh5DBHP0xqfcBQ_7kwqs_LFhuA)](https://youtu.be/o0sKw_8Qr8k)

## Instalação Linux
Até o presente momento, este código funciona apenas para sistema linux com python3 instalado

- Clone o repositório atual
`sudo git clone https://github.com/BRGustavo/colaborarscraping.git colaboraread`

- Crie um ambiente virtual (virtualenv)
`sudo virtualenv venv`

- Ative o ambiente virtual
`. venv/bin/activate`

- Instale as bibliotecas necessárias
`pip3 install -r requeriments.txt`

- Execute o programa
`python3 app.py`

