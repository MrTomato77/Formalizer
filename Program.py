import tkinter as tk
from tkinter import scrolledtext, messagebox
import csv
from pythainlp.util import arabic_digit_to_thai_digit
from pythainlp.tokenize import word_tokenize, sent_tokenize
import spacy_thai
import pyperclip

# Load spacy-thai model
nlp = spacy_thai.load()
Path = r".\src\Sorted_Thai_Word.csv"

# Word reader
word_map = {}
with open(Path, 'r', encoding='utf-8') as read_file:
    reader = csv.reader(read_file)
    for row in reader:
        if len(row) >= 2:
            word_map[row[0]] = row[1]
        else:
            print("Skipping invalid row:", row)

# Word replacing function
def replace_words(text):
    sentences = sent_tokenize(text)
    replaced_sentences = []
    for sentence in sentences:
        tokens = word_tokenize(sentence, engine='newmm')
        replaced_tokens = []
        for token in tokens:
            replaced_word = word_map.get(token, token)
            replaced_tokens.append(replaced_word)
        replaced_sentence = ''.join(replaced_tokens)
        replaced_sentences.append(replaced_sentence)
    return ' '.join(replaced_sentences)

# Function button
def process_text():
    input_text = input_text_area.get("1.0", tk.END)
    if input_text.strip() == "":
        messagebox.showerror("Error", "กรุณาใส่ข้อความ")
        return
    try:
        new_text = replace_words(input_text)
        newer_text = arabic_digit_to_thai_digit(new_text)
        output_text_area.delete("1.0", tk.END)
        output_text_area.insert(tk.END, newer_text)
        messagebox.showinfo("Success", "เปลี่ยนคำคัพท์สำเร็จ")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to copy text to clipboard
def copy_to_clipboard():
    output_text = output_text_area.get("1.0", tk.END)
    pyperclip.copy(output_text)
    messagebox.showinfo("Copied", "คัดลอกข้อความไปยังคลิปบอร์ดสำเร็จ")

# Create main application
root = tk.Tk()
root.title("ภาษาพูดเป็นภาษาทางการ")

# input text area
input_text_label = tk.Label(root, text="Input Text:")
input_text_label.grid(row=0, column=0, sticky="w")
input_text_area = scrolledtext.ScrolledText(root, width=100, height=6, font=(20))
input_text_area.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# output text area
output_text_label = tk.Label(root, text="Output Text:")
output_text_label.grid(row=2, column=0, sticky="w")
output_text_area = scrolledtext.ScrolledText(root, width=100, height=6, font=(20))
output_text_area.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# buttons
process_button = tk.Button(root, text="เปลี่ยนคำ", command=process_text)
process_button.grid(row=4, column=0, pady=5)

copy_button = tk.Button(root, text="คัดลอกไปยังคลิปบอร์ด", command=copy_to_clipboard)
copy_button.grid(row=4, column=1, pady=5)

# Run app
root.mainloop()
