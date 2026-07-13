from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QToolBar
)

from PySide6.QtGui import QAction

from ui.expense_page import ExpensePage
from ui.dashboard_page import DashboardPage


class MainWindow(QMainWindow):

    def __init__(self, database):
        super().__init__()

        self.database = database

        self.setWindowTitle("Expense Tracker Pro")

        self.resize(1100, 700)

        self.create_pages()
        self.create_menu()
        self.create_toolbar()

        self.statusBar().showMessage("Ready")

    def create_pages(self):

        self.stack = QStackedWidget()

        self.dashboard_page = DashboardPage(self.database)
        self.expense_page = ExpensePage(self.database)

        self.dashboard_page.edit_callback = self.open_edit_page
        self.expense_page.refresh_callback = self.dashboard_page.refresh

        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.expense_page)

        self.setCentralWidget(self.stack)

    def create_menu(self):

        menu = self.menuBar()

        file_menu = menu.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

        view_menu = menu.addMenu("View")

        dashboard = QAction("Dashboard", self)
        dashboard.triggered.connect(self.show_dashboard)

        expense = QAction("Add Expense", self)
        expense.triggered.connect(self.show_expense_page)

        view_menu.addAction(dashboard)
        view_menu.addAction(expense)

    def create_toolbar(self):

        toolbar = QToolBar()

        self.addToolBar(toolbar)

        dashboard = QAction("Dashboard", self)
        dashboard.triggered.connect(self.show_dashboard)

        expense = QAction("Add Expense", self)
        expense.triggered.connect(self.show_expense_page)

        toolbar.addAction(dashboard)
        toolbar.addAction(expense)

    def show_dashboard(self):

        self.dashboard_page.refresh()

        self.stack.setCurrentWidget(
            self.dashboard_page
        )

    def show_expense_page(self):

        self.expense_page.clear_form()
        self.expense_page.editing_id = None
        self.expense_page.save_button.setText("Save Expense")

        self.stack.setCurrentWidget(
            self.expense_page
        )

    def open_edit_page(self, expense):

        self.expense_page.load_expense(expense)

        self.stack.setCurrentWidget(
            self.expense_page
        )
