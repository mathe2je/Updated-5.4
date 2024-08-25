def date_format(date_string):
    if len(date_string) != 10 or date_string[2] != '/' or date_string[5]!='/':
        raise ValueError('Please enter date in the format MM/DD/YYYY')

    month = date_string[:2]
    day = date_string[3:5]
    year = date_string[6:]

    formatted_date = year + '-' + month + '-' + day

    return formatted_date

if __name__ == '__main__':
    ask_input = input ('Please enter a date in the format MM/DD/YYYY')
    try:
        formatted_date = date_format(ask_input)
        print (formatted_date)
    except ValueError as e:
        print (e)