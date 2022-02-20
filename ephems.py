def solar_system_full(time_now, loc, table):
    from informer import Informer

    inf = Informer()

    from astropy.coordinates import solar_system_ephemeris, AltAz  #, EarthLocation, SkyCoord
    from astropy.coordinates import get_body, get_moon, get_sun
    import time
    from convert_coord import convert_coord

    with solar_system_ephemeris.set('builtin'):
        for i, body_str in enumerate(solar_system_ephemeris.bodies_to_compute):
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
        for line in table_str.split('\n'):
            print(line)
            time.sleep(0.1)


def custom_bodies(upd_time, loc, table):
    from informer import Informer
    inf = Informer()
    from astropy.coordinates import solar_system_ephemeris, AltAz, SkyCoord  #, EarthLocation
    from astropy.coordinates import get_body, get_moon, get_sun
    import astropy
    #import numpy as np
    import time
    from convert_coord import convert_coord

    bodies_to_compute = input("[?] enter bodies for calculation, separating their by space: ").split()
    global time_now
    time_now, time_str = upd_time()
    inf.set_loading('calculating')

    with solar_system_ephemeris.set('builtin'):
        for i, body_str in enumerate(bodies_to_compute):
            if body_str in solar_system_ephemeris.bodies:
                if body_str == 'sun':
                    body = get_sun(time_now)
                elif body_str == 'moon':
                    body = get_moon(time_now)
                else:
                    body = get_body(body_str, time_now, loc)
            else:
                try:
                    body = SkyCoord.from_name(body_str)
                except astropy.coordinates.name_resolve.NameResolveError:
                    inf.set_error(
                        False,
                        f'Unable to find coordinates for name {body_str}')
            body_aa = body.transform_to(AltAz(obstime=time_now, location=loc))

            body_to_str = body.to_string('hmsdms').split()
            body_aa_to_str = body_aa.to_string('dms').split()
            dist = body.distance
            last = '---'
            if isinstance(dist, astropy.coordinates.Distance):
                if dist.au >= 0.2:
                    last = f'{round(dist.au, 3)} AU'
                else:
                    last = f'{round(dist.km, 3)} km'
            table.add_row([
                i + 1,
                body_str.capitalize(),
                convert_coord(body_to_str[0], 'ra'),
                convert_coord(body_to_str[1], 'dec'),
                convert_coord(body_aa_to_str[0], 'dec'),
                convert_coord(body_aa_to_str[1], 'dec'),
                last,
            ])
        table_str = table.get_string()
        inf.set_success(False, 'calculated!')
        print()
        for line in table_str.split('\n'):
            print(line)
            time.sleep(0.1)
