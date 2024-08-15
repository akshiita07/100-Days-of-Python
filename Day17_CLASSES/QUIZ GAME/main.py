# import questions from data.py
from data import question_data
# import class Question from question_model.py
from question_model import Question
# import quiz brain class to get new questions & input
from quiz_brain import QuizBrain

# empty list that will contain 
question_bank=[]
# iterate over all question_data & create object of Question class
for ques in question_data:
    # from dictionary: ques["text"]     ques["answer"]
    newQuestionObject=Question(ques["text"],ques["answer"])
    question_bank.append(newQuestionObject)
    
# contains all objects:
# print(question_bank)

#make object:

# keep on showing questions until they get over
quiz=QuizBrain(question_bank)
while quiz.questionsAreLeft():
    quiz.giveNewQues()

#after all ques r completed then show final score
print(f"The quiz is completed🚀! Your final score is: {quiz.score}/{quiz.qNo}")