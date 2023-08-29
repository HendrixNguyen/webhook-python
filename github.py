from requests import Session

class GitHubClient(Session):
    ## Hàm init là hàm khởi tạo các biến khi tạo 1 class
    def __init__(self, token):
        super().__init__()
        self._token = token

    ## Overrite lại hàm request
    def request(self, method, url, **kwargs):
        url = f'https://api.github.com/{url}'
        headers = kwargs.pop('headers', {})
        headers.setdefault('Authorization', f'Bearer {self._token}')
        resp = super().request(method, url, headers=headers, **kwargs)
        return resp
