import sys
import ctypes

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from database.database import Database
from ui.main_window import MainWindow
from theme import apply_theme


def set_app_id():

    try:

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "ExpenseTrackerProMax.App"
        )

    except Exception:

        pass


def main():

    set_app_id()

    app = QApplication(sys.argv)

    app.setApplicationName(
        "Expense Tracker Pro Max"
    )

    icon_path = "assets/icon.ico"

    app.setWindowIcon(
        QIcon(icon_path)
    )

    apply_theme(app)

    database = Database()

    window = MainWindow(database)

    window.setWindowIcon(
        QIcon(icon_path)
    )

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":

    main()
