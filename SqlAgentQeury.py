from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.llms import Ollama #can change to other llm
from dbconfig import sqlDatabase

#setup database
database = sqlDatabase()
db = database.connect()

# setup llm
#this case i use sqlcoder becuase is suitable for this task becuase it's fine-tuned on SQL queries
llm = Ollama(model="sqlcoder",temperature=0)

# Create db chain
QUERY = """
Given an input question, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
Use the following format:

"Question": "Question here"
"SQLQuery": "SQL Query to run"
"SQLResult": "Result of the SQLQuery"
"Answer": "Final answer here"

"Command: {question}"
"""

# Setup the database chain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
# input prompt
context = db.get_context()
def get_prompt():
    print("Database :",db.dialect)
    while True:
        print("type 'help' for help")
        prompt = input("Enter a prompt: ")
        if prompt.lower() == 'exit':
            print('Exiting...')
            break
        elif prompt.lower() == 'help':
            print("'tables' : List of tables")
            print("'context' : The current context")
            print("'exit' to exit")
            pass
        elif prompt.lower() == 'tables':
            print("List of Tables",db.get_usable_table_names())
            pass
        elif prompt.lower() == 'context':
            print(list(context))
            print(context["table_info"])
            pass
        else:
            try:
                question = QUERY.format(question=prompt)
                result = db_chain.run(question)
                print(result)
            except Exception as e:
                print("Wrong syntax",e)
                pass

get_prompt()