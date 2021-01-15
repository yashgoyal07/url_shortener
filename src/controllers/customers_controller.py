from models.mysql_model import MysqlModel
from helpers.mysql_queries import create_customer, find_customer, update_customer, create_user
import logging


class CustomersController(object):
    def __init__(self):
        self.mysql_model_obj = MysqlModel()

    def find_customer(self, cus_id):
        result = self.mysql_model_obj.query(query=find_customer, query_params=(cus_id,))
        return result

    def create_customer(self, cus_id, name=None, email=None, mobile=None, password=None):
        response = CustomersController().find_customer(cus_id=cus_id)
        if not response:
            if name is None and email is None and mobile is None and password is None:
                result = self.mysql_model_obj.query(query=create_user, query_params=(cus_id,))
            else:
                result = self.mysql_model_obj.query(query=create_customer, query_params=(cus_id, name, email, mobile, password))
        else:
            if name is None and email is None and mobile is None and password is None:
                result = "Already Existed"
            else:
                result = self.mysql_model_obj.query(query=update_customer, query_params=(name, email, mobile, password, cus_id))
        return result

    def create_user(self, cus_id):
        result = self.mysql_model_obj.query(query=create_user, query_params=(cus_id,))
        if result == "No Response":
            return True
        else:
            return False
