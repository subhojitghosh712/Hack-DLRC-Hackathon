# dna sequence

import urllib.request as urlreq

weburl = urlreq.urlopen(
    "https://firebasestorage.googleapis.com/v0/b/hack-dlrc.appspot.com/o/inputs%2Fq1%2F0.txt?alt=media&token=08916175-a246-460f-9504-66342425185d"
)

data = weburl.read().decode().split("\n")
new = []
for i in data:
    if "\r" in i:
        j = i.split("\r")
        new.append(j)
    else:
        continue

rna_1 = new[0][0]
rna_2 = new[2][0]
count = 0
acceptable = [("A", "T"), ("T", "A"), ("C", "G"), ("G", "C")]

for i in zip(rna_1, rna_2):
    count += 1
    if i in acceptable:
        print(f"{count} is ok")
    else:
        print(f"=====> at {count} there is wrongly paired =>{i}")
