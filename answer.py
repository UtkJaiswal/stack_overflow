from datetime import datetime
from typing import List, Set, Dict


class Answer:
    def __init__(self, id:str, question_id: str, answer: str, answered_by: str):
        self.id: str = id
        self.question_id: str = question_id
        self.answer: str = answer
        self.answered_by: str = answered_by
        self.answered_at = datetime.now()
        self.updated_at = ""
        self.reputation: Set[str] = {}

    def get_answer(self):
        return self
    
    def update_answer(self, answer: str):
        self.answer = answer
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