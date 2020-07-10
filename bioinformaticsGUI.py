import tkinter as tk #import tkinter as tk
from dnaFuncs import * #import all functions from dnaFuncs
from proteinFuncs import * #import all funcs from proteinFuncs
from readFASTA import * #import all funcs from readFASTA

#function to get value of checkbuttons
def buttonClick():

    outputWindow.delete('1.0', tk.END) #delete all entries in outputWindow

#------------------------------single line entry analysis----------------------
    if seqTypeVar.get() == 1: #single line entry
        sequence = dnaSeqCheck(sequenceEntry.get('1.0', 'end-1c')) #checks that seq is valid

        #for each button, checks if selected. if True, output is printed
        if gcVar.get() == 1:
            outputWindow.insert(tk.INSERT, "GC content: " + str(gcContent(sequence))+"\n")
        if revCompVar.get() == 1:
            outputWindow.insert(tk.INSERT, "Reverse complement: " + reverseComp(sequence)+"\n")
        if transVar.get() == 1:
            outputWindow.insert(tk.INSERT, "Transciption: " + transcription(sequence)+"\n")
        if translationVar.get() == 1:
            outputWindow.insert(tk.INSERT, "Translation: " + translation(sequence)+"\n")
#----------------------------FASTA input analysis------------------------------
    elif seqTypeVar.get() == 2: #FASTA input
        seqEntryDict = readFASTA(sequenceEntry.get('1.0', 'end-1c').splitlines())

        for entry in seqEntryDict:
            outputWindow.insert(tk.INSERT, "Sequence ID: " + str(entry) + '\n')
            sequence = dnaSeqCheck(seqEntryDict[entry])
            #for each button, checks if selected. if True, output is printed
            if gcVar.get() == 1:
                outputWindow.insert(tk.INSERT, "GC content: " + str(gcContent(sequence))+"\n")
            if revCompVar.get() == 1:
                outputWindow.insert(tk.INSERT, "Reverse complement: " + reverseComp(sequence)+"\n")
            if transVar.get() == 1:
                outputWindow.insert(tk.INSERT, "Transciption: " + transcription(sequence)+"\n")
            if translationVar.get() == 1:
                outputWindow.insert(tk.INSERT, "Translation: " + translation(sequence)+"\n")


window = tk.Tk() #create tkinter winde
window.title("Bioinformatics Suite") #changes title of window
greeting = tk.Label(text = "Enter sequence to analyze:") #adds a test text to the window
analysisText = tk.Label(text = 'Analysis Options:')

#determine if single sequence or FASTA
seqTypeVar = tk.IntVar()
singleSeq = tk.Radiobutton(text = "Single Sequence", variable = seqTypeVar, value = 1)
multiSeq = tk.Radiobutton(text = "FASTA", variable = seqTypeVar, value = 2)

#create varaible to save the value of the checkbuttons
entryScrollbar = tk.Scrollbar()
entryScrollbar.pack(side = tk.RIGHT, fill = tk.Y)
sequenceEntry = tk.Text(yscrollcommand = entryScrollbar.set,height = 5, borderwidth = 2, relief = tk.GROOVE)

gcVar = tk.IntVar()
revCompVar = tk.IntVar()
transVar = tk.IntVar()
translationVar = tk.IntVar()

#create the check buttons for the various DNA functions
gcContentSelect = tk.Checkbutton(text = 'GC Content', variable = gcVar)
reverseCompSelect = tk.Checkbutton(text = 'Reverse Complement', variable = revCompVar)
transcriptionSelect = tk.Checkbutton(text = 'Transciption', variable = transVar)
translationSelect = tk.Checkbutton(text = 'Translation', variable = translationVar)

#create button to analyse the seq, connected to buttonClick func
analyzeButton = tk.Button(text = "Analyze", command = buttonClick)

outputText = tk.Label(text = "Analysis Output:") #add text to denote output

outputWindow = tk.Text(height = 10, borderwidth = 2, relief = tk.GROOVE)

#pack all components into window
greeting.pack()
sequenceEntry.pack()
singleSeq.pack()
multiSeq.pack()
analysisText.pack()
gcContentSelect.pack()
reverseCompSelect.pack()
transcriptionSelect.pack()
translationSelect.pack()
analyzeButton.pack()
outputText.pack()
outputWindow.pack()

window.mainloop() #run window loop
