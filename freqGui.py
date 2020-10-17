from guizero import App, Text, TextBox, PushButton


#data I gotta send to Kathyrn
lightFreq = 0
audioFreq = 0
runStatusAudio = False
runStatusLight = False

def getFreqValue():

    global lightFreq
    global audioFreq
    global runStatusAudio
    global runStatusLight
    
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
            
    displayLight.value = "Light Frequency: " + str(lightFreq)
    displayAudio.value = "Audio Frequency: " + str(audioFreq)
    
def onOffAudio():

    global audioFreq
    global runStatusAudio
    
   
    runStatusAudio = not runStatusAudio
    
    onOffAudio.text = "Audio status: " + str(runStatusAudio)
    
def onOffLight():

    global lightFreq
    global runStatusLight
    
    runStatusLight = not runStatusLight
    
    onOffLight.text = "Light status: " + str(runStatusLight)
   

    
freqGui = App(title="Neurotherapy Control GUI") #start of app




mainDisplay = Text(freqGui, text="Welcome",size=36, font="Roboto") #main display




lightTitle = Text(freqGui,text="Light Frequency",size=24,font="Roboto")
lightFreqInput = TextBox(freqGui, width="40")
audioTitle = Text(freqGui,text="Audio Frequency",size=24,font="Roboto")
audioFreqInput = TextBox(freqGui, width="40")
updateFreqValue = PushButton(freqGui,command=getFreqValue,text="Update Frequency Values")

displayLight = Text(freqGui,text="No values set",size=24,font="Roboto")
displayAudio = Text(freqGui,text="No values Set",size=24,font="Roboto")

errFlagBox = Text(freqGui,text="**",size=24,font="Roboto")

onOffLight = PushButton(freqGui,command=onOffLight,text="Light status: Standby")
onOffAudio = PushButton(freqGui,command=onOffAudio,text="Audio status: Standby")


            

freqGui.display()
