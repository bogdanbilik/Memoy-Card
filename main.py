from PyQt5.QtWidgets import QApplication
from time import sleep

app = QApplication([])


from main_window import*
from menu_window import*

class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question 
        self.answer = answer 
        self.wrong_answer1 = wrong_ans1 
        self.wrong_answer2 = wrong_ans2 
        self.wrong_answer3 = wrong_ans3 
        self.actual = True 
        self.count_asked = 0 
        self.count_right = 0 
    def got_right(self):
        self.count_asked += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_asked += 1

q1 = Question("Яблуко", "apple", "sssss", "dddd", "aaaaa")
q2 =
q3 



def back_menu():
    menu_w.hide()
    window.show()


btn_back.clicked.connect(back_menu)

def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()

btn_rest.clicked.connect(rest)


v1_lineEdits = QVBoxLayout()
v1_lineEdits.addWidget(le_question)
v1_lineEdits.addWidget(le_right_ans)
v1_lineEdits.addWidget(le_wrong_ans1)
v1_lineEdits.addWidget(le_wrong_ans2)
v1_lineEdits.addWidget(le_wrong_ans3)





menu_w.show()
app.exec_()