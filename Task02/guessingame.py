from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QWidget, QHBoxLayout, QVBoxLayout, QLabel,QLineEdit
import random

class testMainWindow (QMainWindow):
    def __init__(self,app):
        super().__init__()

        self.app = app
        self.setWindowTitle("Guessing Game")
        self.setGeometry(100,100,400,200)

        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        self.menu = self.menuBar()
        self.filemenu = self.menu.addMenu("&File")
        self.helpmenu = self.menu.addMenu("&Help")
        self.aboutAct = self.helpmenu.addAction("About")
        self.quitAct = self.filemenu.addAction("Quit")
        self.quitAct.triggered.connect(self.app_quit)
        self.aboutAct.triggered.connect(self.about_act)

        self.Layoutset = QVBoxLayout(self.mainWidget)

        self.inVlayout = QHBoxLayout()
        self.Layoutset.addLayout(self.inVlayout)

        self.label = QLabel("Number Guessing Game\n I have Selected a number between 1 to 10")
        self.attemptlabel = QLabel("Attempts : ")
        self.inVlayout.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)

        self.Layoutset.addWidget(self.attemptlabel)
        self.attemptlabel.setAlignment(Qt.AlignCenter)

        self.line_edit = QLineEdit(self)
        self.Layoutset.addWidget(self.line_edit)
        

        self.guessbutton = QPushButton("Guess !")
        self.guessbutton.clicked.connect(self.game)
        self.Layoutset.addWidget(self.guessbutton)
        self.secret_number = random.randint(1, 10)

        #Debugging
        # print(self.secret_number)
        # print(type(self.secret_number)) Debugging
        self.attempts = 0

    def game(self):
        try:
            guess = int(self.line_edit.text())

            # print(type(guess))
            # print(guess) Debugging

            self.attempts += 1
            self.attemptlabel.setText(f"Attempts : {str(self.attempts)} ")

            if guess < self.secret_number:
                QMessageBox.critical(self,"Wrong","Too low! Try Again.",QMessageBox.Ok)
            elif guess > self.secret_number:
                QMessageBox.critical(self,"Wrong","Too high! Try again.",QMessageBox.Ok)
                if guess > 10:
                    QMessageBox.critical(self,"Wrong","Enter Number Between Given Criteria",QMessageBox.Ok)
            else:
                QMessageBox.information(self,"Congrats",f"Congratulations! You guessed the number in {self.attempts} attempts.",QMessageBox.Ok)
        except ValueError:
            QMessageBox.critical(self,"Wrong","Invalid input. Please enter a valid integer.",QMessageBox.Ok)
        
    def app_quit(self):
        self.app.quit()

    def about_act (self):
        QMessageBox.information(self,"About","This is a guessing game for internship purposes",QMessageBox.Ok)
        






