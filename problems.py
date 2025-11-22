from PySide6 import QtWidgets

class CustomProblem(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # Set window title & size
        self.setWindowTitle("Custom Problem Difficulty")
        self.resize(300, 150)

        # Set overall page layout
        main_layout = QtWidgets.QVBoxLayout()
        second_layout = QtWidgets.QHBoxLayout()
        third_layout = QtWidgets.QHBoxLayout()
        fourth_layout = QtWidgets.QHBoxLayout()

        main_layout.addLayout(second_layout)
        main_layout.addLayout(third_layout)
        main_layout.addLayout(fourth_layout)

        # Set input for number ranges
        self.range_1 = QtWidgets.QInputDialog()
        self.range_1.setInputMode(QtWidgets.QInputDialog.InputMode.TextInput)
        self.range_1.setOption(QtWidgets.QInputDialog.InputDialogOption.NoButtons)
        self.range_1.setLabelText("Enter range of the first number:")
        self.range_1.textValueChanged.connect(self.set_range_1_input)
        self.range_1_value = ""
        second_layout.addWidget(self.range_1)

        self.range_2 = QtWidgets.QInputDialog()
        self.range_2.setInputMode(QtWidgets.QInputDialog.InputMode.TextInput)
        self.range_2.setOption(QtWidgets.QInputDialog.InputDialogOption.NoButtons)
        self.range_2.setLabelText("Enter range of the second number:")
        self.range_2.textValueChanged.connect(self.set_range_2_input)
        self.range_2_value = ""
        third_layout.addWidget(self.range_2)

        # Set okay & cancel buttons
        self.okay = QtWidgets.QPushButton("Okay", parent=self)
        self.okay.clicked.connect(self.submit)
        fourth_layout.addWidget(self.okay)
        self.cancel = QtWidgets.QPushButton("Cancel", parent=self)
        self.cancel.clicked.connect(self.eject)
        fourth_layout.addWidget(self.cancel)

        self.setLayout(main_layout)
        self.exec_()

    def submit(self):
        pass

    def eject(self):
        self.close()

    def set_range_1_input(self, text_value):
        self.range_1_value = text_value

    def set_range_2_input(self, text_value):
        self.range_2_value = text_value

    def get_range_1_2(self):
        return self.range_1_value, self.range_2_value