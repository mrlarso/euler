import random

paths = []
while True:
    path = []
    choice = ["down","right"]
    move_count = {"down":0,"right":0}
    while len(choice) > 0:
        this_turn = random.choice(choice)
        move_count[this_turn] += 1
        path.append(this_turn)
        for i in choice:
            if move_count[i] == 20:
                choice.remove(i)
    #print path
    if path not in paths:
        paths.append(path)
    print len(paths)
    #raw_input()
