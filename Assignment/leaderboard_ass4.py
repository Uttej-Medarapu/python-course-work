import random
leaderboard=[]
# leaderboard=[random.randint(100,500)for i in range(10)]
# print(leaderboard)
while True:
    print("1. create a leaderboard")
    print("2.highest score")
    print("3.lowest")
    print("4.add players")
    print("5.remove player")
    print("6.check leaderboard")
    print("7.add single player")
    print("8.find a player")
    print("9.sort(high to low)")    
    print("10.top player")
    print("11.least payer")
    print("12.score division(Gold,Silver,Bronze)")
    print("13.clear")
    print("14.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        leaderboard=[{random.randint(0,500)}for i in range(10)]
        print(leaderboard)  
        print(type(leaderboard))   
    elif choice==2:
        print(max(leaderboard))
    elif choice==3:
        print(min(leaderboard))
    elif choice==4:
        leaderboard.append([random.randint(0,500)])
        print(leaderboard)
    elif choice==5:
        leaderboard.extend([random.randint(0,500)] for i in range(3))
        print(leaderboard)
    elif choice==6:
        leaderboard.pop(random.randint(0,9))
        print(leaderboard)
    elif choice==7:
        print(leaderboard)
    elif choice==8:
        index = int(input("Enter player index to find: "))
        if 0 <= index < len(leaderboard):
            print("Player score:", leaderboard[index])
    elif choice==9:
        sorted_leaderboard = sorted(leaderboard, key=lambda x: list(x)[0], reverse=True)
        print(sorted_leaderboard)
    elif choice==10:
         Find=leaderboard[random.randint(0,9)]
         print(Find)
    elif choice==11:
            index_first_value = leaderboard[0]
            count = leaderboard.count(index_first_value)
            print(f"Score {index_first_value} appears {count} times.")
    elif choice==12:
        index_first_value = leaderboard[0]
        medal=int(next(iter(index_first_value)))
        print(medal)
        if (medal) >= 400:
            print("gold medal")
        elif 200<= medal <= 399:
            print("silver medal")
        else: 
            print("bronze")
    elif choice==13:
        leaderboard.clear()
        print("leaderboard cleared")
    elif choice==14:
        print("exit")
        break

    else:
        print("INVALID CHOICE...TRY AGAIN!!!")
    