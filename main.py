while True:
    print("light.level:" + input.light_level())
    if input.light_level() < 4:
        light.set_all(light.rgb(23, 238, 196))
    elif input.light_level() > 14:
        light.set_all(light.rgb(220, 17, 109))
    