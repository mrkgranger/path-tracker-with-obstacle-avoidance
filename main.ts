let distance = 0
basic.showLeds(`
    . # # # .
    . # # # .
    . . # . .
    . # # # .
    . # # # .
    `)
Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
Tinybit.RGB_Car_Program().clear()
Tinybit.RGB_Car_Program().show()
basic.forever(function () {
    distance = Tinybit.Ultrasonic_Car()
    if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.White) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.White)) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 20)
    } else if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.Black) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.White)) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Left, 20)
    } else if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.White) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.Black)) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Right, 20)
    } else {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Stop, 0)
    }
    if (distance < 10) {
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        music.playTone(262, music.beat(BeatFraction.Whole))
    }
})
basic.forever(function () {
    if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.White) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.White)) {
        basic.showArrow(ArrowNames.South)
    } else if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.Black) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.White)) {
        basic.showArrow(ArrowNames.SouthEast)
    } else if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.White) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.Black)) {
        basic.showArrow(ArrowNames.SouthWest)
    } else {
        basic.showIcon(IconNames.No)
    }
})
basic.forever(function () {
    if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.White) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.White)) {
        Tinybit.RGB_Car_Big(Tinybit.enColor.Green)
        Tinybit.RGB_Car_Program().showColor(neopixel.colors(NeoPixelColors.Green))
    } else if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.Black) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.White)) {
        Tinybit.RGB_Car_Big(Tinybit.enColor.Yellow)
        Tinybit.RGB_Car_Program().showColor(neopixel.colors(NeoPixelColors.Yellow))
    } else if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.White) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.Black)) {
        Tinybit.RGB_Car_Big(Tinybit.enColor.Yellow)
        Tinybit.RGB_Car_Program().showColor(neopixel.colors(NeoPixelColors.Yellow))
    } else {
        Tinybit.RGB_Car_Big(Tinybit.enColor.Red)
        Tinybit.RGB_Car_Program().showColor(neopixel.colors(NeoPixelColors.Red))
    }
})
basic.forever(function () {
    if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.White) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.White)) {
        soundExpression.happy.playUntilDone()
    } else if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.Black) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.White)) {
        music.playTone(131, music.beat(BeatFraction.Whole))
    } else if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.White) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.Black)) {
        music.playTone(131, music.beat(BeatFraction.Whole))
    } else {
        music.playTone(988, music.beat(BeatFraction.Whole))
    }
})
