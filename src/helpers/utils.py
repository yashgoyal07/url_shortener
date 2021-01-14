import os
import random


def get_environment():
    return os.environ.get("my_env", "local")


def short_link_generator():
    result = ""
    char_list = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    for i in range(6):
        result += random.choice(char_list)
    return result