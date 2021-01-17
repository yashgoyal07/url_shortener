import logging
from models.mysql_model import MysqlModel
from helpers.mysql_queries import create_slink


class LinksController(object):
    def __init__(self):
        self.mysql_model_obj = MysqlModel()

    def create_slink(self,slink, long_link, customer_id):
        try:
            self.mysql_model_obj.dml_query(query=create_slink, query_params=(slink, long_link, customer_id))
        except Exception as err:
            logging.error(f'error from create_slink occured due to {err}')
            raise
