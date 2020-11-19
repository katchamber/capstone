from guizero import App, Text, TextBox, PushButton
from tonegen3 import ToneGenerator
import RPi.GPIO as IO  
from time import sleep 


IO.setwarnings(False) 
IO.setmode (IO.BCM)
IO.setup(13,IO.OUT)



#data I gotta send to Kathyrn
lightFreq = 0 #integer: light frequency
audioFreq = 0 #interger: audio frequency
runStatusAudio = False #boolean: False implies audio off, True implies audio on
runStatusLight = False #boolean: False implies light off, True implies light on
durationValue = 0
amplitude = 0.50
generator = ToneGenerator()

def getFreqValue():
    #called upon pressing main button, updateFreqValue
    #checks user input for both light and audio frequencies
    #checks for input to be in range
    #if out of range, resets value to 0 and informs user of error
    #sends lightFreq and audioFreq to main script
    
    global lightFreq
    global audioFreq
    global runStatusAudio
    global runStatusLight
    
    try:
        if ((int(lightFreqInput.value) < 0) or (int(lightFreqInput.value) > 60)):
            lightFreq=0
            err1 = True
        else:
            lightFreq = int(lightFreqInput.value)
            err1 = False
        if ((int(audioFreqInput.value) < 0) or (int(audioFreqInput.value) > 60)):
            audioFreq=0
            err2 = True
        else:
            audioFreq = int(audioFreqInput.value)
            err2 = False
        if(err2 or err1):
            errFlagBox.value = '*Error*'
        else:
            errFlagBox.value = 'Frequencies Updated'
            
        
    except ValueError:
        errFlagBox.value = 'Please input a value'
        lightFreq = 0
        audioFreq = 0
    displayLight.value = "Light Frequency: " + str(lightFreq)
    displayAudio.value = "Audio Frequency: " + str(audioFreq)
        
    
def onOffAudio():
    #flips value of boolean runStatusAudio, updates user visuals
    #send boolean runStatusAudio to main script
    
    global audioFreq
    global runStatusAudio
    
    runStatusAudio = True
    onOffAudio.text = "Audio status: " + str(runStatusAudio)
    
    if (runStatusAudio == True):
        generator.play(audioFreq, durationValue, amplitude)
        
        runStatusAudio = False
    
    onOffAudio.text = "Audio status: " + str(runStatusAudio)
    
    
def onOffLight():
    #flips value of boolean runStatusLight, updates user visuals
    #send boolean runStatusLight to main script
    
    global lightFreq
    global runStatusLight
    
    runStatusLight = not runStatusLight
    if(runStatusLight == True):
        p = IO.PWM(13,lightFreq)
        p.start(80)
    elif(runStatusLight == False):
        p.stop()
        IO.output(13, IO.LOW)
        
    onOffLight.text = "Light status: " + str(runStatusLight)

def updateDuration():
    global durationValue
    global runStatusAudio
    try:
        if(int(durationInput.value) < 0):
            durationValue = 0
            durationPrompt.value = "Please enter a valid duration time"
        else:
            durationValue = int(durationInput.value)
            durationPrompt.value = "Test duration updated"
    except ValueError:
        durationValue = 0
        durationPrompt.value = "Please enter a valid duration time"

    
   
freqGui = App(title="Neurotherapy Control GUI") #start app

mainDisplay = Text(freqGui, text="Welcome",size=36, font="Roboto") #main display

lightTitle = Text(freqGui,text="Light Frequency",size=24,font="Roboto") #main Light Frequency display (int lightFreq)
lightFreqInput = TextBox(freqGui, width="40") #accepts user input for (int lightFreq)

audioTitle = Text(freqGui,text="Audio Frequency",size=24,font="Roboto") #main Audio Frequency display (int audioFreq)
audioFreqInput = TextBox(freqGui, width="40") #accepts user input for (int audioFreq)

updateFreqValue = PushButton(freqGui,command=getFreqValue,text="Update Frequency Values") #updates both (ints audioFreq, lightFreq)

lineBreak = Text(freqGui,text="",size=24)

durationPrompt = Text(freqGui,text="Please enter a test duration",size=24,font="Roboto")
durationInput = TextBox(freqGui, width="40")
durationButton = PushButton(freqGui,command=updateDuration,text="Update test duration")

lineBreak = Text(freqGui,text="",size=24)

displayLight = Text(freqGui,text="Light Frequency: " + str(lightFreq),size=24,font="Roboto") #display for current (int lightFreq)
displayAudio = Text(freqGui,text="Audio Frequency: " + str(audioFreq),size=24,font="Roboto") #display for current (int audioFreq)

errFlagBox = Text(freqGui,text="**",size=24,font="Roboto") #displays if there is currently an error in the acceptance of user inputs

onOffLight = PushButton(freqGui,command=onOffLight,text="Light status: False") #changes status of (boolean runStatusLight
onOffAudio = PushButton(freqGui,command=onOffAudio,text="Audio status: False") #changes status of (boolean runStatusAudio)

freqGui.display() #end app
