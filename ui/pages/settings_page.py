from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QMessageBox
)

from services.backup_manager import BackupManager


class SettingsPage(QWidget):

    def __init__(self, database):
        super().__init__()

        self.database = database

        self.backup_manager = BackupManager()

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("Settings")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            padding:10px;
        """)

        layout.addWidget(title)

        self.backup_button = QPushButton(
            "Create Database Backup"
        )

        self.backup_button.clicked.connect(
            self.create_backup
        )

        layout.addWidget(
            self.backup_button
        )

        self.restore_button = QPushButton(
            "Restore Database Backup"
        )

        self.restore_button.clicked.connect(
            self.restore_backup
        )

        layout.addWidget(
            self.restore_button
        )

        layout.addStretch()

    def create_backup(self):

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save Backup",
            "",
            "Database Files (*.db)"
        )

        if filename:

            result = self.backup_manager.create_backup(
                filename
            )

            if result:

                QMessageBox.information(
                    self,
                    "Backup",
                    "Backup created successfully."
                )

    def restore_backup(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select Backup",
            "",
            "Database Files (*.db)"
        )

        if filename:

            result = self.backup_manager.restore_backup(
                filename
            )

            if result:

                QMessageBox.information(
                    self,
                    "Restore",
                    "Database restored successfully. Restart application."
                )
