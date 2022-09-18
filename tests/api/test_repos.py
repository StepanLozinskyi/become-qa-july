from providers.data.repositories_provider import RepositoriesProvider

def test_check_repos_can_be_fount(github_api_client):
    repo = RepositoriesProvider.existing_repository()
    repos = github_api_client.get_repos(repo['name'])

    assert repos['total_count'] >= repo['total_count']

def test_check_repos_can_not_be_fount(github_api_client):
    repo = RepositoriesProvider.non_existing_repository()
    repos = github_api_client.get_repos(repo['name'])

    assert repos['total_count'] == repo['total_count']