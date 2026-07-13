from PySide6.QtWidgets import QApplication


finance_theme = """

QMainWindow {

    background-color: #EAF4FF;

}


QWidget {

    font-family: "Segoe UI";

    font-size: 14px;

    color: #0F172A;

}


/* MENU */

QMenuBar {

    background-color: #0B2A4A;

    color: white;

}


QMenuBar::item {

    color: white;

    padding: 6px 12px;

}


QMenuBar::item:selected {

    background-color: #2563EB;

}


QMenu {

    background-color: white;

    color: #0F172A;

}


QMenu::item {

    background-color: white;

    color: #0F172A;

    padding: 8px 25px;

}


QMenu::item:selected {

    background-color: #DBEAFE;

}



/* TOOLBAR */

QToolBar {

    background-color: #0B2A4A;

}


QToolButton {

    color: white;

}



/* LABELS */

QLabel {

    color: #0F172A;

}



/* CARDS */

QFrame#summaryCard {

    background-color: white;

    border-radius: 15px;

    border: 1px solid #BFDBFE;

}



/* INPUTS */

QLineEdit,
QComboBox,
QTextEdit,
QDateEdit {

    background-color: white;

    color: #0F172A;

    border: 1px solid #93C5FD;

    border-radius: 8px;

    padding: 8px;

}



/* ALL BUTTONS */

QPushButton {

    background-color: #E2E8F0;

    color: #0F172A;

    border-radius: 8px;

    padding: 10px 18px;

    font-weight: bold;

    border: 1px solid #CBD5E1;

}



QPushButton:hover {

    background-color: #CBD5E1;

}



/* MAIN BLUE BUTTONS */

QPushButton#saveButton,
QPushButton#exportButton,
QPushButton#refreshButton {

    background-color: #2563EB;

    color: white;

    border: none;

}



QPushButton#saveButton:hover,
QPushButton#exportButton:hover,
QPushButton#refreshButton:hover {

    background-color: #1D4ED8;

}



/* TABLE */

QTableWidget {

    background-color: white;

    color: #0F172A;

    alternate-background-color: #EFF6FF;

}



QTableWidget::item {

    color: #0F172A;

}


QTableWidget::item:selected {

    background-color: #93C5FD;

    color: #0F172A;

}


QHeaderView::section {

    background-color: #0B2A4A;

    color: white;

    padding: 8px;

}



/* STATUS BAR */

QStatusBar {

    background-color: #0B2A4A;

    color: white;

}

"""


def apply_theme(app: QApplication):

    app.setStyleSheet(
        finance_theme
    )
