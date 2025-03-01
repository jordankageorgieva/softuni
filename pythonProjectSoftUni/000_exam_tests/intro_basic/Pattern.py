command = input()
while True:
    if not command or command == "END":
        break

    pass

    try:
        command = input()
    except EOFError as e:
            break