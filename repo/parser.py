from models.repo import Repo

class RepoParser():
    @classmethod
    def parse(cls, response):
        repos = []
        for i in range(len(response)):
            repo = response[i]
            repo = Repo(repo["id"], repo["name"], repo["description"], repo["language"])
            repos.append(repo)
        return repos