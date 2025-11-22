from PySide6 import QtCore, QtWidgets, QtGui

import problems
import setting_timer
import setting_problems
import selected_topic
import questions

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Placeholders for values from other windows / popups
        self.new_window = None
        self.topic_selected = 0
        self.difficulty_selected = 0

        # Set window size & title
        self.setWindowTitle("Mental Math")
        self.setFixedSize(800, 300)

        # Set overall page layout
        main_layout = QtWidgets.QVBoxLayout()
        second_layout = QtWidgets.QHBoxLayout()
        topic_layout = QtWidgets.QHBoxLayout()
        difficulty_layout = QtWidgets.QHBoxLayout()
        start_layout = QtWidgets.QHBoxLayout()
        timer_or_problems_layout = QtWidgets.QHBoxLayout()

        # Add additional layouts to page layout
        main_layout.addLayout(second_layout)
        main_layout.addLayout(topic_layout)
        main_layout.addLayout(difficulty_layout)
        main_layout.addLayout(timer_or_problems_layout)
        main_layout.addLayout(start_layout)

        # Add title text
        title_layout = QtWidgets.QLabel("MENTAL\nMATH")
        title_layout.setFont(QtGui.QFont('Arial', 30))
        title_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        second_layout.addWidget(title_layout)

        # Add topic selection & associated text
        learning_label = QtWidgets.QLabel("What are you learning today?")
        learning_label.setFont(QtGui.QFont('Arial', 20))
        learning_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        topic_layout.addWidget(learning_label)

        self.learning_options = QtWidgets.QComboBox()
        self.learning_options.addItems(["Addition", "Subtraction", "Multiplication", "Division", "Mix"])
        self.learning_options.currentIndexChanged.connect(self.topic_changed)
        topic_layout.addWidget(self.learning_options)

        # Add difficulty selection & associated text
        difficulty_label = QtWidgets.QLabel("What difficulty?")
        difficulty_label.setFont(QtGui.QFont('Arial', 20))
        difficulty_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        difficulty_layout.addWidget(difficulty_label)

        self.difficulty_options = QtWidgets.QComboBox()
        self.difficulty_options.addItems(["Easy", "Medium", "Hard", "Custom"])
        self.difficulty_options.currentIndexChanged.connect(self.difficulty_changed)
        difficulty_layout.addWidget(self.difficulty_options)

        # Add timer or problems selection & associated text
        timer_or_problems_label = QtWidgets.QLabel("Timer and/or number of problems?\t\t")
        timer_or_problems_label.setFont(QtGui.QFont('Arial', 20))
        timer_or_problems_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        timer_or_problems_layout.addWidget(timer_or_problems_label)

        self.timer_checkbox = QtWidgets.QCheckBox("Timer")
        self.timer_checkbox.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.timer_checkbox.stateChanged.connect(self.timer_state_change)
        timer_or_problems_layout.addWidget(self.timer_checkbox)

        self.problems_checkbox = QtWidgets.QCheckBox("Number\nof problems")
        self.problems_checkbox.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.problems_checkbox.stateChanged.connect(self.problem_state_change)
        timer_or_problems_layout.addWidget(self.problems_checkbox)

        # Add a submit button to start
        submit_button = QtWidgets.QPushButton("Start", self)
        submit_button.setFixedSize(70, 40)
        submit_button.clicked.connect(self.start_button)
        start_layout.addWidget(submit_button)

        # Main widget to display all elements
        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def topic_changed(self, index):
        if index == 4:
            selected_topic.CustomTopic()
        else:
            self.topic_selected = index

    def difficulty_changed(self, index):
        if index == 3:
            problems.CustomProblem()
        else:
            self.difficulty_selected = index

    def timer_state_change(self):
        if self.timer_checkbox.isChecked():
            setting_timer.Timer()

    def problem_state_change(self):
        if self.problems_checkbox.isChecked():
            setting_problems.NumberOfProblems()

    def start_button(self, toggled):
        self.new_window = questions.Questions(self.topic_selected, self.difficulty_selected)

        if not self.new_window:
            self.new_window = None

app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()