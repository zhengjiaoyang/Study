import random

class monkey:
    is_mather = 0
    drive = 0

class land:
    mather = []
    children = []
    def add_member(self,passenger):
        for member in passenger:

            if member.is_mather == 1:
                self.mather.append(member)
            else:
                self.children.append(member)

    def del_member(self,passenger):
         for member in passenger:
             if member.is_mather == 1:
                 self.mather.remove(member)
             else:
                 self.children.remove(member)

class boat:

    dir == 0

    mather = []
    children = []

    run = 0

    def get_passenger(self,passenger):
        for member in passenger:

            if member.is_mather == 1:
                self.mather.append(member)
            else:
                self.children.append(member)

    def cross_river(self,src,dst,passenger):

        if len(passenger) > 2 or len(passenger) < 1:
            print("Sorry，the passenger number invalid")
        for member in passenger:
            if member.drive == 1:
                run = 1

        if run == 0:
            print("Sorry,there is nobayd can drive the boat")
            return False
        else:
            src.del_member(passenger)
            dst.add_member(passenger)
            dir = ~dir

    def del_passenger(self,passenger):
        for member in passenger:
            if member.is_mather == 1:
                self.mather.remove(member)
            else:
                self.children.remove(member)


def check_status(position):
    for child in position.children:
        if len(position.mather) == 0:
            pass
        else:
            if str(child) not in map(str(),position.mather):
                print("Error,%s child %s will be heat"%(position,child))
                return False

def choose_passenger(boat,src,dst):
    if boat.dir == 0:
        land = src
    else:
        land = dst

    passenger = []
    passenger_list = []
    passenger_list.extend(land.mather)
    passenger_list.extend(land.children)
    passenger_num = random.randint(0,1)
    for i in range(passenger_num + 1):
        random_passenger = random.randint(0,len(passenger_list)-1)
        passenger.append(passenger_list[random_passenger])
        passenger_list.pop(random_passenger)

    boat.get_passenger(passenger)
    if not check_status(boat):
        boat.del_passenger(passenger)
        choose_passenger(land)

    return passenger

if __name__ == "__main__":
    #init
    A, B, C, a, b, c = [monkey() for i in range(6)]
    for mather in [A, B, C]:
        mather.is_mather = 1
        mather.drive = 1

    for children in [a, b, c]:
        children.is_mather = 0
        children.drive = 0

    c.drive = 1

    src_land = land()
    dst_land = land()

    boat = boat()

    src_land.mather = [A, B, C]
    src_land.children = [a, b, c]

    result = 1 #结果，1=pass，0=fail
    cnt = 0 #渡河的次数

    last_passenger = []
    passenger = []
    repeat = 0

    while(len(dst_land.mather) != 3 or len(src_land.mather) != 3):
        for position in [src_land,dst_land,boat]:
            if not check_status(position):
                print("Sorry, this way may failed")
                result = 0
                break

        passenger = (boat,src_land,dst_land)
        if passenger == last_passenger:
            repeat += 1
            if repeat >= 10:
                print("Error,endless loop")
                break
            continue
        last_passenger == passenger
        repeat = 0













