import voicemeeter

# version of voicemeeter
spud = "potato"

# pass parameters to the main script when running to change values
# Macro Deck examples:
#
# -     strip6 output a1
# -     strip6 gain up
#


def strip6(action, value):
    with voicemeeter.remote(spud, delay=0.025) as vmr:
        action = action
        value = value

        if action == "gain":
            if value == "up":
                vmr.inputs[6].gain += 2
            elif value == "down":
                vmr.inputs[6].gain -= 2

        if action == "mute":
            if vmr.inputs[6].mute == True:
                vmr.inputs[6].mute = False
            elif vmr.inputs[6].mute == False:
                vmr.inputs[6].mute = True

        if action == "output":
            if value == "a1":
                if vmr.inputs[6].A1 == False:
                    vmr.inputs[6].A1 = True
                    if vmr.inputs[6].A2 == True:
                        vmr.inputs[6].A2 = False
                elif vmr.inputs[6].A1 == True:
                    vmr.inputs[6].A1 = False

            if value == "a2":
                if vmr.inputs[6].A2 == False:
                    vmr.inputs[6].A2 = True
                if vmr.inputs[6].A1 == True:
                    vmr.inputs[6].A1 = False
                elif vmr.inputs[6].A2 == True:
                    vmr.inputs[6].A2 = False

            if value == "b2":
                if vmr.inputs[6].B2 == True:
                    vmr.inputs[6].B2 = 0
                elif vmr.inputs[6].B2 == False:
                    vmr.inputs[6].B2 = 1

            elif value == "off":
                vmr.inputs[6].A1 = False
                vmr.inputs[6].A2 = False
                vmr.inputs[6].B2 = False
