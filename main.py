import streamlit as st

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def text_to_morse(text):
    """Convert text to Morse code."""
    morse_code = []
    for char in text.upper():
        if char in morse_dict:
            morse_code.append(morse_dict[char])
    return ' '.join(morse_code)

def morse_to_text(morse_code):
    """Convert Morse code to text."""
    text = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in morse_dict.items():
            if morse == code:
                text += char
    return text

# Streamlit UI
st.title("Morse Code Converter")

conversion_type = st.radio("Select Conversion Type:", ('Text to Morse Code', 'Morse Code to Text'))

if conversion_type == 'Text to Morse Code':
    text_input = st.text_input("Enter text to convert to Morse code:")
    if st.button("Convert"):
        morse_code = text_to_morse(text_input)
        st.write("Morse code:", morse_code)
elif conversion_type == 'Morse Code to Text':
    morse_input = st.text_input("Enter Morse code to convert to text (use space between codes):")
    if st.button("Convert"):
        text_output = morse_to_text(morse_input)
        st.write("Text:", text_output)
