import olem 

def _spin_command() -> None:
    olem.turn(180)

def _led_command(color: str) -> None:
    olem.led_on(olem.LEDALL, color)

def _display_img_command() -> None:
    img = olem.display_img("images/check.bin")
    olem.delay_ms(2000)
    olem.display_del(img)

def parse(message: str) -> None:
    # No message received
    if message == "":
        return
    
    args = message.split(' ')

    if args[0] == "spin":
        _spin_command()
    elif args[0] == "led":
        _led_command(args[1])
    elif args[0] == "img":
        _display_img_command()