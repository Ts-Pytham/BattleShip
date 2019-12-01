def strcmp(string1, string2, Bool = True):
    value = 1
    if len(string1) == len(string2):
        for i,j in zip(string1, string2):
            if Bool == True:
                if 122 >= ord(i) >= 65 and 122 >= ord(j) >= 65:
                    if ord(i) == ord(j) or ord(i)-ord(j) == 32 or ord(i)-ord(j) == -32:
                        value = 0
                    else:
                        value = 1
                        break
                else:
                    if ord(i) == ord(j):
                        value = 0
                    else:
                        value = 1
                        break
            else:
                if ord(i)-ord(j) == 0:
                    value = 0
                else:
                    value = 1
                    break
        return value
    else:
        return 1


def strcpy(dest, origin):
    dest = ""
    origin = ""
    dest = origin
    return dest


def strlen(string):
    n = 0
    for _ in string:
         n += 1
    print(n)
    return n


def strcat(dest, string):
    dest += string
    return dest
