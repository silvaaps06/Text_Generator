import time
import tensorflow as tf
import warnings
import pyttsx3
from playsound import playsound
import time
import multiprocessing
import re
import os
warnings.filterwarnings("ignore")
import os
import random
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 


def run_model(user_choice,button_choice, seed_input, size=750):
    """ Reads the model according to the user's choices
    and predicts the type of text requested
    user_choice = rap | poems | politic-speech
    """
    one_step_reloaded = tf.saved_model.load(f'/Users/AnaPSilva/Documents/Ana/Ironhack/Bootcamp/Final_Project/Models/{user_choice}/{button_choice}')
    states = None
    next_char = tf.constant([seed_input])
    result = [next_char]
    
    #SIZE ADVICE: 750 for poems
    if user_choice == 'poems':
        for n in range(size):
            next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
            result.append(next_char)
            final_text = tf.strings.join(result)[0].numpy().decode("utf-8")

    #SIZE ADVICE: 1200 for rap
    elif user_choice == 'rap':
        for n in range(size):
            next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
            result.append(next_char)
            final_text = tf.strings.join(result)[0].numpy().decode("utf-8")

    #SIZE ADVICE: 1000 for politics
    elif user_choice == 'politic-speech':
        for n in range(size):
            next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
            result.append(next_char)
            final_text = tf.strings.join(result)[0].numpy().decode("utf-8")

    return final_text


def voice_definer(button_choice,x):
    engine = pyttsx3.init()
    if (button_choice == 'Emily Dickinson') | (button_choice == 'Maya Angelou'):
        engine.setProperty('voice','com.apple.speech.synthesis.voice.ava')
        engine.setProperty("rate", 185)
        engine.setProperty("volume",2)        
        engine.say(x)
        engine.runAndWait()
    elif (button_choice == 'Oscar Wilde') | (button_choice == 'Shakespeare'):
        engine.setProperty('voice','com.apple.speech.synthesis.voice.daniel.premium')
        engine.setProperty("volume",2)    
        engine.say(x)
        engine.runAndWait()
    elif (button_choice == 'Eminem') | (button_choice == 'Kanye') | (button_choice == '50cent'):
        engine.setProperty('voice','com.apple.speech.synthesis.voice.alex')
        engine.setProperty("rate", 275)
        engine.setProperty("volume",2)
        engine.say(x)
        engine.runAndWait()
    else:
        engine.setProperty('voice','com.apple.speech.synthesis.voice.fred')
        engine.setProperty("rate", 200)
        engine.setProperty("volume",2)
        engine.say(x)
        engine.runAndWait()


def define_which_sound(user_choice):
  """Define which sound """
  if user_choice == 'rap':
    sound_path = random.choice(os.listdir("/Users/AnaPSilva/Documents/Ana/Ironhack/Bootcamp/Final_Project/HTML/Sound/rap"))
    return "HTML/Sound/rap/" + sound_path
  elif user_choice== 'poems':
    sound_path = random.choice(os.listdir("../Sound/poems/"))
    return sound_path
  else:
    sound_path = random.choice(os.listdir("../Sound/politic-speech/"))
    return sound_path

def multiple_cool(user_choice,button_choice,x):
    """multiple actions at the same time
    background sound and speech to text """
    p1 = multiprocessing.Process(target=playsound, args=([define_which_sound(user_choice)]))
    p2 = multiprocessing.Process(target=voice_definer, args=([button_choice,x]))
    return p1.start(),p2.start(), x