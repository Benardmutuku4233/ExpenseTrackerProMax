from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout
)

from ui.charts import ExpenseChart


class ReportsPage(QWidget):

    def __init__(self, database):

        super().__init__()

        self.database = database

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel(
            "Reports & Analytics"
        )

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#0F172A;
        """)

        layout.addWidget(
            title
        )

        self.chart = ExpenseChart(
            self.database
        )

        layout.addWidget(
            self.chart
        )

        buttons = QHBoxLayout()

        self.refresh_button = QPushButton(
            "Refresh"
        )

        self.refresh_button.setStyleSheet("""
    QPushButton {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        padding: 10px 18px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #1D4ED8;
    }
""")

        self.refresh_button.setObjectName(
            "refreshButton"
        )

        self.refresh_button.clicked.connect(
            self.refresh
        )

        self.export_pdf_button = QPushButton(
            "Export PDF"
        )

        self.export_pdf_button.setStyleSheet("""
    QPushButton {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        padding: 10px 18px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #1D4ED8;
    }
""")

        self.export_pdf_button.setObjectName(
            "exportButton"
        )
        self.export_excel_button = QPushButton(
            "Export Excel"
        )

        self.export_excel_button.setStyleSheet("""
    QPushButton {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        padding: 10px 18px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #1D4ED8;
    }
""")
        self.export_excel_button.setObjectName(
            "exportButton"
        )

        buttons.addStretch()

        buttons.addWidget(
            self.refresh_button
        )

        buttons.addWidget(
            self.export_pdf_button
        )

        buttons.addWidget(
            self.export_excel_button
        )

        layout.addLayout(
            buttons
        )

    def refresh(self):

        self.chart.refresh_chart()
