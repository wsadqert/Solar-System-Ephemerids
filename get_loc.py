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
					inf.set_loading(False, 'getting coordinates')
					loc: EarthLocation = EarthLocation.from_geodetic(lat=lat, lon=long)
					inf.set_loaded()
				except (ValueError, astropy.units.UnitsError):
					inf.set_error(False, "invalid data")
			else:
				inf.set_error(False, "incorrect choice")

			if mode in (1, 2, 3):
				inf.set_loading(False, 'getting coordinates')
				loc = EarthLocation.of_address(address)
				inf.set_loaded()

		except astropy.coordinates.name_resolve.NameResolveError:
			inf.set_error(False, f"Unable to retrieve coordinates for address '{address}'")

		else:
			if mode != 4:
				inf.set_success(False, f"location found: lat = {round(loc.lat.deg, 3)}, long = {round(loc.lon.deg, 3)}")
			break
	return loc


def get_loc_offline() -> EarthLocation:
	while True:
		print("""Location entry options:
	1. By coordinates""")
		try:
			lat, long = float(input("latitude: ")), float(input("longitude: "))
			inf.set_loading(False, 'getting coordinates')
			loc: EarthLocation = EarthLocation.from_geodetic(lat=lat, lon=long)
			inf.set_loaded()
		except (ValueError, astropy.units.UnitsError):
			inf.set_error(False, "invalid data")
			continue
		break

	return loc
