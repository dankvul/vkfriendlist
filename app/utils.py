import requests
from config import Config


url_for_connection = f'https://oauth.vk.com/authorize?client_id={Config.VK_APP_ID}&display=page&redirect_uri={Config.REDIRECT_URI}' \
          f'&scope=friends&response_type=code&v=5.103'


def get_code_url(access_code: str):
    return f'https://oauth.vk.com/access_token?client_id={Config.VK_APP_ID}&client_secret={Config.VK_APP_SECURED_KEY}&' \
          f'redirect_uri={Config.REDIRECT_URI}&code={access_code}'

def get_users_count(user_id: int, access_token: str) -> int:
    url_friend_count = 'https://api.vk.com/method/friends.get'
    params = {'access_token': access_token,
              'user_ids': int(user_id),
              'count': '0',
              'v': '5.103'}
    friend_count_response = requests.get(url_friend_count, params=params)
    data = friend_count_response.json()
    return data


def get_user_json(access_token: str) -> dict:
    url_friend_list = 'https://api.vk.com/method/users.get'
    params = {'access_token': access_token,
              'fields': 'photo_50',
              'v': '5.103'}
    friend_list_response = requests.get(url_friend_list, params=params)
    data = friend_list_response.json()
    return data


def get_searched_users_json(user_id: int, access_token: str, query: str) -> list:
    url_searched_users = 'https://api.vk.com/method/friends.search'
    params = {'access_token': access_token,
              'q': query,
              'user_id': int(user_id),
              'fields': 'photo_100, education',
              'v': '5.103'}
    searched_users_response = requests.get(url_searched_users, params=params)
    data = searched_users_response.json()
    return data