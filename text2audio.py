from gtts import gTTS
from playsound import playsound
    

def textAudio(text):
    audio = gTTS(text)
    audio.save('hello.mp3')
    playsound('hello.mp3')
    
    
if __name__ == '__main__':
    textAudio('Now we are all set to write a sample program that converts text to speech')