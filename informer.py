from typing import NoReturn


class Informer:
	def __init__(self):
		pass

	def set_loading(self, return_: bool, text: str = "loading...") -> NoReturn:
		end = ''
		if return_:
			end = '\r'
		print(f"[...] {text}...", end=end, flush=True)

	def set_loaded(self, text: str = "Done") -> NoReturn:
		print(text, flush=True)

	def set_info(self, return_: bool, text: str = "info") -> NoReturn:
		end = '\n'
		if return_:
			end = '\r'
		print(f"[i] {text}" + ' ' * 10, end=end, flush=True)

	def set_question(self, text: str = "question") -> str:
		return input(f"[?] {text}: ")

	def set_success(self, return_: bool, text: str = "success!") -> NoReturn:
		end = '\n'
		if return_:
			end = '\r'
		print(f"[+] {text}" + ' ' * 10, end=end, flush=True)

	def set_warning(self, return_: bool, text: str = "warning!") -> NoReturn:
		end = '\n'
		if return_:
			end = '\r'
		print(f"[!] {text}" + ' ' * 10, end=end, flush=True)

	def set_error(self, return_: bool, text: str = "error!") -> NoReturn:
		end = '\n'
		if return_:
			end = '\r'
		print(f"[×] {text}" + ' ' * 10, end=end, flush=True)
