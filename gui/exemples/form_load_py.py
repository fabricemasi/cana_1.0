import sys

from PySide6 import QtWidgets as qtw

from gui.UI.form_main_window import Ui_main_window
# binv = os.environ["BINV"]
binv = "cana_1.0"


# class MainWindow(QMainWindow):
class MainWindow(qtw.QWidget, Ui_main_window):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # self.show()


        self.setWindowTitle(binv)





if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = qtw.QApplication(sys.argv)

    # Instancier et afficher votre fenêtre graphique.
    window = MainWindow()
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())
