# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CrawlingUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DomecallCrawling(object):
    def setupUi(self, DomecallCrawling):
        DomecallCrawling.setObjectName("DomecallCrawling")
        DomecallCrawling.resize(586, 598)
        DomecallCrawling.setMinimumSize(QtCore.QSize(383, 436))
        self.centralwidget = QtWidgets.QWidget(DomecallCrawling)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 561, 524))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.sub_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.sub_layout.setContentsMargins(0, 0, 0, 0)
        self.sub_layout.setObjectName("sub_layout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_2.addWidget(self.textBrowser_3, 1, 0, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout_2.addWidget(self.textBrowser_4, 1, 1, 1, 1)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.gridLayout_2.addWidget(self.textBrowser_7, 3, 0, 1, 1)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout_2.addWidget(self.textBrowser_5, 2, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_2.addWidget(self.textBrowser_2, 0, 1, 1, 1)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout_2.addWidget(self.textBrowser_6, 2, 1, 1, 1)
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.gridLayout_2.addWidget(self.textBrowser_1, 0, 0, 1, 1)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.gridLayout_2.addWidget(self.textBrowser_8, 3, 1, 1, 1)
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.gridLayout_2.addWidget(self.textBrowser_10, 4, 1, 1, 1)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.gridLayout_2.addWidget(self.textBrowser_9, 4, 0, 1, 1)
        self.sub_layout.addLayout(self.gridLayout_2)
        self.select_layout = QtWidgets.QHBoxLayout()
        self.select_layout.setObjectName("select_layout")
        self.set_grid_layout = QtWidgets.QGridLayout()
        self.set_grid_layout.setObjectName("set_grid_layout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_groupcode = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_groupcode.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.lineEdit_groupcode.setObjectName("lineEdit_groupcode")
        self.gridLayout.addWidget(self.lineEdit_groupcode, 0, 1, 1, 1)
        self.pw_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        self.pw_label_2.setFont(font)
        self.pw_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.pw_label_2.setObjectName("pw_label_2")
        self.gridLayout.addWidget(self.pw_label_2, 1, 0, 1, 1)
        self.lineEdit_datecode = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_datecode.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_datecode.setObjectName("lineEdit_datecode")
        self.gridLayout.addWidget(self.lineEdit_datecode, 1, 1, 1, 1)
        self.id_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        self.id_label_2.setFont(font)
        self.id_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.id_label_2.setObjectName("id_label_2")
        self.gridLayout.addWidget(self.id_label_2, 0, 0, 1, 1)
        self.set_grid_layout.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.select_layout.addLayout(self.set_grid_layout)
        self.radio_layout = QtWidgets.QVBoxLayout()
        self.radio_layout.setObjectName("radio_layout")
        self.select_layout.addLayout(self.radio_layout)
        self.sub_layout.addLayout(self.select_layout)
        self.star_stop_layout = QtWidgets.QHBoxLayout()
        self.star_stop_layout.setObjectName("star_stop_layout")
        self.MacroStart_bt = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.MacroStart_bt.setObjectName("MacroStart_bt")
        self.star_stop_layout.addWidget(self.MacroStart_bt)
        self.MacroSop_bt = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.MacroSop_bt.setObjectName("MacroSop_bt")
        self.star_stop_layout.addWidget(self.MacroSop_bt)
        self.sub_layout.addLayout(self.star_stop_layout)
        DomecallCrawling.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DomecallCrawling)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 24))
        self.menubar.setObjectName("menubar")
        DomecallCrawling.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DomecallCrawling)
        self.statusbar.setObjectName("statusbar")
        DomecallCrawling.setStatusBar(self.statusbar)

        self.retranslateUi(DomecallCrawling)
        self.MacroStart_bt.clicked.connect(DomecallCrawling.start) # type: ignore
        self.MacroSop_bt.clicked.connect(DomecallCrawling.stop) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DomecallCrawling)
        DomecallCrawling.setTabOrder(self.lineEdit_groupcode, self.lineEdit_datecode)
        DomecallCrawling.setTabOrder(self.lineEdit_datecode, self.MacroStart_bt)
        DomecallCrawling.setTabOrder(self.MacroStart_bt, self.MacroSop_bt)

    def retranslateUi(self, DomecallCrawling):
        _translate = QtCore.QCoreApplication.translate
        DomecallCrawling.setWindowTitle(_translate("DomecallCrawling", "MainWindow"))
        self.lineEdit_groupcode.setPlaceholderText(_translate("DomecallCrawling", "A2"))
        self.pw_label_2.setText(_translate("DomecallCrawling", "<html><head/><body><p>마지막 번호</p></body></html>"))
        self.lineEdit_datecode.setPlaceholderText(_translate("DomecallCrawling", "A16533"))
        self.id_label_2.setText(_translate("DomecallCrawling", "<html><head/><body><p>시작 번호</p></body></html>"))
        self.MacroStart_bt.setText(_translate("DomecallCrawling", "매크로 시작"))
        self.MacroSop_bt.setText(_translate("DomecallCrawling", "매크로 중지"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DomecallCrawling = QtWidgets.QMainWindow()
    ui = Ui_DomecallCrawling()
    ui.setupUi(DomecallCrawling)
    DomecallCrawling.show()
    sys.exit(app.exec_())