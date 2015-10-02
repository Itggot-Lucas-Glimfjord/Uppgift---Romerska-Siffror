def romanize(value):
    def repeat_char(integer, char):
        test = ""
        for i in range(integer):
            test += char
        return test
    temp = []
    for num, place in zip(reversed(str(value)), [0,1,2,3]):

        num = int(num)

        if place == 0:
            if num < 4:
                temp.append(repeat_char(integer=num, char="I"))
            elif num == 4:
                temp.append("IV")
            elif num == 9:
                temp.append("IX")
            else:
                temp.append("V" + repeat_char(integer=num - 5, char="I"))
        elif place == 1:
            if num < 4:
                temp.append(repeat_char(integer=num, char="X"))
            elif num == 4:
                temp.append("XL")
            elif num == 9:
                temp.append("XC")
            else:
                temp.append("L" + repeat_char(integer=num - 5, char="X"))
        elif place == 2:
            if num < 4:
                temp.append(repeat_char(integer=num, char="C"))
            elif num == 4:
                temp.append("CD")
            elif num == 9:
                temp.append("CM")
            else:
                temp.append("D" + repeat_char(integer=num - 5, char="C"))
        elif place == 3:
            temp.append(repeat_char(integer=num, char="M"))
        else:
            return "Not Valid"

    print "".join(reversed(temp))

romanize(2033)
