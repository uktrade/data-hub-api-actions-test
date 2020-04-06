#!/usr/bin/env python

"""
This is a script that does the following:

- takes a release type (major, minor or patch) as input and determines the new version number
- runs `git fetch`
- creates a local branch based on origin/develop
- bumps the version number
- generates a changelog for the release
- commits and pushes these changes
- opens your web browser to the create PR page for the pushed branch

The script will abort if:

- there are uncommitted changes
- there are no news fragments on origin/develop
- the changelog branch for the new version already exists
- there are news fragments left behind after the changelog is generated
"""

import argparse
import os
import subprocess
import sys
from getpass import getpass

import requests

from script_utils.command import CommandError, print_error
from script_utils.git import any_uncommitted_changes, local_branch_exists, remote_branch_exists
from script_utils.news_fragments import list_news_fragments
from script_utils.versioning import (
    get_next_version,
    ReleaseType,
    set_current_version,
    VERSION_FILE_PATH,
)

ORG = 'uktrade'
REPO = 'data-hub-api-actions-test'

GITHUB_BASE_REPO_URL = f'https://github.com/{ORG}/{REPO}'
GITHUB_API_PULLS_URL = f'https://api.github.com/repos/{ORG}/{REPO}/pulls'

parser = argparse.ArgumentParser(
    description='Bump the version, update the changelog and open a PR.',
)
parser.add_argument('release_type', type=ReleaseType, choices=ReleaseType.__members__.values())


def prepare_release(release_type):
    """Bump the version, update the changelog and open a PR."""
    remote = 'origin'

    if any_uncommitted_changes():
        raise CommandError(
            'There are uncommitted changes. Please commit, stash or delete them and try again.',
        )

    subprocess.run(['git', 'fetch'], check=True)
    subprocess.run(['git', 'checkout', f'{remote}/develop'], check=True, capture_output=True)

    new_version = get_next_version(release_type)

    branch = f'changelog/{new_version}'
    pr_title = f'Prepare for release {new_version}'
    pr_body = f'This bumps the version and adds the changelog for version {new_version}.'
    commit_message = f"""{pr_title}\n\n{pr_body}"""

    if local_branch_exists(branch):
        raise CommandError(
            f'Branch {branch} already exists locally. Please delete it and try again.',
        )

    if remote_branch_exists(branch):
        raise CommandError(
            f'Branch {branch} already exists remotely. Please delete it on GitHub and try again.',
        )

    if not list_news_fragments():
        raise CommandError('There are no news fragments.')

    subprocess.run(['git', 'checkout', '-b', branch, f'{remote}/develop'], check=True)
    subprocess.run(['towncrier', '--version', str(new_version), '--yes'], check=True)

    remaining_news_fragment_paths = list_news_fragments()
    if remaining_news_fragment_paths:
        joined_paths = '\n'.join(str(path) for path in remaining_news_fragment_paths)

        raise CommandError(
            'These news fragments were left behind:\n\n'
            f'{joined_paths}\n\n'
            'They may be misnamed. Please investigate.',
        )

    set_current_version(new_version)

    subprocess.run(['git', 'add', VERSION_FILE_PATH], check=True)
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)
    subprocess.run(['git', 'push', '--set-upstream', remote, branch], check=True)

    token = os.environ.get('GITHUB_TOKEN') or getpass('GitHub access token: ')

    pr_response = requests.post(
        GITHUB_API_PULLS_URL,
        headers={
            'Authorization': f'Bearer {token}',
        },
        json={
            'title': pr_title,
            'base': 'develop',
            'head': branch,
            'body': pr_body,
        },
    )
    pr_response.raise_for_status()
    # add release label to the PR
    issue_url = pr_response['issue_url']
    github_api_add_label_url = f'{issue_url}/labels'
    add_label_response = requests.post(
        github_api_add_label_url,
        headers={
            'Authorization': f'Bearer {token}',
        },
        json={'labels': ['release']},
    )
    add_label_response.raise_for_status()

    return branch


def main():
    """Run the script using command-line arguments."""
    args = parser.parse_args()

    try:
        branch_name = prepare_release(args.release_type)
    except (CommandError, subprocess.CalledProcessError) as exc:
        print_error(exc)
        sys.exit(1)
        return

    print(  # noqa: T001
        f'Branch {branch_name} was created, pushed and opened in your web browser. If anything '
        f'is wrong, edit your local branch manually and use git push --force-with-lease.',
    )


if __name__ == '__main__':
    main()
