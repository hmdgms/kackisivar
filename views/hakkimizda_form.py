# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hakkimizda.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HakkimizdaForm(object):
    def setupUi(self, HakkimizdaForm):
        HakkimizdaForm.setObjectName("HakkimizdaForm")
        HakkimizdaForm.resize(615, 300)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(HakkimizdaForm)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 80, 571, 111))
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setEnabled(False)

        self.labelProjeAdi = QtWidgets.QLabel(HakkimizdaForm)
        self.labelProjeAdi.setGeometry(QtCore.QRect(120, 10, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(10)
        self.labelProjeAdi.setFont(font)
        self.labelProjeAdi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelProjeAdi.setStyleSheet("\n"
"\n"
"font: 87 36pt \"Arial Black\";")
        self.labelProjeAdi.setObjectName("labelProjeAdi")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(HakkimizdaForm)
        self.commandLinkButton.setGeometry(QtCore.QRect(450, 200, 141, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(HakkimizdaForm)
        QtCore.QMetaObject.connectSlotsByName(HakkimizdaForm)

    def retranslateUi(self, HakkimizdaForm):
        _translate = QtCore.QCoreApplication.translate
        HakkimizdaForm.setWindowTitle(_translate("HakkimizdaForm", "Hakkında"))
        self.plainTextEdit.setPlainText(_translate("HakkimizdaForm", "Hakkında\n"
"Anlık olarak bina içinde kaç kişi olduğunu istatistiksel olarak gösteren bir uygulamadır.\n"
"\n"
"Uygulamada; kameradan alınan görüntüler anlık olarak işlenip binaya giren ve çıkan kişi sayısı takip edilmektedir."))
        self.labelProjeAdi.setText(_translate("HakkimizdaForm", "KAÇ KİŞİ VAR"))
        self.commandLinkButton.setText(_translate("HakkimizdaForm", "GitHub"))
        self.commandLinkButton.setDescription(_translate("HakkimizdaForm", "Github adresine gitmek için tıklayınız"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HakkimizdaForm = QtWidgets.QWidget()
    ui = Ui_HakkimizdaForm()
    ui.setupUi(HakkimizdaForm)
    HakkimizdaForm.show()
    sys.exit(app.exec_())
