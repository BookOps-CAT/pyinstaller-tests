import os
from tkinter import *
from tkinter.ttk import *


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.columnconfigure(0, minsize=300)
        container.grid(padx=10)

        baseFrm = Frame(container)
        baseFrm.grid(row=0, column=0)

        self.msg = StringVar()

        buttonA = Button(baseFrm, text="button A", command=self.foo)
        buttonA.grid(row=0, column=0, padx=20, pady=5)

        buttonB = Button(baseFrm, text="button B", command=self.bar)
        buttonB.grid(row=1, column=0, padx=20, pady=5)

        label = Label(baseFrm, textvariable=self.msg)
        label.grid(row=2, column=0, padx=20, pady=10)

        separator = Separator(baseFrm, orient=HORIZONTAL)
        separator.grid(row=3, column=0, sticky="snew")

        closeBtn = Button(baseFrm, text="close", command=self.quit)
        closeBtn.grid(row=4, column=0, padx=20, pady=10)

    def foo(self):
        self.msg.set("Foo")

    def bar(self):
        self.msg.set("Bar")


def run():
    # This should start and launch your app!
    app = App()
    s = Style()
    if os.name == "nt":
        s.theme_use("xpnative")
    app.title("BookOps Test Application")
    app.mainloop()


if __name__ == "__main__":
    run()
