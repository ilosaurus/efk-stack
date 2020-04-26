import datetime, sys, time, random, string

def randomString(stringLength=10):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

while True:
    time.sleep(30)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" - SIMPLEAPPS ORDER-"+randomString(14)+" "+str(random.randrange(10,99,1)), flush=True)
