import astropy
from astropy.time import Time
from astropy.coordinates import EarthLocation, SkyCoord, solar_system_ephemeris, AltAz, get_body, get_moon, get_sun
from convert_coord import convert_coord
from prettytable import PrettyTable
from informer import Informer

inf = Informer()

table = PrettyTable()
table.field_names = ['№', 'Name of body', 'Right ascension, hms', 'Declination, dms', 'Azimuth, °', 'Altitude, °', 'Distance']


def solar_system_full(time_now: Time, loc: EarthLocation):
	with solar_system_ephemeris.set('builtin'):
		for i, body_str in enumerate(solar_system_ephemeris.bodies):
			if body_str == 'sun':
				body = get_sun(time_now)
			elif body_str == 'moon':
				body = get_moon(time_now)
			else:
				body = get_body(body_str, time_now, loc)

			body_altAz = body.transform_to(AltAz(obstime=time_now, location=loc))

			body_to_str = body.to_string('hmsdms').split()
			body_altAz_to_str = body_altAz.to_string('dms').split()

			table.add_row([
				i + 1,
				body_str.capitalize(),
				convert_coord(body_to_str[0], 'ra'),
				convert_coord(body_to_str[1], 'dec'),
				convert_coord(body_altAz_to_str[0], 'dec'),
				convert_coord(body_altAz_to_str[1], 'dec'),
				round(body.distance.au, 3)
			])
		table_str = table.get_string()
		inf.set_success(False, 'calculated!')
		print()
		print(table_str)


def custom_bodies(time_now: Time, loc: EarthLocation, bodies_to_compute: tuple[str]):
	inf.set_loading('calculating...')

	with solar_system_ephemeris.set('builtin'):
		for i, body_str in enumerate(bodies_to_compute):
			if body_str in solar_system_ephemeris.bodies:
				if body_str == 'sun':
					body = get_sun(time_now)
				elif body_str == 'moon':
					body = get_moon(time_now)
				else:
					body = get_body(body_str, time_now, loc)
			else:
				try:
					body = SkyCoord.from_name(body_str)
				except astropy.coordinates.name_resolve.NameResolveError:
					inf.set_error(
						False,
						f'Unable to find coordinates for name {body_str}')
			body_altAz = body.transform_to(AltAz(obstime=time_now, location=loc))

			body_to_str = body.to_string('hmsdms').split()
			body_altAz_to_str = body_altAz.to_string('dms').split()
			dist = body.distance
			last = '---'
			if isinstance(dist, astropy.coordinates.Distance):
				if dist.au >= 0.2:
					last = f'{round(dist.au, 3)} AU'
				else:
					last = f'{round(dist.km, 3)} km'
			table.add_row([
				i + 1,
				body_str.capitalize(),
				convert_coord(body_to_str[0], 'ra'),
				convert_coord(body_to_str[1], 'dec'),
				convert_coord(body_altAz_to_str[0], 'dec'),
				convert_coord(body_altAz_to_str[1], 'dec'),
				last,
				])
		table_str = table.get_string()
		inf.set_success(False, 'calculated!')
		print()
		print(table_str)
