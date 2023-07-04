
def eat():
    food = []
    print("있는 음식을 입력! (,로 구분!).")
    food = input().split(',')

    print("머먹을까아?")

    for i in range(len(food)):
        print(food[i],"먹을까? (y/n))")
        ans = input()
        if ans == 'y':
            print(food[i],"먹자")
            break
        elif i == len(food)-1:
            print("그럼 머먹을껀데!!")
        else:
            continue
        
eat()
