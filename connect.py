import this
import os
import psycopg2
import dotenv
import logging
from contentList import retorna_dados

#  Arquivo onde nosso log sera salvo apos rodarmos o script.
logging.basicConfig(filename="log_info.txt", level=logging.INFO)

dotenv.load_dotenv()


class DBConnet:
    def __init__(self, databse, user, passw, host):
        self.database = databse
        self.user = user
        self.password = passw
        self.host = host
        self.port = "5432"
        self.conn = self.connection()
        self.cursor = self.conn.cursor()
        self.count = 0

    def connection(self):
        return psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

# Função para realizarmos a consulta no banco, na linha 56 temos o comando SQL.
    def execQuery(self, cmd):
        self.cursor.execute(cmd)
        self.conn.commit()
        data = self.cursor.fetchall()
        return data

# Função para realizarmos o insert no banco. 
    def insertQuery(self, cmd):
        try:
            self.cursor.execute(cmd)
            self.conn.commit()
            count = self.cursor.rowcount
            print(count, "Record inserted successfully into mobile table")
            logging.info('Query realizada:  ' + cmd + '\n')

        except (Exception, psycopg2.Error) as error:
            logging.info(
                'FATAL ERROS: Failed to insert record into mobile table', error)
            print("Failed to insert record into mobile table", error)

# Lembre-se, para conseguir utilizar as funções da classe a cima precisara fazer referencia com "obj" a baixo.
obj = DBConnet("Nome do seu banco", "EX:postgres", "EX:postgres", "IP do seu banco")
'''
        *Outra maneira de realizar a conexão com o banco. 
        *Utilizando as variaveis criadas na função "connection", é preciso utilizar os modulos "psycopg2 e os" importados no inicio.
    obj = DBConnet(os.getenv('database'), os.getenv('user') , os.getenv('password') , os.getenv('host'))
'''


sql = 'SELECT  * FROM sua_tabela'

result = obj.execQuery(sql)
print(result)

data = retorna_dados()

for i in data:
    insert = "INSERT INTO sua_tabela(col1, col2, col3, col4, col5)VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(
        i, i, "Teste", "Teste", "Teste", "Teste")
        # O comando a baixo realizara o insert no banco
    # obj.insertQuery(insert)
    # print(insert)
    # print(i)

exit()