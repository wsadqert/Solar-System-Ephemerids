from informer import Informer
from astropy.coordinates import EarthLocation
import astropy

inf = Informer()


def get_loc():
    while True:
        print('''Location entry options:
        1. By address (city + country)
        2. By address (house + street + city + country)
        3. By address (custom)
        4. By coordinates''')
        try:
            mode = int(input('your choice: '))
            if mode == 1:
                address = f'{input("city: ")}, {input("country: ")}'
            elif mode == 2:
                address = f'{input("house: ")} {input("street: ")}, {input("city: ")}, {input("country: ")}'
            elif mode == 3:
                address = input("address: ")
            elif mode == 4:
                lat, long = input("lat: "), input("long: ")
                inf.set_loading()
                loc = EarthLocation.from_geodetic(lat=lat, lon=long)
            else:
                raise ValueError
            if mode in range(1, 4):
                inf.set_loading()
                loc = EarthLocation.of_address(address)
        except ValueError:
            inf.set_error('invalid choice')
        except astropy.coordinates.name_resolve.NameResolveError:
            inf.set_error(f'Unable to retrieve coordinates for address \'{address}\'')
        else:
            inf.set_success(
                f"location found: lat={round(loc.lat.deg, 3)}, long={round(loc.lon.deg, 3)}"
            )
            break
        finally:
            print()
    return loc
