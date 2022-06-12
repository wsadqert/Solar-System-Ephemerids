import astropy
from astropy.coordinates import EarthLocation

from ephemerids._constants import *
from ephemerids.informer import Informer

inf = Informer()


def get_loc() -> EarthLocation:
	while True:
		print(location_entry_options)
		try:
			mode: int = int(input('your choice: '))
		except ValueError:
			inf.set_error("incorrect choice", None, False)
			continue
		
		if mode not in (1, 2, 3, 4):
			inf.set_error("incorrect choice", None, False)
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
			lat, long = [float(input(i)) for i in (" ‣latitude: ", " ‣longitude: ")]
			inf.set_loading('getting coordinates')
			
			if not (-180 <= lat <= 180 and -90 <= long <= 90):
				inf.set_error('invalid data', None, False)
				continue
			
			loc: EarthLocation = EarthLocation.from_geodetic(lat=lat, lon=long)
			inf.set_loaded()
		
		try:
			if mode in (1, 2, 3):
				inf.set_loading('getting coordinates')
				loc = EarthLocation.of_address(address)
				inf.set_loaded()
		except astropy.coordinates.name_resolve.NameResolveError:
			inf.set_error(f"{unable_retrieve} '{address}'", None, False)
		else:
			inf.set_success(f"location found: lat = {round(loc.lat.deg, 3)}, long = {round(loc.lon.deg, 3)}")
			break
	return loc


def get_loc_offline() -> EarthLocation:
	while True:
		print(location_entry_options_no_inet)
		
		lat, long = [float(input(i)) for i in (" ‣latitude: ", " ‣longitude: ")]
		inf.set_loading('getting coordinates')
		
		if not (-180 <= lat <= 180 and -90 <= long <= 90):
			inf.set_loaded()
			inf.set_error('invalid data', None, False)
			continue
			
		loc: EarthLocation = EarthLocation.from_geodetic(lat=lat, lon=long)
		inf.set_loaded()
		return loc
