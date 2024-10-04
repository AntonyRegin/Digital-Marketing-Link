// script.js

document.getElementById('whatsappForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);

    fetch('/send-message', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const output = document.getElementById('output');
        if (data.status === 'success') {
            output.innerText = data.message;
        } else {
            output.innerText = 'Error: ' + data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
