from src.image_to_text import img2text
from src.story_generator import story_generator
from src.text_to_audio import text2speech
import streamlit as st
import requests

def main():
    st.set_page_config(page_title = "AI story Teller", page_icon ="🤖")

    st.header("We turn images to story!")
    upload_file = st.file_uploader("Choose an image...", type = 'jpg')  #uploads image

    if upload_file is not None:
        print(upload_file)
        binary_data = upload_file.getvalue()
        
        # save image
        with open (upload_file.name, 'wb') as f:
            f.write(binary_data)
        st.image(upload_file, caption = "Image Uploaded", use_container_width = True) # display image

        scenario = img2text(upload_file.name) #text2image
        story = story_generator(scenario) # create a story
        text2speech(story) # convert generated text to audio

        # display scenario and story
        with st.expander("scenario"):
            st.write(scenario)
        with st.expander("story"):
            st.write(story)
        
        # Mostra o audio em inglês
        # st.audio("audio.flac")

        # Mostra o audio em português
        st.audio("audio.mp3")

# the main
if __name__ == "__main__":
    main()