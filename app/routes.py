from flask import Blueprint, request, render_template, redirect, make_response, url_for, flash
from config import Config
from app.utils import get_user_json, url_for_connection, get_code_url, get_searched_users_json, get_users_count
import requests


route_gate = Blueprint('route_gate', __name__)


@route_gate.route('/connect', methods=['GET'])
def connect():
    return redirect(url_for_connection)


@route_gate.route('/get_code', methods=['GET'])
def get_code():
    access_code = request.args.get('code')
    url = get_code_url(access_code)
    response = requests.get(url)
    data = response.json()
    if 'access_token' in data:     
        return redirect(f'/set_cookies/{data["expires_in"]}/{data["access_token"]}')
    else: 
        flash('Error getting session key')
    return redirect(url_for('route_gate.main')) 


@route_gate.route('/set_cookies/<int:max_age>/<access_token>', methods=['GET'])
def set_cookies(max_age: int, access_token: str):
    cookie_response = make_response(redirect(url_for('route_gate.main')))
    cookie_response.set_cookie('access_token', access_token, max_age=max_age)
    return cookie_response


@route_gate.route('/search/', methods=['GET'])
@route_gate.route('/search/<string:query>', methods=['GET'])
def search(query: str = None):
    acces_token = request.cookies.get('access_token')
    if acces_token is None:
        redirect(url_for('routes_gate.main'))

    client_json = get_user_json(acces_token)
    if 'error' in client_json:
        flash('Error getting user_data')
        return redirect(url_for('route_gate.main'))
    client_data = client_json['response'][0]
    
    user_id = client_data['id']

    friends_json = get_searched_users_json(user_id=user_id, access_token=acces_token, query=query)
    if 'error' in friends_json:
        flash('Error getting friends')
        return redirect(url_for('route_gate.main'))
    friends_data = friends_json['response']['items']
    
    friends_num = get_users_count(user_id, acces_token)
    if 'error' in friends_num:
        flash('Error getting user_data')
        return redirect(url_for('route_gate.main'))
    friends_num = friends_num['response']['count']

    return render_template('main.html', authorized=True, client_data=client_data, friends_data=friends_data, count=friends_num)


@route_gate.route('/', methods=['GET'])
def main():
    acces_token = request.cookies.get('access_token')
    if acces_token is None:
        return render_template('main.html', authorized=False)

    client_json = get_user_json(acces_token)
    if 'error' in client_json:
        flash('Error getting user_data')
        return render_template('main.html', authorized=False)
    client_data = client_json['response'][0]

    user_id = client_data['id']

    friends_num = get_users_count(user_id, acces_token)
    if 'error' in friends_num:
        flash('Error getting friend_count_data')
        return redirect(url_for('route_gate.main'))
    friends_num = friends_num['response']['count']

    return render_template('main.html', authorized=True, client_data=client_data, count=friends_num)
