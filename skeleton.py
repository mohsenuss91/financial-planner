"""
A simple and minimalistic data analytics tool for personal finance.

Olivia Wung
Richard Lu
1.12.14

"""
import pandas
import csv
import sys
import datetime
import os
from PyQt4 import QtGui, QtCore
from operator import itemgetter

class FinanceTool(QtGui.QMainWindow):

	"""should pull and store previous data here"""
	def __init__(self):
		# //FIXME

		# inheriting from parent class qtgui
		super(FinanceTool, self).__init__()

		self.initUI()

	def initUI(self):

		self.pdateText = QtGui.QLineEdit(self)
		self.pdateText.move(50, 50)
		self.pdateText.setText(QtCore.QDate.currentDate().toString("MM/dd/yyyy"))

		self.pdate = QtGui.QPushButton("Date", self)
		self.pdate.move(150, 50)
		self.pdate.clicked.connect(self.inputRange)

		self.amount = QtGui.QLineEdit(self)
		self.amount.move(300, 50)

		self.type = QtGui.QComboBox(self)
		self.type.setSizeAdjustPolicy(0)
		self.type.addItem("Giving")
		self.type.addItem("Groceries")
		self.type.addItem("Eating Out")
		self.type.addItem("Medical")
		self.type.addItem("Leisure")
		self.type.move(400, 50)

		self.save = QtGui.QPushButton("Save", self)
		self.save.move(550, 50)
		self.save.clicked.connect(self.Save)

		# second row
		self.startText = QtGui.QLineEdit(self)
		self.startText.move(50, 100)

		self.start = QtGui.QPushButton("Start Date", self)
		self.start.move(150, 100)
		self.start.clicked.connect(self.inputRange)

		self.endText = QtGui.QLineEdit(self)
		self.endText.move(300, 100)

		self.end = QtGui.QPushButton("End Date", self)
		self.end.move(400, 100)
		self.end.clicked.connect(self.inputRange)

		self.run = QtGui.QPushButton("Analyze", self)
		self.run.move(550, 100)
		self.run.clicked.connect(self.Analyze)

		self.setGeometry(300, 170, 700, 400)
		self.setWindowTitle("Personal Finance Tool")
		self.show()

	def inputRange(self):

		self.check = self.sender()
		self.popup = Calendar(self.check, self.pdateText, self.startText, self.endText)

	def Save(self):
		# save data to csv 
		# str(.currentText())
		if not os.path.exists("Monthly Reports"):
			os.mkdir("Monthly Reports")

		currentCSV = str(QtCore.QDate.currentDate().toString("MM-yyyy"))

		# reads in data
		self.paymentsList = []
		try:
			f = open("Monthly Reports/%s.csv" % currentCSV, "rb")
		except:
			f = open("Monthly Reports/%s.csv" % currentCSV, "wb")
			tempWriter = csv.writer(f)
			tempWriter.writerow(["Date", "Amount", "Type"])
			f.close()
			f = open("Monthly Reports/%s.csv" % currentCSV, "rb")
		reader = csv.reader(f)
		for row in reader:
			self.paymentsList.append(row)
		f.close()

		Date = self.pdateText.text()
		Amount = self.amount.text()
		Type = self.type.currentText()

		LineToWrite = [Date, Amount, Type]

		self.paymentsList.append(LineToWrite)
		self.newPaymentsList = [self.paymentsList[0]] + sorted(self.paymentsList[1:], key=itemgetter(0, 2))
	
		f = open("Monthly Reports/%s.csv" % currentCSV, "wb")
		writer = csv.writer(f)
		for row in self.newPaymentsList:
			writer.writerow(row)
		f.close()

		self.amount.setText("")

	def Analyze(self):
		# general summary statistics here
		# add a check if end date is after start date
		return  

class Calendar(QtGui.QWidget):

	def __init__(self, check, pdate, startText, endText):

		super(Calendar, self).__init__()
		self.check = check
		self.pdateText = pdate
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
		elif self.check.text() == "End Date":
			self.endText.setText(self.date.toString("MM/dd/yyyy"))
		else: 
			self.pdateText.setText(self.date.toString("MM/dd/yyyy"))

		self.close()


# runs the script
def main():
	app = QtGui.QApplication(sys.argv)
	ex = FinanceTool()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()




