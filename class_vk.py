class BaseClient:
    BASE_URL = None

    method = None
    http_method = None

    def get_params(self):
        pass

    def get_json(self):
        pass

    def get_headers(self):
        pass

    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)

    def _get_data(self, method, http_method):
        response = None

        # todo выполнить запрос

        return self.response_handler(response)

    def response_handler(self, response):
        return response

    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )


class myvk(BaseClient):
    import time
    import vk
    vkapi = vk.API(access_token='c07292a9068f872724ecc7821ccecf9f210b4329b2e05c26c852c13cb692f8fbc4785cfdd8d3e1abddd63')
    #все года друзей
    AllYears = []
    #тут лежат айдишники
    AllFriends=[]
    #айдишник пользователя
    user_id =''
    ArrayYears = []

    #заполнение user_id
    #запуск получения йдишников друзей
    def __init__(self, id):
        myvk.user_id = id
        myvk.get_ids(myvk)
        myvk.get_data(myvk)

    #получение айдишников друзей
    #AllFriends заполняется айдишниками
    def get_ids(self):
        vkapi = myvk.vk.API(access_token='c07292a9068f872724ecc7821ccecf9f210b4329b2e05c26c852c13cb692f8fbc4785cfdd8d3e1abddd63')
        temp = myvk.vkapi.friends.get(user_id = myvk.user_id)  # дик принятый
        myvk.AllFriends = temp['items']
        return ()

    #получение года рождения всех друзей и занесение в AllYears
    def get_data(self):
        errors = 0
        # ВК не любит много запросов сразу...
        for friend in myvk.AllFriends:
            try:
                temp = myvk.vkapi.users.get(user_ids=str(friend), fields='bdate')
                temp1 = temp[0]
                myvk.AllYears.append(temp1['bdate'])
            except:
                errors = errors + 1
            myvk.time.sleep(2)

        # Обработка загруженных данных
        for i in myvk.AllYears:
            if myvk.ReturnYear(i) != 0:
                myvk.ArrayYears.append(int(myvk.ReturnYear(i)))

        myvk.ArrayYears.sort()

        return ()

    # На вход дата рождения полностью, на выход год
    def ReturnYear(temp):
        if len(temp) < 6:
            return 0
        elif temp[len(temp) - 4] != '.' or temp[len(temp) - 3] != '.' or temp[len(temp) - 2] != '.' or temp[
                    len(temp) - 1] != '.':
            return (
            int(temp[len(temp) - 4]) * 1000 + int(temp[len(temp) - 3]) * 100 + int(temp[len(temp) - 2]) * 10 + int(
                temp[len(temp) - 1]))
        else:
            return 0


    # Строит Вертикальную гистограмму
    def PrintAnswer(self):
        temp = myvk.ArrayYears[0]
        dlina = 0
        for i in myvk.ArrayYears:
            if i == temp:
                dlina = dlina + 1
            else:
                print(2016 - temp, ' ', dlina * '#' + '#')
                dlina = 0
                temp = i


