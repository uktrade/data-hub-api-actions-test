#!/usr/bin/env python

"""
This is a script that:

- runs `git fetch`
- creates a branch release/<version> based on origin/develop
- pushes this branch
- opens your web browser to the create PR page for the pushed branch (with master as
the base branch)

The script will abort if:

- a tag for the current version already exists
- there are news fragments on origin/develop
- there are uncommitted changes
- the release branch for the current version already exists
"""

import argparse
import os
import subprocess
import sys
from getpass import getpass

import requests

from script_utils.command import CommandError, print_error
from script_utils.git import (
    any_uncommitted_changes,
    local_branch_exists,
    remote_branch_exists,
    remote_tag_exists,
)
from script_utils.news_fragments import list_news_fragments
from script_utils.versioning import get_current_version

ORG = 'uktrade'
REPO = 'data-hub-api-actions-test'

GITHUB_BASE_REPO_URL = f'https://github.com/{ORG}/{REPO}'
GITHUB_API_PULLS_URL = f'https://api.github.com/repos/{ORG}/{REPO}/pulls'
RELEASE_GUIDE_URL = (
    f'https://github.com/{ORG}/{REPO}/blob/develop/docs/'
    'How%20to%20prepare%20a%20release.md'
)
PR_BODY_TEMPLATE = """This is the release PR for version {version}.

Refer to [How to prepare a release]({release_guide_url}) for further information and the next \
steps.
"""

# Currently no real arguments – just used for --help etc.
parser = argparse.ArgumentParser(
    description='Create and push a release branch for the current version.',
)


def create_release_branch():
    """Create and push a release branch."""
    remote = 'origin'

    if any_uncommitted_changes():
        raise CommandError(
            'There are uncommitted changes. Please commit, stash or delete them and try again.',
        )

    subprocess.run(['git', 'fetch'], check=True)
    subprocess.run(['git', 'checkout', f'{remote}/develop'], check=True, capture_output=True)

    version = get_current_version()

    branch = f'release/{version}'
    tag = f'v{version}'

    if remote_tag_exists(tag):
        raise CommandError(
            f'A remote tag {tag} currently exists. It looks like version {version} has '
            f'already been released.',
        )

    news_fragment_paths = list_news_fragments()
    if news_fragment_paths:
        joined_paths = '\n'.join(str(path) for path in news_fragment_paths)

        raise CommandError(
            'These are news fragments on origin/develop:\n\n'
            f'{joined_paths}\n\n'
            'Is the changelog up to date?',
        )

    if local_branch_exists(branch):
        raise CommandError(
            f'Branch {branch} already exists locally. Please delete it and try again.',
        )

    if remote_branch_exists(branch):
        raise CommandError(
            f'Branch {branch} already exists remotely. Please delete it on GitHub and try again.',
        )

    subprocess.run(['git', 'checkout', '-b', branch, f'{remote}/develop'], check=True)
    subprocess.run(['git', 'push', '--set-upstream', remote, branch], check=True)

    token = os.environ.get('GITHUB_TOKEN') or getpass('GitHub access token: ')

    pr_response = requests.post(
        GITHUB_API_PULLS_URL,
        headers={
            'Authorization': f'Bearer {token}',
        },
        json={
            'title': f'Release {version}',
            'base': 'master',
            'head': branch,
            'body': PR_BODY_TEMPLATE.format(version=version, release_guide_url=RELEASE_GUIDE_URL),
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
    """Run the script from the command line."""
    parser.parse_args()

    try:
        branch_name = create_release_branch()
    except (CommandError, subprocess.CalledProcessError) as exc:
        print_error(exc)
        sys.exit(1)
        return

    print(  # noqa: T001
        f'Branch {branch_name} was created, pushed and opened in your web browser.',
    )


if __name__ == '__main__':
    main()
