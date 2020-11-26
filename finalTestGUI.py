from guizero import App, Text, TextBox, PushButton
#from tonegen3 import ToneGenerator
#import RPi.GPIO as IO  
from time import sleep 


#IO.setwarnings(False) 
#IO.setmode (IO.BCM)
#IO.setup(13,IO.OUT)



#dev stuff: don't change if you don't know what you're doing
freqLowLim = 20 #lowest allowable limit for both light and audio freq
freqHighLim = 60 #highest allowable limit for both light and audio freq
#generator = ToneGenerator()
PWMpin = 13 #specifies which pin the PWM comes out from

#default values: you can change these as long as they fit in the bounds defined above
lightFreq = 40 #integer: light frequency
audioFreq = 40 #interger: audio frequency
durationValue = 10 #determines how long the test runs for
amplitude = 0.50 #affects volume of audio, literally represents the amplitude of the sine wave it generates
dutyCycle = 80 #specifies duty cycle of the PWM


def getFreqValue():
    #called upon pressing main button, updateFreqValue
    #checks user input for both light and audio frequencies
    #checks for input to be in range
    #if out of range, informs user of error
    
    global lightFreq
    global audioFreq
    
    try:
    
        if ((int(lightFreqInput.value) < freqLowLim) or (int(lightFreqInput.value) > freqHighLim)):
            err1 = True
        else:
            lightFreq = int(lightFreqInput.value)
            err1 = False
            
        if ((int(audioFreqInput.value) < freqLowLim) or (int(audioFreqInput.value) > freqHighLim)):
            err2 = True
        else:
            audioFreq = int(audioFreqInput.value)
            err2 = False
            
        if(err2 or err1):
            errFlagBox.value = 'Frequency Error: Please enter a valid integer (' + str(freqLowLim) + "Hz " + str(freqHighLim) + "Hz)"
        else:
            errFlagBox.value = 'Frequencies Updated'
            
        
    except ValueError:
        errFlagBox.value = 'Please input a value'
    displayLight.value = "Light Frequency: " + str(lightFreq)
    displayAudio.value = "Audio Frequency: " + str(audioFreq)
        
    
def runAudio():
    #runs audio at spec freq
    
    global audioFreq
    #generator.play(audioFreq, durationValue, amplitude)
    
    
def runLight():
    #runs a PWM at spec freq to trigger light panel
    
    global lightFreq
    global PWMpin
    global dutyCycle
    
    #p = IO.PWM(PWMpin,lightFreq)
    #p.start(dutyCycle)
    #sleep(durationValue)
    #p.stop()
    #IO.output(PWMpin, IO.LOW)

def updateCycle():
    #updates the dutyCycle variable
    
    global dutyCycle
    
    try:
    
        if ((int(cycleInput.value) > 0) and (int(cycleInput.value) < 100)):
            dutyCycle = int(cycleInput.value)
            cyclePrompt.value = "Enter a duty cycle"
        else:
            cyclePrompt.value = "Duty Cycle Error: Please enter a valid integer (0 100)"
            
    except ValueError:
        cyclePrompt.value = "Error: Please enter a value"
        
    displayCycle.value = "Duty Cycle: " + str(dutyCycle)
    
def updateAmplitude():
    #updates the amplitude variable
    
    global amplitude
    
    try:
    
        if ((float(ampInput.value) > 0) and (float(ampInput.value) < 100)):
            amplitude = float(ampInput.value)
            ampPrompt.value = "Enter an amplitude"
        else:
            ampPrompt.value = "Amplitude Error: Please enter a valid "
            
    except ValueError:
        ampPrompt.value = "Error: Please enter a value"
        
    displayAmp.value = "Amplitude: " + str(amplitude)
        
def updateDuration():
    global durationValue
    global runStatusAudio
    
    try:
        if(int(durationInput.value) < 1):
            durationPrompt.value = "Please enter a valid duration time"
        else:
            durationValue = int(durationInput.value)
            durationPrompt.value = "Enter a test duration"
            
    except ValueError:
        durationPrompt.value = "Please enter a valid duration time"
        
    displayDuration.value = "Test Duration: " + str(durationValue)+"s"

    
   
freqGui = App(title="Neurotherapy Control GUI") #start app

mainDisplay = Text(freqGui, text="Welcome",size=36, font="Roboto") #main display

errFlagBox = Text(freqGui,text="**",size=24,font="Roboto") #displays if there is currently an error in the acceptance of user inputs
lightTitle = Text(freqGui,text="Light Frequency",size=24,font="Roboto") #main Light Frequency display (int lightFreq)
lightFreqInput = TextBox(freqGui, width="40") #accepts user input for (int lightFreq)

audioTitle = Text(freqGui,text="Audio Frequency",size=24,font="Roboto") #main Audio Frequency display (int audioFreq)
audioFreqInput = TextBox(freqGui, width="40") #accepts user input for (int audioFreq)

updateFreqValue = PushButton(freqGui,command=getFreqValue,text="Update Frequency Values") #updates both (ints audioFreq, lightFreq)

lineBreak = Text(freqGui,text="",size=24)

durationPrompt = Text(freqGui,text="Enter a test duration",size=24,font="Roboto")
durationInput = TextBox(freqGui, width="40")
durationButton = PushButton(freqGui,command=updateDuration,text="Update test duration")

lineBreak = Text(freqGui,text="",size=24)

cyclePrompt = Text(freqGui,text="Enter a duty cycle",size=24,font="Roboto")
cycleInput = TextBox(freqGui, width="40")
cycleButton = PushButton(freqGui,command=updateCycle,text="Update duty cycle ")

ampPrompt = Text(freqGui,text="Enter an amplitude",size=24,font="Roboto")
ampInput = TextBox(freqGui, width="40")
cycleButton = PushButton(freqGui,command=updateAmplitude,text="Update amplitude")

lineBreak = Text(freqGui,text="",size=24)

displayLight = Text(freqGui,text="Light Frequency: " + str(lightFreq)+"Hz",size=24,font="Roboto") #display for current (int lightFreq)
displayAudio = Text(freqGui,text="Audio Frequency: " + str(audioFreq)+"Hz",size=24,font="Roboto") #display for current (int audioFreq)

displayCycle = Text(freqGui,text="Duty Cycle: " + str(dutyCycle)+"%",size=24,font="Roboto")
displayAmp = Text(freqGui,text="Audio Amplitude: " + str(amplitude),size=24,font="Roboto")
displayDuration = Text(freqGui,text="Test Duration: " + str(durationValue)+"s",size=24,font="Roboto")



onLight = PushButton(freqGui,command=runLight,text="Press to run lights") #changes status of (boolean runStatusLight)
onAudio = PushButton(freqGui,command=runAudio,text="Press to run audio") #changes status of (boolean runStatusAudio)

freqGui.display() #end app
