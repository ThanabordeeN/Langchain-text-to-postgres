from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.llms import Ollama
from dbconfig import sqlDatabase

class SqlAgentQuery:
    def __init__(self, prompt , model=None):
        # Setup database
        self.database = sqlDatabase()
        self.db = self.database.connect()

        self.context = self.db.get_context()

        print("Database:", self.db.dialect)
        self.model = model
        self.answer = self.process_prompt(prompt)
        

    def llm(self, model=None):
        if model is None:
            llm_model = "sqlcoder"
        else:
            llm_model = model
        # Rest of the code
        print("Using model:", llm_model)
        llm = Ollama(model=llm_model, temperature=0)
        return llm
    
    def db_chain(self):
        return SQLDatabaseChain(llm=self.llm(model=self.model), database=self.db, verbose=True)
    
    def QUERY(self):       
        QUERY = """
        Given an input question, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
        Use the following format:

        "Question": "Question here"
        "SQLQuery": "SQL Query to run"
        "SQLResult": "Result of the SQLQuery"
        "Answer": "Final answer here"
        "Command: {question}"
        """
        return QUERY

    def process_prompt(self, prompt):
        try:
            question = self.QUERY().format(question=prompt)
            result = self.db_chain().run(question)
            with open("output.txt", "w") as f:
                f.write(result)
            return result
        except Exception as e:
            print("Wrong syntax", e)
            pass
