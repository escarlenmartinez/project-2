while (true) {
    console.log("light.level:" + input.lightLevel())
    if (input.lightLevel() < 7) {
        light.setAll(light.rgb(23, 238, 196))
    } else if (input.lightLevel() > 14) {
        light.setAll(light.rgb(220, 17, 109))
    } else {
        light.setAll(light.rgb(220, 128, 17))
    }
    
}
