from transformers import pipeline

#img-to-text

def img2text(path):
    img_to_text = pipeline(
    "image-to-text", model="Salesforce/blip-image-captioning-base")
    text = img_to_text(path)[0]['generated_text']
    # return text retorna o texto em ingles
    # Traduzir a legenda para o português (utilizando o modelo MarianMT para tradução)
    translator = pipeline("translation_en_to_pt", model="Helsinki-NLP/opus-mt-tc-big-en-pt")
    translated_text = translator(text)[0]['translation_text']
    
    return translated_text