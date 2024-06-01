// Constants for DOM elements
const emailForm = document.getElementById('emailForm');
const emailText = document.getElementById('emailText');
const emptyInputMessage = document.getElementById('emptyInputMessage');
const result = document.getElementById('result');
const darkModeSwitch = document.getElementById('darkModeSwitch');
const languageSelect = document.getElementById('languageSelect');

// Translations object
const translations = {
  en: { title: "Spam Email Classifier", placeholder: "Enter email text here", button: "Classify Email" },
  es: { title: "Clasificador de Correos Electrónicos no Deseados", placeholder: "Ingrese el texto del correo electrónico aquí", button: "Clasificar correo electrónico" },
  fa: { title: "طبقه بندی ایمیل هرزنامه", placeholder: "متن ایمیل را در اینجا وارد کنید", button: "طبقه بندی ایمیل" },
  fr: { title: "Classificateur d'emails indésirables", placeholder: "Entrez le texte de l'email ici", button: "Classer l'email" },
  it: { title: "Classificatore di email spam", placeholder: "Inserisci qui il testo dell'email", button: "Classifica email" },
  ar: { title: "مصنف البريد الإلكتروني غير المرغوب فيه", placeholder: "أدخل نص البريد الإلكتروني هنا", button: "تصنيف البريد الإلكتروني" }
};

// Function to handle form submission
function handleFormSubmit(e) {
  e.preventDefault();
  const emailTextValue = emailText.value.trim(); // Trim whitespace

  if (emailTextValue === '') {
    emptyInputMessage.style.display = 'block';
    result.textContent = '';
    return; // Stop further execution
  }

  emptyInputMessage.style.display = 'none';

  fetch('http://127.0.0.1:5000/classify', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: emailTextValue })
  })
  .then(response => response.json())
  .then(data => result.textContent = "Result: " + data.result)
  .catch(error => console.error('Error:', error));
}

// Function to handle dark mode switch
function handleDarkModeSwitch() {
  document.body.classList.toggle('dark-mode');
  document.querySelector('textarea').classList.toggle('dark-mode');
}

// Function to handle language change
function handleLanguageChange() {
  const language = this.value;
  document.querySelector('h3').textContent = translations[language].title;
  emailText.placeholder = translations[language].placeholder;
  document.querySelector('button').textContent = translations[language].button;
}

// Function to handle clearing result when input field is clicked
function handleInputClick() {
  result.textContent = '';
}

// Function to handle focus and blur events
function handleFocusBlur(e) {
  this.classList.toggle('focused', e.type === 'focus');
  this.classList.toggle('normal', e.type === 'blur');
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
  emailForm.addEventListener('submit', handleFormSubmit);
  darkModeSwitch.addEventListener('change', handleDarkModeSwitch);
  languageSelect.addEventListener('change', handleLanguageChange);
  emailText.addEventListener('click', handleInputClick);
  emailText.addEventListener('focus', handleFocusBlur);
  emailText.addEventListener('blur', handleFocusBlur);
});