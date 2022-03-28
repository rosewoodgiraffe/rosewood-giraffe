

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()
keyboard.modules = [layers, modtap, encoder_handler]

print("Hello Wrld!")
print(dir(board))
keyboard = KMKKeyboard()

keyboard.col_pins = (board.A3, board.A2, board.A1, board.A0)    # try D5 on Feather, keeboar
keyboard.row_pins = (board.CLK, board.MISO, board.MOSI, board.D10,)    # try D6 on Feather, keeboar
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A,]
]

if __name__ == '__main__':
    keyboard.go()
