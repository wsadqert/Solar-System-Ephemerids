def convert_coord(coord: str, type: str) -> str:
	if type == 'ra':
		l = coord.replace('h', ' ').replace('m', ' ').replace('s', ' ').split()
		return l[0] + 'h ' + l[1] + 'm ' + str(round(float(l[2]), 3)) + 's'

	elif type == 'dec':
		l = coord.replace('d', ' ').replace('m', ' ').replace('s', ' ').split()
		return l[0] + '° ' + l[1] + "'" + str(round(float(l[2]), 3)) + '"'

	else:
		raise ValueError("type must be equal to 'ra' or 'dec'")
