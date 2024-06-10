from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QPushButton, QButtonGroup
from random import shuffle , randint

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



question_list = []
question_list.append(Question('Государственный язык бразилии', "Португальский", "Английский", "Испанский", "Бразильский"))
question_list.append(Question("Какого цвета нет на флаге России?", "Зеленый", "красный", "Белый", "Синий"))
question_list.append(Question("Национальная хижина якутов", "Ураса", "Юрта", "Иглу", "Хата"))
question_list.append(Question("Как назывался особый головной убор, который носили фараоны в Древнем Египте?", "Немес", "Картуз", "Корона", "Убрус"))
question_list.append(Question("Какие огурцы сажал на брезентовом поле герой одноименной песни?", "Алюминиевые", "Медные", "Железные", "Оловянные"))
question_list.append(Question("У какого животного самые большие глаза относительно тела?", "У долгопята", "У лемура", "У летучей мыши", "У тупайи"))
question_list.append(Question("Детинцем на Руси называли...", "Кремль", "Школу", "Княжеский терем", "Монастырь"))
question_list.append(Question("Как называли строителя в старину?", "Зодчий", "Бондарь", "Бортник", "Кормчий"))
question_list.append(Question("Продолжите пословицу: «Знает кошка…»", "«Чье мясо съела»", "«Да мыши не знают»", "«Почем фунт лиха»", "«Где собака зарыта»"))
question_list.append(Question("Как называется человек, покоряющий крыши многоэтажных домов?", "Руфер", "Диггер", "Сталкер", "Байкер"))


app = QApplication([])

# создаем панель вопроса 
que = QLabel('Это вопрос')
button = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

# создаем панель результата
AnsGroupBox = QGroupBox('Результат теста')
lb_Resuil = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Resuil, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

# размещяем все виджеты в окне
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "ответить"

layout_line1.addWidget(que, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
# размещяем в 1 строке обе панели, 1 из них будет скрываться, др показываться
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    RadioGroupBox.show()

def next_question():
    main_w.total += 1
    print('статистика\n - всего вопросов:', main_w.total, '\n - правильных ответов:', main_w.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)       

def ask (q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    que.setText(q.question)
    lb_Correct.setText(q.right_ans)
    show_question()

def show_correct(res):
    lb_Resuil.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_w.score += 1
        print('статистика\n - всего вопросов:', main_w.total, '\n - правильных ответов:', main_w.score)
        print('рейтинг:', round((main_w.score/main_w.total*100), 2), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('рейтинг:', round((main_w.score/main_w.total*100), 2), '%')
def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

button.clicked.connect(click_OK)







main_w = QWidget()
main_w.score = 0
main_w.total = 0
main_w.setLayout(layout_card)
main_w.setWindowTitle('Memory Card')
next_question()
main_w.resize(400,300)
main_w.show()
app.exec_()
