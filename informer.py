class Informer:
    def __init__(self):
        pass

    def set_loading(self, text: str = "loading..."):
        print(f"[...] {text}...{' ' * 10}", end='\r')

    def set_info(self, ret: bool, text: str = "info"):
        if ret:
            print(f"[i] {text}" + ' ' * 10, end='\r')
        else:
            print(f"[i] {text}" + ' ' * 10, end='\n')

    def set_question(self, ret_type: type = str, text: str = "question"):
        return ret_type(input(f"[?] {text}: "))

    def set_success(self, ret: bool, text: str = "success!"):
        if ret:
            print(f"[+] {text}" + ' ' * 10, end='\r')
        else:
            print(f"[+] {text}" + ' ' * 10, end='\n')

    def set_warning(self, ret: bool, text: str = "warning!"):
        if ret:
            print(f"[!] {text}" + ' ' * 10, end='\r')
        else:
            print(f"[!] {text}" + ' ' * 10, end='\n')

    def set_error(self, ret: bool, text: str = "error!"):
        if ret:
            print(f"[×] {text}" + ' ' * 10, end='\r')
        else:
            print(f"[×] {text}" + ' ' * 10, end='\n')
