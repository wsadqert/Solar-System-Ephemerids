from informer import Informer
from astropy.coordinates import EarthLocation, solar_system_ephemeris
from get_loc import get_loc, get_loc_offline
from ephems import solar_system_full, custom_bodies
from update_time import update_time
import requests

inf: Informer = Informer()
inf.set_loading('initializing')

try:
	conn: bool = requests.request('GET', 'https://google.com', timeout=1) == 200
except requests.exceptions.ConnectionError:
	inf.set_warning(False, 'no internet connection')
	conn: bool = False
	print()

inf.set_success(True, 'ready to work')

if conn:
	loc: EarthLocation = get_loc()
else:
	loc: EarthLocation = get_loc_offline()

time_now, _ = update_time()

print()

solar_system_ephemeris.bodies = list(solar_system_ephemeris.bodies)
solar_system_ephemeris.bodies.remove('earth')
solar_system_ephemeris.bodies.remove('earth-moon-barycenter')

print("Available bodies of solar system to compute: 'all', 'sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune'")
if conn:
	print("You also can enter catalogue id of object (ex. M1, NGC553)")

bodies_to_compute: tuple[str] = tuple(
	input("[?] enter bodies for calculation, separating their by space: ").lower().split())

if bodies_to_compute == ('all',):
	solar_system_full(time_now, loc)

elif 'all' in bodies_to_compute and bodies_to_compute != ('all',):
	raise ValueError()

else:
	custom_bodies(time_now, loc, bodies_to_compute, conn)
