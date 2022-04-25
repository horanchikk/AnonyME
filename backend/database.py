from sqlite3 import connect


class Database:
    def __init__(
            self,
            filename: str = 'database.db'
    ) -> None:
        self.connection = connect(filename)
        self.cursor = self.connection.cursor()
