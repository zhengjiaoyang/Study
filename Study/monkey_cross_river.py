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

    dir = 0

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

        if self.dir == 1:
            src,dst = dst,src

        if len(passenger) > 2 or len(passenger) < 1:
            print("Sorry，the passenger number invalid")
        for member in passenger:
            if member.drive == 1:
                run = 1

        if self.run == 0:
            print("Sorry,there is nobayd can drive the boat")
            return False
        else:
            src.del_member(passenger)
            dst.add_member(passenger)
            self.dir = ~ self.dir

    def del_passenger(self,passenger):
        for member in passenger:
            if member.is_mather == 1:
                self.mather.remove(member)
            else:
                self.children.remove(member)

def get_last_status(boat,src,dst,passenger):
    if boat.dir == 1:
        boat.dir = 0
        src.add_member(passenger)
        dst.del_member(passenger)
    else:
        boat.dir = 1
        src.del_member(passenger)
        dst.add_member(passenger)


def check_status(position):
    for child in position.children:
        if len(position.mather) == 0:
            pass
        else:
            if str(child).upper() not in map(str,position.mather):
                print("Error,%s child %s will be heat"%(position,child))
                return False

    return True

def choose_passenger(boat,src,dst):
    if boat.dir == 0:
        land = src
    else:
        land = dst

    passenger = []
    passenger_list = []
    passenger_list.extend(land.mather)
    passenger_list.extend(land.children)
    passenger_num = 0
    if len(passenger_list) > 1:
        passenger_num = random.randint(1,2)
    else:
        passenger_num = 1
    for i in range(passenger_num):
        random_passenger = random.randint(0,len(passenger_list)-1)
        passenger.append(passenger_list[random_passenger])
        passenger_list.pop(random_passenger)

    boat.get_passenger(passenger)
    if not check_status(boat):
        boat.del_passenger(passenger)
        choose_passenger(boat,src,dst)

    return passenger

def check_pass(dst):
    if len(dst.mather) == 3 and len(dst.children) == 3:
        print("Pass ,all monkeys success cross the river")
        return True


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
    cnt = 1 #渡河的次数

    last_passenger = []
    passenger = []
    repeat = 0

    while(len(dst_land.mather) != 3 or len(src_land.mather) != 3):
        for position in [src_land,dst_land,boat]:
            if not check_status(position):
                print("Sorry, this way may failed")
                result = 0
                break

        passenger = choose_passenger(boat,src_land,dst_land)
        if passenger == last_passenger:
            repeat += 1
            if repeat >= 10:
                print("Error,endless loop")
                break
            continue
        last_passenger == passenger
        repeat = 0

        boat.get_passenger(passenger)
        boat.cross_river(src_land,dst_land,passenger)
        boat.del_passenger(passenger)

        status = 1
        for position in [boat,src_land,dst_land]:
            if not check_status(position):
                status = 0
        if status == 0:
            status = 1
            get_last_status(boat,src_land,dst_land,passenger)
            continue

        if check_pass(dst_land):
            break

        print("[Step%d:】\n%s ---%s"%(cnt,src_land,dst_land))
        cnt += 1


















