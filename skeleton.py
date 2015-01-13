"""
A simple and minimalistic data analytics tool for personal finance.

Olivia Wung
Richard Lu
1.12.14

"""
import pandas
import csv
import sys
from PyQt4 import QtGui, QtCore
from operator import itemgetter

class FinanceTool(QtGui.QMainWindow):

	"""should pull and store previous data here"""
	def __init__(self):
		# //FIXME

		# inheriting from parent class qtgui
		super(FinanceTool, self).__init__()

		self.initUI()

		# # reads in data
		# self.aList = []
		# f = open("/////.csv", "rb")
		# reader = csv.reader(f)
		# for row in reader:
		# 	self.aList.append(row)
		# f.close()


		# # to sort data
		# this = sorted(aList, key=itemgetter(0, 2))

	def initUI(self):

		self.startText = QtGui.QLineEdit(self)
		self.startText.move(50, 100)

		self.start = QtGui.QPushButton("Start Date", self)
		self.start.move(150, 100)
		self.start.clicked.connect(self.inputRange)

		self.endText = QtGui.QLineEdit(self)
		self.endText.move(350, 100)

		self.end = QtGui.QPushButton("End Date", self)
		self.end.move(450, 100)
		self.end.clicked.connect(self.inputRange)

		self.run = QtGui.QPushButton("Run", self)
		self.run.move(650, 100)
		self.run.clicked.connect(self.Run)

		self.setGeometry(300, 170, 800, 400)
		self.setWindowTitle("Personal Finance Tool")
		self.show()

	def inputRange(self):

		self.check = self.sender()
		self.popup = Calendar(self.check, self.startText, self.endText)

	def Run(self):
		return  

class Calendar(QtGui.QWidget):

	def __init__(self, check, startText, endText):

		super(Calendar, self).__init__()
		self.check = check
		self.startText = startText
		self.endText = endText
		self.initUI()

	def initUI(self):

		self.calendar = QtGui.QCalendarWidget(self)
		self.calendar.setGridVisible(True)
		self.calendar.move(20, 20)
		self.calendar.clicked[QtCore.QDate].connect(self.saveDate)

		self.setGeometry(400, 300, 500, 220)
		self.setWindowTitle("Select a Date")
		self.show()

	def saveDate(self):
		self.date = self.calendar.selectedDate()
		if self.check.text() == "Start Date":
			self.startText.setText(self.date.toString("MM/dd/yyyy"))
		else:
			self.endText.setText(self.date.toString("MM/dd/yyyy"))

		self.close()


# runs the script
def main():
	app = QtGui.QApplication(sys.argv)
	ex = FinanceTool()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()




