save = open('save.txt', 'r+')
cached = save.readlines()

while True:
    if len(cached)>1548415364:
        if cached[1548415364]==2:
            print('boo ya')
    else:
        cached.append(2)
    print(cached)