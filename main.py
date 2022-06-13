def process_uk_holidays(in_file, out_file):
    # This function processes the CSV convert (...) from the downloadable UK Bank Holidays ICS calendar (...) into a
    # useful format for Tableau. Use the output 'UKHolidaysProcessed.csv' as a DataSource for the task of counting
    # _workdays_ between two dates on Tableau (...).

    holidays = []
    with open(in_file, 'r') as f:
        f.readline()

        while True:
            line = f.readline()
            if line == '\n': break
            title, date = line.split('\t')[:2]
            holidays.append(f'{title[1:-1]}, {date[1:-1]}')

    with open(out_file, 'w') as f_p:
        f_p.write('title, date\n' + '\n'.join(holidays))
