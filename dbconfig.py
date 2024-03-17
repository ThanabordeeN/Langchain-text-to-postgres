from langchain_community.utilities import  SQLDatabase

class sqlDatabase:
    def __init__(self):
        pass
    def connect(self):
        db = SQLDatabase.from_uri(
            f"postgresql+psycopg2://postgres:postgres@localhost:5432/txttosql",
        )
        return db
