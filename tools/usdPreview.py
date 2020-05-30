import os
import sys
import osUtils
from PySide2 import QtCore, QtUiTools, QtWidgets, QtGui

def createUsdPreviews(dr):
    usds = osUtils.getFilesOfType(dr, 'usd')
    usds = [usd for usd in usds if 'usd_shot' in usd]

    for usd in usds:
        start, end = 1, 75
        camera = 'shotCamera'

        usdDir = os.path.dirname(usd)
        destDir = os.path.join(usdDir, 'preview')

        if not os.path.isdir(destDir):
            os.mkdir(destDir)

        cmd = 'usdrecord --frames %s:%s --camera %s --imageWidth 1920 %s %s' % (start, end, camera, usd, destDir + '/tmp.####.png')
        os.system(cmd)

        imageSeq = os.path.join(destDir, 'tmp.####.png')
        os.system('/Applications/ffmpeg -r 24 -i %s %s' % (imageSeq.replace('####', '%04d'), imageSeq.replace('####.png', 'mov')))


class UsdPreviewWidget(QtWidgets.QWidget):
    def __init__(self):
        super(UsdPreviewWidget,self).__init__()
        ui_file = '/Users/christopherbending/Desktop/tutorialTools/ui/usdPreview.ui'
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)

        self.ui.createPreviewsBtn.clicked.connect(self.createPreviews)

        self.ui.usdLineEdit.textChanged.connect(self.refresh)
        self.ui.imageSeqListWidget.doubleClicked.connect(self.play)

        self.ui.imageSeqListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.imageSeqListWidget.customContextMenuRequested.connect(self.openMenu)

        self.refresh()

    def createPreviews(self):
        usdDir = self.ui.usdLineEdit.text()
        createUsdPreviews(usdDir)

    def refresh(self):
        self.ui.imageSeqListWidget.clear()

        usdDir = self.ui.usdLineEdit.text()
        if usdDir:
            for dr in os.listdir(usdDir):
                if os.path.isdir(os.path.join(usdDir, dr)):
                    self.ui.imageSeqListWidget.addItem(os.path.join(usdDir, dr))

    def play(self):
        usdDir = self.ui.usdLineEdit.text()
        sel = self.ui.imageSeqListWidget.selectedItems()
        preview = os.path.join(usdDir, sel[0].text(), 'preview', 'tmp.mov')

        os.system('/Applications/VLC.app/Contents/MacOS/VLC %s' % preview)

    def openMenu(self, position):
        menu = QtWidgets.QMenu(self)
        menu.addAction('open', self.open)
        menu.addAction('play', self.play)

        menu.exec_(self.ui.imageSeqListWidget.viewport().mapToGlobal(position))

    def open(self):
        usdDir = self.ui.usdLineEdit.text()
        sel = self.ui.imageSeqListWidget.selectedItems()

        shotDir = os.path.join(usdDir, sel[0].text())
        usds = osUtils.getFilesOfType(shotDir, 'usd')
        os.system('usdview %s' % usds[0])


def main():
    """ Creates the QApplication and shows the mainWindow
    """
    app = QtWidgets.QApplication(sys.argv)
    win = UsdPreviewWidget()
    win.show()
    sys.exit(app.exec_())

main()
