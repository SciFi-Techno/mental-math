from PySide6 import QtWidgets, QtGui
import random

class Questions(QtWidgets.QMainWindow):
    def __init__(self, topic, difficulty):
        super().__init__()
        self.level = difficulty
        self.operation = topic

        # Set window size & title
        self.setWindowTitle("Questions")
        self.setFixedSize(1000, 500)

        # Set overall page layout
        main_layout = QtWidgets.QVBoxLayout()
        self.second_layout = QtWidgets.QHBoxLayout()
        third_layout = QtWidgets.QHBoxLayout()

        main_layout.addLayout(self.second_layout)
        main_layout.addLayout(third_layout)

        # Numbers & their associated label for the problems
        self.no1 = None
        self.no2 = None
        self.difficulty_level()
        self.n1_label = QtWidgets.QLabel(str(self.no1))
        self.n1_label.setFont(QtGui.QFont("Arial", 24))
        self.n2_label = QtWidgets.QLabel(str(self.no2))
        self.n2_label.setFont(QtGui.QFont("Arial", 24))

        # Set & display the actual question
        topic_symbol = None
        if self.operation == 0:
            topic_symbol = QtWidgets.QLabel("+")
        elif self.operation == 1:
            topic_symbol = QtWidgets.QLabel("-")
        elif self.operation == 2:
            topic_symbol = QtWidgets.QLabel("*")
        topic_symbol.setFont(QtGui.QFont("Arial", 24))

        self.equals = QtWidgets.QLabel("=")
        self.equals.setFont(QtGui.QFont("Arial", 24))

        self.second_layout.addWidget(self.n1_label)
        self.second_layout.addWidget(topic_symbol)
        self.second_layout.addWidget(self.n2_label)
        self.second_layout.addWidget(self.equals)

        # Set & display the input box
        self.answer_box = QtWidgets.QInputDialog()
        self.answer_box.setInputMode(QtWidgets.QInputDialog.InputMode.IntInput)
        self.answer_box.setOption(QtWidgets.QInputDialog.InputDialogOption.NoButtons)
        self.answer_box.setIntRange(-10000, 10000)
        self.answer_box.intValueChanged.connect(self.submit_answer)
        self.answer_box.setLabelText("")

        third_layout.addWidget(self.answer_box)

        # Main widget to display all elements
        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.show()
        self.raise_()

    def submit_answer(self, user_input):
        answer = None

        if self.operation == 0:
            answer = self.no1 + self.no2
        elif self.operation == 1:
            answer = self.no1 - self.no2
        elif self.operation == 2:
            answer = self.no1 * self.no2

        if user_input == answer:
            self.difficulty_level()
            self.n1_label.setText(str(self.no1))
            self.n2_label.setText(str(self.no2))

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