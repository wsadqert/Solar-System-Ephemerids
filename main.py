from informer import Informer
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris
import time
from get_loc import get_loc
from ephems import solar_system_full, custom_bodies

inf = Informer()
inf.set_loading('initializing')


def update_time():
	while True:
		print('''\nTime entry options:\n\tnow. Getting time set in system\n\tcustom. You must manually enter the time''')
		time_mode = input('your choice: ')
		if time_mode == 'now':
			time_str = time.strftime('%Y-%m-%d %H:%M:%S')
			time_now = Time(time_str, format='iso')
			break
		elif time_mode == 'custom':
			inf.set_warning(False, 'please enter UTC time!')
			inf.set_info(False, 'UTC = Tп - GMT')
			values = [
					int(input(comp + ': '))
					for comp in ['hour', 'min', 'sec', 'day', 'month', 'year']
				]
			if values[-1] not in range(1900, 2101):
				inf.set_error(False, "invalid data (year must be in range 1900-2100 AD)")
				continue

			time_str = f'{values[5]}-{values[4]}-{values[3]} {values[0]}:{values[1]}:{values[2]}'
			try:
				time_now = Time(time_str, format='iso')
			except ValueError:
				inf.set_error(False, f'invalid date: {time_str}')
				continue
			break
		else:
			inf.set_error(False, 'invalid choice')
			print()
			continue
	inf.set_success(False, f'time has been set: {time_str}')
	return time_now, time_str


inf.set_success(True, 'ready to work')
time.sleep(0.5)

loc = get_loc()

solar_system_ephemeris.bodies = list(solar_system_ephemeris.bodies)
solar_system_ephemeris.bodies.remove('earth')
solar_system_ephemeris.bodies.remove('earth-moon-barycenter')

print(
	"available bodies to compute: 'sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune'")

bodies_to_compute = input("[?] enter bodies for calculation, separating their by space: ").lower().split()

custom_bodies(update_time=update_time, loc=loc, bodies_to_compute=bodies_to_compute)
