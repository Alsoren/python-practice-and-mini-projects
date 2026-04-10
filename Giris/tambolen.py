import re

def control(int1):
    if int1 < 10:
        int_str = str(int1)
        return "0"+int_str
    else:
        return str(int1)

text = "00:01:25,740 --> 00:01:27,865"

groups = text.split("-->")
group1 = re.split(r"[:]", groups[0])
group2 = re.split(r"[:]", groups[1])
                                
hour = int(group1[0])
minute = int(group1[1])
second = float(group1[2].replace(",", "."))
total = hour * 3600 + minute * 60 + second
group1[0] = control(int(total/3600))
group1[1] = control(int((total%3600)/60))
seconds = (total % 3600) % 60
group1[2] = f"{seconds:06.3f}".replace(".", ",")


hour = int(group2[0])
minute = int(group2[1])
second = float(group2[2].replace(",", "."))
total = hour * 3600 + minute * 60 + second
group2[0] = control(int(total/3600))
group2[1] = control(int((total%3600)/60))
seconds = (total % 3600) % 60
group2[2] = f"{seconds:06.3f}".replace(".", ",")
                
text = ":".join(group1) + " --> " + ":".join(group2)

print(text)