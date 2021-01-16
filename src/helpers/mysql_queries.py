from configs.mysql_config import *

create_customer = f"""INSERT INTO {MysqlConfig.USER_DATABASE}.{MysqlConfig.CUSTOMERS_TABLE} (customer_id, name, email, mobile, password) VALUES (%s, %s, %s, %s, %s)"""
create_user = f"""INSERT INTO {MysqlConfig.USER_DATABASE}.{MysqlConfig.CUSTOMERS_TABLE} (customer_id) VALUES (%s)"""
find_customer = f"""SELECT * FROM {MysqlConfig.USER_DATABASE}.{MysqlConfig.CUSTOMERS_TABLE} WHERE customer_id = %s"""
update_customer = f"""UPDATE {MysqlConfig.USER_DATABASE}.{MysqlConfig.CUSTOMERS_TABLE} SET name = %s, email = %s, mobile = %s, password = %s WHERE cus_id = %s"""
create_slink = f"""INSERT INTO {MysqlConfig.USER_DATABASE}.{MysqlConfig.LINKS_TABLE} (slink_name, slink, long_link, customerid) VALUES (%s, %s, %s, %s)"""