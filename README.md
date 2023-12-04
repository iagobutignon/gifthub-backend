# Executando o projeto

Para executar o backend é necessário a instalação e configuração do Docker.


### Passo a passo

##### (Opcional) Ambiente virtual
Criar um ambiente virtual para a instalação das dependências no Python.
```
virtualenv .venv
```

Ativar o ambiente virtual
```
source ./.venv/bin/activate
```

Atualizar a versão do pip dentro do ambiente virtual
```
python -m pip install --upgrade pip
```

Instalar os packages contidos no arquivo requirements.txt
```
pip install -r ./requirements.txt
```
##### Docker

Dentro da pasta do projeto, crie o container contendo o banco de dados postgres executando o comando abaixo
```
sudo docker-compose up -d 
```

Para localizar o endereço de IP do container que será utilizado na string de conexão execute o comando abaixo
```
sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres // <- "Nome do container"
```

No arquivo database.py, configure a string de conexão.
```
# Estrutura da string de conexão
# "postgresql://usuario:senha@endereco_ip:porta/nome_do_banco"
```
Exemplo:
```
def configure_database(app):
    global engine

    db_url = "postgresql://fabrico:fabrico123@172.21.0.2:5432/banco_do_fabrico"

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    engine = create_engine(db_url)
    database.init_app(app)

    with app.app_context():
        database.create_all()
```

##### Executando o sistema

Para iniciar o sistema execute o comando abaixo, dentro da pasta do projeto
```
python main.py
```