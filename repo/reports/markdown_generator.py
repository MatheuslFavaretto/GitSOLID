class MarkdownGenerator():
    @classmethod
    def build(cls, repos):
        items = ' '.join(
            f'**ID:** {repo.id} **NAME:** {repo.name} **DESCRIPTION:** {repo.description} **LANGUAGE:** {repo.language}\n'
            for repo in repos)
        return f'## REPOS \n{items}'