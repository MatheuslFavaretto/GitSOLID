class Repo():

    def __init__(self, id, name, description, language):
        self._id = id
        self._name = name
        self._description = description
        self._language = language

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    

    @property
    def description(self):
        return self._description
    
    @property
    def language(self):
        return self._language
    
    def __str__(self):
        return f'id: {self._id} name: {self._name} description: {self._description} language: {self._language}'