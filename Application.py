from tkinter import *
import random

transmissionDetail = []
ind = 0
validCodewords = {'0000': '11110', '0001': '01001', '0010': '10100', '0011': '10101',
                          '0100': '01010', '0101': '01011', '0110': '01110', '0111': '01111',
                          '1000': '10010', '1001': '10011', '1010': '10110', '1011': '10111',
                          '1100': '11010', '1101': '11011', '1110': '11100', '1111': '11101'}
def app() :
    def keyword(errorCodeWord):
        for i,j in validCodewords.items():
            if j == errorCodeWord:
                return i

    def receive():
        code.set(str(transmissionDetail[ind+3]))
        print(transmissionDetail[ind+3])

    def exit():
        quit()

    def transmission(dataWord, codeWord, errorPerc, rec):
        global ind
        transmissionDetail.append(dataWord)
        transmissionDetail.append(codeWord)
        transmissionDetail.append(errorPerc)
        transmissionDetail.append(rec)
        d.set(transmissionDetail[ind])
        c.set(transmissionDetail[ind+1])
        e.set(transmissionDetail[ind+2])
        receive()
        ind = ind + 4
        print(transmissionDetail)

    def blockCoding():
        global transmissionDetail

        rec =""
        dataWord = dw.get()
        dw.delete(0, END)
        codeWord = validCodewords[dataWord]
        errorPerc = random.randrange(100)

        if errorPerc > 70:
            errorCodeWord = bin(random.randrange(31)).replace("0b", "")
            errorCodeWord = errorCodeWord.zfill(5)
            if errorCodeWord in validCodewords.values():
                if errorCodeWord == codeWord:
                    labtext.set("LUCKY TRANSMISSION")
                    rec = dataWord
                else:
                    labtext.set("Error Undetected")
                    rec = keyword(errorCodeWord)
            else:
                labtext.set("Error... Discarding Packet !...")
                rec = "****"
        else:
            labtext.set("TRANSMISSION SUCCESS !")
            rec = dataWord

        transmission(dataWord, codeWord, errorPerc, rec)


    start.destroy()
    root = Tk()
    root.title("4B/5B Block Coding")
    root.geometry("1050x700")
    root.config(bg = "gray25")
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    labtext = StringVar()
    labtext.set("------")

    Label(root, text="4B/5B BLOCK CODING",
          bg="gray25",
          fg="gold",
          font=("Bahnschrift SemiBold", 40, "bold"),
          pady="5").pack()

    Label(root, text = "ENTER 4 BIT DATAWORD TO BE TRANSMITED : ",
                bg = "gray25",
                fg = "dark turquoise",
                font = ("Bahnschrift SemiBold", 25),
                pady = "5").pack()

    dw = Entry(root, bg = "black",
                     fg = "lawn green",
                     font = ("Bahnschrift SemiBold", 60),
                     width = "4")
    dw.pack(padx = "10", pady="10")

    Button(root, text = "SEND",
                 command = blockCoding,
                 bg = "cornsilk4",
                 font = ("Bahnschrift SemiBold", 20, "bold")).pack()

    code = StringVar()
    code.set("----")

    rdw = Label(root, textvariable=code, bg="black",
               fg="lawn green",
               font=("Bahnschrift SemiBold", 60),
               width="4")
    rdw.pack(anchor="n", padx = "20", pady="10")

    d = StringVar()
    d.set("------")
    c = StringVar()
    c.set("------")
    e = StringVar()
    e.set("------")

    label = Label(root, text = "Transmission Status : ",
                  font=("Bahnschrift SemiBold", 20),
                  bg="gray25",
                  fg="orange red"
                  )
    label.pack(padx = "10")
    label = Label(root, textvariable = labtext,
                        font = ("Bahnschrift SemiBold", 15),
                        bg = "gray25",
                        fg = "cyan")
    label.pack(padx="10",pady = "10")

    label1 = Label(root, text="Dataword : ",
                   font=("Bahnschrift SemiBold", 15),
                   bg="gray25",
                   fg="orange red"
                   )
    label1.pack(padx="10")
    label1 = Label(root, textvariable = d,
                      font=("Bahnschrift SemiBold", 15),
                      bg="gray25",
                      fg="darkorange1")
    label1.pack(padx="10",pady="10")

    label2 = Label(root, text="Codeword Generated : ",
                   font=("Bahnschrift SemiBold", 15),
                   bg="gray25",
                   fg="orange red"
                   )
    label2.pack(padx="10")
    label2 = Label(root, textvariable = c,
                      font=("Bahnschrift SemiBold", 15),
                      bg="gray25",
                      fg="darkorange1")
    label2.pack(pady="10", padx="10")

    label3 = Label(root, text="Error Expectancy : ",
                   font=("Bahnschrift SemiBold", 15),
                   bg="gray25",
                   fg="orange red"
                   )
    label3.pack(padx="10")
    label3 = Label(root, textvariable = e,
                      font=("Bahnschrift SemiBold", 15),
                      bg="gray25",
                      fg="darkorange1")
    label3.pack(padx="10",pady="10")
    transmissionDetail.clear()

    Button(root, text="EXIT",
           command = exit,
           bg="cornsilk4",
           font=("Bahnschrift SemiBold", 20, "bold")).pack()


    root.mainloop()

start = Tk()
start.title("4B/5B Block Coding")
start.geometry("1081x700")
start.config(bg = "black")

canvas = Canvas(start, width = 1081, height = 610)
canvas.pack()
img = PhotoImage(file = "newbg.gif")
canvas.create_image(540, 310, image=img)

Button(start, text = "GET STARTED", bg = "midnight blue", fg = "cyan", font = ("Bahnschrift SemiBold", 30), command = app).pack()

start.mainloop()