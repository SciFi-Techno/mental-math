from PySide6 import QtWidgets, QtGui, QtCore
import random

class Questions(QtWidgets.QMainWindow):
    def __init__(self, topic, difficulty, time, problems):
        super().__init__()
        self.level = difficulty
        self.operation = topic
        self.time_remain = time
        self.problems_remain = problems

        # Set window size & title
        self.setWindowTitle("Questions")
        self.setFixedSize(800, 300)

        # Set overall page layout
        main_layout = QtWidgets.QVBoxLayout()
        second_layout = QtWidgets.QHBoxLayout()
        self.third_layout = QtWidgets.QHBoxLayout()
        fourth_layout = QtWidgets.QHBoxLayout()

        main_layout.addLayout(second_layout)
        main_layout.addLayout(self.third_layout)
        main_layout.addLayout(fourth_layout)

        # Numbers & their associated label for the problems
        self.no1 = None
        self.no2 = None
        self.difficulty_level()
        self.n1_label = QtWidgets.QLabel(str(self.no1))
        self.n1_label.setFont(QtGui.QFont("Arial", 24))
        self.n1_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.n2_label = QtWidgets.QLabel(str(self.no2))
        self.n2_label.setFont(QtGui.QFont("Arial", 24))
        self.n2_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # Set & display the actual question
        topic_symbol = None
        if self.operation == 0:
            topic_symbol = QtWidgets.QLabel("+")
        elif self.operation == 1:
            topic_symbol = QtWidgets.QLabel("-")
        elif self.operation == 2:
            topic_symbol = QtWidgets.QLabel("*")
        topic_symbol.setFont(QtGui.QFont("Arial", 24))
        topic_symbol.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        equals = QtWidgets.QLabel("=")
        equals.setFont(QtGui.QFont("Arial", 24))
        equals.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.third_layout.addWidget(self.n1_label)
        self.third_layout.addWidget(topic_symbol)
        self.third_layout.addWidget(self.n2_label)
        self.third_layout.addWidget(equals)

        # Set & display the input box
        self.answer_box = QtWidgets.QLineEdit()
        self.answer_box.editingFinished.connect(self.submit_answer)
        fourth_layout.addWidget(self.answer_box)

        # Set & display the timer if option was selected
        if self.time_remain != 0 and self.problems_remain == 0:
            self.time_given = QtCore.QTime(0, self.time_remain // 60, self.time_remain % 60)
            self.timer_label = QtWidgets.QLabel(str(self.time_remain // 60) + ":" + str(self.time_remain % 60))
            self.timer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            self.timer_label.setFont(QtGui.QFont("Arial", 24))
            second_layout.addWidget(self.timer_label)
            my_timer = QtCore.QTimer(self)
            my_timer.timeout.connect(self.time_update)
            my_timer.start(1000)
        # Set & display the number of problems remaining if option was selected
        elif self.problems_remain != 0 and self.time_remain == 0:
            self.problems_label = QtWidgets.QLabel(str(self.problems_remain))
            self.problems_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            self.problems_label.setFont(QtGui.QFont("Arial", 24))
            second_layout.addWidget(self.problems_label)

        # Main widget to display all elements
        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.show()
        self.raise_()

    def submit_answer(self):
        user_input = int(self.answer_box.text())
        answer = None

        if self.operation == 0:
            answer = self.no1 + self.no2
        elif self.operation == 1:
            answer = self.no1 - self.no2
        elif self.operation == 2:
            answer = self.no1 * self.no2

        if self.time_remain != 0 and self.problems_remain == 0:
            if (user_input == answer) and ((self.time_given.minute() != 0) and (self.time_given.second() != 0)):
                self.difficulty_level()
                self.n1_label.setText(str(self.no1))
                self.n2_label.setText(str(self.no2))
        elif self.problems_remain != 0 and self.time_remain == 0:
            if (user_input == answer) and (self.problems_remain != 0):
                self.difficulty_level()
                self.n1_label.setText(str(self.no1))
                self.n2_label.setText(str(self.no2))
                self.problems_remain -= 1
                self.problems_label.setText(str(self.problems_remain))
        else:
            self.close()

        self.answer_box.clear()

    def difficulty_level(self):
        if self.level == 0:
            self.no1 = random.randrange(9)
            self.no2 = random.randrange(9)
        elif self.level == 1:
            self.no1 = random.randrange(10, 99)
            self.no2 = random.randrange(10, 99)
        elif self.level == 2:
            self.no1 = random.randrange(100, 999)
            self.no2 = random.randrange(100, 999)

    def time_update(self):
        self.time_given = self.time_given.addSecs(-1)
        self.timer_label.setText(str(self.time_given.minute()) + ":" + str(self.time_given.second()))

        if self.time_given.minute() == 0 and self.time_given.second() == 0:
            self.close()