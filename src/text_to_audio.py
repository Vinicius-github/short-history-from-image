import requests
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente
load_dotenv()

# Obter a chave
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")


# Para textos em inglês
# #text-to-speech (Hugging Face)
# def text2speech(msg):
#     API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
#     headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
#     payloads = {
#          "inputs" : msg,
#     }
#     response = requests.post(API_URL, headers=headers, json=payloads)

#     with open('audio.flac','wb') as f:
#         f.write(response.content)



# Textos em português (no arquivo story_generator.py foi informado para o texto ser criado em português.)
from gtts import gTTS
import os

def text2speech(msg, filename="audio.mp3"):
    """
    Converte texto em fala e salva como arquivo de áudio.

    """
    
    # Converte texto para fala
    tts = gTTS(text=msg, lang="pt-br", slow=False)
    tts.save(filename)  # Salva o arquivo
    print(f"Áudio salvo como {filename}")

    return filename  # Retorna o nome do arquivo gerado

