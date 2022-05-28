def zero_pad(number_string, zeros, left=True):
    """Return the string with zeros added to the left or right."""
    for i in range(zeros):
        if left:
            number_string = '0' + number_string
        else:
            number_string = number_string + '0'
    return number_string
