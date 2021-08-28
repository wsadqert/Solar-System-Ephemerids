try:
    from informer import Informer

    inf = Informer()
    inf.set_loading('initing')

    from astropy.time import Time
    from astropy.coordinates import solar_system_ephemeris, EarthLocation, SkyCoord, AltAz
    from astropy.coordinates import get_body, get_moon, get_sun
    import time
    from prettytable import PrettyTable
    from convert_coord import convert_coord
    from get_loc import get_loc

    def update_time():
        global time_now
        time_now = Time(time.strftime('%Y-%m-%d %H:%M:%S'), format='iso')

    inf.set_success(True, 'ready to work')
    time.sleep(1)

    loc = get_loc()

    table = PrettyTable()
    table.field_names = [
        '№', 'Name of body', 'Right ascension, hms', 'Declination, dms',
        'Azimuth, °', 'Altitude, °', 'Distance, AU'
    ]

    solar_system_ephemeris.bodies = list(solar_system_ephemeris.bodies)
    solar_system_ephemeris.bodies.remove('earth')
    solar_system_ephemeris.bodies.remove('earth-moon-barycenter')

    update_time()

    inf.set_loading('calculating')

    with solar_system_ephemeris.set('builtin'):
        for i, body_str in enumerate(solar_system_ephemeris.bodies):
            if body_str == 'sun':
                body = get_sun(time_now)
            elif body_str == 'moon':
                body = get_moon(time_now)
            else:
                body = get_body(body_str, time_now, loc)

            body_aa = body.transform_to(AltAz(obstime=time_now, location=loc))

            body_to_str = body.to_string('hmsdms').split()
            body_aa_to_str = body_aa.to_string('dms').split()

            table.add_row([
                i + 1,
                body_str.capitalize(),
                convert_coord(body_to_str[0], 'ra'),
                convert_coord(body_to_str[1], 'dec'),
                convert_coord(body_aa_to_str[0], 'dec'),
                convert_coord(body_aa_to_str[1], 'dec'),
                round(body.distance.au, 3)
            ])
        table_str = table.get_string()
        inf.set_success(False, 'calculated!')
        print()
        for string in table_str.split('\n'):
            print(string)
            time.sleep(0.1)
except KeyboardInterrupt:
    print('\n')
    inf.set_warning(False, 'program interrupted by user')
