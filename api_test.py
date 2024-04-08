import requests

# Define the API endpoint URL
url = 'http://localhost:5000/query'

# Define the data to be sent in the request body
data = {
    'question': 'What is the average salary of employees?'
}

# Send the POST request to the API endpoint
response = requests.post(url, json=data)

# Check if the response is not empty and is in JSON format
print(response.text)
if response.text:
    try:
        # Get the response data
        result = response.json()['result']
        
        # Print the result
        print(result)
    except ValueError:
        print("Response is not in JSON format")
else:
    print("Empty Response")