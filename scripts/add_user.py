import pickle
from datetime import datetime

file_data = 'scripts/user_id.pickle'


def create_new_pickle_file():
    with open(file_data, 'wb') as f:
        user_id = set()
        pickle.dump(user_id, f)


def add_user(message):
    with open(file_data, 'rb') as f:
        user_id = pickle.load(f)
        print(f'{datetime.now()} Инициализация...')
        print(f'Массив загружен: {user_id}')
        print(f'Всего уникальных пользователей: {len(user_id)}')
        if message not in user_id:
            user_id.add(message.from_user.id)
            print(f'Пользователь {message.from_user.id} - {message.from_user.first_name} добавлен в базу')
            with open(file_data, 'wb') as f:
                pickle.dump(user_id, f)
                print(f'База сохранена')
        else:
            print('Пользователь там!')


def read_user_set():
    with open(file_data, 'rb') as f:
        user_id = pickle.load(f)
        answer = f'Всего уникальных пользователей: {len(user_id)}'
        return answer
