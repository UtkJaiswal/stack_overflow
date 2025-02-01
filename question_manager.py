from typing import List, Dict, Set
import uuid
from question import Question
from answer import Answer
from comment import Comment

class QuestionManager:

    def __init__(self):
        self.questions: Dict[str:List[Question]] = {}
        self.answers: List[Answer] = []
        self.comments: List[Comment] = []

        self.tag_index: Dict[str: Set[str]] = {}
        self.keyword_index: Dict[str: Set[str]] = {}
    
    def search_questions(self, index):
        questions = []
        if 'tags' in index:
            tags = index['tags']
            for tag in tags:
                for x in self.tag_index[tag]:
                    questions.append(self.questions[self.tag_index[x]])
            
        if 'keywords' in index:
            keywords = index['keyword']
            for keyword in keywords:
                for x in self.keyword_index[keyword]:
                    questions.append(self.questions[self.keyword_index[x]])
        
        return questions

 
    def post_question(self, question:str, keywords:List[str], tags: List[str], posted_by: str):
        question_id = str(uuid.uuid4)
        question_obj = Question(question_id, question, keywords, tags, posted_by)
        self.questions[question_id] = question_obj

        for tag in tags:
            self.tag_index[tag].add(question_id)

        for keyword in keywords:
            self.keyword_index[keyword].add(question_id)

        return question_obj
    

    def answer_question(self, question_id: str, answer: str, answered_by: str):
        answer_id = str(uuid.uuid4)
        answer = Answer(answer_id, question_id, answer, answered_by)
        self.answers.append(answer)
        return answer
    
    def add_comment(self, type:str, type_id: str, comment: str, commented_by: str):
        comment_id = str(uuid.uuid4)
        comment_obj = Comment(comment_id, type, type_id, comment, commented_by)
        return comment_obj
    
