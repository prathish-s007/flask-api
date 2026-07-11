from flask import Flask, request # Added 'request' here!

# Initialize the Flask application
app = Flask(__name__)

# Route 1: Home page
@app.route('/', methods=['POST'])
def home():
    return "Welcome to the Home Page! This is the main route responding to a POST request."

# Route 2: About page
@app.route('/about', methods=['POST'])
def about():
    return "This is the About Page. We are learning how to use Flask with POST requests!"

# Route 3: Contact page
@app.route('/contact', methods=['POST'])
def contact():
    return "Contact us at support@example.com (POST received)."

# Route 4: A simple greeting (Now accepting form data!)
@app.route('/hello', methods=['POST'])
def hello():
    # request.form looks for data sent in the body of the request
    data = request.form.get('name')
    if not data:
        return 'No name provided. Please include a name in the POST request.', 400
    return f"Hello, {data}! Thanks for sending a POST request."

# Route 5: A farewell message
@app.route('/goodbye', methods=['POST'])
def goodbye():
    return "Goodbye! Thanks for visiting the app via a POST request."

# Run the app
if __name__ == '__main__':
    # debug=True allows the server to auto-reload when you make code changes
    app.run(debug=True)
