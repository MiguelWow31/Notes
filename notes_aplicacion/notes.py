import sys
from time import sleep
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QScrollBar
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
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
        self.opciones.clicked.connect(self.show_opciones)
        self.notes = VentanaNotes()
        self.opciones_menu = Ventana_Opciones()

        self.shadow_inicio = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_inicio.setBlurRadius(13)

        self.shadow_opciones = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_opciones.setBlurRadius(13)

        self.inicio.setGraphicsEffect(self.shadow_inicio)
        self.opciones.setGraphicsEffect(self.shadow_opciones)



    def notes(self):
    	self.notes.exec_()

    def show_opciones(self):
        self.opciones_menu.exec_()


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




        

class Pantalla_Carga(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("Pantalla_Carga.ui", self)

        self.setWindowTitle("Pantalla de carga")

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        self.icono.setGraphicsEffect(shadow)
        self.icono.setIcon(QIcon("imagenes/-pen_96740.ico"))

        #Asi borramos tanto el marco de ventana, como el fondo
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Configuramos el tiempo de la barra de carga
        self.reloj = QTimer()
        self.reloj.timeout.connect(self.barra_carga)
        self.reloj.start(45)

        self.show()

    def barra_carga(self):

        for i in range(1, 101):
            sleep(0.5)

            self.progressBar.setValue(i)

        self.reloj.stop()
        self.close()

        self.ventana_main = VentanaPrincipal()
        self.ventana_main.show()


class Ventana_Opciones(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        uic.loadUi("opciones.ui", self)
        self.setFixedSize(407, 417)

        self.setWindowTitle("Menu Opciones")

        shadow_icono = QGraphicsDropShadowEffect()
        shadow_icono.setBlurRadius(25)

        shadow_frame = QGraphicsDropShadowEffect()
        shadow_frame.setBlurRadius(25)

        shadow_frame2 = QGraphicsDropShadowEffect()
        shadow_frame2.setBlurRadius(25)

        self.icono.setGraphicsEffect(shadow_icono)
        self.frame.setGraphicsEffect(shadow_frame)
        self.frame_2.setGraphicsEffect(shadow_frame2)

        self.sistema.addItem(QIcon("imagenes/pais_sistema/venezuela.ico"), "Venezuela-Liceo")
        self.sistema.addItem(QIcon("imagenes/pais_sistema/colombia.ico"), "Colombia")

        self.exportacion.addItem("Si")
        self.exportacion.addItem("No")










        






if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Pantalla_Carga()
    sys.exit(app.exec_())