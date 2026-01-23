import streamlit as st
French = {
        'Hello' : 'Bonjour',
        'Thank' : 'Merci',
        'Water' : 'Eau',
        'Sun' : 'Soleil',
        'Oui' : 'Yes',
        'Dog' : 'Chien',
        'Cat' : 'Chat',
        'Car' : 'Voiture',
        'Tree' : 'Arbre',
        'Road' : 'Route',
        'School' : 'Ecole',
        'Friend' : 'Ami',
        'Phone' : 'Telephone',
        'Chair' : 'Chaise',
        'Table' : 'Table',
        'Light' : 'Lumiere',
        'Child' : 'Enfant',
        'Work' : 'Travail',
        'Love' : 'Amour',
        'Music' : 'Musique',
}
Igala = {
    "come": "ya",
    "stand": "de",
    "sit": "kpe",
    "Eat": "Unu",
    "morning": "okpo",
    "night": "oche",
    "we/us": "enye",
    "water": "omi",
    "drink": "mu",
    "Face": "eji",
    "understand": "ma",
    "how": "ele",
    "long time": "akpa kpekpe",
    "school": "sukulu",
    "Love": "Ufedo",
    "tomorrow": "ojo ale",
    "write": "kwo",
    "car": "moto",
    "how was your day": "ele ne ojo che",
    "did you sleep well": "ma kpe chọ",
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
    "day": "ojo",
    "night": "oru",
    "teacher": "oluko"
}
Hausa = {
    "chair": "kujera",
    "stone": "dutse",
    "bag": "jaka",
    "shoe": "takalmi",
    "wrapper": "zani",
    "phone": "waya",
    "bed": "godo",
    "food": "abichin",
    "clothes": "kaya",
    "plates": "kwanu",
    "bottle": "gora" ,
    "scissors": "almakachi",
    "knife": "wuka",
    "basket": "kwondo",
    "house": "Gida",
    "money": "kudi" ,
    "car": "mota",
    "water": "ruwa",
    "horse": "doki",
    "bone": "Kashi",
}
Italiano = {
        "love": "amore",
        "Food": "Cibo",
        "Friend": "Amigo",
        "School": "Scuola",
        "House": "Casa",
        "Water": "Aqua",
        "Book": "Libro",
        "Car": "Macchina",
        "Happy": "Felice",
        "Work": "Lavoro",
        "Car": "Macchina",
        "Sun": "Sole",
        "Moon": "Luna",
        "Dog": "Cane",
        "Day": "Giorno",
        "Child": "Bambino",
        "Road": "Strada",
        "Teacher": "Insegnante",
        "Music" : "Musica",
        "Night": "Notte"
}
choice = st.selectbox('language',('french','Igala','yoruba', 'hausa','Italiano'))
word = st.text_input("Enter a word")
def  search_dictionary(word, dictionary):
    return dictionary[word]

if choice == 'french':
    dictionary = french
    your_word = st.text_input('Enter Your word: ')
    st.button('search', on_click = lambda:
     st.title(search_dictionary(your_word.lower(), dictionary)))
elif choice == 'Igala':
    dictionary = Igala
    your_word = st.text_input('Enter Your word: ')
    st.button('search', on_click = lambda:
     st.title(search_dictionary(your_word.lower(), dictionary)))
elif choice == 'yoruba':
    dictionary = yoruba
    your_word = st.text_input('Enter Your word: ')
    st.button('search', on_click = lambda:
     st.title(search_dictionary(your_word.lower(), dictionary)))
elif choice == 'hausa':
    dictionary = hausa
    your_word = st.text_input('Enter Your word: ')
    st.button('search', on_click = lambda:
     st.title(search_dictionary(your_word.lower(), dictionary)))
elif choice == 'Italiano':
    dictionary = Italiano
    your_word = st.text_input('Enter Your word: ')
    st.button('search', on_click = lambda:
     st.title(search_dictionary(your_word.lower(), dictionary)))
