#  Copyright (c) 2022.
#
#
#

class Informer:
	def __init__(self):
		pass

	def set_loading(self, return_: bool, text: str = "loading...") -> None:
		end = ''
		if return_:
			end = '\r'
		print(f"[...] {text}...", end=end, flush=True)

	def set_loaded(self, text: str = "Done") -> None:
		print(text, flush=True)

	def set_info(self, return_: bool, text: str = "info") -> None:
		end = '\n'
		if return_:
			end = '\r'
		print(f"[i] {text}" + ' ' * 10, end=end, flush=True)

	def set_question(self, text: str = "question") -> str:
		return input(f"[?] {text}: ")

	def set_success(self, return_: bool, text: str = "success!") -> None:
		end = '\n'
		if return_:
			end = '\r'
		print(f"[+] {text}" + ' ' * 10, end=end, flush=True)

	def set_warning(self, return_: bool, text: str = "warning!") -> None:
		end = '\n'
		if return_:
			end = '\r'
		print(f"[!] {text}" + ' ' * 10, end=end, flush=True)

	def set_error(self, return_: bool, text: str = "error!") -> None:
		end = '\n'
		if return_:
			end = '\r'
		print(f"[×] {text}" + ' ' * 10, end=end, flush=True)
