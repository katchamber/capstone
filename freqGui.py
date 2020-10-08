from guizero import App, Text, TextBox, PushButton


def getFreqValue():
    if ((int(lightFreqInput.value) < 0) or (int(lightFreqInput.value) > 60)):
        mainDisplay.value ="Light Frequency out of bounds"
        lightFreq=0;
    else:
            lightFreq = int(lightFreqInput.value)
    if ((int(audioFreqInput.value) < 0) or (int(audioFreqInput.value) > 60)):
        mainDisplay.value ="Audio Frequency out of bounds"
        audioFreq=0;
    else:
            audioFreq = int(audioFreqInput.value)
    
    
            

    
freqGui = App(title="Brain Bot")

lightFreq = 0
audioFreq = 0

mainDisplay = Text(freqGui, text="Welcome to the Brain Bot",size=36, font="Roboto") #main display
lightTitle = Text(freqGui,text="Light Frequency",size=24,font="Roboto")
lightFreqInput = TextBox(freqGui, width="40")
audioTitle = Text(freqGui,text="Audio Frequency",size=24,font="Roboto")
audioFreqInput = TextBox(freqGui, width="40")
updateFreqValue = PushButton(freqGui,command=getFreqValue,text="Update Frequency Values")

displayLight = Text(freqGui,text="Light Frequency: " + str(lightFreq),size=24,font="Roboto")
displayAudio = Text(freqGui,text="Audio Frequency: " + str(audioFreq),size=24,font="Roboto")



freqGui.display()



