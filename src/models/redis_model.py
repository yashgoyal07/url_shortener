import redis
from helpers.utils import get_environment
from configs.redis_config import RedisConfig


class RedisModel(object):
    def __init__(self):
        self.infra_env = get_environment()
        self.instance_config = RedisConfig().INSTANCE_CONFIG.get(self.infra_env, {})

    def get_connection(self):
        connection = redis.Redis(host=self.instance_config.get("host"),
                                 port=self.instance_config.get("port"),
                                 db=self.instance_config.get("db"),
                                 password=self.instance_config.get("password"),
                                 socket_timeout=self.instance_config.get("socket_timeout"),
                                 )
        return connection
