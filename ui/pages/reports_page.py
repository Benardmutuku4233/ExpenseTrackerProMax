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

        title = QLabel("Reports & Analytics")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            padding:10px;
        """)

        layout.addWidget(title)

        self.chart = ExpenseChart(self.database)
        layout.addWidget(self.chart)

        buttons = QHBoxLayout()

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)

        buttons.addStretch()
        buttons.addWidget(self.refresh_button)

        layout.addLayout(buttons)

    def refresh(self):

        self.chart.refresh_chart()
