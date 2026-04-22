def greet(name: str) -> str:
    message = f"Hello, {name}!"
    width = len(message) + 4

    frame = "+ " + "=" * (width - 4) + " +\n"
    frame += "  " + message + "  \n"
    frame += "+ " + "=" * (width - 4) + " +"

    return frame

if __name__ == "__main__":
    print(greet("Footprints"))
