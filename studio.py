
import toga

from views.main_view import MainView


def build(app):
    # Initialize the main view
    main_view = MainView()
    main_window = main_view.create_window()
    main_window.show()

def main():
    return toga.App("Studio from SupaLlama", "ai.supallama.studio", startup=build)

if __name__ == "__main__":
    main().main_loop()
