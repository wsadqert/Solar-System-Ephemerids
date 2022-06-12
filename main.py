import http.client as httplib

from astropy.coordinates import EarthLocation
from astropy.time import Time
from rich.traceback import install

from ephemerids._constants import *
from ephemerids.ephems import custom_bodies, solar_system_full
from ephemerids.get_location import get_loc, get_loc_offline
from ephemerids.informer import Informer
from ephemerids.update_time import update_time

inf: Informer = Informer()
inf.set_loading('initializing')
install(width=300, show_locals=True)


def have_internet():
	conn = httplib.HTTPSConnection("1.1.1.1", timeout=5)
	try:
		conn.request("HEAD", '/')
		return True
	except OSError:
		return False
	finally:
		conn.close()


conn = have_internet()
inf.set_loaded()

print()

if not conn:
	inf.set_warning(f'no internet connection')
	conn: bool = False
	print()

if conn:
	loc: EarthLocation = get_loc()
else:
	loc: EarthLocation = get_loc_offline()

print()

time_now: Time = update_time()

solar_system_ephemeris.bodies = bodies

print('\n', available_bodies)

if conn:
	print(body_id_hint)

bodies_to_compute: tuple[str] = tuple(inf.set_question("enter bodies for calculation, separating their by space").lower().split())

while True:
	if bodies_to_compute == ('all',):
		solar_system_full(time_now, loc)
		break
	
	elif 'all' in bodies_to_compute:
		inf.set_error('incorrect input!', None, False)
	
	else:
		custom_bodies(time_now, loc, bodies_to_compute, conn)
		break
