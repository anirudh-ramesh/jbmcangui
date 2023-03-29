from PyQt5 import QtWidgets, QtCore
from src.gui.mainWindow import UserInteractionMainWindow
import sys
import logging
from threading import *

if __name__ == '__main__':
    try:
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) 
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
        logging.basicConfig(filename='.Graphs.log', filemode='w',
                         format='%(name)s - %(levelname)s - %(message)s')
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QtWidgets.QMainWindow()
        userInteractionMainWindow = UserInteractionMainWindow()
        userInteractionMainWindow.setupUi(mainWindow)
        mainWindow.show()
        app.exec_()
        for thread in enumerate(): 
            print(thread.name)
        sys.exit()
    except Exception as exception:\
    logging.error(exception, exc_info=True)