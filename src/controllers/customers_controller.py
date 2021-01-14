from models.mysql_model import MysqlModel
from helpers.mysql_queries import create_customer
import logging

class CustomersController(object):
    def __init__(self):
        self.mysql_model.obj = MysqlModel

    def create_customer(self, name, email, mobile, password):
        query1 = find_customer
        query2 = create_customer
        error = ""
        try:
            result = self.mysql_model_obj.extract_query(query=query1, query_params=(email,))
            if len(result) == 0:
                self.mysql.model.obj.insert_query(query=query2, query_params)