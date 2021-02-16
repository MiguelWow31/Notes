import sys
import json
import docx
import os
from time import sleep
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

qtCreatorFile = os.path.abspath("ui/notes.ui")

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
        self.shadow_inicio.setBlurRadius(15)

        self.shadow_opciones = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_opciones.setBlurRadius(15)

        self.inicio.setGraphicsEffect(self.shadow_inicio)
        self.opciones.setGraphicsEffect(self.shadow_opciones)



    def notes(self):
    	self.notes.exec_()

    def show_opciones(self):
        self.opciones_menu.exec_()


class VentanaNotes(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi(os.path.abspath("ui/notes_2.ui"), self)

        self.setFixedSize(651, 551)

        self.shadow_prueba = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_prueba.setBlurRadius(110)
        self.frame.setGraphicsEffect(self.shadow_prueba)
        self.anadir.clicked.connect(self.texto)
        self.button_promedio.clicked.connect(self.promedio)

        scroll = QScrollBar()
        self.lista.setVerticalScrollBar(scroll)
        self.config()

    def config(self):
        print(os.listdir())


    def promedio(self):

        if self.lista.count() == 0 or self.lista.count() < 2:
            QtWidgets.QMessageBox.warning(self, "Error_numero_notas", "No hay suficientes notas para sacar el promedio", QtWidgets.QMessageBox.Ok)

        else:
            lista_notas = [str(self.lista.item(i).text()[9:12]) for i in range(self.lista.count())]
            float_notas = map(lambda nota: float(nota), lista_notas)
            promedio_text = sum(float_notas) / self.lista.count()
            self.nota.setText(str(promedio_text))
            



    def texto(self):
        self.nota_texto = str(self.entrada.text())

        try:
            self.nota_final = float(self.nota_texto)

            if self.nota_final > 0.9 and self.nota_final < 5.1:
                mala = QIcon("imagenes/calificacion/bueno.ico")
                intermedia = QIcon("imagenes/calificacion/intermedio.ico")
                buena = QIcon("imagenes/calificacion/malo.ico")

                count_lista = str(self.lista.count() + 1)
                elemento = QListWidgetItem(f"Nota {count_lista} - {self.nota_final}", self.lista)
                elemento.setTextAlignment(Qt.AlignCenter)
                self.lista.setIconSize(QSize(40, 40))

                if self.nota_final > 3.9:
                    elemento.setIcon(mala)

                elif self.nota_final > 2.9 and self.nota_final < 4.0:
                    elemento.setIcon(intermedia)

                elif self.nota_final < 3.0:
                    elemento.setIcon(buena)

                self.lista.addItem(elemento)
                self.entrada.setText("") 
            else:
                raise ValueError
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error_contenido", "La informacion ingresada no es valida", QtWidgets.QMessageBox.Ok)

        

class Pantalla_Carga(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi(os.path.abspath("ui/pantalla_carga.ui") , self)

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
        sleep_time = 0.09
        for i in range(1, 101):
            sleep(0.09)
            self.progressBar.setValue(i)

        self.reloj.stop()
        self.close()
        self.ventana_main = VentanaPrincipal()
        self.ventana_main.show()


class Ventana_Opciones(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        uic.loadUi(os.path.abspath("ui/opciones.ui"), self)
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

        self.aplicar.clicked.connect(self.configuracion)
        self.cancelar.clicked.connect(self.salir)

    def salir(self):
        self.close()

    def configuracion(self):

        content_sys = self.sistema.currentText()
        content_export = self.exportacion.currentText()

        dict_config = {"system":content_sys, "export":content_export}

        with open("config.txt", "w") as file:
            json.dump(dict_config, file)

      









if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Pantalla_Carga()
    sys.exit(app.exec_())
