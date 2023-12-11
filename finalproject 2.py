#Partners: Lauren H. and Maegan K.
#Time tracking
'''
Maegan: 30 minutes on 11/15, worked on functions
Lauren: 30 minutes on 11/15, worked on functions
Maegan: 1 hour on 11/15, worked on functions
Maegan: 1 hour on 11/16, worked on functions
Maegan: 1 hour on 11/17, worked on functions
Lauren: 30 mins on 11/17, worked on "story-line" in class
Lauren: 45 mins on 11/17, finished "story-line"
Lauren: 1 hour on 11/17, created graphics
Lauren: 45 mins on 11/17, worked on File IO
Lauren: 1 hr on 11/18, worked on functions
Lauren: 1.5 hr on 11/25, worked on functions -> created a 'restart', need to debug, moved on to create other functions.
Maegan: 2 hours on 11/25 working on debugging restart. scrapped the restart button option
Maegan: 3 hours on 11/26 working out bugs and adding to functions, retried the restart buttons.
Maegan: 30 mins on 11/26 working on win restart
Maegan: 30 mins on 11/28 working on exit game button
Lauren: 45 mins on 11/28 expanded the "story-line"
Lauren: 3.5 hrs on 11/28  worked on adding expanded story-line functions and restart functions. Also tested all options to ensure code is working properly
Maegan: 45 mins on 11/29, worked on graphics
Lauren: 45 mins on 11/29, worked on graphics
Maegan: 30 mins on 12/1, final debug
Lauren: 30 mins on 12/1, final debug
'''

import random
from tkinter import*
from PIL import Image, ImageTk
parent = Tk()
parent.title("Save That Species!")
canvas = Canvas(parent, height = 500, width = 500, bg='white')
canvas.pack()


random_spec = ''
entry = ''
name_but = ''
no_but = ''
yes_but = ''
name = ''
ready = ''
discovery = ''
biol_name = ''
enrty = ''


#Maegan created this function
def exitgame():
    global parent
    parent.destroy()
  
#Maegan created this function
def winrestart():
    global win
    global winrestart
    global winrestart_but
    global im0
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im0)
    winrestart_but.destroy()
    win.destroy()
    opt1()
    
 
#Lauren created this function 11/28
def restart9():
    global fail_9
    global game_over
    global restart9_but
    global im0
    fail_9.destroy()
    game_over.destroy()
    restart9_but.destroy()
    opt1()
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im0)
    
#Lauren created this function 11/28
def restart8():
    global fail_8
    global game_over
    global restart8_but
    global im0
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im0)
    fail_8.destroy()
    game_over.destroy()
    restart8_but.destroy()
    opt1()
    

#Lauren created this function 11/28
def restart7():
    global fail_7
    global game_over
    global restart7_but
    global im0
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im0)
    fail_7.destroy()
    game_over.destroy()
    restart7_but.destroy()
    opt1()
    
#Lauren created this function 11/28
def restart6():
    global fail_6
    global game_over
    global restart6_but
    global im0
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im0)
    fail_6.destroy()
    game_over.destroy()
    restart6_but.destroy()
    opt1()
    
#Maegan created this function
def restart5():
    global fail_5
    global game_over
    global restart5_but
    global im0
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im0)
    fail_5.destroy()
    game_over.destroy()
    restart5_but.destroy()
    opt1()
   
#Maegan created this function
def restart4():
    global fail_4
    global game_over
    global restart4_but
    global im0
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im0)
    fail_4.destroy()
    game_over.destroy()
    restart4_but.destroy()
    opt1()
    
#Maegan created this function 
def restart3():
    global fail_3
    global game_over
    global restart3_but
    global im0
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im0)
    fail_3.destroy()
    game_over.destroy()
    restart3_but.destroy()
    opt1()

#Maegan created this function
def restart2():
    global fail_2
    global game_over
    global restart2_but
    global im0
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im0)
    fail_2.destroy()
    game_over.destroy()
    restart2_but.destroy()
    opt1()

#Maegan created this function
def restart1():
    global fail_1
    global game_over
    global restart1_but
    global im0
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im0)
    fail_1.destroy()
    game_over.destroy()
    restart1_but.destroy()
    opt1()
    
#Lauren created this function 11/25
def wingame():
    global random_spec
    global fail9_but
    global cor9_but
    global wingame
    global win
    global winrestart
    global winrestart_but
    global im0
    global im1
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im1)
    fail9_but.destroy()
    cor9_but.destroy()
    opt_9.destroy()
    win = Label(parent, text = ("You saved the "+random_spec+"!! You win!!"))
    win.pack()
    winrestart_but = Button (parent, text = 'RESTART', command = winrestart)
    winrestart_but.pack()
    
#Lauren created this function 11/25
def opt9():
    global random_spec
    global opt_8
    global fail8_but
    global cor8_but
    global opt_9
    global fail9_but
    global cor9_but
    opt_8.destroy()
    fail8_but.destroy()
    cor8_but.destroy()
    opt_9 = Label(parent, text = ("The ESA accepts your petition! You now have federal funding to save this species! What’s next?"))
    opt_9.pack()
    fail9_but = Button (parent, text = "Throw a party and feed the "+ random_spec +" cake", command = fail9)
    fail9_but.pack()
    cor9_but = Button (parent, text = "Throw a party and feed your team cake", command = wingame)
    cor9_but.pack()

#Lauren created this function 11/25
def fail9():
    global opt_8
    global fail8_but
    global cor8_but
    global restart8
    global random_spec
    global fail_9
    global game_over
    global restart9_but
    global im0
    global im2
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im2)
    opt_9.destroy()
    fail9_but.destroy()
    cor9_but.destroy()
    fail_9 = Label(parent, text = (random_spec+ " is allergic to cake and dies."))
    fail_9.pack()
    game_over = Label (parent, text = "GAME OVER!")
    game_over.pack()
    restart9_but = Button (parent, text = 'RESTART', command = restart9)
    restart9_but.pack()
    #canvas = Canvas(parent, height = 500, width = 500, bg='red').pack()
    
#Lauren created this function 11/28
def opt8():
    global random_spec
    global opt_7
    global fail7_but
    global cor7_but
    global opt_8
    global fail8_but
    global cor8_but
    opt_7.destroy()
    fail7_but.destroy()
    cor7_but.destroy()
    opt_8 = Label(parent, text = ("The people involved in the citizen science program develop a deep love for the " +random_spec+ " \n and you’re receiving more funding. What do you do with the additional funds?"))
    opt_8.pack()
    fail8_but = Button (parent, text = "Legally change your name to "+random_spec+ " master.", command = fail8)
    fail8_but.pack()
    cor8_but = Button (parent, text = "Use the funds to hire a grad student to conduct more research on the species.", command = opt9)
    cor8_but.pack()
    
    
    
#Lauren created this function 11/28
def fail8():
    global imagelist
    global opt_8
    global fail8_but
    global cor8_but
    global name
    global random_spec
    global restart8_but
    global fail_8
    global game_over
    global im0
    global im2
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im2)
    opt_8.destroy()
    fail8_but.destroy()
    cor8_but.destroy()
    fail_8 = Label(parent, text = ("The public cancels you."))
    fail_8.pack()
    game_over = Label (parent, text = "GAME OVER!")
    game_over.pack()
    restart8_but = Button (parent, text = 'RESTART', command = restart8)
    restart8_but.pack()
    #canvas = Canvas(parent, height = 500, width = 500, bg='red').pack()

    
    
    
#Lauren created this function 11/28
def opt7():
    global name
    global random_spec
    global opt_6
    global fail6_but
    global cor6_but
    global opt_7
    global fail7_but
    global cor7_but
    opt_6.destroy()
    fail6_but.destroy()
    cor6_but.destroy()
    opt_7 = Label(parent, text = ("The ESA receives your petition! What does "+name+" do during the 90 day review?"))
    opt_7.pack()
    cor7_but = Button (parent, text = "Set up a citizen scientist program that allows the general public to help you continue to collect data on the"+random_spec+".", command = opt8)
    cor7_but.pack()
    fail7_but = Button (parent, text = "Remove yourself from the study site, it’s illegal to study a species that’s under 90 day review", command = fail7)
    fail7_but.pack()
    
    
    
#Lauren created this function 11/28
def fail7():
    global imagelist
    global opt_7
    global fail7_but
    global cor7_but
    global name
    global random_spec
    global restart7_but
    global fail_7
    global game_over
    global im0
    global im2
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im2)
    opt_7.destroy()
    fail7_but.destroy()
    cor7_but.destroy()
    fail_7 = Label(parent, text = ("It’s not illegal to study a species under 90 day review."))
    fail_7.pack()
    game_over = Label (parent, text = "GAME OVER!")
    game_over.pack()
    restart7_but = Button (parent, text = 'RESTART', command = restart7)
    restart7_but.pack()
    #canvas = Canvas(parent, height = 500, width = 500, bg='red').pack()

    

#Lauren created this function 11/28
def opt6():
    global random_spec
    global opt_5
    global fail5_but
    global cor5_but
    global opt_6
    global fail6_but
    global cor6_but
    opt_5.destroy()
    fail5_but.destroy()
    cor5_but.destroy()
    opt_6 = Label(parent, text = ("You begin writing a petition to the ESA to list the "+random_spec+" as endangered, what are some things your paper needs to include?"))
    opt_6.pack()
    fail6_but = Button (parent, text = "Clear indication of species taxonomic positioning, supporting materials, current population status, trends, and population estimates", command = fail6)
    fail6_but.pack()
    cor6_but = Button (parent, text = "Clear indication of species listing, supporting materials, current population status, trends, and population estimates", command = opt7)
    cor6_but.pack()


#Lauren created this function 11/28
def fail6():
    global imagelist
    global opt_6
    global fail6_but
    global cor6_but
    global name
    global random_spec
    global restart6_but
    global fail_6
    global game_over
    global im0
    global im2
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im2)
    opt_6.destroy()
    fail6_but.destroy()
    cor6_but.destroy()
    fail_6 = Label(parent, text = ("the ESA requires a clear indication of species listing, your petition get’s rejected."))
    fail_6.pack()
    game_over = Label (parent, text = "GAME OVER!")
    game_over.pack()
    restart6_but = Button (parent, text = 'RESTART', command = restart6)
    restart6_but.pack()
    #canvas = Canvas(parent, height = 500, width = 500, bg='red').pack()



#Lauren created this function 11/25
def opt5():
    global random_spec
    global opt_4
    global fail4_but
    global cor4_but
    global opt_5
    global fail5_but
    global cor5_but
    opt_4.destroy()
    fail4_but.destroy()
    cor4_but.destroy()
    opt_5 = Label(parent, text = ("You’ve discovered that "+ random_spec + " fits the requirements \n to list it as endangered under the endangered species act, what’s next? "))
    opt_5.pack()
    cor5_but = Button (parent, text = "Begin writing a petition to the ESA to list the "+random_spec+".", command = opt6)
    cor5_but.pack()
    fail5_but = Button (parent, text = "Storm the capitol!", command = fail5)
    fail5_but.pack()

# Lauren created this function 11/25
def fail5():
    global imagelist
    global opt_4
    global fail4_but
    global cor4_but
    global name
    global random_spec
    global restart5_but
    global fail_5
    global game_over
    global im0
    global im2
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im2)
    opt_5.destroy()
    fail5_but.destroy()
    cor5_but.destroy()
    fail_5 = Label(parent, text = (name + " got arrested! The "+random_spec+" dies of grief"))
    fail_5.pack()
    game_over = Label (parent, text = "GAME OVER!")
    game_over.pack()
    restart5_but = Button (parent, text = 'RESTART', command = restart5)
    restart5_but.pack()
    #canvas = Canvas(parent, height = 500, width = 500, bg='red').pack()
    
# Lauren created this function 11/28    
def opt4():
    global random_spec
    global opt_3
    global fail3_but
    global cor3_but
    global opt_4
    global fail4_but
    global cor4_but
    opt_3.destroy()
    fail3_but.destroy()
    cor3_but.destroy()
    opt_4 = Label(parent, text = ("Your cameras gave you more data on preferred habitats, \n time of day the "+random_spec+" is most active, \n and even preferred foods of the "+random_spec+"! What’s next?"))
    opt_4.pack()
    cor4_but = Button (parent, text = "Use the mark-recapture technique to determine population size", command = opt5)
    cor4_but.pack()
    fail4_but = Button (parent, text = "Continue using the game cameras to determine population size", command = fail4)
    fail4_but.pack()

#Lauren created this function 11/28
def fail4():
    global random_spec
    global opt_4
    global fail4_but
    global cor4_but
    global fail_4
    global restart4_but
    global game_over
    global im0
    global im2
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im2)
    opt_4.destroy()
    fail4_but.destroy()
    cor4_but.destroy()
    fail_4 = Label(parent, text = ("you continued to see the same individuals at each game camera and marked them as different individuals, \n causing you to skew your data to estimate the population as significantly greater than it actually was. \n The " +random_spec+" becomes considerably inbred and goes extinct,"))
    fail_4.pack()
    game_over = Label (parent, text = "GAME OVER!")
    game_over.pack()
    restart4_but = Button (parent, text = 'RESTART', command = restart4)
    restart4_but.pack()
    
    

# Lauren created this function 11/25
def opt3():
    global random_spec
    global opt2
    global fail2_but
    global cor2_but
    global opt_3
    global fail3_but
    global cor3_but 
    opt_2.destroy()
    fail2_but.destroy()
    cor2_but.destroy()
    opt_3 = Label(parent, text = ("You need to create a population estimate of the " +random_spec+ " to determine how threatened this species is. How do you do this?"))
    opt_3.pack()
    fail3_but = Button (parent, text = "Hire a technician to help you track down other "+random_spec+"'s.", command = fail3)
    fail3_but.pack()
    cor3_but = Button (parent, text = "Set up game cameras.", command = opt4)
    cor3_but.pack()

# Lauren created this function 11/25
def fail3():
    global opt_3
    global fail_3
    global cor3_but
    global name
    global game_over
    global restart3_but
    global im0
    global im2
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im2)
    opt_3.destroy()
    fail3_but.destroy()
    cor3_but.destroy()
    fail_3 = Label(parent, text = ("You ran out of funds and coudln't pay your technician. Now you're in debt."))
    fail_3.pack()
    game_over = Label (parent, text = "GAME OVER!")
    game_over.pack()
    restart3_but = Button (parent, text = 'RESTART', command = restart3)
    restart3_but.pack()
    #canvas = Canvas(parent, height = 500, width = 500, bg='red').pack()
   
    

#Lauren created this function
def opt2():
    global correct1_but
    global fail1_but
    global opt_1
    global random_spec
    global opt_2
    global fail2_but
    global cor2_but
    opt_1.destroy()
    correct1_but.destroy()
    fail1_but.destroy()
    opt_2 = Label(parent, text = ("The public loves the "+ random_spec +" and wants to fund a conservation project, what do you do with your funds? "))
    opt_2.pack()
    fail2_but = Button (parent, text = "Use the funds to build a new wildlife refuge!", command = fail2)
    fail2_but.pack()
    cor2_but = Button (parent, text = "Use funds to begin research on species!", command = opt3)
    cor2_but.pack()
  
#Lauren created this function    
def fail2():
    global correct1_but
    global fail1_but
    global opt_1
    global random_spec
    global opt_2
    global fail2_but
    global cor2_but
    global restart2_but
    global name
    global fail_2
    global game_over
    global im0
    global im2
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im2)
    opt_2.destroy()
    fail2_but.destroy()
    cor2_but.destroy()
    fail_2 = Label(parent, text = (name + " ran out of funds!"))
    fail_2.pack()
    game_over = Label (parent, text = "GAME OVER!")
    game_over.pack()
    restart2_but = Button (parent, text = 'RESTART', command = restart2)
    restart2_but.pack()

#Lauren created this function
def opt1():
    global random_spec
    global entry
    global name
    global continue_but
    global correct1_but
    global fail1_but
    global opt_1
    global yes_save
    yes_save.destroy()
    continue_but.destroy()
    opt_1 = Label(parent, text = ("What does " + name + " do first to help the " + random_spec + "?"))     
    opt_1.pack()
    correct1_but = Button(parent, text = "Gain public support!", command = opt2)
    correct1_but.pack()
    fail1_but = Button (parent, text = "Buy a gun!", command = fail1)
    fail1_but.pack()
    

#Lauren created this function
def fail1():
    global correct1_but
    global fail1_but
    global opt_1
    global canvas
    global restart1_but
    global fail_1
    global game_over
    global im0
    global im2
    opt_1.destroy()
    correct1_but.destroy()
    fail1_but.destroy()
    fail_1 = Label(parent, text = ("The " + random_spec + " gets sick and dies!"))
    fail_1.pack()
    canvas.delete()
    canvas.create_image(0,0, anchor=NW, image=im2)
    game_over = Label (parent, text = "GAME OVER!")
    game_over.pack()
    restart1_but = Button (parent, text = 'RESTART', command = restart1)
    restart1_but.pack()
    #canvas = Canvas(parent, height = 500, width = 500, bg='red').pack()
    

#Maegan created this function
def no_button():
    global no_but
    global yes_but
    no_but.destroy()
    yes_but.destroy()
    no_save = Label(parent, text = ("The " + random_spec + " died!"))
    no_save.pack()
    game_over = Label (parent, text = "GAME OVER!")
    game_over.pack()    
               
#Maegan created this functions
def yes_button():
    global no_but
    global yes_but
    global name
    global ready
    global discovery
    global biol_name
    global entry
    global continue_but
    global yes_save
    no_but.destroy()
    yes_but.destroy()
    ready.destroy()
    discovery.destroy()
    biol_name.destroy()
    entry.destroy()
    yes_save = Label(parent, text = (name + ", you have chosen to try and save the " + random_spec + "!"))
    yes_save.pack()
    continue_but = Button (parent, text = "Continue", command = opt1)
    continue_but.pack()
    
#Maegan created this function
def name_get():
    global random_spec
    global entry
    global name_but
    global no_but
    global yes_but
    global name
    global ready
    global biol_name

    biol_name.destroy()
    name = entry.get()
    name_but.destroy()
    ready = Label(parent, text = ("Welcome " + name + "! Are you ready to save the " + random_spec + "?"))     
    ready.pack()
    no_but = Button(parent, text = "No", command = no_button)
    no_but.pack()
    yes_but = Button (parent, text = "Yes", command = yes_button)
    yes_but.pack()


#Maegan created this function
# Lauren edited this function: added File IO, species names, and randomly selecting from txt file on 11/17 
def start_game():
    global start_game
    global random_spec
    global entry
    global name_but
    global discovery
    global biol_name
    global entry
    global fail1
    global game_over
    
        
    spec_name = []
    try:
        with open("spec_name.txt") as spec:
            x = spec.read()
            y = x.split()
            spec_name = y
    except exception as e:
        print("something went wrong")
    
    random_spec = random.choice(spec_name)
    game_start.destroy()
    discovery = Label(parent, text = "You discovered a new species! This species is called a "+random_spec+ ". This species appears to be endangered, let's try to save it!")
    discovery.pack()
    biol_name = Label(parent, text = "What is your biologist name? ")
    biol_name.pack()
    entry = Entry(parent)
    entry.pack()
    name_but = Button(parent, text = "Enter", command = name_get)   
    name_but.pack()

    
          
game_start = Button(parent, text = "START GAME", command = start_game)
game_start.pack()
exit_but = Button (parent, text = "EXIT GAME", command = exitgame)
exit_but.pack()

#Maegan coded the pictures
image0 = Image.open('species.jpg')
im0 = ImageTk.PhotoImage(image0)
canvas.create_image(0,0, anchor=NW, image=im0)

image1 = Image.open('win.jpg')
im1 = ImageTk.PhotoImage(image1)

image2 = Image.open('lose.jpg')
im2 = ImageTk.PhotoImage(image2)


parent.mainloop()

'''
** = complete
• ** Must define and use at least three functions. <--- this is done!
• ** Must import and use at least one external module (other than Tkinter) <---This is done!
• ** Must use a list or dictionary. <--- this is done!
• ** Must use File I/O (input OR output). <--- this is done!
• Must utilize graphics.
• Must be fully functional (i.e., must deliver WORKING software).
• ** Must spend at least 10 hours working on this project. <- this is done for both M + L
• ** Must document your time. <- This is done!
• ** Must document who coded each feature <- This is done!
'''
