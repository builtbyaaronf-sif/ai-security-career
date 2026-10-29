name = input("what is your name? ")

match name:
    case "Alice":
        print("Disney")
    case "Bob":
        print("IRL")
    case _:
        print("You are not Aaron or Bob")