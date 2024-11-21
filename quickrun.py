from viewmodels.main_vm import MainViewModel

vm = MainViewModel()
generated_code = vm.generate_code("sum two integers")
print(generated_code)