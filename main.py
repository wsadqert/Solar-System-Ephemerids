from informer import Informer
from astropy.coordinates import EarthLocation, solar_system_ephemeris
import time
from get_loc import get_loc
from ephems import solar_system_full, custom_bodies
from update_time import update_time

inf = Informer()
inf.set_loading('initializing')


inf.set_success(True, 'ready to work')
time.sleep(0.5)

loc: EarthLocation = get_loc()

solar_system_ephemeris.bodies = list(solar_system_ephemeris.bodies)
solar_system_ephemeris.bodies.remove('earth')
solar_system_ephemeris.bodies.remove('earth-moon-barycenter')

print(
	"available bodies to compute: 'all', 'sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', "
	"'neptune'")

bodies_to_compute: tuple[str] = tuple(input("[?] enter bodies for calculation, separating their by space: ").lower().split())

time_now, _ = update_time()

if bodies_to_compute == ['all']:
	solar_system_full(time_now, loc)
elif 'all' in bodies_to_compute:
	raise ValueError()
else:
	custom_bodies(time_now, loc, bodies_to_compute)
