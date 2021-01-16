import logging
import mysql.connector
from helpers.utils import get_environment
from configs.mysql_config import MysqlConfig


class MysqlModel(object):
    def __init__(self):
        self.infra_env = get_environment()
        self.instance_config = MysqlConfig().INSTANCE_CONFIG.get(self.infra_env, {})

    def get_connection(self):
        connection = mysql.connector.connect(host=self.instance_config.get("host"),
                                             port=self.instance_config.get("port"),
                                             user=self.instance_config.get("username"),
                                             password=self.instance_config.get("password"),
                                             )
        return connection

    def dml_query(self, query, query_params):
        connection = None
        try:
            connection = self.get_connection()
            cur = connection.cursor(dictionary=True)
            cur.execute(query, query_params)
            return cur.rowcount
        except Exception as err:
            logging.error(f'query error due to {err}')
            raise
        finally:
            if connection:
                connection.close()

    def search_query(self, query, query_params):
        connection = None
        try:
            connection = self.get_connection()
            cur = connection.cursor(dictionary=True)
            cur.execute(query, query_params)
            result = cur.fetchall()
            return result
        except Exception as err:
            logging.error(f'query error due to {err}')
            raise
        finally:
            if connection:
                connection.close()
