import time
import tkinter as tk


OLL = [
    "R U2' R2' F R F' U2' R' F R F'",
    "L F L' U2 R U2' R' U2 L F' L'",
    "r' R2 U R' U r U2' r' U M'",
    "l L2' U' L U' l' U2 l U' M'",
    "l' U2 L U L' U l",
    "r U2' R' U' R U' r'",
    "r U R' U R U2' r'",
    "l' U' L U' L' U2 l",
    "R U R' U' R' F R2 U R' U' F'",
    "r R2' U2 R U R' U R U R r'",
    "S' U2 R U R' U R U2' R' S",
    "M' R' U' R U' R' U2 R U' R r'",
    "F U R U' R2' F' R U R U' R'",
    "R' F R U R' F' R F U' F'",
    "l' U' l L' U' L U l' U l",
    "r U r' R U R' U' r U' r'",
    "F R' F' R2 r' U R U' R' U' M'",
    "r U R' U R U2' r2 U' R U' R' U2' r",
    "r' R U R U R' U' M' R' F R F'",
    "r U R' U' M2 U R U' R' U' M'",
    "R U R' U R U' R' U R U2' R'",
    "R U2' R2' U' R2 U' R2' U2' R",
    "R2 D R' U2 R D' R' U2 R'",
    "r U R' U' r' F R F'",
    "F R' F' r U R U' r'",
    "R U2' R' U' R U' R'",
    "R U R' U R U2 R'",
    "r U R' U' r' R U R U' R'",
    "l D l' U l D' l2' U l U' l' U' l",
    "r' D' r U' r' D r2 U' r' U r U r'",
    "R' U' F U R U' R' F' R",
    "L U F' U' L' U L F L'",
    "R U R' U' R' F R F'",
    "f R f' U' r' U' R U M'",
    "R U2' R2' F R F' R U2' R'",
    "L' U' L U' L' U L U L F' L' F",
    "F R' F' R U R U' R'",
    "R U R' U R U' R' U' R' F R F'",
    "f' L F L' U' L' U L S",
    "f R' F' R U R U' R' S'",
    "R U R' U R U2 R' F R U R' U' F'",
    "R' F R F' R' F R F' R U R' U' R U R'",
    "R' U' F' U F R",
    "F U R U' R' F'",
    "F R U R' U' F'",
    "R' U' R' F R F' U R",
    "F R' F' R U2 R U' R' U R U2 R'",
    "F R U R' U' R U R' U' F'",
    "r U' r2' U r2 U r2' U' r",
    "l' U l2 U' l2' U' l2 U l'",
    "F U R U' R' U R U' R' F'",
    "R' F' U' F U' R U R' U R",
    "l' U' L U' L' U L U' L' U2 l",
    "r U R' U R U' R' U R U2 r'",
    "R' F U R U' R2' F' R2 U R' U' R",
    "r U r' U R U' R' U R U' M' U' r'",
    "R U R' U' M' U R U' r'"
    ]

Positisions = [
    "0010010001101011000100100",
    "0111000000101011000100100",
    "0110000001101010100000110",
    "0011010000101010001001100",
    "0000001101011011000000110",
    "0000010110101100000101100",
    "0100000101011010100000110",
    "0001010100101100001001100",
    "0001010100011010001001100",
    "0100000101011011001000100",
    "0100000110011011000000110",
    "0001001100101100000101100",
    "0110000001011100100000110",
    "0011010000011100001001100",
    "0010001001011101000000110",
    "0010010010011100000101100",
    "0010001001101010001001100",
    "0010001010101010000001110",
    "0010001010101011000100100",
    "0010001010101010101000100",
    "0000010101011101010100000",
    "0001010100011101010000010",
    "0000001110011100010001010",
    "0100000110011100011001000",
    "0000001101011100011001000",
    "0000010110011100010101000",
    "0100000101011100110000010",
    "0000001110011010101000100",
    "0100000110011010001001100",
    "0001001100101100100000110",
    "0100000110101100001001100",
    "0001001100011010100000110",
    "0110000010011100001001100",
    "0100000110101010011001000",
    "0010001001101100011001000",
    "0001001100101101001000100",
    "0000001101011010001001100",
    "0100000110011010100100100",
    "0010010010011100100000110",
    "0010001001011100001001100",
    "0101000100011010101000100",
    "0000010110011011001000100",
    "0000001110011010000001110",
    "0000001101011010100100100",
    "0010010010011101001000100",
    "0000001101101010110100000",
    "0101000100011011000100100",
    "0001010100011011000000110",
    "0001010100101101000000110",
    "0100000101011010000101100",
    "0110000001011100000101100",
    "0001010100101011010000010",
    "0000010101011011000100100",
    "0000010101101101000100100",
    "0111000000011100000001110",
    "0010010001011101000100100",
    "0010001010011100101000100"
]

def piktor():
    c.delete("baol")
    ro = 0
    for i in range(len(Positisions[idenz])):
        ro = i // 5
        if Positisions[idenz][i] == "1":
            c.create_rectangle((i%5) * hight/10 + (wid / 2) - (hight / 4) + 1, ro * hight/10 + hight / 4 + 1, ((i%5) + 1) * hight/10 + (wid / 2) - (hight / 4) - 1, (ro + 1)* hight/10 + hight / 4 - 1, fill="red", tag="baol")

def opsate():
    print(idenz)
    c.itemconfigure(alg, text=OLL[idenz])
    c.itemconfigure(ida, text=idenz)
    piktor()

def KNOPP(event):
    global idenz
    if 0 <= int(alleb.get()) <= 56:
        idenz = int(alleb.get())
        
        opsate()
    else: 
        yousuck = c.create_text(600,150, text="You suck!", font=("monocraft 69"), fill="red")
        c.update_idletasks()
        time.sleep(0.5)
        c.delete(yousuck)
        c.update_idletasks()
    alleb.delete(0, "end")

def ballz(event):
    global idenz
    if event.delta == 120:
        idenz += 1
    else:
        idenz -= 1
    if idenz > 56:
        idenz = 0
    elif idenz < 0:
        idenz = 56
    opsate()
    
    
root = tk.Tk()
idenz = 0
wid = 1200
hight = 800

c = tk.Canvas(root, bg="black", width = wid, height = hight)
alg = c.create_text(wid / 2, hight / 8, text = OLL[0], font=("monocraft 25"), fill="white")
ida = c.create_text(wid / 2, 7 * hight / 8, text = idenz, font=("monocraft 25"), fill="white")
alleb = tk.Entry(root, font=("monocraft 25"))
c.create_window(wid / 2, hight / 16, width=69, height=40, window=alleb)
for i in range(6):
    thicc = 1
    if i == 1 or i == 4:
        thicc = 4
    # vertical
    c.create_line([(i * hight/10 + (wid / 2) - (hight / 4), hight / 4), (i * hight/10 + (wid / 2) - (hight / 4), 3 * hight/4)], fill="white", width=thicc,tag="grid_line")
    # horizontal
    c.create_line([((wid / 2) - (hight / 4), i * hight/10 + hight / 4), ((wid / 2) + (hight / 4), i * hight/10 + hight / 4)], fill="white", width=thicc, tag="grid_line")
piktor()  

c.pack(expand=True, fill=tk.BOTH)
c.update()    

c.bind("<MouseWheel>", ballz)
c.bind_all("<Return>", KNOPP)

root.mainloop() 