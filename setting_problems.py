from PySide6 import QtWidgets

class NumberOfProblems(QtWidgets.QInputDialog):
    def __init__(self):
        super().__init__()

        # Set window title & size
        self.setWindowTitle("Set Number Of Problems")
        self.resize(300, 50)

        # Set what input is accepted & the label text
        self.setInputMode(QtWidgets.QInputDialog.InputMode.IntInput)
        self.setLabelText("Total Number of Problems:")

        self.intValueSelected.connect(self.user_input)
        self.num_of_probs = 0

        self.exec()

    def user_input(self, problems):
        self.num_of_probs = problems