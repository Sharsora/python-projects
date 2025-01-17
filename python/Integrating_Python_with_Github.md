### Integrating Python with Github
- Install PyGitHub
- Generate a personal access token
- Use PyGitHub to connect

```sh
pip install PyGithub
```

- Go to GitHub UI and then from settings - Developer settings - personal access token - generate a new token for python
- Now draft a code
- It is used to import a GitHub class from the PyGitHub Library 
- from github - you are importing from a Python module or a package named github
- import Github - import class from github library, it represents the connection to GitHub API

- first, install PyGitHub library, and from that install github module, once you have the module, from that module we will import this GitHub Class
- now provide a token,

```sh
from github import Github

# provide the token
token = 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
g = Github(token)

# Get the authenticated user
user = g.get_user()
print(f"Username: {user.login}")
```
