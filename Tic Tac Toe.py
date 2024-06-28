#!/usr/bin/env python
# coding: utf-8

# In[3]:


#TIC TAC TOE

def printboard(x,y):
    zero="X" if x[0] else("O" if y[0] else 0)
    one="X" if x[1] else("O" if y[1] else 1)
    two="X" if x[2] else("O" if y[2] else 2)
    three="X" if x[3] else("O" if y[3] else 3)
    four="X" if x[4] else("O" if y[4] else 4)
    five="X" if x[5] else("O" if y[5] else 5)
    six="X" if x[6] else("O" if y[6] else 6)
    seven="X" if x[7] else("O" if y[7] else 7)
    eight="X" if x[8] else("O" if y[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
    
        
    
def checkwin(x,y):
    win=[[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
    for i in win:
        if (x[i[0]]+x[i[1]]+x[i[2]])==3: 
            print("X wins")
            return "x"
        if (y[i[0]]+y[i[1]]+y[i[2]])==3:
            print("X wins")
            return "y"
        
    return 0

        
x=[0,0,0,0,0,0,0,0,0]
y=[0,0,0,0,0,0,0,0,0]
flag=0
turn=1
while(True):
    printboard(x,y)
    if turn==1:
        value=int(input("X'turn:{Enter number to place your x} "))
        x[value]=1
    else:
        value=int(input("O'turn:{Enter number to place your o} "))
        y[value]=1
    c=checkwin(x,y)  
    if c!=0:
        print("Match Over ")
        break
    turn = 1-turn 
    


# In[ ]:





# In[ ]:




