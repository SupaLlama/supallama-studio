import toga


def button_handler(widget):
    print("hello world!")


def build(app):
    box = toga.Box()

    button = toga.Button("Hello world")
    button.style.padding = 50
    button.style.flex = 1
    box.add(button)

    return box


def main():
    return toga.App("First App", "ai.supallama", startup=build)


if __name__ == "__main__":
    main().main_loop()
