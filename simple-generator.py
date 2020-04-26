import datetime, time, random, string

def randomString(stringLength=10):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

waktu =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = "simple.log"
file_log = open(filename,'a')

print(waktu+" - SIMPLEAPPS ORDER-"+randomString(14)+" "+str(random.randrange(10,99,1)), file=file_log)
# 2020-04-09 20:21:30 - SIMPLEAPPS ORDER-JVZPSPUMESYIGU 54
