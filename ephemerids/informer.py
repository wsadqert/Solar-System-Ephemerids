from typing import Optional

from ._constants import *


class Informer:
	def __init__(self):
		pass

	def _end(self, return_):
		return '\r' if return_ else '\n'

	def set_loading(self, text: str = "loading...") -> None:
		print(f"[...] {text}...", end='', flush=True)

	def set_loaded(self, text: str = "Done", color: Optional[str] = LIGHTGREEN_EX) -> None:
		if color is None:
			color = LIGHTGREEN_EX
		print(color, text, RESET, sep='', flush=True)

	def set_info(self, text: str = "info") -> None:
		print(f"[i] {text}" + ' ' * 10, flush=True)

	def set_question(self, text: str = "question", color: Optional[str] = CYAN) -> str:
		if color is None:
			color = CYAN
		return input(f"{color}[?]{RESET} {text}: ")

	def set_success(self, text: str = "success!", color: Optional[str] = LIGHTGREEN_EX) -> None:
		if color is None:
			color = LIGHTGREEN_EX
		print(f"{color}[+] {text}{' ' * 10}{RESET}", flush=True)

	def set_warning(self, text: str = "warning!", color: Optional[str] = YELLOW) -> None:
		if color is None:
			color = YELLOW
		print(f"{color}[!] {text}{' ' * 10}{RESET}", flush=True)

	def set_error(self, text: str = "error!", color: Optional[str] = RED, pre: Optional[bool] = True) -> None:
		if color is None:
			color = RED
		if pre:
			print(f"{color}Error{RESET}")
		print(f"{color}[×] {text}{' ' * 10}{RESET}", flush=True)
