# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:30:59 2021

@author: admin
"""

print("Hello world-- Game started")

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
#Import messagebox and promptbox modules for tkinter
import tkinter.simpledialog

import tkinter as tk
from tkinter import messagebox 
 
#this is used for color cycle when player reach end of the game
import threading
import random
 
#try to load PIL (Pillow) module if it is available and drop an error if it is not available
try:
    from PIL import ImageTk, Image
except:
    print("Python PIL package not found. Please install it to be able load images correctly.")
import random
 
dice_num=0
#Assign array for snake holes colors in labels
SNAKE_HOLES = [17,7,  54,34,  64,60,  62,19,   87,24,   93,73,   95,75,  99,78]
snake_mouth=[17,54,64,62,87,93,95,99]
#Assign array for ladder bridges colors in labels
LADDER_BRIDGES = [4,14,   9,31,   20,38,   28,84,   40,59,  51,67,   63,81,    71,80]

username = 'Empty'
qlist=["FFT may be used to calculate 1) DFT 2)IDFT3)Direct Z-Transform 4) Indirect ZTransform. \n a) 1, 2 & 3 are correct \n b) 1 & 2 are correct \n c) 1 & 3 are correct \n d) All the four are correct"]
alist=["b"]
qlist.append("Number of stages the 8 point FFT is divided into ? \n a) 8 \n b) 3 \n c) 2 \n d) 4")
alist.append("b")
qlist.append("Composite FFT algorithm is known as ? \n a) Mixed FFT \n b) Split FFT \n c) both a & b \n d) None of the above")
alist.append("a")#3
qlist.append("In Composite FFT, N has ? \n a) less than one primary factor \n b) more than one primary factor \n c) equals to one primary factor \n d) None of the above")
alist.append("b")
qlist.append("In DIT-FFT for decomposing the DFT for N=6, the flowgraph for N=2.3 means \n a)two 3-point DFTs \n b)three 2-point DFTs \n c) Both a & b \n d)None of the above")
alist.append("a")
qlist.append(" Number of 3-points DFT for Radix-3 DIT –FFT forN=3 and 9 will be respectively \n a) 1 & 1 \n b) 1 & 3 \n c) 3 & 1 \n d) 3 & 3")
alist.append("b")#6
qlist.append("Formula for number of complex additions for Radix-2 DIT-FFT ? \n a) N/2*log₂N \n b) N \n c) N/2 \n d) N*log₂N")
alist.append("a")
qlist.append("Formula for number of complex multiplication for Radix-2 DIT-FFT ? \n a) N/2*log₂N \n b) N \n c) N/2 \n d) N*log₂N")
alist.append("d")
exp=["Since Direct Z-Transform & Indirect ZTransform are not used for the calculation of FFT"]
exp.append("since, the number of stages is 2^n i.e in this case 2^3 is 8.Thus,n=3 is correct answer")
exp.append("Composite FFT is also known as mixture of FFT because it is a mixture of more than single FFT")
exp.append("Since it is made with morte than 1 FFT ")
exp.append("since N=2.3 means two 3-point DFTs")
exp.append("since it is Radix-3, \n thus for n=3, 1 three-point DFT is required \n for n=9,3 three-point DFT is required  ")
exp.append("The number of complex additions for Radix-2 DIT-FFT is N/2*log₂N \n It can be verified by taking N=2,3 and so on ..")
exp.append("The number of complex multiplications for Radix-2 DIT-FFT is N*log₂N \n It can be verified by taking N=2,3 and so on ..")
status=1
qval=0
num=[]



#set current position
player_1_pos=0
player2_pos=0
#count player moves
player_moves=0
player2_moves=0
#count snake bites
player_bites=0
player2_bites=0
#count ladder climbs
player_climb=0
player2_climb=0
#player name variable
player_name=""
player2_name=""
#Time holder
time_elapsed=0
time_elapsed2=0
#status of the answer
status=0
#answer of the question
username= 'Empty'
old_player_pos=0
new_player_pos1=0
c=0
old_player2_pos2=0
new_player2_pos2=0


def randomColor():
    global PlayerMovesLabel
    COLORS = ['red','blue','yellow','pink','lightblue','steel blue','turquoise','sandy brown','purple','violet red','violet','maroon','tomato','orange','green yellow']
    randomColor = random.randint(0, len(COLORS))
    PlayerMovesLabel.config(bg=COLORS[randomColor])
    
def randomColor2():
    global PlayerMovesLabel2
    COLORS = ['red','blue','yellow','pink','lightblue','steel blue','turquoise','sandy brown','purple','violet red','violet','maroon','tomato','orange','green yellow']
    randomColor2 = random.randint(0, len(COLORS))
    PlayerMovesLabel2.config(bg=COLORS[randomColor2])
    
    
 
 
 
def colorCycle():
    global PlayerMovesLabel, time_elapsed
    #put it inside try, so that if in middle of color switching, main thread is closed, it don't crash
    try:
        #assign our timer
        mytimer = threading.Timer(0.2, colorCycle)
        #link timer to main thread, so that if main thread is closed, timer get stopped
        mytimer.daemon = True
        #start timer
        mytimer.start()
 
        #if player is in position 100, start the cycle 
        if player_1_pos==100:
            randomColor()
        else:
            #otherwise keep background white
            PlayerMovesLabel.config(bg='white')
 
        time_elapsed=time_elapsed+1
    except:
        #if error, do nothing. error means program has been exited but thread is running for one more last time.
        return
    
def colorCycle2():
    global PlayerMovesLabel2, time_elapsed2
    #put it inside try, so that if in middle of color switching, main thread is closed, it don't crash
    try:
        #assign our timer
        mytimer2 = threading.Timer(0.2, colorCycle2)
        #link timer to main thread, so that if main thread is closed, timer get stopped
        mytimer2.daemon = True
        #start timer
        mytimer2.start()
 
        #if player is in position 50, start the cycle
        if player2_pos==100:
            randomColor2()
        else:
            #otherwise keep background white
            PlayerMovesLabel2.config(bg='white')
 
        time_elapsed2=time_elapsed2+1
    except:
        #if error, do nothing. error means program has been exited but thread is running for one more last time.
        return
 
 
def movePlayer():
#define our global variables so that function can access variables outside of its scope
    global player_1_pos
    global dice_num
    global player_moves
    global player_bites
    global player_climb
    global grid_array
    global PlayerMovesLabel
    global diceRollLabel
    global time_elapsed
    global c
    global qval
    global num
 
#If player reach goal, reset the counter and colors
    if player_1_pos==100:
        player_1_pos=0
        player_moves=0
        player_1_pos=0
        player_bites=0
        player_climb=0
        grid_array[100-1].config(bg="white")
        time_elapsed=0
        

 
#get our old and new player positions
    old_player_pos=player_1_pos
    new_player_pos=player_1_pos+dice_num
    
    '''for i in snake_mouth:
        grid_array[i-1].config(bg="red")'''
 
#if there is snake bite or ladder climb, show feedback message
    additional_message=""
    
#code to take care when move is more than 50
    if new_player_pos>100:
        new_player_pos=100-(new_player_pos-100)

    
#detect if player go to snake hole
#enumerate snake holes to get their Index ID and
#go through list of snake holes
    for idx,val in enumerate(SNAKE_HOLES):
#in our array, first value (even index number) is snake head, and second value (odd index number) is snake tail, detect head
        if idx % 2 == 0:
#if it is head, and player is on head
            if new_player_pos==SNAKE_HOLES[idx]:
#move player to tail number
                
                global root
                global status
                global idx1
                idx1=idx
                global new_player_pos1
                new_player_pos1=new_player_pos
                
                
                
                player_bites=player_bites+1
                additional_message="Got Bitten"
                player_moves=player_moves+1 
                username = 'Empty'
                root = tk.Tk()
                qval=random.randint(1,8)
                while qval in num:
                       qval=random.randint(1,8)
                       if len(num)>=8:
                           num=[]
                num.append(qval)
                
                mainLabel = tk.Label(root, text=qlist[qval])
                mainLabel.pack()

                mainButton = tk.Button(root, text='Answer', command=onClick)
                mainButton.pack()
              
                #root.mainloop()
                grid_array[new_player_pos1-1].config(bg="blue")
                
                
            
 
#detect if player go to ladder bottom
#enumerate ladder bridges to get their Index ID and
#go through list of ladders
    for idx,val in enumerate(LADDER_BRIDGES):
#in our array, first value (even index number) is ladder bottom, and second value (odd index number) is ladder top, detect bottom
        if idx % 2 == 0:
#if it is ladder bottom, and player is on bottom of ladder
            if new_player_pos==LADDER_BRIDGES[idx]:
#climb the ladder!
                new_player_pos=LADDER_BRIDGES[idx+1]
#Update player climb counter
                player_climb=player_climb+1
                additional_message="Got Climb:"
                
            
 
 
 
#change old position to white
     

    
    if old_player_pos>0:
        grid_array[old_player_pos-1].config(bg="white")
        
  
 
#change new position to yellow
    grid_array[new_player_pos-1].config(bg="blue")
 
    
    
 
#apply change to player position variable
    player_1_pos=new_player_pos
    player_moves=player_moves+1
    
  
 
 
    if player_1_pos == 100:
        PlayerMovesLabel['text'] = player_name+"*WON* Move: " + str(player_moves) + ", Bite1: " + str(player_bites) + ", Climb:" + str(player_climb) + " *WON*"
        tkinter.messagebox.showinfo("*WON*", player_name+" Won the game in "+str(player_moves) + " moves during "+ str(int(time_elapsed/5)) +" seconds!")
    else:
        PlayerMovesLabel['text']=additional_message + "Move: " + str(player_moves) + ", Bite1: " + str(player_bites) + ", Climb:" + str(player_climb)
       
class MyDialog:
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        self.myLabel = tk.Label(top, text='Type your answer below')
        self.myLabel.pack()

        self.myEntryBox = tk.Entry(top)
        self.myEntryBox.pack()

        self.mySubmitButton = tk.Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        global username
        username = self.myEntryBox.get()
        self.top.destroy()

def onClick():
    global player_bites
    global old_player_pos
    global new_player_pos1
    global player_1_pos
    global player_moves
    global qval
    global num
    inputDialog = MyDialog(root)
    root.wait_window(inputDialog.top)
    if username==alist[qval]:
        messagebox.showinfo("Result","Congrats, correct answer. You will stay at the same position.")
        Button(root, text='Quit', command=root.destroy).pack()
        status=0    
    else:
        messagebox.showerror("Result","Oops, wrong answer. You have to move down \n **explanation:- "+exp[qval])
        Button(root, text='Quit', command=root.destroy).pack()
        status=1
    if status==0:
        grid_array[new_player_pos1-1].config(bg="blue")
        
    else:
        grid_array[new_player_pos1-1].config(bg="red")
        new_player_pos=SNAKE_HOLES[idx1+1]
        grid_array[new_player_pos-1].config(bg="blue")
        player_1_pos=new_player_pos

    
   
        
 
def movePlayer2():
#define our global variables so that function can access variables outside of its scope
   
    
    global player2_pos
    global dice_num2
    global player2_moves
    global player2_bites
    global player2_climb
    #global grid_array
    global PlayerMovesLabel2
    global diceRollLabel2
    global time_elapsed2
    global question1
    global qval
    global num
 
#If player reach goal, reset the counter and colors
    
    if player2_pos==100:
        player2_pos=0
        player2_moves=0
        player2_pos=0
        player2_bites=0
        player2_climb=0
        grid_array[100-1].config(bg="white")
        time_elapsed=0
 
#get our old and new player positions
   
    
    old_player2_pos=player2_pos
    new_player2_pos=player2_pos+dice_num2
 
#if there is snake bite or ladder climb, show feedback message
    
    additional2_message=""
#code to take care when move is more than 50
   
        
    if new_player2_pos>100:
        new_player2_pos=100-(new_player2_pos-100)
 
#detect if player go to snake hole
#enumerate snake holes to get their Index ID and
#go through list of snake holes
    for idx,val in enumerate(SNAKE_HOLES):
#in our array, first value (even index number) is snake head, and second value (odd index number) is snake tail, detect head
        if idx % 2 == 0:
#if it is head, and player is on head

                
            if new_player2_pos==SNAKE_HOLES[idx]:
                
#move player to tail number
                #new_player2_pos=SNAKE_HOLES[idx+1]
#Update player bites counter
                
                global root
                global status
                global idx2
                idx2=idx
                global new_player2_pos2
                new_player2_pos2=new_player2_pos
                
                
                qval=random.randint(1,8)
                while qval in num:
                       qval=random.ranintd(1,8) 
                       if len(num)>=8:
                           num=[]
                num.append(qval)
                player2_bites=player2_bites+1
                additional2_message="Got Bitten"
                player2_moves=player2_moves+1 
                username = 'Empty'
                root = tk.Tk()
                mainLabel = tk.Label(root, text=qlist[qval])
                mainLabel.pack()

                mainButton = tk.Button(root, text='Answer', command=onClick2)
                mainButton.pack()
        
                #root.mainloop()
                #grid_array[new_player_pos1-1].config(bg="blue")
 
#detect if player go to ladder bottom
#enumerate ladder bridges to get their Index ID and
#go through list of ladders
    for idx,val in enumerate(LADDER_BRIDGES):
#in our array, first value (even index number) is ladder bottom, and second value (odd index number) is ladder top, detect bottom
        if idx % 2 == 0:
#if it is ladder bottom, and player is on bottom of ladder
            
                
            if new_player2_pos==LADDER_BRIDGES[idx]:
#climb the ladder!
                new_player2_pos=LADDER_BRIDGES[idx+1]
#Update player climb counter
                player2_climb=player2_climb+1
                additional2_message="Got Ladder |_-`| "
 
 
 
 
#change old position to white
 
        
    if old_player2_pos>0 :
        if old_player2_pos not in snake_mouth:
            grid_array[old_player2_pos-1].config(bg="white")
 
#change new position to yellow
    
    
    grid_array[new_player2_pos-1].config(bg="lightblue")
 
#apply change to player position variable
  
    
    player2_pos=new_player2_pos
    player2_moves=player2_moves+1
 
 
    
    if player2_pos == 100:
        PlayerMovesLabel2['text'] =player2_name+"*WON* Move: " + str(player2_moves) + ", Bite2: " + str(player2_bites) + ", Climb:" + str(player2_climb) + " *WON*"
        tkinter.messagebox.showinfo("*WON*", player2_name+" Won the game in "+str(player2_moves) + " moves during "+ str(int(time_elapsed/5)) +" seconds!")
    else:
       
        PlayerMovesLabel2['text']=additional2_message + "Move: " + str(player2_moves) + ", Bite2: " + str(player2_bites) + ", Climb:" + str(player2_climb) 
    
class MyDialog2:
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        self.myLabel = tk.Label(top, text='Type your answer below')
        self.myLabel.pack()

        self.myEntryBox = tk.Entry(top)
        self.myEntryBox.pack()

        self.mySubmitButton = tk.Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        global username
        username = self.myEntryBox.get()
        self.top.destroy()
def onClick2():
    global player2_bites
    global old_player2_pos
    global new_player2_pos2
    global player2_pos
    global player2_moves
    global qval
    global num
    inputDialog = MyDialog(root)
    root.wait_window(inputDialog.top)
    if username==alist[qval]:
        messagebox.showinfo("Result","Congrats, correct answer. You will stay at the same position.")
        Button(root, text='Quit', command=root.destroy).pack()
        status=0
        
    else:
        messagebox.showerror("Result","Oops, wrong answer. You have to move down \n **explanation:- "+exp[qval])
        Button(root, text='Quit', command=root.destroy).pack()
        status=1
    if status==0:
        grid_array[new_player2_pos2-1].config(bg="lightblue")
        
    else:
        grid_array[new_player2_pos2-1].config(bg="red")
        new_player2_pos2=SNAKE_HOLES[idx2+1]
#Update player bites counter
        #grid_array[old_player_pos-1].config(bg="white")
        grid_array[new_player2_pos2-1].config(bg="lightblue")
        player2_pos=new_player2_pos2
        

      
#function when Roll button is clicked
def rollTheDice():
        global dice_num
        global diceRollLabel
        
        for i in snake_mouth:
            grid_array[i-1].config(bg="red")
    #get a random number between 1 to 6
        dice_num=random.randint(1,6)
        
    #write number into label
        diceRollLabel['text']=player_name + " Rolled: " + str(dice_num)
        
    #move the player!
        movePlayer()
        
def rollTheDice2():
        global dice_num2
        global diceRollLabel2
        
        for i in snake_mouth:
            grid_array[i-1].config(bg="red")
    #get a random number between 1 to 6
        dice_num2=random.randint(1,6)
        
    #write number into label
        diceRollLabel2['text']=player2_name + " Rolled: " + str(dice_num2)
        
    #move the player!
        movePlayer2()
 
 

def createGUI():
    global grid_array
    global PlayerMovesLabel
    global diceRollLabel
    global diceWindow
    global player_name
    
    #global grid_array
    global PlayerMovesLabel2
    global diceRollLabel2
    global diceWindow2
    global player2_name
    global test
 
    # create diceWindow
    diceWindow = Tk()
    #test=Tk()
    #test.title("NEW")
    
 
 
    # Set title for diceWindow
    diceWindow.title("SNAKE & LADDERS")
    # Make window not resizable
    diceWindow.resizable(width=True, height=True)
    diceWindow.config(bg='white')
    

    # Load logo if PIL module is installed:
    try:
        #load logo.gif
       logoFile=Image.open("lbg='white'ogo.gif")
        #resize the image to match field size
       logo = logoFile.resize((300, 37), Image.ANTIALIAS)
        #define image type
       logo = ImageTk.PhotoImage(logo)
        #put image into a label
       logoContainer = Label(diceWindow, image = logo,bg='white')
        #show the label
       logoContainer.grid(row=0,column=1,columnspan=10)
 
    except:
    #otherwise just show a label
        RevertLogoImage = Label(diceWindow, text="Snake & Ladder",bg='grey',font=("Arial",50))
        RevertLogoImage.grid(row=0, column=5, columnspan=10)
        print("Logo rendering has been skipped.")
 
    #create moves indicator label
    PlayerMovesLabel = Label(diceWindow, text="Please provide your name", bg='white')
    PlayerMovesLabel.grid(row=1,column=1,columnspan=10)
    
    PlayerMovesLabel2 = Label(diceWindow, text="        Provide your name  ", bg='white')
    PlayerMovesLabel2.grid(row=1,column=1,columnspan=10)
 
    #Create button for GUI
    btnRoll = Button(diceWindow, text="Roll1", command=rollTheDice,bg='blue', width=15)
    
    btnRoll2 = Button(diceWindow, text="Roll2", command=rollTheDice2,bg='lightblue', width=15)
    #show it on screen
    btnRoll.grid(row=3,column=0,columnspan=10)
    
    btnRoll2.grid(row=3,column=9,columnspan=10)
 
    #create our board interface
    #define out array of labels first
    grid_array = []
    for y in range (0,10):
        for x in range (0,10):
            array_num=((x+1)+(y*10))
            grid_array.append(Label(diceWindow, borderwidth=8,text=  array_num  ))
 
            #get x and y and put them into new variable to avoid editing original x/y variables which can cause infinite loop
            xx=x
            yy=y
 
            #a simple control to make board-like numbers to position correctly
            yy=abs(yy-9)
            #reverse the numbers if it is not even row
            if not yy % 2:
                xx=abs(xx-9)
 
            grid_array[array_num - 1].grid(row=  (yy+1)  +4,column=(xx+1)+4)
            #fix problem with windows OS that don't show labels in white color by default
            grid_array[array_num - 1].config(bg='white')
            #take care of snake holes, apply custom colors
            if array_num in SNAKE_HOLES:
                #if it is even index number, means it is snake head
                if SNAKE_HOLES.index(array_num) % 2 == 0:
                    #red is for snake head
                    grid_array[array_num-1].config(fg="black")
                    grid_array[array_num - 1].config(bg='red')
                else:
                    #orange is for snake tail
                    grid_array[array_num-1].config(fg="red")
                    grid_array[array_num - 1].config(bg='white')
 
            #take care of ladder bridges, apply custom colors
            if array_num in LADDER_BRIDGES:
                #if it is even index number, it means it is ladder bottom
                if LADDER_BRIDGES.index(array_num) % 2 == 0:
                    #blue is ladder bottom
                    grid_array[array_num-1].config(fg="white")
                    grid_array[array_num - 1].config(bg='green')
                else:
                    #blue is ladder top
                    grid_array[array_num-1].config(fg="lightgreen")
    #initialize timer
    colorCycle()
    colorCycle2()
 
    #If user cancel promptbox dialog or left name empty, ask again
    while player_name=='' or player_name is None:
        player_name=tkinter.simpledialog.askstring("Player Name1","Please enter your name: ")
        PlayerMovesLabel = Label(diceWindow, text="-Waiting for first Roll -", bg='white')
        PlayerMovesLabel.grid(row=1,column=1,columnspan=10)
        #PlayerMovesLabel['text']='- Waiting for first Roll -'
        
    while player2_name=='' or player2_name is None:
        player2_name=tkinter.simpledialog.askstring("Player Name2","Please enter your name: ")
        PlayerMovesLabel2 = Label(diceWindow, text="-Waiting for second Roll -", bg='white')
        PlayerMovesLabel2.grid(row=1,column=11,columnspan=10)
   #     PlayerMovesLabel2['text']='-Waiting for second Roll -
 
    #create introduction label
    diceRollLabel = Label(diceWindow, bg="white", text="Welcome "+player_name+", Please roll your dice!")
    diceRollLabel.grid(row=2,column=1,columnspan=10)
    
    diceRollLabel2 = Label(diceWindow, bg="white", text="Welcome "+player2_name+", Please roll your dice!")
    diceRollLabel2.grid(row=2,column=10,columnspan=10)
 
    # Establish the window
    diceWindow.mainloop()
 
 
#create GUI to start things up
createGUI()