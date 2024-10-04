from flask import Flask, render_template, request, jsonify
import pywhatkit as kit

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Render HTML template with form for input

# Route to handle the WhatsApp message sending
@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        # Get data from the form
        mobile_number = request.form['mobile']
        message = request.form['message']
        hour = int(request.form['hour'])
        minute = int(request.form['minute'])

        # Send WhatsApp message using pywhatkit
        kit.sendwhatmsg(mobile_number, message, hour, minute)

        return jsonify({"status": "success", "message": "WhatsApp message scheduled successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
