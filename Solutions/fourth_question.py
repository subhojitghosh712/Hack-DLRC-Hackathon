# number system conversion

import urllib.request as urlreq

weburl = urlreq.urlopen(
    "https://firebasestorage.googleapis.com/v0/b/hack-dlrc.appspot.com/o/inputs%2Fq4%2F0.txt?alt=media&token=89c2bb6c-1d4d-4660-85a6-d94e41a8b586"
)

data = weburl.read().decode().split("\n")
new = []
for i in data:
    new.append(i.split("\r")[0])

# - base number

new_data = []
for j in new:
    new_data.append(j.split())
new_data.remove([])

print(new_data)

# take sign then convert from base to 10

"""
def base_convert(base, number):
    number = str(number)
    base = int(base)
    decimal = 0
    power = len(number) - 1
    if base > 10:

    for i in number:
        i = int(i)
        decimal += i * (base**power)
        power -= 1
    return decimal
"""


def base_convert(base, number):
    number = str(number)
    base = int(base)
    decimal = 0
    power = len(number) - 1
    not_decimal = ["A", "B", "C", "D", "E", "F"]
    if base < 10:
        for i in number:
            i = int(i)
            decimal += i * (base**power)
            power -= 1
    elif base > 10:
        for i in number:
            if i.isdigit():
                i = int(i)
                decimal += i * (base**power)
            else:
                num = 10 + int(not_decimal.index(i))
                decimal += num * (base**power)
            power -= 1
    else:
        decimal += int(number)

    return decimal


# main question
main_sum = 0


for actual_number in new_data:
    inp_base = actual_number[1]
    inp_number = actual_number[2]
    if actual_number[0] == "+":
        main_sum += base_convert(inp_base, inp_number)
    elif actual_number[0] == "-":
        main_sum -= base_convert(inp_base, inp_number)
    else:
        print("error")
        break

print(f"The total of this data is {main_sum}")
