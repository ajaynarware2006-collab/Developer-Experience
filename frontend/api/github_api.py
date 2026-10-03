from frontend.api.client import get


def get_github_stats():

    response = get(
        "/devxp/github/stats"
    )

    if response.status_code != 200:
        return None

    return response.json()