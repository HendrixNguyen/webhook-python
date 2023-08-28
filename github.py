from requests import Session

class GitHubClient(Session):
    def __init__(self, token):
        super().__init__()
        self._token = token

    def request(self, method, url, **kwargs):
        url = f'https://api.github.com/{url}'
        headers = kwargs.pop('headers', {})
        headers.setdefault('Authorization', f'Bearer {self._token}')
        resp = super().request(method, url, headers=headers, **kwargs)
        return resp
