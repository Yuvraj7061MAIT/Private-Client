import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize NLTK's sentiment analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment of input text
def analyze_sentiment(text):
    scores = sia.polarity_scores(text)
    total_score = sum(scores.values())
    # Calculate percentage of positive, negative, and neutral sentiments
    pos_percent = scores['pos'] / total_score * 100
    neu_percent = scores['neu'] / total_score * 100
    neg_percent = scores['neg'] / total_score * 100
    return pos_percent, neu_percent, neg_percent

# Function to handle button click event
def on_analyze():
    input_text = text_entry.get("1.0", tk.END).strip()
    if input_text:
        pos_percent, neu_percent, neg_percent = analyze_sentiment(input_text)
        # Update labels with sentiment percentages
        positive_label.config(text=f"Positive: {pos_percent:.2f}%")
        neutral_label.config(text=f"Neutral: {neu_percent:.2f}%")
        negative_label.config(text=f"Negative: {neg_percent:.2f}%")
    else:
        messagebox.showerror("Error", "Please enter text for sentiment analysis.")

# Create main window
root = tk.Tk()
root.title("Sentiment Analysis")

# Create text entry area
text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

# Create analyze button
analyze_button = tk.Button(root, text="Analyze", command=on_analyze)
analyze_button.pack()

# Create labels to display sentiment percentages
positive_label = tk.Label(root, text="Positive:")
positive_label.pack()
neutral_label = tk.Label(root, text="Neutral:")
neutral_label.pack()
negative_label = tk.Label(root, text="Negative:")
negative_label.pack()

# Run the Tkinter event loop
root.mainloop()
