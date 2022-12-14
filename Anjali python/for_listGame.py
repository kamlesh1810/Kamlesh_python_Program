import random

game_list=[]
main_li=[]
player1=[]
player2=[]



while len(main_li)<12:
    tickect=random.randint(1,50)
    if tickect not in main_li:
        main_li.append(tickect)

print(main_li)
print()

game_list=list(main_li)    
player1=main_li[:6]
player2=main_li[6:]


random.shuffle(main_li)
for i in main_li:
    print(i,end=" ")

print()

print(player1)
print(player2)



status=True

while status:
    p1=len(player1)
    p2=len(player2)

    if p1<1 or p2<1:
        status=False
        if p1<1:
            print(f"Player 1 won ")
        else:
            print("Player 2 won ")    
    else:

        input()    # for click event       
        # print("enter enter button for click event")
        main_ticket=random.choice(main_li)
        print(f"        {main_ticket}       ")
        if main_ticket in player1:
            player1.remove(main_ticket)
            main_li.remove(main_ticket)
        elif main_ticket in player2:
            player2.remove(main_ticket)
            main_li.remove(main_ticket)

        print()    
        print(main_li)
        print(player1)
        print(player2
        )





