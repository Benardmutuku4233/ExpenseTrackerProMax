import shutil
import os


class BackupManager:

    def __init__(self, database_file="expense_tracker.db"):
        self.database_file = database_file

    def create_backup(self, backup_location):

        if os.path.exists(self.database_file):

            shutil.copy(
                self.database_file,
                backup_location
            )

            return True

        return False

    def restore_backup(self, backup_file):

        if os.path.exists(backup_file):

            shutil.copy(
                backup_file,
                self.database_file
            )

            return True

        return False
