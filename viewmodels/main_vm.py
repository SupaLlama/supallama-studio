from models.code_gen_model import CodeGenModel


class MainViewModel:
    def __init__(self):
        self.model = CodeGenModel()
    
    def generate_code(self, prompt):
        if not prompt:
            return "Error: Prompt cannot be empty!!!!! :-O  ;-) :-D"

        # Pass the prompt to the Model to generate code
        return self.model.generate_code(prompt)
