from PySide6.QtWidgets import QApplication
import sys
from guessingame import testMainWindow

app = QApplication(sys.argv)
window = testMainWindow(app)


window.show()
app.exec()