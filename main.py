while True:
    print("light.level:" + input.light_level())
    if input.light_level() < 7:
        light.set_all(light.rgb(23, 238, 196))
    elif input.light_level() > 14:
        light.set_all(light.rgb(220, 17, 109))
    else:
        light.set_all(light.rgb(220, 128, 17))
    