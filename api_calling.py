from google import genai
from dotenv import load_dotenv
import os


#loading the env

load_dotenv()

api_key = os.getenv("RAIYAN_API_KEY")
model = os.getenv("MODEL")

client = genai.Client(api_key=api_key)


def note_generator(images):

    prompt ="""
    Summarize the picture in note format at max 150 words, 
    and also use markup language where it needed and convert it to bangla language 
    """
    
    response = client.models.generate_content(
        model= model,
        contents = [images, prompt ]

    )

    return response.text


def quiz_generator(image, dif):
    prompt =f"Generate 3 quizzes based on the {dif} make sure to add markdown and add correct answer after the quiz"
    
    response = client.models.generate_content(
        model= model,
        contents = [image, prompt ]

    )

    return response.text
