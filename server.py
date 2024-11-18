from flask import Flask, request, jsonify, send_from_directory
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",  # Replace with your MySQL username
    "password": "12345678",  # Replace with your MySQL password
    "database": "railway_management"
}

# Serve the main HTML page
@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

# API to check train status
# @app.route('/check-train-status', methods=['POST'])
# def check_train_status():
#     data = request.json
#     train_id = data.get('train_id')

#     if not train_id:
#         return jsonify({"error": "Train ID is required"}), 400

#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor(dictionary=True)
#         query = "SELECT * FROM tickets WHERE train_id = %s"
#         cursor.execute(query, (train_id,))
#         results = cursor.fetchall()

#         if results:
#             return jsonify({"train_id": train_id, "tickets": results})
#         else:
#             return jsonify({"message": f"No tickets found for train ID {train_id}"}), 404
#     except mysql.connector.Error as err:
#         return jsonify({"error": str(err)}), 500
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

# API to check passenger details
# @app.route('/check-passenger-details', methods=['POST'])
# def check_passenger_details():
#     data = request.json
#     passenger_id = data.get('passenger_id')

#     if not passenger_id:
#         return jsonify({"error": "Passenger ID is required"}), 400

#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor(dictionary=True)
#         query = "SELECT * FROM tickets WHERE id = %s"
#         cursor.execute(query, (passenger_id,))
#         result = cursor.fetchone()

#         if result:
#             return jsonify({"passenger": result})
#         else:
#             return jsonify({"message": f"No details found for Passenger ID {passenger_id}"}), 404
#     except mysql.connector.Error as err:
#         return jsonify({"error": str(err)}), 500
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

@app.route('/check-train-status', methods=['POST'])
def check_train_status():
    data = request.get_json()  # Get the JSON data from the request body
    train_id = data.get('train_id')

    # Simulate checking train status from the database
    if train_id == '101' or train_id == '102' or train_id == '103' or train_id == '104':
        return jsonify({'message': f"Train {train_id} is running on time."})
    elif train_id == '105' or train_id == '106' or train_id == '107' or train_id == '108':
        return jsonify({'message': f"Train {train_id} is running late."})
    else:
        return jsonify({'message': f"Train {train_id} not found."})
    
@app.route('/check-passenger-details', methods=['POST'])
def check_passenger_details():
    data = request.get_json()  # Get the JSON data from the request body
    passenger_id = data.get('passenger_id')
    
    pas = {"1001":"Alpha","1002":"Beta","1003":"Charlie","1004":"Delta"}

    # Simulate checking passenger details from the database
    if passenger_id == '1001' or passenger_id == '1002' or passenger_id == '1003' or passenger_id == '1004':
        return jsonify({'message': f"Details for passenger ID {passenger_id}: {pas[passenger_id]}"})
    else:
        return jsonify({'message': f"Passenger ID {passenger_id} not found."})

# API to book a ticket
# @app.route('/book-ticket', methods=['POST'])
# def book_ticket():
#     data = request.json
#     train_id = data.get('train_id')
#     passenger_name = data.get('passenger_name')
#     travel_date = data.get('travel_date')
#     quota = data.get('quota')

#     if not (train_id and passenger_name and travel_date and quota):
#         return jsonify({"error": "All fields are required (train_id, passenger_name, travel_date, quota)"}), 400

#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()
#         query = """
#             INSERT INTO tickets (train_id, passenger_name, travel_date, quota)
#             VALUES (%s, %s, %s, %s)
#         """
#         cursor.execute(query, (train_id, passenger_name, travel_date, quota))
#         connection.commit()

#         return jsonify({"message": "Ticket booked successfully", "ticket_id": cursor.lastrowid}), 201
#     except mysql.connector.Error as err:
#         return jsonify({"error": str(err)}), 500
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

@app.route('/book-ticket', methods=['POST'])
def book_ticket():
    data = request.get_json()  # Get the JSON data from the request body

    train_id = data.get('train_id')
    passenger_name = data.get('passenger_name')
    travel_date = data.get('travel_date')
    passengers = data.get('passengers')
    quota = data.get('quota')

    # Simulate booking ticket logic
    if train_id and passenger_name and travel_date and passengers and quota:
        return jsonify({'message': f"Ticket booked for {passenger_name} on train {train_id} for {travel_date} with {passengers} passenger(s) in {quota} quota."})
    else:
        return jsonify({'message': "Failed to book the ticket. Please provide all details."})

# API to list all tickets
@app.route('/list-tickets', methods=['GET'])
def list_tickets():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM tickets"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            return jsonify({"tickets": results})
        else:
            return jsonify({"message": "No tickets found"}), 404
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
