distance = 0
basic.show_leds("""
    . # # # .
    . # # # .
    . . # . .
    . # # # .
    . # # # .
    """)
Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
Tinybit.RGB_Car_Program().clear()
Tinybit.RGB_Car_Program().show()

def on_forever():
    global distance
    distance = Tinybit.Ultrasonic_Car()
    if Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 60)
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.BLACK) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_LEFT, 60)
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.BLACK):
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RIGHT, 60)
    else:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_STOP, 0)
    if distance < 10:
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
basic.forever(on_forever)

def on_forever2():
    if Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        basic.show_arrow(ArrowNames.SOUTH)
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.BLACK) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.BLACK):
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    else:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever2)

def on_forever3():
    if Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        Tinybit.RGB_Car_Big(Tinybit.enColor.GREEN)
        Tinybit.RGB_Car_Program().show_color(neopixel.colors(NeoPixelColors.GREEN))
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.BLACK) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        Tinybit.RGB_Car_Big(Tinybit.enColor.YELLOW)
        Tinybit.RGB_Car_Program().show_color(neopixel.colors(NeoPixelColors.YELLOW))
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.BLACK):
        Tinybit.RGB_Car_Big(Tinybit.enColor.YELLOW)
        Tinybit.RGB_Car_Program().show_color(neopixel.colors(NeoPixelColors.YELLOW))
    else:
        Tinybit.RGB_Car_Big(Tinybit.enColor.RED)
        Tinybit.RGB_Car_Program().show_color(neopixel.colors(NeoPixelColors.RED))
basic.forever(on_forever3)

def on_forever4():
    if Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        soundExpression.happy.play_until_done()
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.BLACK) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        music.play_tone(131, music.beat(BeatFraction.WHOLE))
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.BLACK):
        music.play_tone(131, music.beat(BeatFraction.WHOLE))
    else:
        music.play_tone(988, music.beat(BeatFraction.WHOLE))
basic.forever(on_forever4)
