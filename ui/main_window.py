from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QToolBar
)

from PySide6.QtGui import QAction

from ui.pages.dashboard_page import DashboardPage
from ui.pages.expense_page import ExpensePage
from ui.pages.reports_page import ReportsPage
from ui.pages.settings_page import SettingsPage


class MainWindow(QMainWindow):

    def __init__(self, database):
        super().__init__()

        self.database = database

        self.setWindowTitle(
            "Expense Tracker Pro Max"
        )

        self.resize(
            1200,
            750
        )

        self.create_pages()
        self.create_menu()
        self.create_toolbar()

        self.statusBar().showMessage(
            "Ready"
        )

        self.show_dashboard()

    def create_pages(self):

        self.stack = QStackedWidget()

        self.stack.setStyleSheet("""
            background: transparent;
        """)

        self.dashboard_page = DashboardPage(
            self.database
        )

        self.expense_page = ExpensePage(
            self.database
        )

        self.reports_page = ReportsPage(
            self.database
        )

        self.settings_page = SettingsPage(
            self.database
        )

        self.dashboard_page.edit_callback = (
            self.open_edit_page
        )

        self.expense_page.refresh_callback = (
            self.refresh_pages
        )

        self.stack.addWidget(
            self.dashboard_page
        )

        self.stack.addWidget(
            self.expense_page
        )

        self.stack.addWidget(
            self.reports_page
        )

        self.stack.addWidget(
            self.settings_page
        )

        self.setCentralWidget(
            self.stack
        )

    def create_menu(self):

        menu = self.menuBar()

        file_menu = menu.addMenu(
            "File"
        )

        exit_action = QAction(
            "Exit",
            self
        )

        exit_action.triggered.connect(
            self.close
        )

        file_menu.addAction(
            exit_action
        )

        view_menu = menu.addMenu(
            "View"
        )

        dashboard_action = QAction(
            "Dashboard",
            self
        )

        dashboard_action.triggered.connect(
            self.show_dashboard
        )

        expense_action = QAction(
            "Expenses",
            self
        )

        expense_action.triggered.connect(
            self.show_expense_page
        )

        reports_action = QAction(
            "Reports",
            self
        )

        reports_action.triggered.connect(
            self.show_reports
        )

        settings_action = QAction(
            "Settings",
            self
        )

        settings_action.triggered.connect(
            self.show_settings
        )

        view_menu.addAction(
            dashboard_action
        )

        view_menu.addAction(
            expense_action
        )

        view_menu.addAction(
            reports_action
        )

        view_menu.addAction(
            settings_action
        )

    def create_toolbar(self):

        toolbar = QToolBar(
            "Main Toolbar"
        )

        self.addToolBar(
            toolbar
        )

        dashboard_action = QAction(
            "Dashboard",
            self
        )

        dashboard_action.triggered.connect(
            self.show_dashboard
        )

        expense_action = QAction(
            "Expenses",
            self
        )

        expense_action.triggered.connect(
            self.show_expense_page
        )

        reports_action = QAction(
            "Reports",
            self
        )

        reports_action.triggered.connect(
            self.show_reports
        )

        settings_action = QAction(
            "Settings",
            self
        )

        settings_action.triggered.connect(
            self.show_settings
        )

        toolbar.addAction(
            dashboard_action
        )

        toolbar.addAction(
            expense_action
        )

        toolbar.addAction(
            reports_action
        )

        toolbar.addAction(
            settings_action
        )

    def refresh_pages(self):

        self.dashboard_page.refresh()

        self.reports_page.refresh()

    def show_dashboard(self):

        self.dashboard_page.refresh()

        self.stack.setCurrentWidget(
            self.dashboard_page
        )

    def show_expense_page(self):

        self.expense_page.clear_form()

        self.expense_page.editing_id = None

        self.expense_page.save_button.setText(
            "Save Expense"
        )

        self.stack.setCurrentWidget(
            self.expense_page
        )

    def show_reports(self):

        self.reports_page.refresh()

        self.stack.setCurrentWidget(
            self.reports_page
        )

    def show_settings(self):

        self.stack.setCurrentWidget(
            self.settings_page
        )

    def open_edit_page(self, expense):

        self.expense_page.load_expense(
            expense
        )

        self.stack.setCurrentWidget(
            self.expense_page
        )
