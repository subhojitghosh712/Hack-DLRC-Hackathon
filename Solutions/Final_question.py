import urllib.request as urlreq

weburl = urlreq.urlopen(
    "https://firebasestorage.googleapis.com/v0/b/hack-dlrc.appspot.com/o/inputs%2Fq7%2Fmapping.json?alt=media&token=37c96934-d4e0-4954-8956-79002ae1dee1"
)

dict = eval(weburl.read().decode())
print(dict)

swapped_dict = {value: key for key, value in dict.items()}
print(swapped_dict)

def Map_F(c):
    return dict[c]
def Map_B(c):
    return swapped_dict[c]

def Hexify(i):
    return hex(i)[2:]

def Prime(n):
    l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,499, 503, 509, 521, 523, 541]
    return l[n]

def Ascii(c):
    return ord(c)

def Append(a, x):
    a.append(x)

def Join(a, s):
    return s.join(map(str, a))

UserEmail = input("Enter your email: ")


StepOne = ''.join(Map_F(Character) for Character in UserEmail)

StepTwo = [Prime(Ascii(Character) - 32) for Character in StepOne]

StepThree = [Hexify(Element) for Element in StepTwo]

StepFour = '-'.join(StepThree)

StepFive = ''.join(Map_B(Character) for Character in StepFour)

print("Encrypted Email:"+StepFive+"<>")
