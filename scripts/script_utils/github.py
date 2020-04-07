from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


class GitHubAPIClient:
    def __init__(self, token):
        _transport = RequestsHTTPTransport(
            url='https://api.github.com/graphql',
            use_json=True,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {token}'
            },
        )

        self._client = Client(
            retries=3,
            transport=_transport,
            fetch_schema_from_transport=False,
        )

    def get_repo_id(self, owner, repo):
        query = gql("""
query($owner:String!, $name: String!) { 
  repository(owner: $owner, name: $name) {
    id
  }
}
    """)
        params = {
            'owner': owner,
            'name': repo,
        }
        result = self._client.execute(query, variable_values=params)
        return result['repository']['id']

    def create_pr(self, repo_id, base, head, title, body, draft=False):
        query = gql("""
mutation($input: CreatePullRequestInput!) { 
  createPullRequest(input:$input) {
    pullRequest {
        id
    }
  }
}
    """)
        params = {
            'input': {
                'repositoryId': repo_id,
                'baseRefName': base,
                'headRefName': head,
                'title': title,
                'body': body,
                'draft': draft,
            },
        }
        result = self._client.execute(query, variable_values=params)
        return result['createPullRequest']['pullRequest']['id']

    def get_label(self, repo_owner, repo_name, label_name):
        query = gql("""
query($repo_owner:String!, $repo_name:String!, $label_name:String!) {
  repository(owner:$repo_owner, name:$repo_name) {
    label(name: $label_name) {
      id
    }
  }
}
    """)
        params = {
            'repo_owner': repo_owner,
            'repo_name': repo_name,
            'label_name': label_name,
        }
        result = self._client.execute(query, variable_values=params)
        return result['repository']['label']['id']

    def add_pr_labels(self, pull_request_id, label_ids):
        query = gql("""
mutation($input: AddLabelsToLabelableInput!) { 
  addLabelsToLabelable(input:$input) {
    clientMutationId
  }
}
    """)
        params = {
            'input': {
                'labelIds': label_ids,
                'labelableId': pull_request_id,
            },
        }
        result = self._client.execute(query, variable_values=params)
        return result

    def mark_pr_ready_for_review(self, pull_request_id):
        query = gql("""
mutation($input: MarkPullRequestReadyForReviewInput!) { 
  markPullRequestReadyForReview(input:$input) {
    clientMutationId
  }
}
    """)
        params = {
            'input': {
                'pullRequestId': pull_request_id,
            },
        }
        result = self._client.execute(query, variable_values=params)
        return result
