import os

def extract_words_with_character(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            words = [word.strip() for word in f.readlines() if '.' in word]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(words))
        
        print(f"Words containing '.' have been saved to '{output_file}'")
    
    except FileNotFoundError:
        print(f"File not found at path: {input_file}")

def main():
    input_file_path = r"D:\Work\NLP\venv\Lib\site-packages\pythainlp\corpus\words_th.txt"
    output_file_path = r"D:\Work\NLP\Project\Project\words_with_dot.txt"
    
    extract_words_with_character(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
