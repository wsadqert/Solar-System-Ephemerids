import astropy
from astropy.coordinates import EarthLocation

from ephemerids._messages import location_entry_options, location_entry_options_no_inet
from ephemerids.informer import Informer

inf = Informer()


def get_loc() -> EarthLocation:
	while True:
		print(location_entry_options)
		try:
			mode: int = int(input('your choice: '))
		except ValueError:
			inf.set_error(False, "incorrect choice")
			continue
			
		if mode not in (1, 2, 3, 4):
			inf.set_error(False, "incorrect choice")
			continue
		
		match mode:
			case 1:
				address: str = f'{input("city: ")}, {input("country: ")}'
			case 2:
				address: str = f'{input("house: ")} {input("street: ")}, {input("city: ")}, {input("country: ")}'
			case 3:
				address: str = input("address: ")
			case 4:
				address: str = '!MODE_COORDINATES!'
			case _:
				address: str = '!ERROR!'
				pass
		
		if address == '!MODE_COORDINATES!':
			try:
				lat, long = float(input("latitude: ")), float(input("longitude: "))
				inf.set_loading(False, 'getting coordinates')
				
				if not (0 <= lat <= 180 and -90 <= lat <= 90):
					raise ValueError
				
				loc: EarthLocation = EarthLocation.from_geodetic(lat=lat, lon=long)
				inf.set_loaded()
			except ValueError:
				inf.set_loaded()
				inf.set_error(False, "invalid data")
		
		try:
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
		print(location_entry_options_no_inet)
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
