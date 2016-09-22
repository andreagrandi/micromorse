# micromorse: Morse communicator for microbit
# by Andrea Grandi - MIT license
# based on: http://microbit-micropython.readthedocs.io/en/latest/tutorials/network.html

from microbit import display, button_a, button_b, sleep
import radio

morse_letter = []

MORSE_CODE_LOOKUP = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0"
}


def display_dot(line_number):
    display.set_pixel(0, line_number, 8)


def display_line(line_number):
    display.set_pixel(0, line_number, 8)
    display.set_pixel(1, line_number, 8)
    display.set_pixel(2, line_number, 8)


def decode(buffer):
    # Attempts to get the buffer of Morse code data from the lookup table. If
    # it's not there, just return a full stop.
    return MORSE_CODE_LOOKUP.get(buffer, '.')


radio.on()


while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.clear()
        letter = ''.join(morse_letter)
        radio.send(letter)
        display.show(decode(letter), clear=True, delay=400)
        morse_letter = []
    else:
        if len(morse_letter) < 5:
            if button_a.is_pressed():
                display_dot(len(morse_letter))
                morse_letter.append('.')
            if button_b.is_pressed():
                display_line(len(morse_letter))
                morse_letter.append('-')

    incoming = radio.receive()
    if incoming:
        letter = decode(incoming)
        display.show(letter, delay=1000, clear=True)
    sleep(300)
