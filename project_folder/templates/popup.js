document.addEventListener('DOMContentLoaded', function() {
  // Function to handle form submission
  document.getElementById('emailForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const emailText = document.getElementById('emailText').value.trim(); // Trim whitespace

    if (emailText === '') {
      // Display empty input message if input is empty
      document.getElementById('emptyInputMessage').style.display = 'block';
      // Clear previous result
      document.getElementById('result').textContent = '';
      return; // Stop further execution
    } else {
      // Hide empty input message if input is not empty
      document.getElementById('emptyInputMessage').style.display = 'none';
    }

    fetch('http://127.0.0.1:5000/classify', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email: emailText })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('result').textContent = "Result: " + data.result;
    })
    .catch(error => console.error('Error:', error));
  });

  // Function to handle dark mode switch
  const darkModeSwitch = document.getElementById('darkModeSwitch');
  darkModeSwitch.addEventListener('change', function() {
    document.body.classList.toggle('dark-mode');
    document.querySelector('textarea').classList.toggle('dark-mode');
  });

  // Translations object
  const translations = {
    en: {
      title: "Spam Email Classifier",
      placeholder: "Enter email text here",
      button: "Classify Email"
    },
    es: {
      title: "Clasificador de Correos Electrónicos no Deseados",
      placeholder: "Ingrese el texto del correo electrónico aquí",
      button: "Clasificar correo electrónico"
    },
    fa: {
      title: "طبقه بندی ایمیل هرزنامه",
      placeholder: "متن ایمیل را در اینجا وارد کنید",
      button: "طبقه بندی ایمیل"
    },
    fr: {
      title: "Classificateur d'emails indésirables",
      placeholder: "Entrez le texte de l'email ici",
      button: "Classer l'email"
    },
    it: {
      title: "Classificatore di email spam",
      placeholder: "Inserisci qui il testo dell'email",
      button: "Classifica email"
    },
    ar: {
      title: "مصنف البريد الإلكتروني غير المرغوب فيه",
      placeholder: "أدخل نص البريد الإلكتروني هنا",
      button: "تصنيف البريد الإلكتروني"
    }
  };

  // Function to handle language change
  document.getElementById('languageSelect').addEventListener('change', function() {
    const language = this.value;
    document.querySelector('h3').textContent = translations[language].title;
    document.getElementById('emailText').placeholder = translations[language].placeholder;
    document.querySelector('button').textContent = translations[language].button;
  });

  // Function to handle clearing result when input field is clicked
  document.getElementById('emailText').addEventListener('click', function() {
    // Clear previous result
    document.getElementById('result').textContent = '';
  });
});
