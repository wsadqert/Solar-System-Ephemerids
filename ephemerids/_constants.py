from typing import Final

import colorama
from astropy.coordinates import solar_system_ephemeris

BLACK = colorama.Fore.BLACK
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.BLUE
MAGENTA = colorama.Fore.MAGENTA
CYAN = colorama.Fore.CYAN
WHITE = colorama.Fore.WHITE
LIGHTGREEN_EX = colorama.Fore.LIGHTGREEN_EX
RESET = colorama.Fore.RESET + '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


body_params: Final[list[str, ...]] = ['№', 'Name of body', 'Right ascension, hms', 'Declination, dms', 'Azimuth, °', 'Altitude, °', 'Distance']

bodies = list(solar_system_ephemeris.bodies)
bodies.remove('earth')
bodies.remove('earth-moon-barycenter')


location_entry_options: Final[str] = f"""{BOLD}Location entry options:{RESET}
	1. By address (city + country)
	2. By address (house + street + city + country)
	3. By address (custom)
	4. By coordinates"""
location_entry_options_no_inet: Final[str] = f"""{BOLD}Location entry options:{RESET}
	1. By coordinates"""
time_entry_options: Final[str] = f"""{BOLD}Time entry options:{RESET}
	now. Getting time set in system
	custom. You must manually enter the time"""
available_bodies: Final[str] = f"{BOLD}Available bodies to compute{RESET}: 'all', {str(bodies)[1:-1]}"
body_id_hint: Final[str] = "You also can enter catalogue id of object (ex. M1, NGC553)"
unable_retrieve: Final[str] = "Unable to retrieve coordinates for address"
only_utc: Final[str] = "please enter UTC time!"
what_is_utc: Final[str] = "UTC = Tп - GMT"
