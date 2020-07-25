import voicemeeter
# version of Voicemeeter
spud = 'potato'


def restart():
    with voicemeeter.remote(spud, delay=0.025) as vmr:
        vmr.restart()
