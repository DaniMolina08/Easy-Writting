# Importing tkinter and all modules..............................................
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#Creating the function wich allow us to navegate through the screens...............
def show_frame(frame):
    frame.tkraise()

#Main frame  ......................................................................
window = tk.Tk()
window.title("Writting Practice")
window.geometry("1160x650+500+100")
window.config(bg='#222a35')
window.state('zoomed')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#Icon..........................................................................
"""icono = tk.PhotoImage(file="Icono.png")
window.iconphoto(True, icono)"""

#Multipe screens..................................................................
home = tk.Frame(window, bg= '#222a35')
part1 = tk.Frame(window, bg= '#222a35')
question1 = tk.Frame(window, bg= '#222a35')
sample1 = tk.Frame(window, bg= '#222a35')
question2 = tk.Frame(window, bg= '#222a35')
sample2 = tk.Frame(window, bg= '#222a35')
question3 = tk.Frame(window, bg= '#222a35')
sample3 = tk.Frame(window, bg= '#222a35')
question4 = tk.Frame(window, bg= '#222a35')
sample4 = tk.Frame(window, bg= '#222a35')
question5 = tk.Frame(window, bg= '#222a35')
sample5 = tk.Frame(window, bg= '#222a35')
part2 = tk.Frame(window, bg= '#222a35')
question6 = tk.Frame(window, bg= '#222a35')
question6_type = tk.Frame(window, bg= '#222a35')
question7 = tk.Frame(window, bg= '#222a35')
question7_type = tk.Frame(window, bg= '#222a35')
part3 = tk.Frame(window, bg= '#222a35')
question8 = tk.Frame(window, bg= '#222a35')
lasto = tk.Frame(window, bg= '#222a35')

#Navegation.......................................................................
for frame in (home, 
              part1,  
              question1, 
              sample1, 
              question2, 
              sample2, 
              question3, 
              question4, 
              question5, 
              sample3, 
              sample4, 
              sample5,
              part2,
              question6,
              question6_type,
              question7,
              question7_type,
              part3,
              question8,
              lasto):
    frame.grid(row=0,column=0,sticky='nsew')
    
#Timer................................................................................
"""
minute=StringVar()
second=StringVar()
  
#hour.set("00")
minute.set("08")
second.set("00")
  
  
minuteEntry= Entry(indications, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=130,y=20)
  
secondEntry= Entry(indications, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=180,y=20)
  
  
def submit():
    try:
        
        temp = int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:   
        
        mins,secs = divmod(temp,60)        
        
        #hours=0
        if mins >60:
                        
            hours, mins = divmod(mins, 60) 
        
        #hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
       
        question1.update()
        time.sleep(1)
  
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
          
        temp -= 1

btn = Button(indications, text='start', bd='5',
             command= submit)
btn.place(x = 70,y = 120)

"""
    
"""Home window -----------------------------------------------------------------------
Where the logo is, and the name  
"""

welcoming = tk.Label(home, 
                     text="TOEIC WRITING SIMULATION", 
                     bg="#222a35", 
                     foreground="white", 
                     font="calibri 70 bold"
                     ).place(
                         x=105, 
                         y=100)

slogan = tk.Label(home, 
                  text="Keep it simple.", 
                  bg="#222a35", 
                  foreground="white", 
                  font="calibri 28 italic"
                  ).place(
                      x=575, 
                      y=225
                      )

frame1_btn = tk.Button(home, 
                       text= "LET´S START!", 
                       font="calibri 28 bold", 
                       bg="#92d050", 
                       foreground="#222a35", 
                       command=lambda:show_frame(part1)
                       ).place(relwidth=0.4, 
                               relheight=0.1, 
                               x=420, 
                               y=535
                               )
                       
logoh = tk.PhotoImage(file="logoa.gif")
lbl_img = tk.Label(home, image=logoh, background="#222a35").place(
    x = 330, 
    y = 335)  

logou = tk.PhotoImage(file="Icono.gif")
lbl_img = tk.Label(home, image=logou).place(
    x = 790, 
    y = 325) 


"""Instructions part 1 window ---------------------------------------------------------------
Intructions are given and timer starts
"""
#ROTULO...............................................................................
rotulo = tk.Label(part1, 
                  text="Indications: Questions 1-5, Sentences based on a picture", 
                  font=("calibri", 35, "bold"), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 130,
                      y = 25 
                        )

indicaciones = tk.Label(part1, 
                        text="In questions 1-5 you will be asked to write sentences based on pictures.  Each picture \nwill have two words that you must use in your sentence. You can change the forms of the words. \n You will be scored on grammar as well as on the relevance of the sentence to the picture.", 
                        font=("calibri", 20), 
                        background="#222a35", 
                        foreground="white"
                        ).place(
                            x=150, 
                            y=130
                               )
                        
#Botton to question 1
indications_start_button = tk.Button(part1, 
                       text= "Start", 
                       font="calibri 28 bold", 
                       bg="#92d050", 
                       foreground="#222a35", 
                       command=lambda:show_frame(question1)
                       ).place(relwidth=0.2, 
                               relheight=0.1, 
                               x=990, 
                               y=555
                               )
                       
#Example

exam_rotulo = tk.Label(part1, 
                  text="Example", 
                  font=("calibri", 30, "bold"), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 550,
                      y = 350
                        )
                  
ex_sentences = tk.Label(part1, 
                      text="Words given: guard / apart \n - Posible answer: The guard is searching the man who has his arms apart.", 
                      bg="#222a35", 
                      foreground="white", 
                      font="calibri 20"
                      ).place(
                          x=500, 
                          y=425)

example_image = PhotoImage(file="example_image.gif")
lbl_img = Label(part1, image=example_image).place(x = 100, y = 370)
                       

"""Question 1-------------------------------------------------------------------------
"""
#ROTULO...............................................................................
rotulo = tk.Label(question1, 
                  text="Question 1 - 5: Pictures", 
                  font=("calibri", 40, "bold"), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 427,
                      y = 25 
                        )
#Key words...........................................................................
wordstouse = tk.Label(question1, 
                      text="Question 1: fishing, at", 
                      bg="#222a35", 
                      foreground="white", 
                      font="calibri 28 bold"
                      ).place(
                         x=800, 
                         y=225
                             )
                      
"""#Entry
cuadro_de_texto = tk.Entry(question1, 
                        font=("calibri", 16, "bold"), 
                        bg = "#222a35", 
                        relief="sunken", 
                        highlightcolor="white", 
                        foreground = "White",
                        justify=tk.CENTER
                        ).place(height=100, 
                                                    width=600, 
                                                    x=650, 
                                                    y=310
                                                    )"""                       
 #TextBox with counter................................................................
 
 
def DeclareWord_CharCountFunc1():
        # Get Content from the TextBox
    TextContent1 = TextBox1.get("1.0", END)
    # Turn The Contents (String) to a Number Value
    CharactersInTextBox1 = len(TextContent1)
    WordsInTextBox1 = len(TextContent1.split())
    # Update the Display Label to Show Number of Characters the Words in TextBox
    DisplayLabel1.config(text=str(CharactersInTextBox1 - 1) + " Characters, " + str(WordsInTextBox1) + " Words")    
    
# Intitialize Word and Character Count Function
def InitWord_CharCount1():
    DeclareWord_CharCountFunc1()
    DisplayLabel1.after(1000, InitWord_CharCount1)
    
# Text Box

TextBox1 = Text(question1, 
               width=60, 
               height=1, 
               font=("calibri", 16, "bold"), 
               wrap="word", 
               undo=True,
               bg = "#222a35",
               foreground = "White",
               relief = "sunken",
               borderwidth=3,
               )
TextBox1.place(x=625, y=340)

# Display Label (COunter)
DisplayLabel1 = Label(question1,  bg = "#222a35", foreground = "White", text="", font=("calibri", 16, "bold"))
DisplayLabel1.place(x=850, y=450)                 

InitWord_CharCount1()

#Button Next question.......................................................................
boton01 = tk.Button(question1,
                    text= "Next", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question2)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 1000,
                        y = 550
                    )
#Button Last Question.......................................................................              
"""
boton02 = tk.Button(question1,
                    text= "Back", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(home)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 625,
                        y = 550
                        )
"""
#Sample responses...........................................................................
boton03 = tk.Button(question1,
                    text= "Check", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(sample1)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 750,
                        y = 550
                        )

#Picture
photo = tk.PhotoImage(file="TOEIC-writing-1.gif")
lbl_img = tk.Label(question1, image=photo).place(
    x = 150, 
    y = 150)   


"""

Sample response 1////////////////////////////////////////////////////////////////////

"""

rotulo0 = tk.Label(sample1, 
                   text="Sample Response:", 
                   font=("calibri", 40, "bold"), 
                   background="#222a35", 
                   foreground="white"
                   )
rotulo0.place( x = 427,
               y = 25)

wordstouse = tk.Label(sample1, 
                      text="There is not a perfect sentence, this could be an option:\n \n - The men stare out at the lake as\n they take a fishing break.", 
                      bg="#222a35", 
                      foreground="white", 
                      font="calibri 25 bold italic"
                      ).place(
                          x=500, 
                          y=250)

boton011 = tk.Button(sample1, 
                    text= "BACK", 
                    font="calibri 28 bold", 
                    command=lambda:show_frame(question1), 
                    bg="#92d050", 
                    foreground="#222a35").place(
                        relwidth=0.4, 
                        relheight=0.1, 
                        x=650, 
                        y=535
                        )


photo11 = PhotoImage(file="TOEIC-writing-1.gif")
lbl_img = Label(sample1, image=photo11).place( x = 150, 
    y = 150)

"""Question 2------------------------------------------------------------------------
"""
#ROTULO...............................................................................
rotulo = tk.Label(question2, 
                  text="Question 2 - 5: Pictures", 
                  font=("calibri", 40, "bold"), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 427,
                      y = 25 
                        )
#Key words...........................................................................
wordstouse = tk.Label(question2, 
                      text="Question 2: together, table", 
                      bg="#222a35", 
                      foreground="white", 
                      font="calibri 28 bold"
                      ).place(
                         x=800, 
                         y=225
                             )
"""#Entry
cuadro_de_texto = tk.Entry(question1, 
                        font=("calibri", 16, "bold"), 
                        bg = "#222a35", 
                        relief="sunken", 
                        highlightcolor="white", 
                        foreground = "White",
                        justify=tk.CENTER
                        ).place(height=100, 
                                                    width=600, 
                                                    x=650, 
                                                    y=310
                                                    )"""                       
 #TextBox with counter................................................................
def DeclareWord_CharCountFunc2():
        # Get Content from the TextBox
    TextContent2 = TextBox2.get("1.0", END)
    # Turn The Contents (String) to a Number Value
    CharactersInTextBox2 = len(TextContent2)
    WordsInTextBox2 = len(TextContent2.split())
    # Update the Display Label to Show Number of Characters the Words in TextBox
    DisplayLabel2.config(text=str(CharactersInTextBox2 - 1) + " Characters, " + str(WordsInTextBox2) + " Words")    
    
# Intitialize Word and Character Count Function
def InitWord_CharCount2():
    DeclareWord_CharCountFunc2()
    DisplayLabel2.after(1000, InitWord_CharCount2)
    
# Text Box

TextBox2 = Text(question2, 
               width=60, 
               height=1, 
               font=("calibri", 16, "bold"), 
               wrap="word", 
               undo=True,
               bg = "#222a35",
               foreground = "White",
               relief = "sunken",
               borderwidth=3,
               )
TextBox2.place(x=625, y=340)

# Display Label (COunter)
DisplayLabel2 = Label(question2,  bg = "#222a35", foreground = "White", text="", font=("calibri", 16, "bold"))
DisplayLabel2.place(x=850, y=450)                 

InitWord_CharCount2()

#Button Next question.......................................................................
boton01 = tk.Button(question2,
                    text= "Next", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question3)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 1100,
                        y = 550
                    )
#Button Last Question.......................................................................              
boton02 = tk.Button(question2,
                    text= "Back", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question1)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 625,
                        y = 550
                        )
#Sample responses...........................................................................
boton03 = tk.Button(question2,
                    text= "Check", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(sample2)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 865,
                        y = 550
                        )

#Picture
photo2 = tk.PhotoImage(file="TOEIC-writing-2.gif")
lbl_img = tk.Label(question2, image=photo2).place(
    x = 60, 
    y = 200)   

"""
Sample Response 2

"""

rotulo02 = tk.Label(sample2, 
                   text="Sample Response:", 
                   font=("calibri", 40, "bold"), 
                   background="#222a35", 
                   foreground="white"
                   )
rotulo02.place( x = 427,
               y = 25)

wordstouse = tk.Label(sample2, 
                      text= "There is not a perfect sentence, this could be an option:\n \n - Three employees have gathered together around an oval table \n to discuss their concerns of the day.", 
                      bg="#222a35", 
                      foreground="white", 
                      font="calibri 19 bold italic"
                      ).place(
                          x=600, 
                          y=280)

boton02 = tk.Button(sample2, 
                    text= "BACK", 
                    font="calibri 28 bold", 
                    command=lambda:show_frame(question2), 
                    bg="#92d050", 
                    foreground="#222a35").place(
                        relwidth=0.4, 
                        relheight=0.1, 
                        x=650, 
                        y=535
                        )


photo22 = PhotoImage(file="TOEIC-writing-2.gif")
lbl_img = Label(sample2, image=photo22).place(x = 60, 
    y = 200)


"""Question 3------------------------------------------------------------------------
"""

#ROTULO...............................................................................
rotulo = tk.Label(question3, 
                  text="Question 3 - 5: Pictures", 
                  font=("calibri", 40, "bold"), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 427,
                      y = 25 
                        )
#Key words...........................................................................
wordstouse = tk.Label(question3, 
                      text="Question 3: beside, chatting", 
                      bg="#222a35", 
                      foreground="white", 
                      font="calibri 28 bold"
                      ).place(
                         x=800, 
                         y=225
                             )
"""#Entry
cuadro_de_texto = tk.Entry(question1, 
                        font=("calibri", 16, "bold"), 
                        bg = "#222a35", 
                        relief="sunken", 
                        highlightcolor="white", 
                        foreground = "White",
                        justify=tk.CENTER
                        ).place(height=100, 
                                                    width=600, 
                                                    x=650, 
                                                    y=310
                                                    )"""                       
 #TextBox with counter................................................................
def DeclareWord_CharCountFunc3():
        # Get Content from the TextBox
    TextContent3 = TextBox3.get("1.0", END)
    # Turn The Contents (String) to a Number Value
    CharactersInTextBox3 = len(TextContent3)
    WordsInTextBox3 = len(TextContent3.split())
    # Update the Display Label to Show Number of Characters the Words in TextBox
    DisplayLabel3.config(text=str(CharactersInTextBox3 - 1) + " Characters, " + str(WordsInTextBox3) + " Words")    
    
# Intitialize Word and Character Count Function
def InitWord_CharCount3():
    DeclareWord_CharCountFunc3()
    DisplayLabel3.after(1000, InitWord_CharCount3)
    
# Text Box

TextBox3 = Text(question3, 
               width=60, 
               height=1, 
               font=("calibri", 16, "bold"), 
               wrap="word", 
               undo=True,
               bg = "#222a35",
               foreground = "White",
               relief = "sunken",
               borderwidth=3,
               )
TextBox3.place(x=625, y=340)

# Display Label (COunter)
DisplayLabel3 = Label(question3,  bg = "#222a35", foreground = "White", text="", font=("calibri", 16, "bold"))
DisplayLabel3.place(x=850, y=450)                 

InitWord_CharCount3()

#Button Next question.......................................................................
boton01 = tk.Button(question3,
                    text= "Next", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question4)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 1100,
                        y = 550
                    )
#Button Last Question.......................................................................              
boton02 = tk.Button(question3,
                    text= "Back", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question2)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 625,
                        y = 550
                        )
#Sample responses...........................................................................
boton03 = tk.Button(question3,
                    text= "Check", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(sample3)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 865,
                        y = 550
                        )

#Picture
photo3 = tk.PhotoImage(file="TOEIC-writing-3.gif")
lbl_img = tk.Label(question3, image=photo3).place(
   x = 130, 
    y = 150) 


"""
Sample Response 3

"""

rotulo02 = tk.Label(sample3, 
                   text="Sample Response:", 
                   font=("calibri", 40, "bold"), 
                   background="#222a35", 
                   foreground="white"
                   )
rotulo02.place( x = 427,
               y = 25)

wordstouse = tk.Label(sample3, 
                      text= "There is not a perfect sentence, this could be an option:\n \n - She is chatting on her cell phone while sitting beside a colleague in the taxi.", 
                      bg="#222a35", 
                      foreground="white", 
                      font="calibri 20 bold italic"
                      ).place(
                          x=450, 
                          y=290)

boton02 = tk.Button(sample3, 
                    text= "BACK", 
                    font="calibri 28 bold", 
                    command=lambda:show_frame(question3), 
                    bg="#92d050", 
                    foreground="#222a35").place(
                        relwidth=0.4, 
                        relheight=0.1, 
                        x=650, 
                        y=535
                        )


photo33 = PhotoImage(file="TOEIC-writing-3.gif")
lbl_img = Label(sample3, image=photo33).place(x = 130, y = 150)


"""Question 4------------------------------------------------------------------------
"""

#ROTULO...............................................................................
rotulo = tk.Label(question4, 
                  text="Question 4 - 5: Pictures", 
                  font=("calibri", 40, "bold"), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 427,
                      y = 25 
                        )
#Key words...........................................................................
wordstouse = tk.Label(question4, 
                      text="Question 4: frame, but", 
                      bg="#222a35", 
                      foreground="white", 
                      font="calibri 28 bold"
                      ).place(
                         x=800, 
                         y=225
                             )
"""#Entry
cuadro_de_texto = tk.Entry(question1, 
                        font=("calibri", 16, "bold"), 
                        bg = "#222a35", 
                        relief="sunken", 
                        highlightcolor="white", 
                        foreground = "White",
                        justify=tk.CENTER
                        ).place(height=100, 
                                                    width=600, 
                                                    x=650, 
                                                    y=310
                                                    )"""                       
 #TextBox with counter................................................................
def DeclareWord_CharCountFunc4():
        # Get Content from the TextBox
    TextContent4 = TextBox4.get("1.0", END)
    # Turn The Contents (String) to a Number Value
    CharactersInTextBox4 = len(TextContent4)
    WordsInTextBox4 = len(TextContent4.split())
    # Update the Display Label to Show Number of Characters the Words in TextBox
    DisplayLabel4.config(text=str(CharactersInTextBox4 - 1) + " Characters, " + str(WordsInTextBox4) + " Words")    
    
# Intitialize Word and Character Count Function
def InitWord_CharCount4():
    DeclareWord_CharCountFunc4()
    DisplayLabel4.after(1000, InitWord_CharCount4)
    
# Text Box

TextBox4 = Text(question4, 
               width=60, 
               height=1, 
               font=("calibri", 16, "bold"), 
               wrap="word", 
               undo=True,
               bg = "#222a35",
               foreground = "White",
               relief = "sunken",
               borderwidth=3,
               )
TextBox4.place(x=625, y=340)

# Display Label (COunter)
DisplayLabel4 = Label(question4,  bg = "#222a35", foreground = "White", text="", font=("calibri", 16, "bold"))
DisplayLabel4.place(x=850, y=450)                 

InitWord_CharCount4()

#Button Next question.......................................................................
boton01 = tk.Button(question4,
                    text= "Next", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question5)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 1100,
                        y = 550
                    )
#Button Last Question.......................................................................              
boton02 = tk.Button(question4,
                    text= "Back", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question3)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 625,
                        y = 550
                        )
#Sample responses...........................................................................
boton03 = tk.Button(question4,
                    text= "Check", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(sample4)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 865,
                        y = 550
                        )

#Picture
photo4 = tk.PhotoImage(file="TOEIC-writing-4.gif")
lbl_img = tk.Label(question4, image=photo4).place(
    x = 60, 
    y = 200) 


"""
Sample Response 4

"""

rotulo02 = tk.Label(sample4, 
                   text="Sample Response:", 
                   font=("calibri", 40, "bold"), 
                   background="#222a35", 
                   foreground="white"
                   )
rotulo02.place( x = 427,
               y = 25)

wordstouse = tk.Label(sample4, 
                      text= "There is not a perfect sentence, this could be an option:\n \n - The frame of the building is almost done but construction has been called off.", 
                      bg="#222a35", 
                      foreground="white", 
                      font="calibri 17 bold italic"
                      ).place(
                          x=600, 
                          y=290)

boton02 = tk.Button(sample4, 
                    text= "BACK", 
                    font="calibri 28 bold", 
                    command=lambda:show_frame(question4), 
                    bg="#92d050", 
                    foreground="#222a35").place(
                        relwidth=0.4, 
                        relheight=0.1, 
                        x=650, 
                        y=535
                        )


photo44 = PhotoImage(file="TOEIC-writing-4.gif")
lbl_img = Label(sample4, image=photo44).place(x = 60, 
    y = 200)

"""Question 5------------------------------------------------------------------------
"""

#ROTULO...............................................................................
rotulo = tk.Label(question5, 
                  text="Question 5 - 5: Pictures", 
                  font=("calibri", 40, "bold"), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 427,
                      y = 25 
                        )
#Key words...........................................................................
wordstouse = tk.Label(question5, 
                      text="Question 5: baggage, open", 
                      bg="#222a35", 
                      foreground="white", 
                      font="calibri 28 bold"
                      ).place(
                         x=800, 
                         y=225
                             )
"""#Entry
cuadro_de_texto = tk.Entry(question1, 
                        font=("calibri", 16, "bold"), 
                        bg = "#222a35", 
                        relief="sunken", 
                        highlightcolor="white", 
                        foreground = "White",
                        justify=tk.CENTER
                        ).place(height=100, 
                                                    width=600, 
                                                    x=650, 
                                                    y=310
                                                    )"""                       
 #TextBox with counter................................................................
def DeclareWord_CharCountFunc5():
        # Get Content from the TextBox
    TextContent5 = TextBox5.get("1.0", END)
    # Turn The Contents (String) to a Number Value
    CharactersInTextBox5 = len(TextContent5)
    WordsInTextBox5 = len(TextContent5.split())
    # Update the Display Label to Show Number of Characters the Words in TextBox
    DisplayLabel5.config(text=str(CharactersInTextBox5 - 1) + " Characters, " + str(WordsInTextBox5) + " Words")    
    
# Intitialize Word and Character Count Function
def InitWord_CharCount5():
    DeclareWord_CharCountFunc5()
    DisplayLabel5.after(1000, InitWord_CharCount5)
    
# Text Box

TextBox5 = Text(question5, 
               width=60, 
               height=1, 
               font=("calibri", 16, "bold"), 
               wrap="word", 
               undo=True,
               bg = "#222a35",
               foreground = "White",
               relief = "sunken",
               borderwidth=3,
               )
TextBox5.place(x=625, y=340)

# Display Label (COunter)
DisplayLabel5 = Label(question5,  bg = "#222a35", foreground = "White", text="", font=("calibri", 16, "bold"))
DisplayLabel5.place(x=850, y=450)                 

InitWord_CharCount5()

#Button Next question.......................................................................
boton01 = tk.Button(question5,
                    text= "Next", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(part2)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 1100,
                        y = 550
                    )
#Button Last Question.......................................................................              
boton02 = tk.Button(question5,
                    text= "Back", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question4)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 625,
                        y = 550
                        )
#Sample responses...........................................................................
boton03 = tk.Button(question5,
                    text= "Check", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(sample5)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 865,
                        y = 550
                        )

#Picture
photo5 = tk.PhotoImage(file="TOEIC-writing-5.gif")
lbl_img = tk.Label(question5, image=photo5).place(
    x = 60, 
    y = 200) 


"""
Sample Response 5

"""

rotulo02 = tk.Label(sample5, 
                   text="Sample Response:", 
                   font=("calibri", 40, "bold"), 
                   background="#222a35", 
                   foreground="white"
                   )
rotulo02.place( x = 427,
               y = 25)

wordstouse = tk.Label(sample5, 
                      text= "There is not a perfect sentence, this could be an option:\n \n - When she got to the arrivals department, \n the tourist noticed that her belongings were falling out of her open baggage.", 
                      bg="#222a35", 
                      foreground="white", 
                      font="calibri 17 bold italic"
                      ).place(
                          x=600, 
                          y=290)

boton02 = tk.Button(sample5, 
                    text= "BACK", 
                    font="calibri 28 bold", 
                    command=lambda:show_frame(question5), 
                    bg="#92d050", 
                    foreground="#222a35").place(
                        relwidth=0.4, 
                        relheight=0.1, 
                        x=650, 
                        y=535
                        )


photo55 = PhotoImage(file="TOEIC-writing-5.gif")
lbl_img = Label(sample5, image=photo55).place(x = 60, 
    y = 200)

"""
Part 2
"""
"""
Indications 
"""

rotulo_part2 = tk.Label(part2, 
                  text="Indications: Questions 6-7: Written Requests", 
                  font=("calibri", 40, "bold"), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 200,
                      y = 60 
                        )

indicactions_part2 = tk.Label(part2, 
                        text="In this part of the test, you will show how well you can write \n a response to an e-mail. \n  \n  Your response will be scored on \n \n •the quality and variety of your sentences, \n  •vocabulary, and organization. \n \n You will have 10 minutes to read and answer each e-mail.", 
                        font=("calibri", 20), 
                        background="#222a35", 
                        foreground="white"
                        ).place(
                            x=300, 
                            y=200
                               )
                        
#Botton to question 1
indications_start_button_part2 = tk.Button(part2, 
                       text= "Start", 
                       font="calibri 28 bold", 
                       bg="#92d050", 
                       foreground="#222a35", 
                       command=lambda:show_frame(question6)
                       ).place(relwidth=0.2, 
                               relheight=0.1, 
                               x=1050, 
                               y=585
                               )     
                       
"""
Question 6 
"""           

#ROTULO...............................................................................
rotulo_question6 = tk.Label(question6, 
                  text="Question 6: Read the email", 
                  font=("calibri", 35, "bold"), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 410,
                      y = 20 
                        )

#Button Next question.......................................................................
boton01 = tk.Button(question6,
                    text= "Next", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question6_type)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 1150,
                        y = 25
                    )
#Picture
photo_emailq6 = tk.PhotoImage(file="email_1.gif")
lbl_img = tk.Label(question6, image=photo_emailq6).place(
    x = 300, 
    y = 110)     

"""

Question 6_type

"""

rotulo_question6 = tk.Label(question6_type, 
                  text="Directions: Respond to the email as if you are trying to sell your house privately Answer the questions \n and provide at least TWO details about the neighbourhood and ONE reason why you can or can't \n negotiate the price", 
                  font=("calibri", 20), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 130,
                      y = 225 
                        )

 #TextBox with counter................................................................
def DeclareWord_CharCountFunc6():
        # Get Content from the TextBox
    TextContent6 = TextBox6.get("1.0", END)
    # Turn The Contents (String) to a Number Value
    
    WordsInTextBox6 = len(TextContent6.split())
    # Update the Display Label to Show Number of Characters the Words in TextBox
    DisplayLabel6.config(text=str(WordsInTextBox6) + " Words")    
    
# Intitialize Word and Character Count Function
def InitWord_CharCount6():
    DeclareWord_CharCountFunc6()
    DisplayLabel6.after(1000, InitWord_CharCount6)
    
# Text Box

TextBox6 = Text(question6_type, 
               width=100, 
               height=8, 
               font=("calibri", 16, "bold"), 
               wrap="word", 
               undo=True,
               bg = "#222a35",
               foreground = "White",
               relief = "sunken",
               borderwidth=3,
               )
TextBox6.place(x=130, y=400)

# Display Label (COunter)
DisplayLabel6 = Label(question6_type,  bg = "#222a35", foreground = "White", text="", font=("calibri", 16, "bold"))
DisplayLabel6.place(x=630, y=630)                 

InitWord_CharCount6()

# Button back to the email..............................................................

boton01 = tk.Button(question6_type,
                    text= "Email", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question6)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 50,
                        y = 25
                    )
                    
buttonnext = tk.Button(question6_type,
                    text= "Next", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question7)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 1125,
                        y = 25
                    )
 
""" 
Question 7 -----------------------------------------------------------------------------
"""

#ROTULO...............................................................................
rotulo_question7 = tk.Label(question7, 
                  text="Question 7: Read the email", 
                  font=("calibri", 35, "bold"), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 410,
                      y = 20 
                        )

#Button Next question.......................................................................
boton07 = tk.Button(question7,
                    text= "Next", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question7_type)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 1150,
                        y = 25
                    )
#Picture
photo_email_7 = tk.PhotoImage(file="email_2.gif")
lbl_img = tk.Label(question7, image=photo_email_7).place(
    x = 240, 
    y = 130)    


"""

Question 7_type

"""

rotulo_question7 = tk.Label(question7_type, 
                  text="Directions: Respond to the email to request more information. Ask for at least TWO details about the plans \n and ONE statement of which plan interests you most and why.", 
                  font=("calibri", 20), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 130,
                      y = 225 
                        )

 #TextBox with counter................................................................
def DeclareWord_CharCountFunc7():
        # Get Content from the TextBox
    TextContent7 = TextBox7.get("1.0", END)
    # Turn The Contents (String) to a Number Value
    
    WordsInTextBox7 = len(TextContent7.split())
    # Update the Display Label to Show Number of Characters the Words in TextBox
    DisplayLabel7.config(text=str(WordsInTextBox7) + " Words")    
    
# Intitialize Word and Character Count Function
def InitWord_CharCount7():
    DeclareWord_CharCountFunc7()
    DisplayLabel7.after(1000, InitWord_CharCount7)
    
# Text Box

TextBox7 = Text(question7_type, 
               width=100, 
               height=8, 
               font=("calibri", 16, "bold"), 
               wrap="word", 
               undo=True,
               bg = "#222a35",
               foreground = "White",
               relief = "sunken",
               borderwidth=3,
               )
TextBox7.place(x=130, y=400)

# Display Label (COunter)
DisplayLabel7 = Label(question7_type,  bg = "#222a35", foreground = "White", text="", font=("calibri", 16, "bold"))
DisplayLabel7.place(x=630, y=630)                 

InitWord_CharCount7()

# Button back to the email..............................................................

boton01 = tk.Button(question7_type,
                    text= "Email", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(question7)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 50,
                        y = 25
                    )
                    
buttonnext = tk.Button(question7_type,
                    text= "Next", 
                    font="calibri 28 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(part3)).place(
                        relwidth=0.14,
                        relheight=0.1, 
                        x = 1125,
                        y = 25
                    )

"""
Part 3-----------------------------------------------------------------------------------------------------------
"""
"""
Indications -----------------------------------------------------------------------------------------------------
"""

rotulo_part3 = tk.Label(part3, 
                  text="Indications: Question 8: Opinion Essay", 
                  font=("calibri", 40, "bold"), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 250,
                      y = 60 
                        )

indicactions_part3 = tk.Label(part3, 
                        text="In this part of the test you will be asked to write an opinion essay \n in which you state, explain, and support reasons about your opinion. \n You will have 30 minutes to plan and write your essay. Leave a little \n time to proofread and edit your essay. Your essay should be 4-5 \n paragraphs in length. It will be rated in terms of organization, \n grammar, vocabulary, and coherence.", 
                        font=("calibri", 20), 
                        background="#222a35", 
                        foreground="white"
                        ).place(
                            x=300, 
                            y=200
                               )
                        
#Botton to question 1
indications_start_button_part3 = tk.Button(part3, 
                       text= "Start", 
                       font="calibri 28 bold", 
                       bg="#92d050", 
                       foreground="#222a35", 
                       command=lambda:show_frame(question8)
                       ).place(relwidth=0.2, 
                               relheight=0.1, 
                               x=1050, 
                               y=585
                               )    
                       
"""
Question 8

"""

rotulo_question8 = tk.Label(question8, 
                  text="Question 8: Some companies block their employees from using social media networks and websites such as Facebook. \n  Do you think managers should trust employees to use time wisely, or do you think it is smart of companies to block \n  access to some sites? Provide reasons and examples to support your opinion.", 
                  font=("calibri", 17), 
                  background="#222a35", 
                  foreground="white"
                  ).place(
                      x = 30,
                      y = 40 
                        )

 #TextBox with counter................................................................
def DeclareWord_CharCountFunc():
        # Get Content from the TextBox
    TextContent8 = TextBox8.get("1.0", END)
    # Turn The Contents (String) to a Number Value
    
    WordsInTextBox8 = len(TextContent8.split())
    # Update the Display Label to Show Number of Characters the Words in TextBox
    DisplayLabel8.config(text=str(WordsInTextBox8) + " Words")    
    
# Intitialize Word and Character Count Function
def InitWord_CharCount8():
    DeclareWord_CharCountFunc()
    DisplayLabel8.after(1000, InitWord_CharCount8)
    
# Text Box

TextBox8 = Text(question8, 
               width=100, 
               height=17, 
               font=("calibri", 15), 
               wrap="word", 
               undo=True,
               bg = "#222a35",
               foreground = "White",
               relief = "sunken",
               borderwidth=3,
               )
TextBox8.place(x=130, y=170)

# Display Label (COunter)
DisplayLabel8 = Label(question8,  bg = "#222a35", foreground = "White", text="", font=("calibri", 16, "bold"))
DisplayLabel8.place(x=630, y=630)                 

InitWord_CharCount8()

# Button back to the end..............................................................

buttonnext = tk.Button(question8,
                    text= "Next", 
                    font="calibri 20 bold", 
                    bg="#92d050", 
                    foreground="#222a35", 
                    command=lambda:show_frame(lasto)).place(
                        relwidth=0.10,
                        relheight=0.1, 
                        x = 1200,
                        y = 50
                    ) 
                    
"""_
lasto-----------------------------------------------------------------------------------------------------

"""

goodbye = tk.Label(lasto, 
                     text="You have finished the Writing Part", 
                     bg="#222a35", 
                     foreground="white", 
                     font="calibri 60 bold"
                     ).place(
                         x=105, 
                         y=100)

slogan = tk.Label(lasto, 
                  text="Toeic Writing Simulation", 
                  bg="#222a35", 
                  foreground="white", 
                  font="calibri 28 italic"
                  ).place(
                      x=500, 
                      y=225
                      )

frame1_btn = tk.Button(lasto, 
                       text= "Back to home", 
                       font="calibri 28 bold", 
                       bg="#92d050", 
                       foreground="#222a35", 
                       command=lambda:show_frame(home)
                       ).place(relwidth=0.4, 
                               relheight=0.1, 
                               x=420, 
                               y=535
                               )
                       
logohh = tk.PhotoImage(file="logoa.gif")
lbl_img = tk.Label(lasto, image=logohh, background="#222a35").place(
    x = 560, 
    y = 335)  

#MOSTRANDO FRAME 1.......................................................................
show_frame(home)
window.mainloop()




