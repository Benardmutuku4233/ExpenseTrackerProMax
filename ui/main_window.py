from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QToolBar,
    QMessageBox
)

from PySide6.QtCore import QSize

from PySide6.QtGui import QAction, QIcon

from ui.pages.dashboard_page import DashboardPage
from ui.pages.expense_page import ExpensePage
from ui.pages.reports_page import ReportsPage

from ui.help_window import HelpWindow


class MainWindow(QMainWindow):

    def __init__(self, database):

        super().__init__()

        self.database = database

        self.help_window = None

        self.setWindowTitle(
            "Expense Tracker Pro Max"
        )

        self.resize(
            1200,
            750
        )

        self.setWindowIcon(
            QIcon(
                "assets/icon.ico"
            )
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

        self.dashboard_page = DashboardPage(
            self.database
        )

        self.expense_page = ExpensePage(
            self.database
        )

        self.reports_page = ReportsPage(
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

        self.setCentralWidget(
            self.stack
        )

    def create_menu(self):

        menu = self.menuBar()

        # FILE

        file_menu = menu.addMenu(
            "File"
        )

        new_action = QAction(
            "New Expense",
            self
        )

        new_action.triggered.connect(
            self.show_expense_page
        )

        exit_action = QAction(
            "Exit",
            self
        )

        exit_action.triggered.connect(
            self.close
        )

        file_menu.addAction(
            new_action
        )

        file_menu.addSeparator()

        file_menu.addAction(
            exit_action
        )

        # VIEW

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

        view_menu.addAction(
            dashboard_action
        )

        view_menu.addAction(
            expense_action
        )

        view_menu.addAction(
            reports_action
        )

        # HELP

        help_menu = menu.addMenu(
            "Help"
        )

        guide_action = QAction(
            "User Guide",
            self
        )

        guide_action.triggered.connect(
            self.show_help
        )

        support_action = QAction(
            "Contact Support",
            self
        )

        support_action.triggered.connect(
            self.contact_support
        )

        help_menu.addAction(
            guide_action
        )

        help_menu.addAction(
            support_action
        )

        # ABOUT

        about_menu = menu.addMenu(
            "About"
        )

        about_action = QAction(
            "About Expense Tracker Pro Max",
            self
        )

        about_action.triggered.connect(
            self.show_about
        )

        about_menu.addAction(
            about_action
        )

    def create_toolbar(self):

        toolbar = QToolBar(
            "Main Toolbar"
        )

        toolbar.setMovable(
            False
        )

        toolbar.setIconSize(
            QSize(
                28,
                28
            )
        )

        self.addToolBar(
            toolbar
        )

        dashboard_action = QAction(
            QIcon(
                "assets/dashboard.png"
            ),
            "Dashboard",
            self
        )

        dashboard_action.triggered.connect(
            self.show_dashboard
        )

        expense_action = QAction(
            QIcon(
                "assets/expense.png"
            ),
            "Add Expense",
            self
        )

        expense_action.triggered.connect(
            self.show_expense_page
        )

        reports_action = QAction(
            QIcon(
                "assets/reports.png"
            ),
            "Reports",
            self
        )

        reports_action.triggered.connect(
            self.show_reports
        )

        refresh_action = QAction(
            QIcon(
                "assets/refresh.png"
            ),
            "Refresh",
            self
        )

        refresh_action.triggered.connect(
            self.refresh_pages
        )

        exit_action = QAction(
            QIcon(
                "assets/exit.png"
            ),
            "Exit",
            self
        )

        exit_action.triggered.connect(
            self.close
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

        toolbar.addSeparator()

        toolbar.addAction(
            refresh_action
        )

        toolbar.addAction(
            exit_action
        )

    def show_help(self):

        self.help_window = HelpWindow()

        self.help_window.show()

    def contact_support(self):

        QMessageBox.information(
            self,
            "Contact Support",
            """
Expense Tracker Pro Max Support

Email:
Benardnzuki039@gmail.com

Thank you for using the application.
"""
        )

    def show_about(self):

        QMessageBox.information(
            self,
            "About",
            """
Expense Tracker Pro Max

Personal Expense Management System

Version: 1.0

Built using Python and PySide6.
"""
        )

    def refresh_pages(self):

        self.dashboard_page.refresh()

        if hasattr(
            self.reports_page,
            "refresh"
        ):

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

        if hasattr(
            self.reports_page,
            "refresh"
        ):

            self.reports_page.refresh()

        self.stack.setCurrentWidget(
            self.reports_page
        )

    def open_edit_page(self, expense):

        self.expense_page.load_expense(
            expense
        )

        self.stack.setCurrentWidget(
            self.expense_page
        )
