import tkinter as tk
from tkinter import ttk  # Import themed Tkinter module
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Himanshu9192/Spelling_Checker")
model = AutoModelForSeq2SeqLM.from_pretrained("Himanshu9192/Spelling_Checker")
# Define pipeline
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

# Function to correct spelling and speak the corrected sentence
def correct_spelling():
    text = text_entry.get("1.0", tk.END).strip()  # Get the text from the text area
    corrected_text = spell_checker(text)
    corrected_text_area.delete("1.0", tk.END)  # Clear the text area
    corrected_text_area.insert(tk.END, corrected_text)  # Display the corrected text
    # If auto-speak mode is enabled, speak the corrected text
    if auto_speak_var.get() == 1:
        engine.say(corrected_text)
        engine.runAndWait()

# Function to check spelling and correct
def spell_checker(text):
    # Perform spelling correction
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, num_return_sequences=1)
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_text

# Function to toggle auto-speak mode
def toggle_auto_speak():
    if auto_speak_var.get() == 1:
        auto_speak_button.config(text="Auto Speak: ON")
    else:
        auto_speak_button.config(text="Auto Speak: OFF")

# Create the main window
window = tk.Tk()
window.title("Spelling Checker")

# Create text entry area
text_entry = tk.Text(window, height=10, width=50)
text_entry.pack(pady=10)

# Create button to correct spelling
correct_button = ttk.Button(window, text="Correct", command=correct_spelling)
correct_button.pack(pady=5)

# Create text area to display corrected text
corrected_text_area = tk.Text(window, height=10, width=50)
corrected_text_area.pack(pady=10)

# Create a checkbutton for auto-speak mode
auto_speak_var = tk.IntVar()
auto_speak_var.set(0)  # Auto-speak mode is initially off
auto_speak_button = tk.Checkbutton(window, text="Auto Speak: OFF", variable=auto_speak_var, command=toggle_auto_speak)
auto_speak_button.pack(pady=5)

# Run the GUI
window.mainloop()
