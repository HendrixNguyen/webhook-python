
from logging import Logger

from github import GitHubClient


actions_repo = 'github-actions'
class Webhook:

    

    def __init__(self, token):
        self.gh = GitHubClient(token=token)

    def dispatch(self, event, data):
        method_name = f'handle_{event}'
        if not event or not hasattr(self, method_name):
            return
        getattr(self, method_name)(data)

    # def handle_ping(self, data):
    #     print(f'Data: {data}')

    def handle_push(self, data):
        repo_name = data.get('repository').get('name')
        commit_before = data.get('before')
        commit_after = data.get('after')
        commit_ref = data.get('ref')
        actor = data.get('pusher').get('name')
        org_name = data.get('organization').get('login')

        print(f'Repo: {repo_name}')
        print(f'Before: {commit_before}')
        print(f'After: {commit_after}')
        print(f'Ref: {commit_ref}')
        print(f'Actor: {actor}')
        print(f'Org: {org_name}')

        res = self.gh.get(f'repos/{org_name}/{actions_repo}/actions/workflows')
        if res.status_code==200:
            _res: dict = res.json()
            arrWorkflows = _res.get('workflows')
            for item in arrWorkflows:
                print('Oject: %s', item)
            
        else:
            print('Failue')
