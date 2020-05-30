import os
import sys
from PySide2 import QtGui, QtWidgets, QtCore
import osUtils

class ClipBrowser(QtWidgets.QWidget):
   def __init__(self):
       super(ClipBrowser, self).__init__()

       self.initUI()

   def initUI(self):
       grid = QtWidgets.QGridLayout()
       movDir = '/Users/christopherbending/Desktop/fbxs'
       movs = osUtils.getFilesOfType(movDir, 'mov')

       self.buttonGroup = QtWidgets.QButtonGroup(self)
       self.buttonGroup.buttonClicked[int].connect(self.keyClick)

       across, down = 0, 0
       for i, mov in enumerate(movs):
           font = QtGui.QFont()
           font.setPointSize(1)

           btn = QtWidgets.QToolButton()
           self.buttonGroup.addButton(btn, ord(str(i)))

           btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
           btn.setText(mov)
           btn.setFont(font)

           icon = QtGui.QIcon()
           thumbnail = mov.replace('mov', 'jpeg')
           icon.addPixmap(QtGui.QPixmap(thumbnail))
           btn.setIcon(icon)
           btn.setIconSize(QtCore.QSize(200, 200))

           grid.addWidget(btn, down, across)
           across += 1

           if across == 4:
               across = 0
               down += 1

           self.setLayout(grid)
           self.show()

   def keyClick(self, key):
       mov = self.buttonGroup.button(key).text()
       os.system('open %s' % mov)


def main():
   app = QtWidgets.QApplication(sys.argv)
   win = ClipBrowser()
   win.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
  main()
