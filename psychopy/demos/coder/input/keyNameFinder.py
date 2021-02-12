from psychopy import visual
from psychopy.hardware import keyboard

# Make window
win = visual.Window(units="height")

# Make instructions textbox
instr = visual.TextBox2(win,
    text="Press any key...",
    font="Open Sans", letterHeight=0.1,
    pos=(0, 0.2))
# Make key name textbox
output = visual.TextBox2(win,
    text="No key pressed yet",
    font="Open Sans", letterHeight=0.1,
    pos=(0, -0.2))
# Make keyboard object
kb = keyboard.Keyboard()
# Listen for keypresses until escape is pressed
keys = kb.getKeys()
while 'escape' not in keys:
    # Draw stimuli
    instr.draw()
    output.draw()
    win.flip()
    # Check keypresses
    keys = kb.getKeys()
    if keys:
        # If a key was pressed, display it
        output.text = f"That key was `{keys[-1].name}`. Press another key."
# End the demo
win.close()