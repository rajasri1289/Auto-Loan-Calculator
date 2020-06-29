from tkinter import *

class GUI:

    def __init__(self, master):
        frame = Frame(root)
        frame.pack()

        self.header = Label(frame, text="Calculate the price of your next car: ")
        self.header.pack()

        self.inFields = Frame(frame)
        self.inFields.pack()

        self.rateEntry = makeEntry(self.inFields, 'APR: ', "4.82")
        self.termEntry = makeEntry(self.inFields, 'Term: ', "4")
        self.ppyEntry = makeEntry(self.inFields, "Payments Per Year: ", "12")
        self.paymentEntry = makeEntry(self.inFields, "Loan Payment: ", "266.00")
        self.downEntry = makeEntry(self.inFields, 'Down Payment: ', '0')

        self.button = Button(frame, text="Calculate", command=self.calc)
        self.button.pack()

        self.resultLabelText = StringVar()
        self.resultLabelText.set("Result")
        self.resultLabel = Label(frame, textvariable=self.resultLabelText)
        self.resultLabel.pack()

    def calc(self):
        rate = float(self.rateEntry.get()) / 100
        term = int(self.termEntry.get())
        ppy = int(self.ppyEntry.get())
        payment = float(self.paymentEntry.get())
        down = float(self.downEntry.get())
        self.resultLabelText.set("Price of next car: $%.2f plus down payment" % principal(rate, term, ppy, payment, down))
