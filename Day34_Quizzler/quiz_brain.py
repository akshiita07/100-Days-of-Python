# ASK USER QUESTION
# CHECK IF USER ANS IS CORRECT OR NOT
import html

# QUIZBRAIN CLASS WITH 2 ATTRIBUTES-> QNO & QLIST
#  + METHOD THAT ASSIGNS A NEW QUESTION
class QuizBrain:
    def __init__(self,question_list):
        self.qNo=0       #by default start from 0
        self.qlist=question_list
        # score user with def value=0
        self.score=0
    
    # returns T/F if still questions r remaining or not:
    def questionsAreLeft(self):
        if self.qNo<len(self.qlist):   #until ques left then T
            return True
        else:
            return False
    
    
    def checkAnswer(self,userAnswer):
        correctAnswer=self.currentQuestion.answer
        # if user writes short forms
        if userAnswer.lower()=="t":
            userAnswer="true"
        elif userAnswer.lower()=="f":
            userAnswer="false"
        #in any casing
        if userAnswer.lower()==correctAnswer.lower():
            # print("Correct Answer 😊")
            self.score+=1
            return True
        else:
            # print("Wrong Answer 😭")
            # print(f"The correct answer is: {correctAnswer}")
            return False
        #also show score to user
        # print(f"Your current score is: {self.score}/{self.qNo}")
        # print()     #just for a new line
    
    def giveNewQues(self):
        #provide a new q
        self.currentQuestion=self.qlist[self.qNo]
        actualAnswer=self.currentQuestion.answer
        # start qno from 1 so (+1)
        self.qNo+=1
        # data is printed along with html entities so unescape them:
        q_text=html.unescape(self.currentQuestion.text  )
        # userInput=input(f"Q.{self.qNo}: {q_text} (True/False)?: ")
        # self.checkAnswer(userInput,actualAnswer)
        return f"Q.{self.qNo}: {q_text}"
              
# obj1=QuizBrain(question_bank) #pass this qbank as list of questions