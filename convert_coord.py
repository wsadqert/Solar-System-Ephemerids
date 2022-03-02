def convert_coord(coord: str, type: str) -> str:
	if type == 'ra':
		coord_str = coord.replace('h', ' ').replace('m', ' ').replace('s', ' ').split()
		return coord_str[0] + 'h ' + coord_str[1] + 'm ' + str(round(float(coord_str[2]), 3)) + 's'

	elif type == 'dec':
		coord_str = coord.replace('d', ' ').replace('m', ' ').replace('s', ' ').split()
		return coord_str[0] + '° ' + coord_str[1] + "' " + str(round(float(coord_str[2]), 3)) + '"'

	else:
		raise ValueError("type must be equal to 'ra' or 'dec'")
