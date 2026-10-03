import requests
from datetime import datetime, timezone, timedelta


GITHUB_API_URL = "https://api.github.com"
GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"


def get_github_headers(access_token: str):

    return {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


# ============================================================
# GITHUB USER
# ============================================================

def get_github_user(
    access_token: str,
):

    response = requests.get(
        f"{GITHUB_API_URL}/user",
        headers=get_github_headers(
            access_token
        ),
        timeout=15,
    )

    response.raise_for_status()

    return response.json()


# ============================================================
# GITHUB GRAPHQL
# ============================================================

def github_graphql(
    access_token: str,
    query: str,
    variables: dict,
):

    response = requests.post(
        GITHUB_GRAPHQL_URL,

        headers={
            "Authorization": (
                f"Bearer {access_token}"
            ),
            "Content-Type": "application/json",
        },

        json={
            "query": query,
            "variables": variables,
        },

        timeout=20,
    )

    response.raise_for_status()

    data = response.json()

    if data.get("errors"):

        raise RuntimeError(
            data["errors"][0].get(
                "message",
                "GitHub GraphQL error.",
            )
        )

    return data["data"]


# ============================================================
# REPOSITORIES
# ============================================================

def get_github_repositories(
    access_token: str,
):

    repositories = []

    page = 1

    while True:

        response = requests.get(
            f"{GITHUB_API_URL}/user/repos",

            headers=get_github_headers(
                access_token
            ),

            params={
                "per_page": 100,
                "page": page,
                "affiliation": "owner",
                "sort": "updated",
            },

            timeout=15,
        )

        response.raise_for_status()

        page_repositories = response.json()

        if not page_repositories:
            break

        repositories.extend(
            page_repositories
        )

        if len(page_repositories) < 100:
            break

        page += 1

    return repositories


def get_owned_repository_count(
    access_token: str,
):

    query = """
    query($login: String!) {
      user(login: $login) {
        repositories(
          first: 1
          ownerAffiliations: OWNER
        ) {
          totalCount
        }
      }
    }
    """

    github_user = get_github_user(
        access_token
    )

    data = github_graphql(
        access_token,
        query,
        {
            "login": github_user["login"],
        },
    )

    return (
        data["user"]["repositories"]["totalCount"]
    )


# ============================================================
# CONTRIBUTIONS
# ============================================================

def get_github_contributions(
    access_token: str,
    username: str,
):

    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          totalCommitContributions
          totalContributions

          contributionCalendar {
            totalContributions

            weeks {
              contributionDays {
                date
                contributionCount
                color
              }
            }
          }
        }
      }
    }
    """

    data = github_graphql(
        access_token,
        query,
        {
            "login": username,
        },
    )

    collection = (
        data["user"]["contributionsCollection"]
    )

    calendar = collection[
        "contributionCalendar"
    ]

    days = []

    for week in calendar["weeks"]:

        for day in week[
            "contributionDays"
        ]:

            days.append(
                {
                    "date": day["date"],
                    "count": day[
                        "contributionCount"
                    ],
                    "color": day["color"],
                }
            )

    return {
        "total_commits": collection[
            "totalCommitContributions"
        ],

        "total_contributions": collection[
            "totalContributions"
        ],

        "days": days,
    }


# ============================================================
# LAST COMMIT
# ============================================================

def get_latest_commit(
    access_token: str,
    username: str,
):

    response = requests.get(
        f"{GITHUB_API_URL}/search/commits",

        headers={
            **get_github_headers(
                access_token
            ),
            "Accept": (
                "application/vnd.github+json"
            ),
        },

        params={
            "q": f"author:{username}",
            "sort": "committer-date",
            "order": "desc",
            "per_page": 1,
        },

        timeout=15,
    )

    if response.status_code != 200:
        return None

    data = response.json()

    items = data.get(
        "items",
        [],
    )

    if not items:
        return None

    commit = items[0]

    return (
        commit
        .get("commit", {})
        .get("author", {})
        .get("date")
    )


# ============================================================
# COMPLETE GITHUB STATS
# ============================================================

def get_github_stats(
    access_token: str,
):

    github_user = get_github_user(
        access_token
    )

    username = github_user["login"]

    repository_count = (
        get_owned_repository_count(
            access_token
        )
    )

    latest_commit = get_latest_commit(
        access_token,
        username,
    )

    contributions = (
        get_github_contributions(
            access_token,
            username,
        )
    )

    return {
        "username": username,

        "name": github_user.get(
            "name"
        ),

        "avatar_url": github_user.get(
            "avatar_url"
        ),

        "repository_count": (
            repository_count
        ),

        "total_commits": (
            contributions[
                "total_commits"
            ]
        ),

        "total_contributions": (
            contributions[
                "total_contributions"
            ]
        ),

        "last_commit_at": (
            latest_commit
        ),

        "contribution_calendar": (
            contributions["days"]
        ),
    }