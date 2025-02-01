class User:
    def __init__(self, id, name, email):
        self.id: str = id
        self.name: str = name
        self.email: str = email
        self.reputation: int = 0

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_reputation(self):
        return self.reputation
    