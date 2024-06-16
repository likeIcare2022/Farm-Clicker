import tkinter as tk
import math
import subprocess
import time

wheat = 0
collect_per_sec = 1

class Game:
    def __init__(self, root):
        global land
        root.title("Farm Clicker")
        self.collect_wheat = None
        self.land = None
        self.widgets()

    def widgets(self):
        global land, collect_wheat, land_label, wheat, wheat_amount, money_label, money, convert_button, auto_collect_button, auto_collect_cost
        collect_wheat = tk.Button(root, text="Collect Wheat", command=self.wheat, font=("Arial Black", 10))
        collect_wheat.pack()
        land_label = tk.Label(root, text=f"Land: {land}", font=("Arial Black", 10))
        land_label.pack()
        wheat_amount = tk.Label(root, text=f"Wheat: {wheat}", font=("Arial Black", 20), pady=25, padx=50)
        wheat_amount.pack()
        money_label = tk.Label(root, text=f"Money: {money}", font=("Arial Black", 10))
        money_label.pack()
        convert_button = tk.Button(root, text="Convert", font=("Arial Black", 10), command=self.convert)
        convert_button.pack()
        auto_collect_button = tk.Button(root, text=f"Hire Worker (Cost: {auto_collect_cost})",
                                        command=self.auto_collect_purchase, font=("Arial Black", 10))
        auto_collect_button.pack()

    def refresh(self):
        global collect_wheat, land_label, wheat_amount, money_label, convert_button, auto_collect_button
        collect_wheat.destroy()
        land_label.destroy()
        wheat_amount.destroy()
        money_label.destroy()
        convert_button.destroy()
        auto_collect_button.destroy()
        self.widgets()

    def wheat(self):
        global wheat, land
        wheat += math.floor(land * 2)
        self.refresh()

    def convert(self):
        global wheat, money
        if wheat == 0:
            print("Not Enough Wheat!")
        else:
            for i in range(wheat):
                money += 3
                wheat = wheat - 1
        self.refresh()

    def auto_collect_purchase(self):
        global auto_collect_cost, money, collect_per_sec
        if money >= auto_collect_cost:
            money = money - auto_collect_cost
            collect_per_sec += 1
            auto_collect_cost = math.floor(auto_collect_cost * 1.5)
        else:
            print("Not Enough Money!")
        print("main cps={0}".format(collect_per_sec))
        self.refresh()


def auto_collect():
    while True:
        global wheat, collect_per_sec
        wheat += collect_per_sec
        time.sleep(1)


if __name__ == "__main__":
    subprocess.Popen(['python', 'music.py'])
    subprocess.Popen(['python', 'auto_collect.py'])

    land = 1
    collect_wheat = None
    land_label = None
    wheat_amount = None
    money = 0
    money_label = None
    convert_button = None
    auto_collect_cost = 10
    auto_collect_button = None

    root = tk.Tk()
    app = Game(root)
    root.mainloop()
