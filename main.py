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
    from ephems import solar_system_full, custom_bodies

    def update_time():
        global time_now, time_str
        while True:
            print('''\nTime entry options:    
    now. Getting time set in system
    custom. Нou must manually enter the time''')
            time_mode = input('you choice: ')
            if time_mode == 'now':
                time_str = time.strftime('%Y-%m-%d %H:%M:%S')
                time_now = Time(time_str, format='iso')
                break
            elif time_mode == 'custom':
                inf.set_warning(False, 'please enter UTC time!')
                inf.set_info(False, 'UTC = Tп - GMT')
                try:
                    values = [
                        int(input(comp + ': '))
                        for comp in ['hour', 'min', 'sec', 'day', 'month', 'year']
                    ]
                    if values[-1] not in range(1900, 2101):
                        inf.set_warning(False, 'year must be in range 1900-2100 AD')
                        raise ValueError
                except ValueError:
                    inf.set_error(False, 'invalid data')
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
        return (time_now, time_str)

    inf.set_success(True, 'ready to work')
    time.sleep(0.5)

    loc = get_loc()

    table = PrettyTable()
    table.field_names = [
        '№', 'Name of body', 'Right ascension, hms', 'Declination, dms',
        'Azimuth, °', 'Altitude, °', 'Distance'
    ]

    solar_system_ephemeris.bodies = list(solar_system_ephemeris.bodies)
    solar_system_ephemeris.bodies.remove('earth')
    solar_system_ephemeris.bodies.remove('earth-moon-barycenter')

    #update_time()

    #solar_system_full(time_now=time_now, loc=loc, table=table)
    custom_bodies(upd_time=update_time, loc=loc, table=table)
    
except KeyboardInterrupt:
    print('\n')
    inf.set_warning(False, 'program interrupted by user')
