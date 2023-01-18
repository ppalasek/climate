import cdsapi

c = cdsapi.Client()

for year in range(1950, 2023):
    print('getting data for {}...'.format(year))
    c.retrieve(
    'reanalysis-era5-land',
    {
        'format': 'grib',
        'variable': '2m_temperature',
        'year': [
            '{}'.format(year),
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': '12:00',
        'area': [
            51.72, -0.57, 51.25,
            0.37,
        ],
    },
    'london/london_{}.grib'.format(year))
