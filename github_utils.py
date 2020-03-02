import os
from pathlib import Path

from github import Github
from git import Repo


g = Github(os.environ.get('GITHUB_TOKEN'))
org = g.get_organization('OpenPecha')


def get_assets_link(repo_name):
    asset_links = []
    repo = org.get_repo(repo_name)
    try:
        latest_release_tag = repo.get_latest_release()
    except:
        print('no latest release found')
    assets = latest_release_tag.raw_data['assets']
    if assets:
        for asset in assets:
            asset_links.append(asset['browser_download_url'])
    else:
        asset_links.append('No assets')
    return asset_links
