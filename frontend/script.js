async function predictSpam() {

    const message = document.getElementById("message").value;

    const resultDiv = document.getElementById("result");

    if (message.trim() === "") {

        resultDiv.innerHTML = "Please enter a message";

        return;
    }

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );

        const data = await response.json();

        console.log(data);

        resultDiv.innerHTML =
            `<h2>Prediction: ${data.prediction}</h2>`;

    }

    catch (error) {

        console.error(error);

        resultDiv.innerHTML =
            "Error connecting to backend";
    }
}