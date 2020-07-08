import config
from vedis import Vedis


# Запрашиваем из базы статус пользователя
def get_current_state(user_id):
    with Vedis(config.db_file) as db:
        try:
            return db[user_id].decode()
        except KeyError:  # Если такого ключа/пользователя в базе не оказалось
            return "-1"   # Значение по умолчанию-начало диалога


# Сохраняем текущий статус пользователя в базу
def set_state(user_id, value):
    with Vedis(config.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            print('Проблемка с юзером!')
            return False