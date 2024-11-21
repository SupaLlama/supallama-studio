import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from viewmodels.main_vm import MainViewModel


class MainView:
    def __init__(self):
        self.viewmodel = MainViewModel()

    def create_window(self):
        # Input prompt
        self.prompt_input = toga.MultilineTextInput(
            placeholder="Please describe the code you'd like to generate",
            style=Pack(flex=1)
        )

        # Button to generate code
        self.generate_button = toga.Button(
            "Generate Code!",
            on_press=self.on_press_generate_button,
            style=Pack(padding_left=5)
        )
        
        # Output area
        self.output_area = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=1, height=200)
        )
    
        # Layout
        input_box = toga.Box(
            children=[self.prompt_input, self.generate_button],
            style=Pack(direction=COLUMN, padding=5) 
        )
        main_box = toga.Box(
            children=[input_box, self.output_area],
            style=Pack(direction=COLUMN, padding=15)
        )

        # Create the main window
        window = toga.MainWindow(title="Code Generator")
        window.content = main_box
        return window
    
    def on_press_generate_button(self, widget):
        prompt = self.prompt_input.value.strip()
        if not prompt:
            self.output_area.value = "Please enter a function description"

        # Use the ViewModel to process the request
        generated_code = self.viewmodel.generate_code(prompt)
        self.output_area.value = generated_code
