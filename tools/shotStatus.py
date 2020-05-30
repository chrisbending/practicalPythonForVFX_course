import sys
import os
import json
from PySide2 import QtCore, QtUiTools, QtWidgets
import csv

jsonFile = '/Users/christopherbending/Desktop/shotStatus.json'

artists = ['bob', 'frank', 'anne']
shotStatus = ['to do', 'in progress', 'review', 'approved']

class ShotStatusWidget(QtWidgets.QWidget):
   def __init__(self):
       super(ShotStatusWidget, self).__init__()
       ui_file = '/Users/christopherbending/Desktop/tutorialTools/ui/shotStatus.ui'
       self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)

       self.ui.saveBtn.clicked.connect(self.saveJson)
       self.ui.reportBtn.clicked.connect(self.generateCSV)

       self.shotStatus = {}
       with open(jsonFile) as json_file:
           self.shotStatus = json.load(json_file)

       self.populate()

   def populate(self):
       self.ui.shotStatusTreeWidget.clear()
       for sequence in self.shotStatus:
           for shot, details in self.shotStatus[sequence].iteritems():

               self.artistComboBox = QtWidgets.QComboBox(self)
               self.artistComboBox.addItems(artists)

               artist = self.shotStatus[sequence][shot]['artist']
               index = self.artistComboBox.findText(artist, QtCore.Qt.MatchFixedString)
               self.artistComboBox.setCurrentIndex(index)

               self.statusComboBox = QtWidgets.QComboBox(self)
               self.statusComboBox.addItems(shotStatus)

               artist = self.shotStatus[sequence][shot]['status']
               index = self.statusComboBox.findText(artist, QtCore.Qt.MatchFixedString)
               self.statusComboBox.setCurrentIndex(index)

               item = QtWidgets.QTreeWidgetItem(self.ui.shotStatusTreeWidget, [sequence, shot, '', ''])
               self.ui.shotStatusTreeWidget.setItemWidget(item, 2, self.artistComboBox)
               self.ui.shotStatusTreeWidget.setItemWidget(item, 3, self.statusComboBox)

   def saveJson(self):
       root = self.ui.shotStatusTreeWidget.invisibleRootItem()
       child_count = root.childCount()

       for i in xrange(child_count):
           item = root.child(i)
           sequence = item.text(0)
           shot = item.text(1)

           artistComboBox = self.ui.shotStatusTreeWidget.itemWidget(item, 2)
           statusComboBox = self.ui.shotStatusTreeWidget.itemWidget(item, 3)

           self.shotStatus[sequence][shot]['artist'] = artistComboBox.currentText()
           self.shotStatus[sequence][shot]['status'] = statusComboBox.currentText()

       jsonStr = json.dumps(self.shotStatus, indent=4)
       with open(jsonFile, 'w') as f:
           f.write(jsonStr)

       QtWidgets.QMessageBox.information(QtWidgets.QMessageBox(), 'JSON stored', 'Shot data updated:\n%s' % jsonFile, QtWidgets.QMessageBox.Ok)

   def generateCSV(self):
       with open(jsonFile.replace('.json', '.csv'), 'wb') as csvfile:
           fileWriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           fileWriter.writerow(['sequence', 'shot', 'artist', 'status'])

           for sequence in self.shotStatus:
               for shot, details in self.shotStatus[sequence].iteritems():
                   fileWriter.writerow([sequence, shot, details['artist'], details['status']])


def main():
   app = QtWidgets.QApplication(sys.argv)
   app.setStyle('plastique')
   win = ShotStatusWidget()
   win.show()
   sys.exit(app.exec_())

main()
