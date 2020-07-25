import voicemeeter
# version of Voicemeeter
spud = 'potato'


def muteAll():
    # Strips you want to mute
    myInputs = 0, 1, 5, 6, 7
    with voicemeeter.remote(spud, delay=0.025) as vmr:
        for i in myInputs:
            if vmr.inputs[i].mute == False:
                vmr.inputs[i].mute = True
            elif vmr.inputs[i].mute == True:
                vmr.inputs[i].mute = False
