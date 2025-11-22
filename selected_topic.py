from PySide6 import QtWidgets

class CustomTopic(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # Set window title & size
        self.setWindowTitle("Multi-Topic Selection")
        self.resize(300, 150)

        # Set overall page layout
        main_layout = QtWidgets.QVBoxLayout()
        second_layout = QtWidgets.QHBoxLayout()
        third_layout = QtWidgets.QHBoxLayout()

        main_layout.addLayout(second_layout)
        main_layout.addLayout(third_layout)

        # Add checkboxes for selecting topics
        self.addition = QtWidgets.QCheckBox("Addition")
        self.subtraction = QtWidgets.QCheckBox("Subtraction")
        self.multiplication = QtWidgets.QCheckBox("Multiplication")
        self.division = QtWidgets.QCheckBox("Division")
        second_layout.addWidget(self.addition)
        second_layout.addWidget(self.subtraction)
        second_layout.addWidget(self.multiplication)
        second_layout.addWidget(self.division)

        # Add buttons to set the change
        self.okay = QtWidgets.QPushButton("Okay", parent=self)
        self.cancel = QtWidgets.QPushButton("Cancel", parent=self)
        self.okay.clicked.connect(self.submit)
        self.cancel.clicked.connect(self.eject)
        third_layout.addWidget(self.okay)
        third_layout.addWidget(self.cancel)

        self.setLayout(main_layout)
        self.exec_()

    def submit(self):
        pass

    def eject(self):
        self.close()