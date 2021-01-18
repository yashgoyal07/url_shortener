import logging
from models.mysql_model import MysqlModel
from helpers.mysql_queries import create_slink, show_slink, find_long_link


class LinksController(object):
    def __init__(self):
        self.mysql_model_obj = MysqlModel()

    def create_slink(self,slink, long_link, customer_id):
        try:
            self.mysql_model_obj.dml_query(query=create_slink, query_params=(slink, long_link, customer_id))
        except Exception as err:
            logging.error(f'error from create_slink occured due to {err}')
            raise

    def show_slink(self, customer_id):
        try:
            result = self.mysql_model_obj.dql_query(query=show_slink , query_params=(customer_id,))
            return result
        except Exception as err:
            logging.error(f'error from show_slink occurred due to {err}')
            raise

    def find_long_link(self, slink):
        try:
            result = self.mysql_model_obj.dql_query(query=find_long_link, query_params=(slink,))
            return result
        except Exception as err:
            logging.error(f'error from find_customer occurred due to {err}')
            raise