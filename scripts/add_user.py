import pickle

file_data = 'scripts/user_id.pickle'


def add_user(id):
    with open(file_data, 'rb') as f:
        user_id = pickle.load(f)
        print(f'Массив загружен: {user_id}')
        if id not in user_id:
            print(f'Пользователя {id} нет в базе')
            user_id.add(id)
            print(f'Пользователь {id} добавлен в базу')
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


answer = read_user_set()
