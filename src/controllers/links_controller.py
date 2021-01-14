import logging
from models.mysql_model import MysqlModel
from helpers.utils import short_link_generator
from helpers.mysql_queries import create_short_link

class LinksController(object):
    def __init__(self):
        self.mysql_model_obj = MysqlModel()

    def create_short_link(self, llink, userid):
        query = create_short_link
        slink = short_link_generator()
        error = ""
        try:
            self.mysql_model_obj.insert_query(query=query, query_params=(slink, llink, userid))
        except Exception as err:
            logging.error(f"jaan gayi due to {err}")
            error = "something went wrong"
        return error




    def short_link_deleter(self):


    def short_link_changer(self):