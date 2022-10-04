def on_gesture_shake():
    global set_hand_to
    set_hand_to = 0
    if set_hand_to == 1:
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
    elif set_hand_to == 2:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
    else:
        basic.show_leds("""
            # # . . #
                        # # . # .
                        . # # . .
                        # # . # .
                        # # . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

set_hand_to = 0
makerbit.connect_lcd(39)

def on_forever():
    makerbit.show_string_on_lcd1602("Luz", makerbit.position1602(LcdPosition1602.POS1), 16)
    makerbit.show_string_on_lcd1602("" + str((Environment.read_light_intensity(AnalogPin.P0))),
        makerbit.position1602(LcdPosition1602.POS17),
        16)
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
