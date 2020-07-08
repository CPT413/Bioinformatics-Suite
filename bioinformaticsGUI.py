import tkinter as tk #import tkinter as tk
from dnaFuncs import * #import all functions from dnaFuncs
from proteinFuncs import * #import all funcs from proteinFuncs
from readFASTA import * #import all funcs from readFASTA

#function to get value of checkbuttons
def buttonClick():

    sequence = dnaSeqCheck(sequenceEntry.get())
    if gcVar.get() == 1:
        print(gcContent(sequence))
    if revCompVar.get() == 1:
        print(reverseComp(sequence))

window = tk.Tk() #create tkinter winde
window.title("Bioinformatics Suite") #changes title of window
greeting = tk.Label(text = "Enter sequence to analyze:") #adds a test text to the window

#create varaible to save the value of the checkbuttons
sequenceEntry = tk.Entry()
gcVar = tk.IntVar()
revCompVar = tk.IntVar()
transVar = tk.IntVar()
translationVar = tk.IntVar()

#create the chekc buttons for the various DNA functions
gcContentSelect = tk.Checkbutton(text = 'GC Content', variable = gcVar)
reverseCompSelect = tk.Checkbutton(text = 'Reverse Complement', variable = revCompVar)
transcriptionSelect = tk.Checkbutton(text = 'Transciption', variable = transVar)
translationSelect = tk.Checkbutton(text = 'Translation', variable = translationVar)

#create button to analyse the seq, connected to buttonClick func
analyzeButton = tk.Button(text = "Analyze", command = buttonClick)

#pack all components into window
greeting.pack()
sequenceEntry.pack()
gcContentSelect.pack()
reverseCompSelect.pack()
transcriptionSelect.pack()
translationSelect.pack()
analyzeButton.pack()

window.mainloop() #run window loop
