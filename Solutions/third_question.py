# dna sequence

import urllib.request as urlreq

weburl = urlreq.urlopen(
    "https://firebasestorage.googleapis.com/v0/b/hack-dlrc.appspot.com/o/inputs%2Fq3%2F0.txt?alt=media&token=e5c9d9de-57b6-4f8c-88bc-4046285d3d41"
)

data = weburl.read().decode().split("\n")
new = []

for i in data:
    if i == "\r":
        new.append("sys")
    elif "-" in i:
        j = i.split("\r")
        m = j[0].split("-")
        new.append(m)
    else:
        continue
new.append("sys")

systems = []
subsystem = []
for i in new:
    if i == "sys":
        systems.append(subsystem)
        subsystem = []
        continue
    else:
        subsystem.append(i)

c = 1
avgl = []
for i in systems:
    s = 0
    avg = 0
    np = 0
    for planet in i:
        v = float(planet[0][1:])
        r = float(planet[1][1:])

        t = 2 * 3.14 * r / v
        m = (4 * (3.14**2) * (r**3)) / (6.67 * (10**-11) *(t*t))

        s += m
        np += 1
    avg = s / np
    avgl.append(avg)
    c += 1

print(len(avgl))

for i in range(len(avgl)):
    avgl[i] = [i+1,avgl[i]]

print(avgl)

max = 1
maxv = avgl[0][1]

for i in avgl:
    if i[1] > maxv:
        maxv = i[1]
        max = i[0]

print(max)