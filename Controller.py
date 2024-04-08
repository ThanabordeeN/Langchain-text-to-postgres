from flask import Flask, request
from SqlAgentQeury_Class import SqlAgentQuery

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query_employee():
    data = request.get_json()
    question = data['question']
    
    # Create an instance of SqlAgentQuery
    query = SqlAgentQuery(question)
    
    # Perform the query and get the result
    sent = {'result': query.answer}
    return sent

if __name__ == '__main__':
    app.run()
