from models.mysql_model import MysqlModel
from helpers.mysql_queries import create_slink


class LinksController(object):
    def __init__(self):
        self.mysql_model_obj = MysqlModel()

    def create_slink(self, slink_name, slink, long_link, customerid):
        query = create_slink
        result = self.mysql_model_obj.dml_query(query=query, query_params=(slink_name, slink, long_link, customerid))

