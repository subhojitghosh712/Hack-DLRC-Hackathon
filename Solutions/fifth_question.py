import urllib.request as urlreq

weburl = urlreq.urlopen(
    "https://firebasestorage.googleapis.com/v0/b/hack-dlrc.appspot.com/o/inputs%2Fq5%2F0.txt?alt=media&token=c24c1022-c3de-4d5e-857a-8464bd0bd95d"
)

data = weburl.read().decode().split("\r\n")
new = data[0].replace(" a ", " ").replace(" an ", " ").replace(" the ", " ").split()


print(new)
print(len(new))
c = 0
a = 0

while a < len(new) - 2:
    if (new[a][0] == new[a + 1][0]) and (new[a][0] == new[a + 2][0]):
        c += 1
    a+=1
print(c)