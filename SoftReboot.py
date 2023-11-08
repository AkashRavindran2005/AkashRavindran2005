import os 
try:
    import streamlit as st
except ImportError:
    os.system('pip install streamlit')
    import streamlit as st
try:
    from translate import Translator
except ImportError:
    os.system("pip install translate")
    from translate import Translator

st.title("Language Translator")
languages = {
  "Afrikaans": "af",
  "Albanian": "sq" ,
  "Amharic":"am",
  "Arabic":"ar",
  "Armenian":"hy",
  "Azerbaijani":"az",
  "Basque": "eu",
  "Belarusian": "be",
  "Bengali": "bn",
  "Bosnian": "bs",
  "Bulgarian":"bg",
  "Catalan":  "ca",
  "Cebuano": "ceb",
  "Chinese Simplified": "zh-CN",
  "Chinese Traditional": "zh-TW",
  "Corsican": "co",
  "Croatian": "hr",
  "Czech": "cs",
  "Danish": "da",
  "Dutch": "nl",
  "English": "en",
  "Esperanto":"eo",
  "Estonian": "et",
  "Finnish": "fi",
  "French":"fr",
  "Frisian": "fy",
  "Galician": "gl",
  "Georgian": "ka",
  "German": "de",
  "Greek": "el",
  "Gujarati": "gu",
  "Haitian Creole": "ht",
  "Hausa": "ha",
  "Hawaiian": "haw",
  "Hebrew": "he",
  "Hindi": "hi",
  "Hmong": "hmn",
  "Hungarian": "hu",
  "Icelandic": "is",
  "Igbo": "ig",
  "Indonesian": "id",
  "Irish": "ga",
  "Italian": "it",
  "Japanese":"ja",
  "Javanese": "jv",
  "Kannada": "kn",
  "Kazakh": "kk",
  "Khmer": "km",
  "Kinyarwanda": "rw",
  "Korean": "ko",
  "Kurdish": "ku",
  "Kyrgyz": "ky",
  "Lao": "lo",
  "Latvian":  "lv",
  "Lithuanian": "lt",
  "Luxembourgish": "lb",
  "Macedonian": "mk",
  "Malagasy": "mg",
  "Malay":  "ms",
  "Malayalam": "ml",
  "Maltese": "mt",
  "Maori": "mi",
  "Marathi":  "mr",
  "Mongolian": "mn",
  "Myanmar (Burmese)": "my",
  "Nepali": "ne",
  "Norwegian": "no",
  "Nyanja (Chichewa)":  "ny",
  "Odia (Oriya)": "or",
  "Pashto": "ps",
  "Persian": "fa",
  "Polish": "pl",
  "Portuguese": "pt",
  "Punjabi": "pa",
  "Romanian":"ro",
  "Russian": "ru",
  "Samoan":  "sm",
  "Scots Gaelic": "gd",
  "Serbian":"sr",
  "Sesotho": "st",
  "Shona": "sn",
  "Sindhi": "sd",
  "Sinhala (Sinhalese)": "si",
  "Slovak": "sk",
  "Slovenian": "sl",
  "Somali": "so",
  "Spanish": "es",
  "Sundanese":"su",
  "Swahili": "sw",
  "Swedish": "sv",
  "Tagalog (Filipino)": "tl",
  "Tajik": "tg",
  "Tamil": "ta",
  "Tatar": "tt",
  "Telugu": "te",
  "Thai": "th",
  "Turkish": "tr",
  "Turkmen":"tk",
  "Ukrainian": "uk",
  "Urdu": "ur",
  "Uyghur": "ug",
  "Uzbek": "uz",
  "Vietnamese": "vi",
  "Welsh": "cy",
  "Xhosa": "xh",
  "Yiddish": "yi",
  "Yoruba": "yo",
  "Zulu":  "zu"
}
l=[]
for i in languages:
    l.append(i)
result1 = st.selectbox(label="Input Language", options=l)
text = st.text_input("Enter a text")
if text:
    result = st.selectbox(label="Translation Language", options=l)
    translator = Translator(from_lang=languages[result1],to_lang=languages[result])
    translation = translator.translate(text)
    st.write(translation)