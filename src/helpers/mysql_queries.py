from configs.mysql_config import *

create_short_link = f"""INSERT INTO {MysqlConfig.USER_DATABASE}.{MysqlConfig.SLINKS_TABLE} (slink, llink, userid) VALUES (%s, %s, %s)"""