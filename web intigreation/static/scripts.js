document.getElementById("translateButton").addEventListener("click", () => {
    // Loop through all elements with class 'translatable'
    document.querySelectorAll('.translatable').forEach(element => {
        const text = element.innerText.trim();  // Get the text content of the element
        translateText(text)
            .then(translatedText => {
                element.innerText = translatedText;  // Replace text with translated text
            })
            .catch(error => {
                console.error("Translation Error:", error);
            });
    });
});

async function translateText(text) {
    const response = await fetch("http://127.0.0.1:5000/translate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            text: text,
        }),
    });
    const data = await response.json();
    return data.translated_text;
}
