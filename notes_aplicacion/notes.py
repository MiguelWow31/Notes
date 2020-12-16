import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QScrollBar
from PyQt5.QtGui import *
from PyQt5.QtCore import *

qtCreatorFile = "notes.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class VentanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.inicio.clicked.connect(self.notes)
        self.notes = VentanaNotes()

        self.shadow_inicio = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_inicio.setBlurRadius(13)

        self.shadow_opciones = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_opciones.setBlurRadius(13)

        self.inicio.setGraphicsEffect(self.shadow_inicio)
        self.opciones.setGraphicsEffect(self.shadow_opciones)

    def notes(self):
    	self.notes.exec_()


class VentanaNotes(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("notes_2.ui", self)

        self.setFixedSize(651, 551)

        self.shadow_prueba = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_prueba.setBlurRadius(110)
        self.frame.setGraphicsEffect(self.shadow_prueba)
        self.anadir.clicked.connect(self.texto)

        

    def texto(self):
        self.nota_texto = str(self.entrada.text())

        self.lista.setStyleSheet("QListWidget {color: white; font-size: 10px;}")
        
        try:
            self.nota_final = float(self.nota_texto)
            self.lista.addItem(str(self.nota_final))
            self.entrada.setText("")



        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error_contenido", "La informacion ingresada no es valida", QtWidgets.QMessageBox.Ok)



        

        



if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec_())