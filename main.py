import sys

from PySide6.QtWidgets import QApplication

from database.database import Database
from ui.main_window import MainWindow


def main():

    app = QApplication(sys.argv)

    database = Database()

    window = MainWindow(database)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
