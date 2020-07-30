def age_check(dat,mon,yea,pdat,pmon,pyea):
    if int(pdat)<=int(dat) and int(pmon)<=int(mon) and int(pyea)>int(yea):
        if int(pmon)<=int(mon) and int(pdat)<int(dat):
            pdat = int(pdat)+30
            pmon = int(pmon)+11
            pyea = int(pyea)-1
            print(f"You are  {int(pdat)-int(dat)}/{int(pmon)-int(mon)}/{int(pyea)-int(yea)} year old")
            print(f"You will turn 100 year old in {30 - (int(pdat)-int(dat))}/{12 - (int(pmon)-int(mon))}/{99 - (int(pyea)-int(yea))}")
            if int(pyea)-int(yea)>100:
                print("You are the oldest person alive")
        elif int(pdat)==int(dat) and int(pmon)==int(mon):
            print(f"You are  {int(pdat)-int(dat)}/{int(pmon)-int(mon)}/{int(pyea)-int(yea)} year old")
            print(f"You will turn 100 year old in {30 - (int(pdat)-int(dat))}/{12 - (int(pmon)-int(mon))}/{99 - (int(pyea)-int(yea))}")
            if int(pyea)-int(yea)>100:
                print("You are the oldest person alive")
        elif int(pdat)==int(dat) and int(pmon)<int(mon):
            pmon = int(pmon)+11
            pyea = int(pyea)-1
            print(f"You are  {int(pdat)-int(dat)}/{int(pmon)-int(mon)}/{int(pyea)-int(yea)} year old")
            print(f"You will turn 100 year old in {30 - (int(pdat)-int(dat))}/{12 - (int(pmon)-int(mon))}/{99 - (int(pyea)-int(yea))}")
            if int(pyea)-int(yea)>100:
                print("You are the oldest person alive")
    elif int(pdat)>int(dat) and int(pmon)>int(mon) and int(pyea)>=int(yea):
        print(f"You are  {int(pdat)-int(dat)}/{int(pmon)-int(mon)}/{int(pyea)-int(yea)} year old")
        print(f"You will turn 100 year old in {30 - (int(pdat)-int(dat))}/{12 - (int(pmon)-int(mon))}/{99 - (int(pyea)-int(yea))}")
        if int(pyea)-int(yea)>100:
                print("You are the oldest person alive")
    elif int(pdat)<int(dat) and int(pmon)>int(mon) and int(pyea)>=int(yea):
        pdat = int(pdat)+30
        pmon = int(pmon)-1
        print(f"You are  {int(pdat)-int(dat)}/{int(pmon)-int(mon)}/{int(pyea)-int(yea)} year old")
        print(f"You will turn 100 year old in {30 - (int(pdat)-int(dat))}/{12 - (int(pmon)-int(mon))}/{99 - (int(pyea)-int(yea))}")
        if int(pyea)-int(yea)>100:
                print("You are the oldest person alive")
    elif int(pdat)<=int(dat) and int(pmon)<=int(mon) and int(pyea)<=int(yea):
        print("Come On! Your ain't Born yet!")
    elif int(pdat)>=int(dat) and int(pmon)<=int(mon) and int(pyea)<=int(yea):
        print("Come On! Your ain't Born yet!")
    elif int(pdat)<=int(dat) and int(pmon)>=int(mon) and int(pyea)<=int(yea):
        print("Come On! Your ain't Born yet!")
    elif int(pdat)>=int(dat) and int(pmon)>=int(mon) and int(pyea)<=int(yea):
        print("Come On! Your ain't Born yet!")

while True:
    DateOfBirth=input("Plese Enter your DOB(dd/mm/yyyy) to know your current Age.")
    TodaysDate =input("Plese Enter todays Date(dd/mm/yyyy).")
    if "/" not in DateOfBirth and "/" not in TodaysDate:
        print("Please Re-Enter inputs and use '/' ")
        continue
    elif "/" in DateOfBirth and "/" in  TodaysDate:
        break

dat,mon,yea = DateOfBirth.split("/")
pdat,pmon,pyea = TodaysDate.split("/")
age_check(dat,mon,yea,pdat,pmon,pyea)