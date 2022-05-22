from typing import Literal


def convert_coord(coord: str, type: Literal['ra', 'dec']) -> str:
	"""
	Style 1 - 0h1m2.3454321s (input for type 'ra')\n
	Style 2 - 0h 1m 2.345s (return for type 'ra')\n
	Style 3 - 0d1m2.3454321s (input for type 'dec')\n
	Style 4 - 0° 1' 2.345" (return for type 'dec')\n

	:param coord: coordinate of body, formatted by Style 1 or Style
	:param type: type of coordinate ('ra' or 'dec)
	:return: coordinate of body, formatted by
	"""
	if type == 'ra':
		coord_str = coord.replace('h', ' ').replace('m', ' ').replace('s', ' ').split()
		return coord_str[0] + 'h ' + coord_str[1] + 'm ' + str(round(float(coord_str[2]), 3)) + 's'

	elif type == 'dec':
		coord_str = coord.replace('d', ' ').replace('m', ' ').replace('s', ' ').split()
		return coord_str[0] + '° ' + coord_str[1] + "' " + str(round(float(coord_str[2]), 3)) + '"'

	else:
		raise ValueError("type must be equal to 'ra' or 'dec'")
