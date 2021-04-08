def format_financial_record(record):
    """
    Format the financial record from a string to a float.
    Remove any invalid chars and convert to float type.
    """
    # Remove commas from string
    tempRecord = record.replace(',', '')
    # Remove spaces from string
    tempRecord = tempRecord.replace(' ', '')

    startsWithDash = tempRecord.startswith('-')
    # The string is just a dash
    if startsWithDash and len(tempRecord) == 1:
        return None

    if startsWithDash:
        tempRecord = tempRecord.replace('-', '')
        num = int(round(float(tempRecord)))
        num = num - (num * 2)
        num = round(num) * 1000000
        return num
    else:
        num = int(round(float(tempRecord))) * 1000000
        return num
