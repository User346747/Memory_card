#создай приложение для запоминания информации
from  PyQt5.QtCore import Qt
from random import shuffle, randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QButtonGroup, QMessageBox
app = QApplication([])
screen = QWidget()
screen.setWindowTitle("Memory Card")
screen.resize(500,500)
screen.number = 0
screen.correct = 0
screen.wrong = 0
screen.all = 0
q = QLabel("Какой национальности не существует?")
answer_button = QPushButton("Ответить")
button1 = QRadioButton("Энцы")
button2 = QRadioButton("Чулымцы")
button3 = QRadioButton("Смурфы")
button4 = QRadioButton("Алеуты")
VLayout = QVBoxLayout()
HLayout1 = QHBoxLayout()
HLayout2 = QHBoxLayout()
ExtraLayout = QVBoxLayout()
VLayout2 = QVBoxLayout()
tip = QPushButton("Получить подсказку")
box = QGroupBox("Варианты ответов:")
box2 = QGroupBox("Результат:")
tip_text = QLabel(" ")
txt = QLabel(" ")
ABox = QButtonGroup()
VLayout.addWidget(q, alignment = Qt.AlignCenter)
HLayout1.addWidget(button1, alignment = Qt.AlignCenter)
HLayout1.addWidget(button2, alignment = Qt.AlignCenter)
HLayout2.addWidget(button3, alignment = Qt.AlignCenter)
HLayout2.addWidget(button4, alignment = Qt.AlignCenter)
VLayout.addWidget(txt, alignment = Qt.AlignCenter)
VLayout.addWidget(tip_text, alignment = Qt.AlignCenter)
VLayout.addWidget(tip, alignment = Qt.AlignCenter)
VLayout2.addLayout(HLayout1)
VLayout2.addLayout(HLayout2)
box.setLayout(VLayout2)
box2.setLayout(ExtraLayout)
VLayout.addWidget(box)
box.show()
VLayout.addWidget(answer_button, alignment = Qt.AlignCenter)
ABox.addButton(button1)
ABox.addButton(button2)
ABox.addButton(button3)
ABox.addButton(button4)
answers = [button1, button2, button3, button4]
tip.haveTip = False
class Question():
    def __init__(self,quest, right, w1, w2, w3):
        self.quest = quest
        self.right = right
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
    def useSelf(self):
        q.setText(self.quest)
        answers[0].setText(self.right)
        answers[1].setText(self.w1)
        answers[2].setText(self.w2)
        answers[3].setText(self.w3)
#exclusive
tip_text.hide()
tips = ["Ответ: Энцы", "Подсказка: Португальский"
, "Перевод: Variable"]
quests = [
    Question(
    "Какой национальности не существует?"
    ,"Энцы", "Чулымцы", "Смурфы","Алеуты"),
    Question(
    "Государственный язык Бразилии",
    "Португальский","Испанский",
    "Итальянский", "Бразильский"
    ),
    Question(
    'Выбери перевод слова "переменная"',
    "variable","variation","changing","variant"
    )]
screen.setLayout(VLayout)
def showStats():
    print("Статистика:")
    print("  -Количество вопросов:", len(quests))
    print("  -Количество правильных ответов:",
     screen.correct)
    print("  -Количество ошибок:", screen.wrong)
    print("  -Всего вопросов:", screen.all)
    print("  -Ваш рейтинг:", 
    screen.correct/screen.all*100)
def showGroupBoxResult():
    box.hide()
    answer_button.setText("Следующий вопрос")
    if answers[0].isChecked():
        screen.correct += 1
        txt.setText("Правильно!")
    else:
        screen.wrong += 1
        txt.setText("Неправильно!")
    screen.all += 1
    txt.show()
    showStats()
    if (len(quests) == 0):
        answer_button.setText("Выйти")
def showGroupBoxAnswering():
    txt.hide()
    answer_button.setText("Ответить")
    #box.setChecked(False)
    ABox.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    ABox.setExclusive(True)
    #box.setChecked(True)
    box.show()
    get_next_question()
#    get_random_question()

def setShowGroupBox():
    if answer_button.text() == "Ответить":
        showGroupBoxResult()
        q.hide()
    elif answer_button.text() == "Следующий вопрос":
        showGroupBoxAnswering()
        q.show()
    else:
        screen.close()
def ask(quest: Question):
    shuffle(answers)
    quest.useSelf()
def get_next_question():
    screen.number = randint(0, len(quests) - 1)
    ask(quests[screen.number])
    del quests[screen.number]
def showTip():
    if tip.haveTip == False:
        tip_text.hide()
        tip.setText("Получить подсказку")
        tip.haveTip = True
    else:
        tip_text.setText(tips[screen.number])
        tip.setText("Скрыть подсказку")
        tip_text.show()
        tip.haveTip = False
tip.clicked.connect(showTip)
#def get_random_question():
#   screen.number = randint(0, len(quests) - 1)
#   ask(quests[screen.number])
answer_button.clicked.connect(setShowGroupBox)
screen.show()
app.exec_()