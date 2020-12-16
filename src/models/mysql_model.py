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
