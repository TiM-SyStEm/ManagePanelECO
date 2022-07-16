from tkinter import *
import threading
import time

class App(Tk):
    active = []
    btn5 = None
    btn6 = None
    btn7 = None
    btn8 = None
    btn9 = None
    btn10 = None
    startV1_2 = False
    V1 = "0В"
    V2 = "0В"
    tempW1 = 0
    cubeST = 0
    listB = 0
    mPL = 0
    res = None
    startMake = False
        
    def start_gc1(self):
        self.active.append("gc1")
    def start_gc2(self):
        self.active.append("gc2")
    def stop_gc1(self):
        self.active.remove("gc1")
    def stop_gc2(self):
        self.active.remove("gc2")
    def start_water1(self):
        self.active.append("water1")
    def stop_water1(self):
        self.active.remove("water1")
    def start_bum1(self):
        self.active.append("bum1")
    def konBUM1(self):
        if "bum1" in self.active:
            self.active.remove("bum1")
            self.btn6["text"] = "Выкл."
        else:
            self.active.append("bum1")
            self.btn6["text"] = "Вкл."
    def konNW1(self):
        if "linenagr" in self.active:
            self.active.remove("lineagr")
            self.btn5["text"] = "Выкл."
        else:
            self.active.append("lineagr")
            self.btn5["text"] = "Вкл."

    def konPL1(self):
        if "pl1" in self.active:
            self.active.remove("pl1")
            self.btn7["text"] = "Выкл."
        else:
            self.active.append("pl1")
            self.btn7["text"] = "Вкл."

    def konST1(self):
        if "st1" in self.active:
            self.active.remove("st1")
            self.btn8["text"] = "Выкл."
        else:
            self.active.append("st1")
            self.btn8["text"] = "Вкл."

    def konAVR1(self):
        if "avr1" in self.active:
            self.active.remove("avr1")
            self.btn9["text"] = "Выкл."
        else:
            self.active.append("avr1")
            self.btn9["text"] = "Вкл."

    def konAVR2(self):
        if "avr2" in self.active:
            self.active.remove("avr2")
            self.btn10["text"] = "Выкл."
        else:
            self.active.append("avr2")
            self.btn10["text"] = "Вкл."
    def __init__(self):
        super().__init__()
        self.title("Пульт управления комплексом ЭКО")
        self.geometry("1280x720")
        
        self.label1 = Label(text="Гидроцентр 1", fg="#000", bg="#D7D7D7", font=14)
        self.label1.grid(row=0, column=0, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn = Button(text="Пуск", background="#50C83F", foreground="white", font=14, command=self.start_gc1)
        self.btn.grid(row=1, column=0, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn1 = Button(text="Стоп", background="#EB0042", foreground="white", font=14, command=self.stop_gc1)
        self.btn1.grid(row=2, column=0, ipadx=10, ipady=6, padx=10, pady=10)

        self.label2 = Label(text="Гидроцентр 2", fg="#000", bg="#D7D7D7", font=14)
        self.label2.grid(row=0, column=1, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn2 = Button(text="Пуск", background="#50C83F", foreground="white", font=14, command=self.start_gc2)
        self.btn2.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn3 = Button(text="Стоп", background="#EB0042", foreground="white", font=14, command=self.stop_gc2)
        self.btn3.grid(row=2, column=1, ipadx=10, ipady=6, padx=10, pady=10)

        self.label3 = Label(text="Напряжение сети 1", fg="#000", bg="#D7D7D7", font=14)
        self.label3.grid(row=0, column=2, ipadx=10, ipady=6, padx=10, pady=10)
        self.napr1 = Label(text=self.V1, fg="#50C878", bg="#D7D7D7", font=14)
        self.napr1.grid(row=0, column=3, ipadx=10, ipady=6, padx=10, pady=10)
        self.label4 = Label(text="Напряжение сети 2", fg="#000", bg="#D7D7D7", font=14)
        self.label4.grid(row=1, column=2, ipadx=10, ipady=6, padx=10, pady=10)
        self.napr2 = Label(text=self.V2, fg="#50C878", bg="#D7D7D7", font=14)
        self.napr2.grid(row=1, column=3, ipadx=10, ipady=6, padx=10, pady=10)

        self.label5 = Label(text="Контроль воды", fg="#000", bg="#D7D7D7", font=14)
        self.label5.grid(row=3, column=0, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn3 = Button(text="Поток", background="#50C83F", foreground="white", font=14, command=self.start_water1)
        self.btn3.grid(row=4, column=0, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn4 = Button(text="Остановить", background="#EB0042", foreground="white", font=14, command=self.stop_water1)
        self.btn4.grid(row=5, column=0, ipadx=10, ipady=6, padx=10, pady=10)

        self.label6 = Label(text="Линия нагрева воды", fg="#000", bg="#D7D7D7", font=14)
        self.label6.grid(row=0, column=4, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn5 = Button(text="Выкл.", background="#838996", foreground="white", font=14, command=self.konNW1)
        self.btn5.grid(row=0, column=5, ipadx=10, ipady=6, padx=10, pady=10)

        self.label7 = Label(text="Конвеер бумаги", fg="#000", bg="#D7D7D7", font=14)
        self.label7.grid(row=1, column=4, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn6 = Button(text="Выкл.", background="#838996", foreground="white", font=14, command=self.konBUM1)
        self.btn6.grid(row=1, column=5, ipadx=10, ipady=6, padx=10, pady=10)

        self.label8 = Label(text="Конвеер пластика", fg="#000", bg="#D7D7D7", font=14)
        self.label8.grid(row=2, column=4, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn7 = Button(text="Выкл.", background="#838996", foreground="white", font=14, command=self.konPL1)
        self.btn7.grid(row=2, column=5, ipadx=10, ipady=6, padx=10, pady=10)

        self.label9 = Label(text="Конвеер стекла", fg="#000", bg="#D7D7D7", font=14)
        self.label9.grid(row=3, column=4, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn8 = Button(text="Выкл.", background="#838996", foreground="white", font=14, command=self.konST1)
        self.btn8.grid(row=3, column=5, ipadx=10, ipady=6, padx=10, pady=10)

        self.label10 = Label(text="Аварийный слив 1", fg="#EB4C42", bg="#D7D7D7", font=14)
        self.label10.grid(row=4, column=4, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn9 = Button(text="Выкл.", background="#EB4C42", foreground="white", font=14, command=self.konAVR1)
        self.btn9.grid(row=4, column=5, ipadx=10, ipady=6, padx=10, pady=10)

        self.label11 = Label(text="Аварийный слив 2", fg="#EB4C42", bg="#D7D7D7", font=14)
        self.label11.grid(row=5, column=4, ipadx=10, ipady=6, padx=10, pady=10)
        self.btn10 = Button(text="Выкл.", background="#EB4C42", foreground="white", font=14, command=self.konAVR2)
        self.btn10.grid(row=5, column=5, ipadx=10, ipady=6, padx=10, pady=10)

        self.label12 = Label(text="Горяч. вода", fg="#000", bg="#D7D7D7", font=14)
        self.label12.grid(row=3, column=2, ipadx=10, ipady=6, padx=10, pady=10)

        self.label14 = Label(text=str(self.tempW1) + "°C", fg="#50C878", bg="#D7D7D7", font=14)
        self.label14.grid(row=3, column=3, ipadx=10, ipady=6, padx=10, pady=10)

        self.res = Label(text=f"Кубов стекла = {self.cubeST}\nЛистов бумаги = {self.listB}\nМетров пластика = {self.mPL}", fg="#50C878", bg="#D7D7D7", font=14)
        self.res.grid(row=6, column=0, ipadx=10, ipady=6, padx=10, pady=10)
    def make(self):
        self.cubeST += 0.00001
        self.listB += 0.0001
        self.mPL += 0.00001
        self.res["text"] = f"Кубов стекла = {round(self.cubeST, 1)}\nЛистов бумаги = {round(self.listB, 1)}\nМетров пластика = {round(self.mPL, 1)}"
    def run_action(self):
            print("Симуляция начата!")
            while True:
                if self.active == ['gc1', 'gc2', 'water1', 'st1', 'pl1', 'bum1', 'lineagr']:
                    self.make()
                    if self.tempW1 != 90:
                        self.tempW1 = 90
                        self.after(5000, lambda: self.tepmW1_to90())
                    if self.V1 != 10000 and self.V2 != 10000:
                        self.V1 = 10000
                        self.V2 = 10000
                        self.after(5000, lambda: self.V1_V2_to10kv())
                elif "avr1" in self.active and "avr2" in self.active:
                    pass
            print("Симуляция окончена!")

    def start_action(self):
        thread = threading.Thread(target=self.run_action)
        print(threading.main_thread().name)
        print(thread.name)
        thread.start()
    def tepmW1_to90(self):
        self.label14["text"]=str(self.tempW1) + "°C"
    def V1_V2_to10kv(self):
        self.napr1["text"] = str(self.V1) + "В"
        self.napr2["text"] = str(self.V2) + "В"
if __name__ == "__main__":
    app = App()
    app.start_action()
    app.mainloop()
         
