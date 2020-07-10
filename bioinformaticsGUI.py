import tkinter as tk #import tkinter as tk
from dnaFuncs import * #import all functions from dnaFuncs
from proteinFuncs import * #import all funcs from proteinFuncs
from readFASTA import * #import all funcs from readFASTA

def dnaGUI():
    """
    Function to launch the DNA Bioinformatics GUI.
    """


    def buttonClick():

        outputWindow.delete('1.0', tk.END) #delete all entries in outputWindow

    #------------------------------single line entry analysis----------------------
        if seqTypeVar.get() == 1: #single line entry
            #proof read sequence
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
                #prints seq id to text box
                outputWindow.insert(tk.INSERT, "Sequence ID: " + str(entry) + '\n')
                #proof read sequence
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


    dnaWindow = tk.Toplevel(master=menuWindow)
    dnaWindow.title("DNA Suite") #changes title of window

     #creates and packs label for text entry box
    entryText = tk.Label(dnaWindow,text = "Enter sequence to analyze:")
    entryText.pack()

    #creates and packs entry text box
    sequenceEntry = tk.Text(dnaWindow, height = 5, borderwidth = 2, relief = tk.GROOVE)
    sequenceEntry.pack()

    #creates and packs Radiobutton for single or FASTA input select
    seqTypeVar = tk.IntVar() #variable to store Radiobutton value
    #value of 1 == single seq, value == 2 FASTA
    singleSeq = tk.Radiobutton(dnaWindow, text = "Single Sequence", variable = seqTypeVar, value = 1)
    multiSeq = tk.Radiobutton(dnaWindow, text = "FASTA", variable = seqTypeVar, value = 2)
    singleSeq.pack()
    multiSeq.pack()

    #creates and packs lable of analysis options
    analysisText = tk.Label(dnaWindow, text = 'Analysis Options:')
    analysisText.pack()

    #create and pack checkbuttons for analysis options
    #crates variables to store analysis variable options to
    gcVar = tk.IntVar()
    gcContentSelect = tk.Checkbutton(dnaWindow, text = 'GC Content', variable = gcVar)
    gcContentSelect.pack()
    revCompVar = tk.IntVar()
    reverseCompSelect = tk.Checkbutton(dnaWindow, text = 'Reverse Complement', variable = revCompVar)
    reverseCompSelect.pack()
    transVar = tk.IntVar()
    transcriptionSelect = tk.Checkbutton(dnaWindow, text = 'Transciption', variable = transVar)
    transcriptionSelect.pack()
    translationVar = tk.IntVar()
    translationSelect = tk.Checkbutton(dnaWindow, text = 'Translation', variable = translationVar)
    translationSelect.pack()

    #create and pack button to analyse the seq, connected to buttonClick func
    analyzeButton = tk.Button(dnaWindow, text = "Analyze", command = buttonClick)
    analyzeButton.pack()

    #create and pack output box label
    outputText = tk.Label(dnaWindow, text = "Analysis Output:") #add text to denote output
    outputText.pack()

    #create and pack output box
    outputWindow = tk.Text(dnaWindow, height = 10, borderwidth = 2, relief = tk.GROOVE)
    outputWindow.pack()

    window.mainloop() #run window loop

#create and label menu window
menuWindow = tk.Tk()
menuWindow.title("Bioinformatics Suite Menu")

dnaButton = tk.Button(text = "DNA Suite", command = dnaGUI)
dnaButton.pack()


menuWindow.mainloop()
