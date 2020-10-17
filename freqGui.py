from guizero import App, Text, TextBox, PushButton

#data I gotta send to Kathyrn
lightFreq = 0 #integer: light frequency
audioFreq = 0 #interger: audio frequency
runStatusAudio = False #boolean: False implies audio off, True implies audio on
runStatusLight = False #boolean: False implies light off, True implies light on

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
    
    runStatusAudio = not runStatusAudio
    
    onOffAudio.text = "Audio status: " + str(runStatusAudio)
    
def onOffLight():
    #flips value of boolean runStatusLight, updates user visuals
    #send boolean runStatusLight to main script
    
    global lightFreq
    global runStatusLight
    
    runStatusLight = not runStatusLight
    
    onOffLight.text = "Light status: " + str(runStatusLight)
   
freqGui = App(title="Neurotherapy Control GUI") #start app

mainDisplay = Text(freqGui, text="Welcome",size=36, font="Roboto") #main display

lightTitle = Text(freqGui,text="Light Frequency",size=24,font="Roboto") #main Light Frequency display (int lightFreq)
lightFreqInput = TextBox(freqGui, width="40") #accepts user input for (int lightFreq)

audioTitle = Text(freqGui,text="Audio Frequency",size=24,font="Roboto") #main Audio Frequency display (int audioFreq)
audioFreqInput = TextBox(freqGui, width="40") #accepts user input for (int audioFreq)

updateFreqValue = PushButton(freqGui,command=getFreqValue,text="Update Frequency Values") #updates both (ints audioFreq, lightFreq)

displayLight = Text(freqGui,text="Light Frequency: " + str(lightFreq),size=24,font="Roboto") #display for current (int lightFreq)
displayAudio = Text(freqGui,text="Audio Frequency: " + str(audioFreq),size=24,font="Roboto") #display for current (int audioFreq)

errFlagBox = Text(freqGui,text="**",size=24,font="Roboto") #displays if there is currently an error in the acceptance of user inputs

onOffLight = PushButton(freqGui,command=onOffLight,text="Light status: Standby") #changes status of (boolean runStatusLight
onOffAudio = PushButton(freqGui,command=onOffAudio,text="Audio status: Standby") #changes status of (boolean runStatusAudio)

freqGui.display() #end app
