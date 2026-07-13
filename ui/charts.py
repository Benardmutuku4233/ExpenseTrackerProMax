from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PySide6.QtWidgets import QWidget, QVBoxLayout


class ExpenseChart(QWidget):

    def __init__(self, database):
        super().__init__()

        self.database = database

        self.figure = Figure(figsize=(6, 4))
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

        self.refresh_chart()

    def refresh_chart(self):

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        data = self.database.get_category_summary()

        if not data:
            ax.text(
                0.5,
                0.5,
                "No expense data available",
                ha="center",
                va="center",
                fontsize=14
            )
            self.canvas.draw()
            return

        categories = [row[0] for row in data]
        amounts = [row[1] for row in data]

        ax.pie(
            amounts,
            labels=categories,
            autopct="%1.1f%%",
            startangle=90
        )

        ax.set_title("Expenses by Category")

        self.canvas.draw()
