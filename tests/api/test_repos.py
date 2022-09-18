def test_check_repos_can_be_fount(github_api_client):
    # Check user can find any existion repo from github
    repos = github_api_client.get_repos('become-qa-auto')

    assert repos['total_count'] != 0
    assert len(repos['items']) != 0

def test_check_repos_can_not_be_fount(github_api_client):
    # Check user can find any existion repo from github
    repos = github_api_client.get_repos('werwerewrewr242331we123')

    assert repos['total_count'] == 0
    assert len(repos['items']) == 0