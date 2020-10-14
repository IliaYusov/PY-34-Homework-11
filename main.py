import requests


class VKUser:
    API_BASE_URL = 'https://api.vk.com/method/'
    TOKEN = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'
    VERSION = '5.124'

    def __init__(self, user_id):
        self.id = user_id

    def __str__(self):
        return f'https://vk.com/id{self.id}'

    def __and__(self, other):
        friends = self.get_friends()
        other_friends = other.get_friends()
        if isinstance(friends, list) and isinstance(other_friends, list):
            return list(set(self.get_friends()) & set(other.get_friends()))
        return f'Error in {self.id + " " if not isinstance(friends, list) else ""}' \
               f'{other.id + " " if not isinstance(other_friends, list) else ""}friends list'

    def get_friends(self):
        api_url = VKUser.API_BASE_URL + 'friends.get'
        parameters = {
            'access_token': VKUser.TOKEN,
            'v': VKUser.VERSION,
            'user_id': self.id
        }
        response = requests.get(api_url, params=parameters)
        if 'error' in response.json():
            return response.json()['error']['error_msg']
        return response.json()['response']['items']
