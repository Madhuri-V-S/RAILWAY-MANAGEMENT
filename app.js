// This function handles the action when the "Check!" button is clicked
function getOption() {
    const opt = document.querySelector("#option-select");
    const option = opt.value;
    const div = document.querySelector("#operation");

    // Clear previous content
    div.innerHTML = '';

    if (option === "status") {
        div.innerHTML = `
            <label for="train-id">Train ID: </label>
            <input type="text" id="train-id" placeholder="Enter your train number">
            <button onclick="checkTrainStatus()">Check Status</button>
        `;
    } else if (option === "passenger-details") {
        div.innerHTML = `
            <label for="passenger-id">Passenger ID: </label>
            <input type="text" id="passenger-id" placeholder="Enter passenger ID">
            <button onclick="checkPassengerDetails()">Check Details</button>
        `;
    } else if(option === "book-ticket"){
        div.innerHTML = `
            <label for="train-id">Train ID: </label>
            <input type="text" id="train-id" placeholder="Enter your train number"> <br><br>
            <label for="passenger-name">Passenger Name: </label>
            <input type="text" id="passenger-name" placeholder="Enter passenger name"> <br><br>
            <label for="date">Travel date: </label>
            <input type="date" id="date"> <br><br>
            <label for="passengers">Number of Passengers: </label>
            <input type="number" id="passengers" placeholder="Enter number of passengers" min="1"> <br><br>
            <label for="quota">Quota: </label>
            <select id="quota">
                <option value="General">General</option>
                <option value="Tatkal">Tatkal</option>
                <option value="Ladies">Ladies</option>
                <option value="Senior-citizen">Senior Citizen</option>
                <option value="Lower-berth">Lower Berth</option>
            </select> <br><br>
            <button onclick="bookingTicket()">Check Availability</button>
        `;
    }
}

// This function checks the status of a train based on train ID
function checkTrainStatus() {
    const trainId = document.querySelector("#train-id").value;

    // Prepare the JSON data to be sent
    const data = { train_id: trainId };

    // Send the data to the Flask server using Fetch API
    fetch('http://127.0.0.1:5000/check-train-status', {
        method: 'POST',  // POST request
        headers: {
            'Content-Type': 'application/json'  // Specify that we are sending JSON data
        },
        body: JSON.stringify(data)  // Convert the JavaScript object to a JSON string
    })
    .then(response => response.json())  // Convert the response to JSON
    .then(data => {
        // Handle the response data (e.g., show the status)
        alert(data.message);  // Example: displaying a message from the server
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// This function checks the details of a passenger based on passenger ID
function checkPassengerDetails() {
    const passengerId = document.querySelector("#passenger-id").value;

    // Prepare the JSON data to be sent
    const data = { passenger_id: passengerId };

    // Send the data to the Flask server using Fetch API
    fetch('http://127.0.0.1:5000/check-passenger-details', {
        method: 'POST',  // POST request
        headers: {
            'Content-Type': 'application/json'  // Specify that we are sending JSON data
        },
        body: JSON.stringify(data)  // Convert the JavaScript object to a JSON string
    })
    .then(response => response.json())  // Convert the response to JSON
    .then(data => {
        // Handle the response data (e.g., display passenger details)
        alert(data.message);  // Example: displaying a message from the server
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// This function books a ticket based on user input (train ID, passenger name, date, number of passengers, quota)
function bookingTicket() {
    const trainId = document.querySelector("#train-id").value;
    const passengerName = document.querySelector("#passenger-name").value;
    const travelDate = document.querySelector("#date").value;
    const passengers = document.querySelector("#passengers").value;
    const quota = document.querySelector("#quota").value;

    // Prepare the JSON data to be sent
    const data = {
        train_id: trainId,
        passenger_name: passengerName,
        travel_date: travelDate,
        passengers: passengers,
        quota: quota
    };

    // Send the data to the Flask server using Fetch API
    fetch('http://127.0.0.1:5000/book-ticket', {
        method: 'POST',  // POST request
        headers: {
            'Content-Type': 'application/json'  // Specify that we are sending JSON data
        },
        body: JSON.stringify(data)  // Convert the JavaScript object to a JSON string
    })
    .then(response => response.json())  // Convert the response to JSON
    .then(data => {
        // Handle the response data (e.g., show confirmation or error messages)
        alert(data.message);  // Example: displaying a confirmation message from the server
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

