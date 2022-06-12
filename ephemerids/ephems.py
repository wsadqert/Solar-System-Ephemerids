from time import sleep

import astropy
from astropy.coordinates import AltAz, Distance, EarthLocation, SkyCoord, get_body, get_moon, get_sun
from astropy.time import Time
from prettytable import PrettyTable

from ephemerids._constants import *
from ephemerids.convert_coord import convert_coord
from ephemerids.informer import Informer

inf: Informer = Informer()

table: PrettyTable = PrettyTable()
table.field_names = body_params
table.horizontal_char = '—'
table.vertical_char = '│'


def solar_system_full(time_now: Time, loc: EarthLocation):
	inf.set_loading('calculating')

	with solar_system_ephemeris.set('builtin'):
		for i, body_str in enumerate(solar_system_ephemeris.bodies):
			if body_str == 'sun':
				body: SkyCoord = get_sun(time_now)
			elif body_str == 'moon':
				body: SkyCoord = get_moon(time_now)
			else:
				body: SkyCoord = get_body(body_str, time_now, loc)

			body_altAz = body.transform_to(AltAz(obstime=time_now, location=loc))

			body_to_str: list[str] = body.to_string('hmsdms').split()
			body_altAz_to_str: list[str] = body_altAz.to_string('dms').split()

			dist: Distance = body.distance

			if isinstance(dist, Distance):
				if dist.au >= 0.2:
					dist_str: str = f"{round(dist.au, 3)} AU"
				else:
					dist_str: str = f"{int(round(dist.km, -2))} km"
			else:
				dist_str = "unknown"

			table.add_row([
				i + 1,
				body_str.capitalize(),
				convert_coord(body_to_str[0], 'ra'),
				convert_coord(body_to_str[1], 'dec'),
				convert_coord(body_altAz_to_str[0], 'dec'),
				convert_coord(body_altAz_to_str[1], 'dec'),
				dist_str
			])

		inf.set_loaded()
		print()
		sleep(1)
		print(table)


def custom_bodies(time_now: Time, loc: EarthLocation, bodies_to_compute: tuple[str], conn: bool):
	inf.set_loading('calculating')

	with solar_system_ephemeris.set('builtin'):
		for i, body_name in enumerate(bodies_to_compute):
			if body_name in solar_system_ephemeris.bodies:
				if body_name == 'sun':
					body: SkyCoord = get_sun(time_now)
				elif body_name == 'moon':
					body: SkyCoord = get_moon(time_now)
				else:
					body: SkyCoord = get_body(body_name, time_now, loc)
			if conn:
				try:
					body: SkyCoord = SkyCoord.from_name(body_name)
				except astropy.coordinates.name_resolve.NameResolveError:
					inf.set_error(f'Unable to find coordinates for name {body_name}', None, False)

			body_altAz: SkyCoord = body.transform_to(AltAz(obstime=time_now, location=loc))

			body_coord = body.to_string('hmsdms').split()
			body_altAz_coord = body_altAz.to_string('dms').split()

			dist: Distance = body.distance
			
			if isinstance(dist, Distance):
				if dist.au >= 0.2:
					dist_str: str = f"{round(dist.au, 3)} AU"
				else:
					dist_str: str = f"{int(round(dist.km, -2))} km"
			else:
				dist_str = "unknown"

			table.add_row([
				i + 1,
				body_name.capitalize(),
				convert_coord(body_coord[0], 'ra'),
				convert_coord(body_coord[1], 'dec'),
				convert_coord(body_altAz_coord[0], 'dec'),
				convert_coord(body_altAz_coord[1], 'dec'),
				dist_str,
				])

		inf.set_loaded()
		print()
		sleep(1)
		print(table)
