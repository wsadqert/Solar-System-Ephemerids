
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
        for line in table_str.split('\n'):
            print(line)
            time.sleep(0.1)