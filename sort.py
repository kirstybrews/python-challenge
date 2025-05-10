def volume(width, height, length):
    return width * height * length

def get_bulky(width, height, length):
    bulky = False

    if width >= 150:
        bulky = True
    if height >= 150:
        bulky = True
    if length >= 150:
        bulky = True
    if volume(width, height, length) >= 1000000:
        bulky = True

    return bulky

def sort(width, height, length, mass):
    heavy = mass >= 20
    bulky = get_bulky(width, height, length)

    stack = "STANDARD"

    if bulky and heavy:
        stack = "REJECTED"
    elif bulky or heavy:
        stack = "SPECIAL"

    return stack
    