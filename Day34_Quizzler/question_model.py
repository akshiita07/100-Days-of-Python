# CREATE QUESTION CLASS THAT HAS 2 ATTRIBUTES: QUESTION_TEXT & CORRECT_ANS:
class Question:
    # constructor
    def __init__(self,qtext,cAns):
        self.text=qtext
        self.answer=cAns
        
# Object:
# obj1=Question("2+3=5",True)
# print(f"The question is: {obj1.text} and its correct ans: {obj1.answer}")