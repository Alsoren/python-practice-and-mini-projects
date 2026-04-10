def control(int1):
    if int1 < 10:
        int_str = str(int1)
        return "0"+int_str
    else:
        return str(int1)