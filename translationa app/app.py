import tkinter as tk
from transformers import MBart50TokenizerFast, MBartForConditionalGeneration
from gtts import gTTS
import os

class TranslationApp:
    def __init__(self, master):
        self.master = master
        master.title("Translation App")

        # Left Frame
        self.left_frame = tk.Frame(master)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10)

        self.label_enter_text = tk.Label(self.left_frame, text="Enter the text:")
        self.label_enter_text.grid(row=0, column=0, pady=(0, 5))

        self.entry_text = tk.Entry(self.left_frame, width=40)
        self.entry_text.grid(row=1, column=0, padx=5)

        # Right Frame
        self.right_frame = tk.Frame(master)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10)

        self.label_translated_text = tk.Label(self.right_frame, text="Translated text:")
        self.label_translated_text.grid(row=0, column=0, pady=(0, 5))

        self.translation_output = tk.Label(self.right_frame, wraplength=300, justify="left")
        self.translation_output.grid(row=1, column=0, padx=5)

        # Language Selection
        self.languages = {"Hindi": "hi_IN", "Arabic": "ar_AR", "German": "de_DE", "Spanish": "es_XX"}
        self.selected_language = tk.StringVar()
        self.selected_language.set("Hindi")

        self.language_option_menu = tk.OptionMenu(master, self.selected_language, *self.languages.keys())
        self.language_option_menu.grid(row=1, column=0, columnspan=2, pady=5)

        # Translate Button
        self.translate_button = tk.Button(master, text="Translate", command=self.translate)
        self.translate_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Speak Translation Button
        self.speak_button = tk.Button(master, text="Speak Translation", command=self.speak_translation)
        self.speak_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Load the tokenizer and model
        model_name = "SnypzZz/Llama2-13b-Language-translate"
        self.tokenizer = MBart50TokenizerFast.from_pretrained(model_name, src_lang="en_XX")
        self.model = MBartForConditionalGeneration.from_pretrained(model_name)

    def translate(self):
        text = self.entry_text.get()
        target_lang = self.languages[self.selected_language.get()]
        inputs = self.tokenizer(text, return_tensors="pt")
        generated_tokens = self.model.generate(**inputs, forced_bos_token_id=self.tokenizer.lang_code_to_id[target_lang])
        translated_text = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        self.translation_output.config(text=translated_text)

    def speak_translation(self):
        text_to_speak = self.translation_output.cget("text")
        if text_to_speak:
            # Choose the correct language for gTTS
            target_lang = self.selected_language.get()
            if target_lang == "Hindi":
                lang = "hi"
            elif target_lang == "Arabic":
                lang = "ar"
            elif target_lang == "German":
                lang = "de"
            elif target_lang == "Spanish":
                lang = "es"
            else:
                lang = "en"  # Default to English if language not supported

            # Save the translated text to a temporary file
            tts = gTTS(text=text_to_speak, lang=lang)
            tts.save("temp.mp3")

            # Play the temporary file
            os.system("start temp.mp3")

def main():
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
