const micButton = document.querySelector('button[type="button"]');
const inputBox = document.querySelector('input[name="message"]');

if (micButton) {

    const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    if (SpeechRecognition) {

        const recognition = new SpeechRecognition();

        recognition.lang = "en-IN";
        recognition.interimResults = false;

        micButton.onclick = () => {
            recognition.start();
        };

        recognition.onresult = (event) => {
            inputBox.value = event.results[0][0].transcript;
        };

        recognition.onerror = (event) => {
            alert("Microphone Error: " + event.error);
        };

    } else {
        alert("Speech Recognition is not supported in this browser.");
    }
}