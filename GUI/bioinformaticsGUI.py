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
                outputWindow.insert(tk.INSERT, "\n")

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

    dnaWindow.mainloop() #run window loop

def proteinGUI():
    """
    Function to launch the Protein Bioinformatics GUI.
    """


    def buttonClick():

        outputWindow.delete('1.0', tk.END) #delete all entries in outputWindow

    #------------------------------single line entry analysis----------------------
        if seqTypeVar.get() == 1: #single line entry
            #proof read sequence
            sequence, style = proteinSeqCheck(sequenceEntry.get('1.0', 'end-1c')) #checks that seq is valid

            #for each button, checks if selected. if True, output is printed
            if molecWeightVar.get() == 1:
                if style == 3:
                    outputWindow.insert(tk.INSERT, "Molecular Weight (g/mol): " + str(molecularWeight(threeToOne(sequence)))+"\n")
                else:
                    outputWindow.insert(tk.INSERT, "Molecular Weight (g/mol): " + str(molecularWeight(sequence))+"\n")
            if (oneToThreeVar.get() == 1) and (style == 1):
                outputWindow.insert(tk.INSERT, "One-to-Three: " + oneToThree(sequence)+"\n")
            if (threeToOneVar.get() == 1) and (style == 3):
                outputWindow.insert(tk.INSERT, "Three-to-one: " + threeToOne(sequence)+"\n")
            if isoVar.get() == 1:
                if style == 3:
                    outputWindow.insert(tk.INSERT, "Isoelectric Point: " + str(isoelectricPoint(threeToOne(sequence)))+"\n")
                else:
                    outputWindow.insert(tk.INSERT, "Isoelectric Point: " + str(isoelectricPoint(sequence))+"\n")
            if netChargeVar.get() == 1:
                if style == 3:
                    outputWindow.insert(tk.INSERT, "Net-Charge: " + str(netCharge(threeToOne(sequence), float(netChargepH.get('1.0', 'end-1c'))))+"\n")
                else:
                    outputWindow.insert(tk.INSERT, "Net-Charge: " + str(netCharge(sequence, float(netChargepH.get('1.0', 'end-1c'))))+"\n")
    #----------------------------FASTA input analysis------------------------------
        elif seqTypeVar.get() == 2: #FASTA input
            seqEntryDict = readFASTA(sequenceEntry.get('1.0', 'end-1c').splitlines())

            for entry in seqEntryDict:
                #prints seq id to text box
                outputWindow.insert(tk.INSERT, "Sequence ID: " + str(entry) + '\n')
                #proof read sequence
                sequence, style = proteinSeqCheck(seqEntryDict[entry]) #checks that seq is valid

                #for each button, checks if selected. if True, output is printed
                if molecWeightVar.get() == 1:
                    if style == 3:
                        outputWindow.insert(tk.INSERT, "Molecular Weight (g/mol): " + str(molecularWeight(threeToOne(sequence)))+"\n")
                    else:
                        outputWindow.insert(tk.INSERT, "Molecular Weight (g/mol): " + str(molecularWeight(sequence))+"\n")
                if (oneToThreeVar.get() == 1) and (style == 1):
                    outputWindow.insert(tk.INSERT, "One-to-Three: " + oneToThree(sequence)+"\n")
                if (threeToOneVar.get() == 1) and (style == 3):
                    outputWindow.insert(tk.INSERT, "Three-to-one: " + threeToOne(sequence)+"\n")
                if isoVar.get() == 1:
                    if style == 3:
                        outputWindow.insert(tk.INSERT, "Isoelectric Point: " + str(isoelectricPoint(threeToOne(sequence)))+"\n")
                    else:
                        outputWindow.insert(tk.INSERT, "Isoelectric Point: " + str(isoelectricPoint(sequence))+"\n")
                if netChargeVar.get() == 1:
                    if style == 3:
                        outputWindow.insert(tk.INSERT, "Net-Charge: " + str(netCharge(threeToOne(sequence), float(netChargepH.get('1.0', 'end-1c'))))+"\n")
                    else:
                        outputWindow.insert(tk.INSERT, "Net-Charge: " + str(netCharge(sequence, float(netChargepH.get('1.0', 'end-1c'))))+"\n")

                outputWindow.insert(tk.INSERT, "\n") #adds line break between entries
    proteinWindow = tk.Toplevel(master=menuWindow)
    proteinWindow.title("Protein Suite") #changes title of window

     #creates and packs label for text entry box
    entryText = tk.Label(proteinWindow,text = "Enter sequence to analyze:")
    entryText.pack()

    #creates and packs entry text box
    sequenceEntry = tk.Text(proteinWindow, height = 5, borderwidth = 2, relief = tk.GROOVE)
    sequenceEntry.pack()

    #creates and packs Radiobutton for single or FASTA input select
    seqTypeVar = tk.IntVar() #variable to store Radiobutton value
    #value of 1 == single seq, value == 2 FASTA
    singleSeq = tk.Radiobutton(proteinWindow, text = "Single Sequence", variable = seqTypeVar, value = 1)
    multiSeq = tk.Radiobutton(proteinWindow, text = "FASTA", variable = seqTypeVar, value = 2)
    singleSeq.pack()
    multiSeq.pack()

    #creates and packs lable of analysis options
    analysisText = tk.Label(proteinWindow, text = 'Analysis Options:')
    analysisText.pack()

    #create and pack checkbuttons for analysis options
    #crates variables to store analysis variable options to
    molecWeightVar = tk.IntVar()
    molecWeighttSelect = tk.Checkbutton(proteinWindow, text = 'Molecular Weight', variable = molecWeightVar)
    molecWeighttSelect.pack()
    oneToThreeVar = tk.IntVar()
    onetoThreeVarSelect = tk.Checkbutton(proteinWindow, text = 'One-to-Three', variable = oneToThreeVar)
    onetoThreeVarSelect.pack()
    threeToOneVar = tk.IntVar()
    threeToOneSelect = tk.Checkbutton(proteinWindow, text = 'Three-to-One', variable = threeToOneVar)
    threeToOneSelect.pack()
    isoVar = tk.IntVar()
    isoelectricSelect = tk.Checkbutton(proteinWindow, text = 'Isoelectric Point', variable = isoVar)
    isoelectricSelect.pack()
    netChargeVar = tk.IntVar()
    netChargeSelect = tk.Checkbutton(proteinWindow, text = 'Net Charge', variable = netChargeVar)
    netChargeSelect.pack()
    pHLabel = tk.Label(proteinWindow, text = "pH to determine Net-Charge")
    pHLabel.pack()
    netChargepH = tk.Text(proteinWindow, height = 1, width = 5, borderwidth = 2, relief = tk.GROOVE)
    netChargepH.pack()

    #create and pack button to analyse the seq, connected to buttonClick func
    analyzeButton = tk.Button(proteinWindow, text = "Analyze", command = buttonClick)
    analyzeButton.pack()

    #create and pack output box label
    outputText = tk.Label(proteinWindow, text = "Analysis Output:") #add text to denote output
    outputText.pack()

    #create and pack output box
    outputWindow = tk.Text(proteinWindow, height = 10, borderwidth = 2, relief = tk.GROOVE)
    outputWindow.pack()

    proteinWindow.mainloop() #run window loop

#create and label menu window
menuWindow = tk.Tk()
menuWindow.title("Bioinformatics Suite Menu")

dnaButton = tk.Button(text = "DNA Suite", command = dnaGUI)
dnaButton.pack()

proteinButton = tk.Button(text = "Protein Suite", command = proteinGUI)
proteinButton.pack()

menuWindow.mainloop()
