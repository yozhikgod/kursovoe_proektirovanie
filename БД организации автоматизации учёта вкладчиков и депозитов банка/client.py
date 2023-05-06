# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.twStaffs = QtWidgets.QTableWidget(self.centralwidget)
        self.twStaffs.setGeometry(QtCore.QRect(0, 260, 691, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.twStaffs.setFont(font)
        self.twStaffs.setObjectName("twStaffs")
        self.twStaffs.setColumnCount(0)
        self.twStaffs.setRowCount(0)
        self.pbFind = QtWidgets.QPushButton(self.centralwidget)
        self.pbFind.setGeometry(QtCore.QRect(460, 117, 75, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pbFind.setFont(font)
        self.pbFind.setObjectName("pbFind")
        self.cbColNames = QtWidgets.QComboBox(self.centralwidget)
        self.cbColNames.setGeometry(QtCore.QRect(460, 55, 167, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbColNames.sizePolicy().hasHeightForWidth())
        self.cbColNames.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbColNames.setFont(font)
        self.cbColNames.setObjectName("cbColNames")
        self.leFind = QtWidgets.QLineEdit(self.centralwidget)
        self.leFind.setEnabled(True)
        self.leFind.setGeometry(QtCore.QRect(460, 86, 167, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leFind.sizePolicy().hasHeightForWidth())
        self.leFind.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leFind.setFont(font)
        self.leFind.setObjectName("leFind")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(520, 30, 44, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(360, 50, 86, 92))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbOpen = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbOpen.sizePolicy().hasHeightForWidth())
        self.pbOpen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbOpen.setFont(font)
        self.pbOpen.setMouseTracking(False)
        self.pbOpen.setTabletTracking(False)
        self.pbOpen.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pbOpen.setAutoDefault(False)
        self.pbOpen.setObjectName("pbOpen")
        self.verticalLayout.addWidget(self.pbOpen)
        self.pbInsert = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbInsert.sizePolicy().hasHeightForWidth())
        self.pbInsert.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbInsert.setFont(font)
        self.pbInsert.setMouseTracking(False)
        self.pbInsert.setTabletTracking(False)
        self.pbInsert.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pbInsert.setAutoDefault(False)
        self.pbInsert.setObjectName("pbInsert")
        self.verticalLayout.addWidget(self.pbInsert)
        self.pbDelete = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbDelete.sizePolicy().hasHeightForWidth())
        self.pbDelete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbDelete.setFont(font)
        self.pbDelete.setMouseTracking(False)
        self.pbDelete.setTabletTracking(False)
        self.pbDelete.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pbDelete.setAutoDefault(False)
        self.pbDelete.setObjectName("pbDelete")
        self.verticalLayout.addWidget(self.pbDelete)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 0, 323, 254))
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leFio = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leFio.setFont(font)
        self.leFio.setObjectName("leFio")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leFio)
        self.label_9 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.leFio_2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leFio_2.setFont(font)
        self.leFio_2.setObjectName("leFio_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leFio_2)
        self.label_10 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.leFio_3 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leFio_3.setFont(font)
        self.leFio_3.setObjectName("leFio_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.leFio_3)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.rbFemale = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbFemale.setFont(font)
        self.rbFemale.setObjectName("rbFemale")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rbFemale)
        self.rbMale = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbMale.setFont(font)
        self.rbMale.setObjectName("rbMale")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rbMale)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.formLayout)
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.sbAge = QtWidgets.QDateEdit(self.widget)
        self.sbAge.setObjectName("sbAge")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sbAge)
        self.label_4 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lePhone = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lePhone.setFont(font)
        self.lePhone.setToolTip("")
        self.lePhone.setInputMask("")
        self.lePhone.setObjectName("lePhone")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lePhone)
        self.label_5 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.leEmail = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leEmail.setFont(font)
        self.leEmail.setObjectName("leEmail")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.leEmail)
        self.label_6 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.sbAge_2 = QtWidgets.QDateEdit(self.widget)
        self.sbAge_2.setObjectName("sbAge_2")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.sbAge_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbFind.setText(_translate("MainWindow", "Найти"))
        self.label_8.setText(_translate("MainWindow", "Поиск"))
        self.pbOpen.setText(_translate("MainWindow", "Открыть"))
        self.pbInsert.setText(_translate("MainWindow", "Добавить"))
        self.pbDelete.setText(_translate("MainWindow", "Удалить"))
        self.label.setText(_translate("MainWindow", "Фамилия:"))
        self.label_9.setText(_translate("MainWindow", "Имя:"))
        self.label_10.setText(_translate("MainWindow", "Отчестов:"))
        self.label_2.setText(_translate("MainWindow", "Пол:"))
        self.rbFemale.setText(_translate("MainWindow", "Ж"))
        self.rbMale.setText(_translate("MainWindow", "М"))
        self.label_3.setText(_translate("MainWindow", "Дата рождения:"))
        self.label_4.setText(_translate("MainWindow", "Телефон:"))
        self.label_5.setText(_translate("MainWindow", "Почта:"))
        self.label_6.setText(_translate("MainWindow", "Дата регистрации"))
