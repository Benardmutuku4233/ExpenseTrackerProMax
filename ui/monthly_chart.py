from PySide6.QtWidgets import QWidget, QVBoxLayout

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MonthlyChart(QWidget):

    def __init__(self, database):

        super().__init__()

        self.database = database

        layout = QVBoxLayout(self)

        self.figure = Figure(
            figsize=(6, 2.5)
        )

        self.canvas = FigureCanvasQTAgg(
            self.figure
        )

        layout.addWidget(
            self.canvas
        )

        self.refresh_chart()

    def refresh_chart(self):

        self.figure.clear()

        ax = self.figure.add_subplot(
            111
        )
        ax.grid(
            axis="y",
            linestyle="--",
            alpha=0.3
        )
        data = self.database.get_monthly_summary()

        if not data:

            ax.text(
                0.5,
                0.5,
                "No Monthly Data",
                ha="center",
                va="center"
            )

            self.canvas.draw()

            return

        months = []

        amounts = []

        for item in data:

            months.append(
                item[0]
            )

            amounts.append(
                item[1]
            )

        ax.bar(
            months,
            amounts
        )

        ax.set_title(
            "Monthly Expenses"
        )

        ax.set_xlabel(
            "Month"
        )

        ax.set_ylabel(
            "Amount (KSh)"
        )

        ax.tick_params(
            axis="x",
            rotation=45
        )

        self.figure.tight_layout()

        self.canvas.draw()
