from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')
        
        # Here you can add email sending logic or database storage
        # For now, we'll just return a success response
        
        print(f"Contact Form Submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Message: {message}")
        print(f"Time: {datetime.now()}")
        
        return jsonify({
            'success': True,
            'message': 'Thank you for contacting us! We will get back to you soon.'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Something went wrong. Please try again.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)