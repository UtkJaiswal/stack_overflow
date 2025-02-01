from datetime import datetime

class Comment:
    def __init__(self, id:str, type: str, type_id: str, comment: str, commented_by: str):
        self.id = id
        self.type = type
        self.type_id = type_id
        self.comment = comment
        self.commented_by = commented_by
        self.commented_at = datetime.now()

        return self
    

    
        