import flask
from webhook import Webhook

GH_OWNER = 'phananhthoai'
GH_TOKEN = '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'

app = flask.Flask(__name__)
wk = Webhook(token=GH_TOKEN)

@app.route('/')
def root():
  return flask.redirect(f'https://github.com/{GH_OWNER}')

@app.route('/webhook', methods=(['POST']))
def webhook():
  wk.dispatch(flask.request.headers.get('X-GitHub-Event'), flask.request.json)
  return 'OK'


#def test() -> None:
#  response = requests.get('https://api.github.com/repos/elofun-devops/github-actions/actions/workflows', headers = {'Authorization': 'Bearer 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'})
#  print(response)

if __name__ == '__main__':
  app.run('0.0.0.0', '5000', debug=True)
