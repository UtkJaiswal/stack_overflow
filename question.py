from typing import List, Set, Dict
from datetime import datetime
from user import User

class Question:

    def __init__(self, id: str, question: str, keywords: List[str], tags: List[str], posted_by: str):
        self.id: str = id
        self.question: str = question
        self.keywords: List[str] = keywords
        self.tags: List[str] = tags
        self.posted_by: str = posted_by
        self.created_at = datetime.now()
        self.updated_at = ""
        self.reputation: Set[str] = {}

        return self
    
    def update_question(self, question: str, keywords: List[str], tags: List[str]):
        self.question = question
        self.keywords = keywords
        self.tags = tags
        self.updated_at = datetime.now()
        return self
    
    def update_reputation(self, user_id: str):
        if user_id in self.reputation:
            self.reputation.remove(user_id)
        else:
            self.reputation.add(user_id)
        return
    
    def get_reputation_count(self):
        return len(self.reputation)