def process_uk_holidays(in_file, out_file):
    # This function processes the CSV convert (https://www.projectwizards.net/en/support/ics2csv-converter ) from the
    # downloadable UK Bank Holidays ICS calendar (https://www.gov.uk/bank-holidays) into a useful format for Tableau.
    # Use the output 'UKHolidaysProcessed.csv' as a DataSource for the task of counting _workdays_ between two dates on
    # Tableau (https://kb.tableau.com/articles/howto/calculating-the-number-of-business-days-in-a-month).

    holidays = []
    with open(in_file, 'r') as f:
        f.readline()

        while True:
            line = f.readline()
            if line == '\n': break
            title, date = line.split('\t')[:2]
            holidays.append(f'{title[1:-1]}, {date[1:-1]}')

    with open(out_file, 'w') as f_p:
        f_p.write('Holiday Name, Holiday Date\n' + ' 00:00:00\n'.join(holidays))