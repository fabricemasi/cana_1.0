import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Titre")


if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # Instancier et afficher votre fenêtre graphique.
    window = MainWindow()
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())