from informer import Informer
from astropy.coordinates import EarthLocation
import astropy

inf = Informer()


def get_loc() -> EarthLocation:
	while True:
		print("""Location entry options:
	1. By address (city + country)
	2. By address (house + street + city + country)
	3. By address (custom)
	4. By coordinates""")
		try:
			mode: int = int(input('your choice: '))
			if mode == 1:
				address: str = f'{input("city: ")}, {input("country: ")}'
			elif mode == 2:
				address: str = f'{input("house: ")} {input("street: ")}, {input("city: ")}, {input("country: ")}'
			elif mode == 3:
				address: str = input("address: ")
			elif mode == 4:
				try:
					lat, long = float(input("latitude: ")), float(input("longitude: "))
					inf.set_loading()
					loc: EarthLocation = EarthLocation.from_geodetic(lat=lat, lon=long)
				except ValueError:
					inf.set_error(False, "invalid data (could not convert string to float)")
			else:
				inf.set_error(False, "incorrect choice")

			if mode in (1, 2, 3):
				inf.set_loading()
				loc = EarthLocation.of_address(address)

		except astropy.coordinates.name_resolve.NameResolveError:
			inf.set_error(False, f"Unable to retrieve coordinates for address '{address}'")

		else:
			if mode != 4:
				inf.set_success(False, f"location found: lat = {round(loc.lat.deg, 3)}, long = {round(loc.lon.deg, 3)}")
			else:
				inf.set_success(False, 'ok')
			break
	print()
	return loc
