class HTMLGenerator():
    @classmethod
    def build(cls, repos):
        items = ' '.join(
            f'<strong>ID: </strong>{repo.id} <strong>NAME: </strong>{repo.name} <strong>DESCRIPTION: </strong>{repo.description} <strong>LANGUAGE: </strong>{repo.language}\n'
            for repo in repos)
        return f'<p>{items}</p>'