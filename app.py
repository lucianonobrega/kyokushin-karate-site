#importações
from flask import Flask, render_template, request
from config import mydb #importa a conexão com o banco de dados do arquivo config.py
#inicialização da aplicação
app = Flask(__name__)
#instancia a importação do banco de dados na variável banco e cria o cursor para a execução de comandos sql
banco = mydb
cursor = banco.cursor()
#abaixo estão todas as rotas do site
@app.route("/", methods=["GET"])
@app.route("/kyokushin-karate", methods=["GET"])
def kyokushin_karate():
    return render_template("kyokushin_karate.html")

@app.route("/aulas", methods=["GET"])
def aulas():
    return render_template("aulas.html")

@app.route("/nosso-dojo", methods=["GET"])
def nosso_dojo():
    return render_template("nosso_dojo.html")

@app.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template("cadastro.html")
#aqui é o local que são armazenados os dados do formulário e enviados para o banco de dados, caso tudo esteja ok
@app.route("/dados-formulario", methods=["POST"])
def dados_formulario():
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    idade = request.form["idade"]
    sexo = request.form["sexo"]
    telefone = request.form["telefone"]
    email = request.form["email"]
    try:
        if nome.isalpha() and sobrenome.isalpha(): #verifica se o nome e sobrenome são caracteres
            if idade.isnumeric() and idade > "0": #verifica se a idade é um número e se é positivo
                if 8 <= len(telefone) <= 9: #verifica se o comprimento do número de telefone está de acordo
                    if "@" and "." in email: #verifica se o email possui @ e .
                        comando = "INSERT INTO bw_database(nome, sobrenome, idade, sexo, telefone, email) VALUES(%s, %s, %s, %s, %s, %s)" #se tudo acima estiver ok, insere os dados no banco de dados
                        dados = (nome, sobrenome, idade, sexo, telefone, email)
                        cursor.execute(comando, dados)
                        banco.commit()
                        return render_template("cadastro.html", status="sucesso")
                else:
                    return render_template("cadastro.html", status="telefone_inválido")
    except Exception as E:
        print(f"Erro: {E}")
        return render_template("cadastro.html", status="Erro")

if __name__ == "__main__":
    app.run(debug=True)