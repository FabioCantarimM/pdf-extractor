import os

import psycopg2
from sqlalchemy import create_engine


class RDSPostgreSQLManager:
    def __init__(
        self, db_name=None, db_user=None, db_password=None, db_host=None, db_port="5432"
    ):

        if (
            not self.check_environment_variables
            and db_name is None
            and db_user is None
            and db_password is None
            and db_host is None
        ):
            raise ValueError("As credenciais do Banco não foram fornecidas.")

        self.db_name = db_name or os.getenv("DB_NAME")
        self.db_user = db_user or os.getenv("DB_USER")
        self.db_password = db_password or os.getenv("DB_PASSWORD")
        self.db_host = db_host or os.getenv("DB_HOST")
        self.db_port = db_port

    def connect(self):
        try:
            connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port,
            )
            print("Conexão bem-sucedida ao banco de dados PostgreSQL.")
            return connection
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao banco de dados PostgreSQL: {e}")
            return None

    def execute_query(self, query):
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                connection.commit()
                connection.close()
                return result
            else:
                print("Não foi possível estabelecer a conexão com o banco de dados.")
                return None
        except psycopg2.Error as e:
            print(f"Erro ao executar a consulta SQL: {e}")
            return None

    def execute_insert(self, query, values):
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor()
                cursor.execute(query, values)
                connection.commit()
                cursor.close()
                connection.close()
                print("Inserção bem-sucedida.")
            else:
                print("Não foi possível estabelecer a conexão com o banco de dados.")
        except psycopg2.Error as e:
            print(f"Erro ao executar a inserção SQL: {e}")

    @staticmethod
    def check_environment_variables():
        if (
            not os.getenv("DB_NAME")
            or not os.getenv("DB_USER")
            or not os.getenv("DB_PASSWORD")
            or not os.getenv("DB_HOST")
        ):
            print("As variáveis de ambiente do banco não estão configuradas.")
            return False
        else:
            print("Variáveis de ambiente para o Banco foram configuradas corretamente.")
            return True

    def alchemy(self):
        self.engine = create_engine(
            f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        )
        return self.engine
