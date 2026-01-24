import streamlit as st

# --- Dictionaries ---
French = {
    'hello': 'bonjour',
    'thank you': 'merci',
    'water': 'eau',
    'sun': 'soleil',
    'dog': 'chien',
    'cat': 'chat',
    'car': 'voiture',
    'tree': 'arbre',
    'road': 'route',
    'school': 'ecole',
    'friend': 'ami',
    'phone': 'telephone',
    'chair': 'chaise',
    'table': 'table',
    'light': 'lumiere',
    'child': 'enfant',
    'work': 'travail',
    'love': 'amour',
    'music': 'musique',
}

Igala = {
    "come": "ya",
    "stand": "de",
    "sit": "kpe",
    "eat": "unu",
    "morning": "okpo",
    "night": "oche",
    "water": "omi",
    "drink": "mu",
    "face": "eji",
    "understand": "ma",
    "school": "sukulu",
    "love": "ufedo",
    "car": "moto",
    "yes": "ee",
    "mother": "iya"
}

Yoruba = {
    "water": "omi",
    "food": "ounje",
    "house": "ile",
    "man": "okunrin",
    "woman": "obinrin",
    "child": "omo",
    "book": "iwe",
    "school": "ile-iwe",
    "sun": "oorun",
    "moon": "osupa",
    "dog": "aja",
    "cat": "ologbo",
    "road": "ona",
    "car": "oko ayokele",
    "money": "owo",
    "friend": "ore",
    "love": "ife",
}

Hausa = {
    "chair": "kujera",
    "stone": "dutse",
    "bag": "jaka",
    "shoe": "takalmi",
    "phone": "waya",
    "bed": "godo",
    "food": "abinchi",
    "house": "gida",
    "money": "kudi",
    "car": "mota",
    "water": "ruwa",
    "school": "makaranta",
    "book": "littafi",
    "friend": "aboki",
    "teacher": "malami",
    "help": "taimako",
    "home": "gida",
    "yes": "eh",
    "no": "a'a",
    "night": "dare",
    "bread": "gurasa",
    "afternoon": "rana"
}


Italiano = {
    "love": "amore",
    "food": "cibo",
    "friend": "amico",
    "school": "scuola",
    "house": "casa",
    "water": "acqua",
    "book": "libro",
    "car": "macchina",
    "sun": "sole",
    "moon": "luna",
    "dog": "cane",
    "day": "giorno",
    "child": "bambino",
    "road": "strada",
    "teacher": "insegnante",
    "music": "musica",
    "night": "notte"
}

# --- Logic ---
def search_dictionary(word, dictionary):
    return dictionary.get(word, "❌ Word not found")

choice = st.selectbox('Language', ('French','Igala','Yoruba','Hausa','Italiano'))
your_word = st.text_input("Enter your word").lower()

if st.button("Search"):
    if choice == 'French':
        st.success(search_dictionary(your_word, French))
    elif choice == 'Igala':
        st.success(search_dictionary(your_word, Igala))
    elif choice == 'Yoruba':
        st.success(search_dictionary(your_word, Yoruba))
    elif choice == 'Hausa':
        st.success(search_dictionary(your_word, Hausa))
    elif choice == 'Italiano':
        st.success(search_dictionary(your_word, Italiano))
