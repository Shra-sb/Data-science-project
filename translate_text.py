
from googletrans import Translator

translator = Translator()

def translate(text, target_lang='hi'):
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except:
        return text
