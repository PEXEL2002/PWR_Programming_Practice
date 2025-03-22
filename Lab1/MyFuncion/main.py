def Add(stri=""):
    if len(stri) == 0:
        return 0
    if stri.find(",\n") > (-1) or stri.find("\n,")>(-1) or stri.find(",\t") > (-1)or stri.find("\t,")>(-1):
        raise ValueError
    stri = stri.replace("\n",',')
    stri = stri.replace("\t",",")
    numbers = stri.strip().split(",")
    numbers = [float(i) for i in numbers]
    return sum(numbers)

