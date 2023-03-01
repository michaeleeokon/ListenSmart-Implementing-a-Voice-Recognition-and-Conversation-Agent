from neuralintents  import GenericAssistant
import speech_recognition as sr
import pyaudio
import pyttsx3 as tts
import sys
import pyttsx3

recognizer = sr.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = ['Go Shopping', 'Clean Room', 'Record Video']

speaker.say("Hello. How may i help you")
speaker.runAndWait()


def create_note():
    
    global recognizer
    print("What do you want to do")
    speaker.say("What do want to write unto to your note?")
    speaker.runAndWait()
    
    done = False
    
    while not done:
        print("Creating a note")
        try:
            
            with sr.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                note = recognizer.recognize_google(audio)
                note = note.lower()
                
                speaker.say("Choose a filname!")
                speaker.runAndWait()
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                filename = recognizer.recognize_google(audio)
                filename = filename.lower()
                
            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename}")
                
        except sr.UnknownValueError:
            recognizer = recognizer.Recognizer()
            speaker.say("I did not understand you! try again!")
            speaker.runAndWait()
            
def add_todo():
    
    global recognizer
    print("What todo do you want to add?")
    speaker.say("What todo do you want to add?")
    speaker.runAndWait()
    
    done = False
    
    while not done:
        print("Listening to audio")
        try:
            
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)
                item = recognizer.recognize_google(audio)
                item = item.lower() 
                
                todo_list.append(item)
                done = True
                
                speaker.say(f"I added {item} to the to do list!")
                speaker.runAndWait()
        except sr.UnknownValueError:
            
            recognizer = sr.Recognizer()
            print("I did not understand. Please try again")
            speaker.say("I did not understand. Please try again")
                      
def show_todos():
    
    print("Listening to todo audio")
    speaker.say("The item on your to do list are the following")
    for item in todo_list:
        
        speaker.say(item)
        speaker.runAndWait()
        
def hello():
    speaker.say("Hello. What can i do for you?")
    speaker.runAndWait()
    
    
def quit():
    speaker.say("Bye!")
    speaker.runAndWait()
    sys.exit(0)
    
mappings = {
    
    "create_note":create_note,
    "exit":quit
}    
                            
assistant = GenericAssistant('pattern.json', intent_methods=mappings)
assistant.train_model()

while True: 
    try:
      with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
        message  = recognizer.recognize_google(audio)
        message = message.lower() 
        speaker.say(message)
        assistant.request(message)
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()



# obtain audio from the microphone

# with sr.Microphone() as source:
#     print("Say something!")
#     recognizer.adjust_for_ambient_noise(source, duration=0.2)
#     audio = recognizer.listen(source)
#     recognizer.recognize_google(audio)
#     print(audio)