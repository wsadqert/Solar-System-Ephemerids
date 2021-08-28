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
                try:
                    lat, long = float(input("lat: ")), float(input("long: "))
                    inf.set_loading()
                    loc = EarthLocation.from_geodetic(lat=lat, lon=long)
                except ValueError:
                    raise TypeError
            else:
                raise ValueError
            if mode in range(1, 4):
                inf.set_loading()
                loc = EarthLocation.of_address(address)
        except ValueError:
            inf.set_error(False, 'invalid choice')
            print()
        except TypeError:
            inf.set_error(False, 'invalid data')
            print()
        except astropy.coordinates.name_resolve.NameResolveError:
            inf.set_error(
                False,
                f'Unable to retrieve coordinates for address \'{address}\'')
            print()
        except:
            raise
        else:
            if mode!=4:
                inf.set_success(
                    False,
                    f"location found: lat={round(loc.lat.deg, 3)}, long={round(loc.lon.deg, 3)}")
            else:
                inf.set_success(False, 'ok')
            break
    return loc
