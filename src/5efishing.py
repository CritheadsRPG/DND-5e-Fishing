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
    ocean = Button(frame, text='Ocean', width=10, command=lambda : FishResults('ocean', rolls))
    shore = Button(frame, text='Shore', width=10, command=lambda : FishResults('shore', rolls))
    sea = Button(frame, text='Sea', width=10, command=lambda : FishResults('sea', rolls))

    saltlabel.grid(column=0, row=1)
    ocean.grid(column=0, row=2)
    shore.grid(column=0, row=3)
    sea.grid(column=0, row=4)
    
    #Brackish Water Options in column 1
    brackishlabel = Label(frame, text='Brackish')
    estuary = Button(frame, text='Estuary', width=10, command=lambda : FishResults('estuary', rolls))
    bay = Button(frame, text='Bay', width=10, command=lambda : FishResults('bay', rolls))
    bracklake = Button(frame, text='Lake', width=10, command=lambda : FishResults('bracklake', rolls))

    brackishlabel.grid(column=1, row=1)
    estuary.grid(column=1, row=2)
    bay.grid(column=1, row=3)
    bracklake.grid(column=1, row=4)

    #Fresh Water Options in column 2
    freshlabel = Label(frame, text='Fresh')
    river = Button(frame, text='River', width=10, command=lambda : FishResults('river', rolls))
    freshlake = Button(frame, text='Lake', width=10, command=lambda : FishResults('freshlake', rolls))
    swamp = Button(frame, text='Swamp', width=10, command=lambda : FishResults('swamp', rolls))

    freshlabel.grid(column=2, row=1)
    river.grid(column=2, row=2)
    freshlake.grid(column=2, row=3)
    swamp.grid(column=2, row=4)

    #Misc Options
    misclabel = Label(frame, text='Misc')
    deepsea = Button(frame, text='Deep Sea', width=10, command=lambda : FishResults('deepsea', rolls))
    underground = Button(frame, text='Underground', width=10, command=lambda : FishResults('underground', rolls))
    arcane = Button(frame, text='Arcane', width=10, command=lambda : FishResults('arcane', rolls))

    misclabel.grid(column=3, row=1)
    deepsea.grid(column=3, row=2)
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

        def PrepEco(rolls):
            resultsframe.destroy()
            ClearFrame(frame)
            Ecosystem(rolls)

        if rolls == 0:
            rollresults.insert(END, 'Looks like you didn\'t make any casts. Select Back to try again or Continue to close.')
            back = Button(resultsframe, text='Back', command=lambda : RestartSkillCheck(), width=10)
            cont = Button(resultsframe, text='Continue', command=lambda : exit(), width=10)
        else:
            for roll in range(0,rolls):
                outcome = randint(1,20)
                rollresults.insert(END, f'Roll # {roll+1}: {outcome} + {modifier}\n')
                if outcome == 1: 
                    rollresults.insert(END, 'Critical Failure! :(')
                    outcomeslist.append('fail')
                elif outcome == 20:
                    rollresults.insert(END, 'Critical Success! :)')
                    outcomeslist.append('success')
                else:
                    outcomeslist.append(outcome+modifier)

            back = Button(resultsframe, text='Back', command=lambda : RestartSkillCheck(), width=10)
            cont = Button(resultsframe, text='Continue', command=lambda : PrepEco(outcomeslist), width=10)

        rollresults.grid(columnspan=3, rowspan=2)
        back.grid(column=0, row=3)
        cont.grid(column=2, row=3)
    

    #Confirm the input numbers and get back a result of the rolls
    confirm = Button(frame, text='Confirm Modifier and Casts', command=lambda : RollD20(casts, modifier))
    confirm.grid(columnspan=2, row=3)

    frame.pack()
    return

#Clear the main frame so it can be rebuilt
def ClearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    return

#Get the results of each fishing roll
def FishResults(water, rolls):
    ocean = ['anchovy - 1/10 cp', 'sardine - 1/10 cp', 'snapper - 5 cp', 'eel - 8 cp', 'hake - 1 sp', 'cod - 1 sp', 'salmon - 2 sp', 'barracuda - 2 sp 5 cp', 'tuna - 3 sp', 'grouper - 4 cp', 'pufferfish - 5 sp',  'sunfish - 8 sp', 'sailfish - 8 sp', 'marlin - 8 sp', 'shark - 1 gp']
    shore = ['anchovy - 1/10 cp', 'bluefish - 5 cp', 'snapper - 5 cp', 'eel - 8 cp', 'mackerel - 1 sp', 'drum - 1 sp', 'flounder - 1 sp', 'barracuda - 1 sp', 'seatrout - 7 cp', 'pufferfish - 5 sp', 'snook - 7 sp', 'ray - 9 sp', 'zebrafish - 1 gp', 'shark - 1 gp']
    sea = ['anchovy - 1/10 cp', 'goby - 1 cp', 'pecarina - 1 cp', 'scup - 6 cp', 'shad - 1 cp', 'bream - 8 cp', 'porgy - 4 cp', 'eel - 8 cp', 'hagfish - 3 cp', 'pinfish - 4 cp', 'barracuda - 1 sp',  'pufferfish - 5 sp', 'mackerel - 2 sp', 'sturgeon - 5 sp']
    estuary = ['sole - 1 cp', 'perch - 1 cp', 'flounder - 1 sp', 'eel - 8 cp', 'barramundi - 5 cp', 'bass - 5 cp', 'bream - 8 cp', 'pufferfish - 5 sp', 'mullet - 7 cp', 'trout - 7 cp', 'snapper - 5 cp', 'drum - 1 sp', 'grouper - 4 cp', 'sturgeon - 5 sp']
    bay = ['smelt - 1/10 cp', 'perch - 1 cp', 'herring - 6 cp', 'haddock - 7 cp', 'eel - 8 cp', 'bass - 5 cp', 'cod - 7 cp', 'pufferfish - 5 sp', 'scup - 6 cp', 'pollock - 1 sp', 'halibut - 1 sp', 'flounder - 1 sp', 'mackerel - 2 sp', 'tuna - 3 sp', 'shark - 1 gp']
    bracklake = ['goby - 1 cp', 'mudskipper - 3 cp', 'sheepshead - 4 cp', 'bass - 5 cp', 'snook - 6 cp', 'eel - 8 cp', 'tarpon - 1 sp', 'catfish - 7 cp', 'drum - 5 cp', 'pufferfish - 5 sp']
    river = ['pickerel - 1/10 cp', 'bluegill - 1 cp', 'crappie - 2 cp', 'perch - 4 cp', 'catfish - 5 cp', 'carp - 4 cp', 'bass - 5 cp', 'trout - 7 cp', 'salmon - 2 sp', 'pike - 3 sp', 'sturgeon - 5 sp', 'muskellunge (muskie) - 5 sp', 'paddldfish - 7 sp']
    freshlake = ['pickerel - 1/10 cp', 'bluegill - 1 cp', 'crappie - 2 cp', 'perch - 4 cp', 'catfish - 7 cp', 'carp - 4 cp', 'bass - 5 cp', 'trout - 7 cp', 'bowfin - 7 cp', 'pike - 3 sp', 'sturgeon - 5 sp', 'muskellunge (muskie) - 5 sp']
    swamp = ['pickerel - 1/10 cp', 'darter - 1/5 cp', 'bluegill - 1 cp', 'crappie - 2 cp', 'perch - 4 cp', 'catfish - 7 cp', 'carp - 4 cp', 'murrel - 5 cp', 'bass - 5 cp', 'eel - 8 cp', 'gar - 9 cp', 'muskellunge (muskie) - 5 sp']
    critfail = ['shoe', 'broken glasses', 'stick', 'weeds', 'algae', 'hung line - have to cut', 'old clothing']
    critsucc = ['another fishing rod - 5 sp', 'a small coin purse with 100 copper pieces', 'a small item with a minor enchantment', 'a particularly rare fish worth 1 gold piece', 'a healing herb equal to a lesser healing potion']
    deepsea = ['frogfish - 1 gp', 'batfish - 1 gp', 'handfish - 1 gp', 'viperfish - 1 gp', 'anglerfish - 1 gp', 'oarfish - 1 gp']
    underground = ['blind tetra - 5 cp', 'cavefish - 5 cp', 'characid - 5 cp', 'caveskipper - 5 cp', 'luminescent pickerel - 1 gp', 'cave salamander - 3 sp', 'sightless bass - 5 cp']
    arcane = ['comet - 5 gp', 'goldbulb - 3 gp', 'acidfish - 1 gp', 'blink-fish - 10 gp', 'stone fish - 1 gp', 'illisquid - 25 gp', 'babblefish - 10 gp', 'ghostfish - 5 gp']

    resultsframe = Toplevel(window)
    resultsframe.title('Catches')
    restart = Button(resultsframe, text='Restart', width=10, command=lambda : RestartSkillCheck())
    exitbutton = Button(resultsframe, text='Quit', width=10, command=lambda : CloseWindows())
    catchresults = ScrolledText(resultsframe, width=50, height=10)
    multiplier = 1 #default multiplier is 1

    def select(lst, mult):
        chosen = randint(0, (len(lst)-1))
        if mult > 1:
            catchresults.insert(END, f'{mult} x {lst[chosen]}\n')
        else:
            catchresults.insert(END, f'{lst[chosen]}\n')

        return

    for roll in rolls:
        if roll == 'fail':
            multiplier = 1
            select(critfail, multiplier)
        elif roll == 'success':
            multiplier = 1
            select(critsucc, multiplier)
        else:
            if roll <= 15:
                multiplier = 1
            elif roll <= 20:
                multiplier = 2
            elif roll > 20:
                multiplier = 3
            if water == 'ocean': (select(ocean, multiplier))
            if water == 'shore': (select(shore, multiplier))
            if water == 'sea': (select(sea, multiplier))
            if water == 'estuary': (select(estuary, multiplier))
            if water == 'bay': (select(bay, multiplier))
            if water == 'bracklake': (select(bracklake, multiplier))
            if water == 'river': (select(river, multiplier))
            if water == 'freshlake': (select(freshlake, multiplier))
            if water == 'swamp': (select(swamp, multiplier))
            if water == 'deepsea': (select(deepsea, multiplier))
            if water == 'underground': (select(underground, multiplier))
            if water == 'arcane': (select(arcane, multiplier))

    def RestartSkillCheck():
        resultsframe.destroy()
        ClearFrame(frame)
        SkillCheck()
        return

    def CloseWindows():
        resultsframe.destroy()
        window.destroy()
        return

    catchresults.grid(columnspan=3, rowspan=2)
    restart.grid(column=0, row=3)
    exitbutton.grid(column=2, row=3)

    return

if __name__ == '__main__':
    SkillCheck() #all other functions flow from this one
    window.mainloop()