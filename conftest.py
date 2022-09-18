from applications.api.github_api import GitHubAPI
from config.config import Config
import pytest

@pytest.fixture
def github_api_client(): #scope='function/class/module/session' -> вказати після чого виклик yield
    github_api_client = GitHubAPI(Config.base_url)
    #return github_api_client
    #print("END-UP-TEST") #=> НЕ виконається після тесту
    yield github_api_client
    print("END-UP-TEST") #=> Виконається після тесту