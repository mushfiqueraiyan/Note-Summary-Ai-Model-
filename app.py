import streamlit as st
from api_calling import note_generator, quiz_generator
from PIL import Image
from gtts import gTTS
import io

st.title("Note Summary Ai")
st.markdown("This is an ai note taking summary")
st.divider()

with st.sidebar:
    st.header("Tools")
    images = st.file_uploader('Upload your files',
                     type=['jpg', 'jpeg', 'png'],
                     accept_multiple_files=True
                     )
    pil_images = []

    for image in images:
        pil_img = Image.open(image)
        pil_images.append(pil_img)

    if pil_images :
        if len(images) > 3:
            st.error("Upload at max 3 images")
        
        else:
            st.subheader('Your uploaded images')
            col = st.columns(len(images))
          
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

    #Dificulty
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ('Easy', 'Medium', 'hard'),
        index= None
    )

   

    pressed = st.button("Click the button to initiate AI", type="primary")



if pressed:
    if not images:
        st.error("Please select at least 1 image")
    if not selected_option:
        st.error("Please select at least a difficulty")
    
    if images and selected_option:
        #note
            with st.container(border=True):
                st.subheader("Your Note")
                
            with st.spinner("AI is writing notes for you"):
                    note = note_generator(pil_images)
                    st.markdown(note)
        #Audio
            with st.container(border=True):
                st.subheader("Audio Trascription")

                with st.spinner("Audio is Loading.."):

                    #Clearing markdown 
                    note = note.replace("#","")
                    note = note.replace("*","")
                    note = note.replace("-","")
                    note = note.replace("'","")
                    note = note.replace("","")

                    speech = gTTS(note,lang='bn',slow=False)

                    audio_buffer = io.BytesIO()
                    speech.write_to_fp(audio_buffer)

                    st.audio(audio_buffer)


        #Quiz
            with st.container(border=True):
                st.subheader(f"Quiz ({selected_option}) level")

                with st.spinner("Quiz is cooking..."):
                    quiz = quiz_generator(pil_images, selected_option)

                    st.markdown(quiz)



