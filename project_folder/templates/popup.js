document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('emailForm').addEventListener('submit', function(e) {
    e.preventDefault();
    var emailText = document.getElementById('emailText').value;

    fetch('http://127.0.0.1:5000/classify', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email: emailText })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('result').textContent = data.result;
    })
    .catch(error => console.error('Error:', error));
  });
});
