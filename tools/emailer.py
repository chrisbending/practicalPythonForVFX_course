import sys
from PySide2 import QtUiTools, QtWidgets
import yagmail

class EmailWidget(QtWidgets.QWidget):
   def __init__(self):
       super(EmailWidget, self).__init__()

       ui_file = '/Users/christopherbending/Desktop/tutorialTools/ui/emailer.ui'
       self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)

       self.ui.send.clicked.connect(self.send)

   def send(self):
       yag = yagmail.SMTP('chrispbending@gmail.com')
       to = self.ui.toLE.text()
       subject = self.ui.subjectLE.text()
       body = self.ui.bodyTE.toPlainText()
       yag.send(to, subject, body)

def main():
   app = QtWidgets.QApplication(sys.argv)
   win = EmailWidget()
   win.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
  main()
