import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
layer = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layer, encoder_handler]

#Define Cols&Rows per Nibble board
keyboard.col_pins = (board.A3, board.A2, board.A1, board.A0)
keyboard.row_pins = (board.CLK, board.MISO, board.MOSI, board.D10)
#Do I need this? Maybe
#rollover_cols_every_rows = 4
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#GPIO Encoder, on Key
encoder_handler.pins = ((board.D8, board.D9, False)

# Filler keys
_______ = KC.TRNS
xxxxxxx = KC.NO

# Layers
#LYR_STD, LYR_EXT = 0, 1

#TO_STD = KC.DF(LYR_STD)
#MT_EXT = KC.MO(LYR_EXT)

#REPL Tests
print("Hello World!")
print(dir(board))

# Keymap

keyboard.keymap = [
    # Standard (ISO) Layer
    [
                 KC.ESC , KC.N1  , KC.N2  , KC.N3  , KC.N4  , KC.N5  , KC.N6  , KC.N7  , KC.N8  , KC.N9  , KC.N0  , KC.MINS, KC.EQL , KC.BSPC,
        KC.A   , KC.TAB , KC.Q   , KC.W   , KC.E   , KC.R   , KC.T   , KC.Y   , KC.U   , KC.I   , KC.O   , KC.P   , KC.LBRC, KC.RBRC, KC.DEL ,
        xxxxxxx, KC.CAPS, KC.A   , KC.S   , KC.D   , KC.F   , KC.G   , KC.H   , KC.J   , KC.K   , KC.L   , KC.SCLN, KC.QUOT, KC.NUHS, xxxxxxx,
        KC.A  ,  KC.LSFT, KC.NUBS, KC.Z   , KC.X   , KC.C   , KC.V   , KC.B   , KC.N   , KC.M   , KC.COMM, KC.DOT , KC.SLSH, KC.UP  , KC.ENT ,
        KC.A  ,  KC.LCTL, KC.LGUI, xxxxxxx, KC.LALT, KC.A   , xxxxxxx, KC.SPC , xxxxxxx, KC.RALT, KC.A   , KC.RSFT, KC.LEFT, KC.DOWN, KC.RGHT,
    ],
    # Extra Keys Layer
#    [
#        TO_STD , KC.F1  , KC.F2  , KC.F3  , KC.F4  , KC.F5  , KC.F6  , KC.F7  , KC.F8  , KC.F9  , KC.F10 , KC.F11 , KC.F12 , KC.RESET,
#        _______, KC.N1  , KC.N2  , KC.N3  , KC.N4  , KC.N5  , KC.N6  , KC.N7  , KC.N8  , KC.N9  , KC.N0  , KC.MINS, KC.EQL , _______,
#        xxxxxxx, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, xxxxxxx,
#        KC.LSFT, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, KC.PGUP, _______,
#       KC.LCTL, KC.LGUI, xxxxxxx, KC.LALT, MT_EXT , xxxxxxx, _______, xxxxxxx, _______, TO_NUM , _______, KC.HOME, KC.PGDN, KC.END ,
#    ]
]


encoder_handler.map = ( (KC.UP, KC.DOWN), # Standard
 #                       (KC.VOLD, KC.VOLU) # Extra
                    )


if __name__ == '__main__':
    keyboard.go()
