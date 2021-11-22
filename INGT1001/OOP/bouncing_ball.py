import assets.functions as funcs


screen, clock, ball, width, height, sound = funcs.setup()


if __name__ == "__main__":
    while True:
        funcs.animation(screen, clock, ball, width, height, sound)
