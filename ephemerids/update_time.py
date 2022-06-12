import time

from astropy.time import Time

from ephemerids._constants import *
from ephemerids.informer import Informer

inf: Informer = Informer()


def update_time() -> Time:
	while True:
		print(time_entry_options)

		time_mode: str = input('your choice: ')

		time_str: str = time.strftime('%Y-%m-%d %H:%M:%S')
		time_now: Time = Time(time_str, format='iso')

		if time_mode == 'now':
			time_str = time.strftime('%Y-%m-%d %H:%M:%S')
			time_now = Time(time_str, format='iso')
			break

		elif time_mode == 'custom':
			inf.set_warning(only_utc)
			inf.set_info(what_is_uts)

			values: list[int] = [
					int(input(comp + ': '))
					for comp in ['hour', 'minute', 'second', 'day', 'month', 'year']
				]

			hour, min_, sec, day, month, year = values

			if year not in range(1900, 2101):
				inf.set_error("invalid data (year must be in range 1900-2100 AD)")
				continue

			time_str: str = f"{year}-{month}-{day} {hour}:{min_}:{sec}"

			try:
				time_now: Time = Time(time_str, format='iso')
			except ValueError:
				inf.set_error(f'invalid date: {time_str}')
				continue

			break

		else:
			inf.set_error('invalid choice')
			print()
			continue

	inf.set_success(f'time has been set: {time_str}')
	return time_now
