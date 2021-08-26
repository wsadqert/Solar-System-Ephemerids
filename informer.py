class Informer:
    def __init__(self):
        pass

    def set_loading(self, text="loading..."):
        print(f"[...] {text}" + ' ' * 10, end='\r')

    def set_success(self, text="success!"):
        print(f"[+] {text}" + ' ' * 10)

    def set_error(self, text="error!"):
        print(f"[×] {text}" + ' ' * 10)
