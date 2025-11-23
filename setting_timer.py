from PySide6 import QtWidgets

class Timer(QtWidgets.QInputDialog):
    def __init__(self):
        super().__init__()

        # Set window title & size
        self.setWindowTitle("Set Timer")
        self.resize(300, 50)

        # Set what input is accepted & the label text
        self.setInputMode(QtWidgets.QInputDialog.InputMode.IntInput)
        self.setLabelText("Total Session Length (in seconds):")

        self.intValueSelected.connect(self.user_input)
        self.custom_time = 0

        self.exec()

    def user_input(self, seconds):
        self.custom_time = seconds

    def get_time(self):
        return self.custom_time