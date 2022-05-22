import http.client as httplib

from astropy.coordinates import EarthLocation, solar_system_ephemeris
from astropy.time import Time
from rich.traceback import install

from ephemerids.ephems import solar_system_full, custom_bodies
from ephemerids.get_location import get_loc, get_loc_offline
from ephemerids.informer import Informer
from ephemerids.update_time import update_time

inf: Informer = Informer()
inf.set_loading(False, 'initializing')
install(width=300, show_locals=True)


def have_internet():
	conn = httplib.HTTPSConnection("1.1.1.1", timeout=5)
	try:
		conn.request("HEAD", '/')
		return True
	except Exception:
		return False
	finally:
		conn.close()


conn = have_internet()
inf.set_loaded()

if not conn:
	inf.set_warning(False, 'no internet connection')
	conn: bool = False
	print()

if conn:
	loc: EarthLocation = get_loc()
else:
	loc: EarthLocation = get_loc_offline()

time_now: Time = update_time()

print()

solar_system_ephemeris.bodies = list(solar_system_ephemeris.bodies)
solar_system_ephemeris.bodies.remove('earth')
solar_system_ephemeris.bodies.remove('earth-moon-barycenter')

print(f"Available bodies to compute: 'all', {str(solar_system_ephemeris.bodies)[1:-1]}")
if conn:
	print("You also can enter catalogue id of object (ex. M1, NGC553)")

bodies_to_compute: tuple[str] = tuple(input("[?] enter bodies for calculation, separating their by space: ").lower().split())

if bodies_to_compute == ('all',):
	solar_system_full(time_now, loc)

elif 'all' in bodies_to_compute and bodies_to_compute != ('all',):
	raise ValueError()

else:
	custom_bodies(time_now, loc, bodies_to_compute, conn)
