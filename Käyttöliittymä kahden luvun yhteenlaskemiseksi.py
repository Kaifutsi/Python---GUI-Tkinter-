import tkinter as tk
 
def laske():
 
  if valRadio.get() == 1:
    pros=(((maara.get())*(hinta.get()) / 100) * 3)
    yhte = round(((maara.get())*(hinta.get()) + pros),2)
  elif valRadio.get() == 2:
    pros=(((maara.get())*(hinta.get()) / 100) * 2)
    yhte = round(((maara.get())*(hinta.get()) - pros),2)
  elif valRadio.get() == 3:
    pros=(((maara.get())*(hinta.get()) / 100) * 4)
    yhte = round(((maara.get())*(hinta.get()) - pros),2)
  else:
    yhte = round((maara.get())*(hinta.get()),2)
  yhtLuvut.set(yhte)
 
 
root = tk.Tk()
valRadio = tk.DoubleVar()
yhtLuvut=tk.DoubleVar()
maara =tk.DoubleVar()
hinta =tk.DoubleVar()
 
 
tk.Label(root, text="""Lasken tilauksen loppusumman huomioiden tilausmäärän, a'hinnan ja maksutavan:""").grid(row = 0, column = 0) 
tk.Label( text="Annatko ostettavan tuotteen määrät:" ).grid(row=1,column = 0)
tk.Label( text="Annatko ostettavan tuotteen hinnan:").grid(row=2,column=0)
yhteLuvut=tk.Label(text="(result)", textvariable=yhtLuvut).grid(row=8,column=1)
 
tk.Entry(textvariable = maara).grid(row=1, column=1)
tk.Entry(textvariable = hinta).grid(row=2, column=1)
 
lisaa_3 = tk.Radiobutton(text="Käteinen + 3% lisää hintaa",variable=valRadio, value=1).grid(row=4, sticky="w")
ale_2 = tk.Radiobutton(text="VISA - 2% alennus",variable=valRadio, value=2).grid(row=5, sticky="w")
ale_4 = tk.Radiobutton(text="OP tilisiirto -4%",variable=valRadio, value=3).grid(row=6, sticky="w")
 
yht = tk.Button(text="Laske yhteen!", command=laske).grid(row=7, column=1)
 
root.mainloop()