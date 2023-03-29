from PyQt5 import QtWidgets
from src.gui.sharedcomnponets.sharedcomponets import GUIToolKit

class Toolbar(QtWidgets.QToolBar):

        def __init__(self,main_window, tabedWidget,  parent=None):
            super().__init__(parent)

            # self.openDBC = QtWidgets.QToolButton(main_window)
            # self.openDBCAction = QtWidgets.QAction(main_window)
            # self.openDBCAction.setIcon(GUIToolKit.getIconByName('open'))
            # self.openDBCAction.triggered.connect(tabedWidget.openFile)
            # self.openDBC.setDefaultAction(self.openDBCAction)
            # self.addWidget(self.openDBC)


            #Select option for choosing data list or plot
            self.selectGraphics = QtWidgets.QToolButton(main_window)
            self.selectGraphics.setIcon(GUIToolKit.getIconByName('add_motor'))
            self.selectGraphics.setObjectName('selectGraphics')
            self.selectGraphics.setPopupMode(QtWidgets.QToolButton.InstantPopup)

            self.selectGraphicsMenu = QtWidgets.QMenu(self.selectGraphics)

            self.addList  = QtWidgets.QAction("List",self.selectGraphicsMenu)
            self.addList.setIcon(GUIToolKit.getIconByName('form'))
            self.addList.triggered.connect(tabedWidget.startList)

            self.addPlot  = QtWidgets.QAction("Plot",self.selectGraphicsMenu)
            self.addPlot.setIcon(GUIToolKit.getIconByName('tree'))
            self.addPlot.triggered.connect(tabedWidget.startPlot)
            
            self.selectGraphicsMenu.addAction(self.addList)
            self.selectGraphicsMenu.addAction(self.addPlot)
            self.selectGraphics.setMenu(self.selectGraphicsMenu)
            self.addWidget(self.selectGraphics)

           
