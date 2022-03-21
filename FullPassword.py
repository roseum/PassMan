class FullPassword():
    def __init__(self, name, password):
        self.password = password
        self.name = name

    def dump(self):
        return {'name': self.name,
                'password': self.password}
