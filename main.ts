input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    set_hand_to = 0
    if (set_hand_to == 1) {
        basic.showLeds(`
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        `)
    } else if (set_hand_to == 2) {
        basic.showLeds(`
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        `)
    } else {
        basic.showLeds(`
            # # . . #
                        # # . # .
                        . # # . .
                        # # . # .
                        # # . . #
        `)
    }
    
})
let set_hand_to = 0
makerbit.connectLcd(39)
basic.forever(function on_forever() {
    makerbit.showStringOnLcd1602("Luz", makerbit.position1602(LcdPosition1602.Pos1), 16)
    makerbit.showStringOnLcd1602("" + ("" + Environment.ReadLightIntensity(AnalogPin.P0)), makerbit.position1602(LcdPosition1602.Pos17), 16)
    basic.pause(1000)
})
basic.forever(function on_forever2() {
    
})
