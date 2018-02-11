#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtWidgets import (QDialog, QDialogButtonBox, QLabel, QLineEdit,
                             QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QApplication)
import datetime
import pickle
import os


class Cliente:

    def __init__(self, nombre, identificador, Gastado):
        self.Nombre = nombre
        self.ID = identificador
        self.GastoAcumulado = Gastado

    def __getstate__(self):
        # Serialización
        nueva = self.__dict__.copy()
        nueva.update({"UltimaCompra": str(datetime.datetime)})
        return nueva

    def __setstate__(self, state):
        # Deserialización
        self.__dict__ = state

    def actualizarGasto(self, gastado):
        self.GastoAcumulado += gastado


class VentanaCajero(QDialog):

    def __init__(self, parent=None, username=""):
        super(VentanaCajero, self).__init__(parent)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.clienteLabel = QLabel("Nombre cliente", self)
        self.clienteText = QLineEdit(self)
        self.idLabel = QLabel("RUT", self)
        self.idText = QLineEdit(self)
        self.gastadoLabel = QLabel("Gastado", self)
        self.gastadoText = QLineEdit(self)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(self.clienteLabel)
        self.verticalLayout.addWidget(self.clienteText)
        self.verticalLayout.addWidget(self.idLabel)
        self.verticalLayout.addWidget(self.idText)
        self.verticalLayout.addWidget(self.gastadoLabel)
        self.verticalLayout.addWidget(self.gastadoText)
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.serializarCliente)
        self.buttonBox.rejected.connect(self.close)

    def serializarCliente(self):
        #####

        ID_cliente = self.idText.text()
        Archivo_cliente = str(ID_cliente) + ".walkcart"

        # Verificamos si cliente existe en DB
        if Archivo_cliente in os.listdir("ClientesDB"):

            # Existe -> Abrimos, cambiamos y cerramos

            with open("ClientesDB/" + Archivo_cliente, "rb") as file:
                cliente_existente = pickle.load(file)

            cliente_existente.actualizarGasto(int(self.gastadoText.text()))

            with open("ClientesDB/" + Archivo_cliente, "wb") as file:
                pickle.dump(cliente_existente, file)

        else:
            # No existe -> Creamos y cerramos
            nuevo_cliente = Cliente(
                self.clienteText.text(),
                int(self.idText.text()),
                int(self.gastadoText.text())
            )

            nuevo_archivo = "ClientesDB/" + str(nuevo_cliente.ID) + ".walkcart"

            with open(nuevo_archivo, "wb") as file:
                pickle.dump(nuevo_cliente)
        #####

        self.clienteText.setText("")
        self.idText.setText("")
        self.gastadoText.setText("")


class VentanaAdmin(QDialog):

    def __init__(self, parent=None):
        super(VentanaAdmin, self).__init__(parent)

        self.archivoButton = QPushButton("TOP")
        self.archivoButton.clicked.connect(self.generarArchivo)

        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.close)

        self.horizontalLayout = QVBoxLayout(self)
        self.horizontalLayout.addWidget(self.archivoButton)
        self.horizontalLayout.addWidget(self.cancelButton)

    def generarArchivo(self):
        #####

        # Tomamos una lista con todos los clientes

        cliente_TOP = False

        for file_ in os.listdir("ClientesDB"):
            if file_.endswith(".walkcart"):
                with open("ClientesDB/" + file_, "rb") as file:
                    nuevo_cliente = pickle.load(file)
                    if not cliente_TOP:
                        cliente_TOP = nuevo_cliente
                    else:
                        if cliente_TOP.GastoAcumulado <= nuevo_cliente:
                            cliente_TOP = nuevo_cliente

        Top = cliente_TOP
        # Serializamos

        import json

        with open("TOP.walkcart", "w") as file_:
            json.dump(Top.__dict__, file_)

    #####


class Input(QWidget):

    def __init__(self, parent=None):
        super(Input, self).__init__(parent)

        self.userNameText = QLineEdit(self)

        self.pushButtonWindow = QPushButton(self)
        self.pushButtonWindow.setText("Iniciar Sesión")
        self.pushButtonWindow.clicked.connect(self.on_pushButton_clicked)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.userNameText)
        self.layout.addWidget(self.pushButtonWindow)

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        #####

        # Obtenemos el input dado
        Usuario = self.userNameText.text()

        # Tomamos la lista de cajeros
        with open("cajeros.walkcart", "rb") as file:
            CajerosAutorizados = pickle.load(file)

        print(CajerosAutorizados)

        # Identificación de usuario
        if Usuario == "WalkcartUnlimited":
            # Interfaz para admin
            self.ventanaUsuario = VentanaAdmin(self)
            self.hide()
            self.ventanaUsuario.show()
        elif Usuario in CajerosAutorizados:
            # Interfaz para cajero
            self.ventanaUsuario = VentanaCajero(
                self, username=self.userNameText.text())
            self.hide()
            self.ventanaUsuario.show()

        #####


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('Log-in WM')

    main = Input()
    main.show()

    sys.exit(app.exec_())
