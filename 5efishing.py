#Tkinter provides GUI tools
from tkinter import Tk
from tkinter import Button
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import IntVar
from tkinter.scrolledtext import ScrolledText
from tkinter import Toplevel
from tkinter import END
from random import randint

window = Tk() #create a window
window.title('Fedwin\'s Fishing Companion')

frame = Frame(window)

#Select the ecosystem in which you are fishing
def Ecosystem(rolls):
    #Main label
    typelabel = Label(frame, text='Select which body of water closest matches your current location.')
    typelabel.grid(columnspan=4, row=0)
    
    #Salt Water options in Column 0
    saltlabel = Label(frame, text='Salt')
    ocean = Button(frame, text='Ocean', width=10)
    shore = Button(frame, text='Shore', width=10)
    sea = Button(frame, text='Sea', width=10)

    saltlabel.grid(column=0, row=1)
    ocean.grid(column=0, row=2)
    shore.grid(column=0, row=3)
    sea.grid(column=0, row=4)
    
    #Brackish Water Options in column 1
    brackishlabel = Label(frame, text='Brackish')
    estuary = Button(frame, text='Estuary', width=10)
    bay = Button(frame, text='Bay', width=10)
    bracklake = Button(frame, text='Lake', width=10)

    brackishlabel.grid(column=1, row=1)
    estuary.grid(column=1, row=2)
    bay.grid(column=1, row=3)
    bracklake.grid(column=1, row=4)

    #Fresh Water Options in column 2
    freshlabel = Label(frame, text='Fresh')
    river = Button(frame, text='River', width=10)
    freshlake = Button(frame, text='Lake', width=10)
    swamp = Button(frame, text='Swamp', width=10)

    freshlabel.grid(column=2, row=1)
    river.grid(column=2, row=2)
    freshlake.grid(column=2, row=3)
    swamp.grid(column=2, row=4)

    #Misc Options
    misclabel = Label(frame, text='Misc')
    ice = Button(frame, text='Ice', width=10)
    underground = Button(frame, text='Underground', width=10)
    arcane = Button(frame, text='Arcane', width=10)

    misclabel.grid(column=3, row=1)
    ice.grid(column=3, row=2)
    underground.grid(column=3, row=3)
    arcane.grid(column=3, row=4)

    frame.pack()
    return 

#Perform a fishing skillcheck
def SkillCheck():
    framelabel = Label(frame, text='Perform a skillcheck!')
    framelabel.grid(columnspan=2, row=0)

    #Get the user's proficiency modifier for fishing
    modlabel = Label(frame, text='Please enter your proficiency modifier:')
    modifier = IntVar()
    modifierentry = Entry(frame, textvariable=modifier, width=2)
    modlabel.grid(column=0, row=1)
    modifierentry.grid(column=1, row=1)

    #Get number of casts from the user
    castslabel = Label(frame, text='How many casts will you perform?:')
    casts = IntVar()
    castsentry = Entry(frame, textvariable=casts, width=2)
    castslabel.grid(column=0, row=2)
    castsentry.grid(column=1, row=2)

    #Choose a random int between 1 and 20 a number of times as specified and return a list of the outcomes
    def RollD20(rolls, modifier):
        rolls = rolls.get()
        modifier = modifier.get()

        outcomeslist = []

        resultsframe = Toplevel(frame)
        resultsframe.title('Skill Check Results')

        rollresults = ScrolledText(resultsframe, width=50, height=10)
        
        def RestartSkillCheck():
            resultsframe.destroy()
            SkillCheck()
            return

        if rolls == 0:
            rollresults.insert(END, 'Looks like you didn\'t make any casts. Select Back to try again or Continue to close.')
            back = Button(resultsframe, text='Back', command=lambda : RestartSkillCheck(), width=10)
            cont = Button(resultsframe, text='Continue', command=lambda : exit(), width=10)
        else:
            for roll in range(0,rolls):
                outcome = randint(1,20)
                rollresults.insert(END, f'Roll # {roll+1}: {outcome} + {modifier}\n')
                if outcome == 1: 
                    rollresults.insert('Critical Failure! :(')
                    outcomeslist.append('fail')
                elif outcome == 20:
                    rollresults.insert('Critical Success! :)')
                    outcomeslist.append('success')
                else:
                    outcomeslist.append(outcome+modifier)

            back = Button(resultsframe, text='Back', command=lambda : RestartSkillCheck(), width=10)
            cont = Button(resultsframe, text='Continue', command=lambda : Ecosystem(outcomeslist), width=10)

        rollresults.grid(columnspan=3, rowspan=2)
        back.grid(column=0, row=3)
        cont.grid(column=2, row=3)

    #Confirm the input numbers and get back a result of the rolls
    confirm = Button(frame, text='Confirm Modifier and Casts', command=lambda : RollD20(casts, modifier))
    confirm.grid(columnspan=2, row=3)

    frame.pack()
    return

if __name__ == '__main__':
    SkillCheck() #all other functions flow from this one
    window.mainloop()