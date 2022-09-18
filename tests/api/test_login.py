import requests
import pytest
from applications.api.github_api import GitHubAPI
from config.config import Config


# def test_http_status_code200_initial_test():
#     r = requests.get('https://api.github.com/zen')
#     assert r.status_code == 200

# def test_user_exists_initial_test():
#     r = requests.get('https://api.github.com/users/defunkt')
#     assert r.json()['login'] == 'defunkt'
#     assert r.json()['id'] == 2

# def test_user_non_exists_initial_test():
#     r = requests.get('https://api.github.com/users/wqeqweqwrtq2313etwer')
#     assert r.status_code == 404
#     assert r.json()['message'] == 'Not Found'

# def test_user_exists_without_fixture():
#     github_api_client = GitHubAPI(Config.base_url)
#     user = github_api_client.get_user('defunkt')
#     assert user['login'] == 'defunkt'
#     assert user['id'] == 2

# def test_user_non_exists_without_fixture():
#     github_api_client = GitHubAPI(Config.base_url)
#     with pytest.raises(requests.exceptions.HTTPError):
#         user = github_api_client.get_user('wqeqweqwrtq2313etwe')

# def test_user_exists(github_api_client):
#     user = github_api_client.get_user('defunkt')
#     assert user['login'] == 'defunkt'
#     assert user['id'] == 2

# def test_user_non_exists(github_api_client):
#     with pytest.raises(requests.exceptions.HTTPError):
#         user = github_api_client.get_user('wqeqweqwrtq2313etwe')