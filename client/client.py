class Client:
    def __init__(self, **kwargs):
        if 'name' in kwargs:
            self._name =  kwargs['name']