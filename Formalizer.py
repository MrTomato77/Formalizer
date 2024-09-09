import streamlit as st
import csv
import os
from pythainlp.util import arabic_digit_to_thai_digit
from pythainlp.tokenize import word_tokenize, sent_tokenize
import spacy_thai
import clipboard  # Import the clipboard module

# Load spacy-thai model
nlp = spacy_thai.load()

# Define the file path
file_path = os.path.join('src', 'Sorted_Thai_Word.csv')

# Initialize word map
word_map = {}

# Load the word map from the CSV file
try:
    with open(file_path, 'r', encoding='utf-8') as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            if len(row) >= 2:
                word_map[row[0]] = row[1]
            else:
                print("Skipping invalid row:", row)
except FileNotFoundError:
    st.toast(f"File not found: {file_path}")
except Exception as e:
    st.toast(f"An error occurred while reading the file: {str(e)}")

# Word replacing function
def replace_words(text):
    sentences = sent_tokenize(text)
    replaced_sentences = []
    for sentence in sentences:
        tokens = word_tokenize(sentence, engine='newmm')
        replaced_tokens = [word_map.get(token, token) for token in tokens]
        replaced_sentence = ''.join(replaced_tokens)
        replaced_sentences.append(replaced_sentence)
    return ' '.join(replaced_sentences)

# Streamlit app
st.title("ภาษาพูดเป็นภาษาทางการ")

# Create two columns
col1, col2 = st.columns(2)

# Input text area and Convert button on the left (col1)
with col1:
    input_text = st.text_area("Input Text:", height=300)

    # Convert text
    if st.button("เปลี่ยนคำ"):
        if input_text.strip() == "":
            st.toast("กรุณาใส่ข้อความ")
        else:
            try:
                new_text = replace_words(input_text)
                newer_text = arabic_digit_to_thai_digit(new_text)
                st.session_state.output_text = newer_text
                st.toast("ข้อความถูกเปลี่ยนเรียบร้อยแล้ว")
            except Exception as e:
                st.toast(f"An error occurred: {str(e)}")

# Initialize session state
if 'output_text' not in st.session_state:
    st.session_state.output_text = ""  # Initialize as an empty string

# Output text area and Copy button on the right (col2)
with col2:
    st.text_area("Output Text:", value=st.session_state.output_text, height=300)

    # Copy to clipboard button always visible
    if st.button("คัดลอก"):
        try:
            clipboard.copy(st.session_state.output_text)  # Copy the output text (even if empty)
            if st.session_state.output_text.strip():
                st.toast("คัดลอกข้อความสำเร็จ")
            else:
                st.toast("ไม่มีข้อความที่จะคัดลอก")
        except Exception as e:
            st.toast(f"An error occurred with clipboard: {str(e)}")
