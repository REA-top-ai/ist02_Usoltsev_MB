import os
from dotenv import load_dotenv
import requests as r
from pprint import pprint

load_dotenv()

GitHub_api = os.getenv('GITHUB_API_KEY')
Base_URL = 'https://api.github.com'

headers = {'Authorization': f'Bearer {GitHub_api}', 'Accept': 'application/vnd.github+json', 'X-Frame-Options': 'DENY'}
# cookies = {'': 'has_recent_activity'}

def get_user(username):
    user = r.get(url=f'{Base_URL}/users/{username}', headers=headers)
    return user.json()

def get_repos(username):
    repos = r.get(url=f'{Base_URL}/users/{username}/repos', headers=headers)
    return repos.json()

def get_languages(username, repo):
    languages = r.get(url=f'{Base_URL}/repos/{username}/{repo}/languages', headers=headers)
    return languages.json()

def get_contributors(username, repo):
    contributors = r.get(url=f'{Base_URL}/users/{username}/repos/{repo}/contributors', headers=headers)
    return contributors.json()

def get_activity(username, page=None):
    params = {'per_page': 15, 'page': page}
    activity = r.get(url=f'{Base_URL}/users/{username}/events', headers=headers, params=params)
    return activity.json()


def get_all_activ(username):
    all_activ = []
    for page in range(15):
        all_activ += get_activity(username, page)
    return all_activ

def get_inf_repos(username, repos):
    sum_stars = 0
    sum_forks = 0
    sum_readmes = 0
    languages = {}
    for repo in repos:
        sum_stars += int(repo['stargazers_count'])
        sum_forks += int(repo['fork'])
        sum_readmes += int(repo['has_wiki'])
        repo_languages = get_languages(username, repo.get('name'))
        for key in repo_languages.keys():
            if key in languages:
                languages[key] += repo_languages[key]
            else:
                languages[key] = repo_languages[key]

    return {
        'languages': languages,
        'total_stars': sum_stars,
        'mean_count_stars': sum_stars//len(repos),
        'total_forks': sum_forks,
        'total_readmes': sum_readmes
    }


def get_info(username):
    user = get_user(username)
    repos = get_repos(username)
    activ = get_all_activ(username)

    info = {
        'username': user.get('login'),
        'created_at': user.get('created_at'),
        'followers': user.get('followers'),
        'all_repos': len(repos),
        'activ': activ,
    }
    info.update(get_inf_repos(username, repos))

    # pprint(user)
    # print(repos)
    # pprint(activ[0])
    # pprint(info)
    # print(len(activ))
    # print(len(repos))
    #pprint(repos[0])

    return info


#pprint(get_info('Amontapelir'))