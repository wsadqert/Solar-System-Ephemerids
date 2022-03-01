class Informer:
    def __init__(self):
        pass

    def set_loading(self, text: str = "loading..."):
        print(f"[...] {text}...{' ' * 10}", end='\r')

    def set_info(self, return_: bool, text: str = "info"):
        if return_:
            print(f"[i] {text}" + ' ' * 10, end='\r')
        else:
            print(f"[i] {text}" + ' ' * 10, end='\n')

    def set_question(self, ret_type: type = str, text: str = "question"):
        return ret_type(input(f"[?] {text}: "))

    def set_success(self, return_: bool, text: str = "success!"):
        if return_:
            print(f"[+] {text}" + ' ' * 10, end='\r')
        else:
            print(f"[+] {text}" + ' ' * 10, end='\n')

    def set_warning(self, return_: bool, text: str = "warning!"):
        if return_:
            print(f"[!] {text}" + ' ' * 10, end='\r')
        else:
            print(f"[!] {text}" + ' ' * 10, end='\n')

    def set_error(self, return_: bool, text: str = "error!"):
        if return_:
            print(f"[×] {text}" + ' ' * 10, end='\r')
        else:
            print(f"[×] {text}" + ' ' * 10, end='\n')
