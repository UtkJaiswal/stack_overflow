from typing import List, Dict, Set
import uuid
from question import Question
from answer import Answer
from comment import Comment

class QuestionManager:

    def __init__(self):
        self.questions: Dict[str:Question] = {}
        self.answers: Dict[str: List[Answer]] = {}
        self.comments: Dict[str:List[Comment]] = {}
        self.user_questions: Dict[str: List[str]] = {}

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
    
    def search_question_by_user(self, user_id):
        questions = []

        user_question_ids = self.user_questions[user_id]

        for question_id in user_question_ids:
            questions.append(self.questions[question_id])

        return questions

    
    def question_details(self, question_id):
        question = self.questions[question_id]
        question_comments = []
        for x in self.comments:
            if x == question_id:
                question_comments.append(self.comments[x])

        answers = []

        for x in self.answers:
            if x == question_id:
                answers.append({
                    "answer": self.answers[x],
                    "_answer_comments": self.comments[self.answers[x]["id"]]
                })

        return {
            "question": question,
            "question_comments": question_comments,
            "answers": answers
        }


 
    def post_question(self, question:str, keywords:List[str], tags: List[str], posted_by: str):
        question_id = str(uuid.uuid4)
        question_obj = Question(question_id, question, keywords, tags, posted_by)
        self.questions[question_id] = question_obj

        for tag in tags:
            self.tag_index[tag].add(question_id)

        for keyword in keywords:
            self.keyword_index[keyword].add(question_id)

        self.user_questions[posted_by].append(question_id)

        return question_obj
    

    def answer_question(self, question_id: str, answer: str, answered_by: str):
        answer_id = str(uuid.uuid4)
        answer = Answer(answer_id, question_id, answer, answered_by)
        self.answers[question_id].append(answer)
        return answer
    
    def add_comment(self, type:str, type_id: str, comment: str, commented_by: str):
        comment_id = str(uuid.uuid4)
        comment_obj = Comment(comment_id, type, type_id, comment, commented_by)
        self.comments[comment_id].append(comment_obj)

        return comment_obj
    

    def vote_question(self, question_id, user_id):
        isUpvote = True
        if user_id in self.questions[question_id]["reputation"]:
            self.questions[question_id]["reputation"].remove(user_id)
            isUpvote = False

        else:
            self.questions[question_id]["reputation"].add(user_id)

        return isUpvote
    
    def vote_answer(self, answer_id, user_id):
        isUpvote = True
        if user_id in self.questions[answer_id]["reputation"]:
            self.questions[answer_id]["reputation"].remove(user_id)
            isUpvote = False

        else:
            self.questions[answer_id]["reputation"].add(user_id)

        return isUpvote




