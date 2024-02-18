import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap


class ImageViewer(QWidget):
    def __init__(self, image_paths):
        super().__init__()

        self.image_paths = image_paths

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Image Viewer")

        main_layout = QVBoxLayout(self)

        # Créer un layout pour contenir les images
        image_layout = QHBoxLayout()

        current_row_width = 0
        max_row_width = self.width()  # Largeur maximale de la fenêtre

        for image_path in self.image_paths:
            pixmap = QPixmap(image_path)

            if not pixmap.isNull():
                label = QLabel()
                label.setPixmap(pixmap.scaledToWidth(200))  # Redimensionner l'image pour l'afficher dans la fenêtre

                image_layout.addWidget(label)

                # Calculer la largeur actuelle de la ligne d'images
                current_row_width += label.width()

                if current_row_width > max_row_width:
                    main_layout.addLayout(image_layout)
                    image_layout = QHBoxLayout()
                    current_row_width = 0

        if image_layout.count() > 0:
            main_layout.addLayout(image_layout)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    image_paths = [
        "/home/fabrice/Bureau/hotrod.png",
        "/home/fabrice/Bureau/lego.png",
        "/home/fabrice/Bureau/town.png"
    ]

    viewer = ImageViewer(image_paths)
    viewer.show()

    sys.exit(app.exec())
