from tkinter import *

class ApplicationRenommage(Frame):
    def __init__(self):
        super().__init__()
        self.grid()
        self.boutons()
        self.labels()
        self.textfields()
        self.menu_regles()
        self.recupere()
        
    def boutons(self):
        self.bouton_renommer = Button(self, text="Renommer", command=self.recupere)
        self.bouton_renommer.grid(row=40, column=4)

        self.bouton_nomoriginal = Checkbutton(self, text="Nom original")
        self.bouton_nomoriginal.grid(row=32, column=2)
        
        self.bouton_nomfichier = Checkbutton(self, text="Nom personnalisé")
        self.bouton_nomfichier.grid(row=33, column=2)

        self.bouton_aucune = Button(self, text="Aucune")
        self.bouton_aucune.grid(row=32, column=0)

        self.bouton_aucune = Button(self, text="Lettre", width=6)
        self.bouton_aucune.grid(row=33, column=0)

        self.bouton_aucune = Button(self, text="Chiffre", width=6)
        self.bouton_aucune.grid(row=34, column=0)

    def menu_regles(self):
        self.menuregles = Menu(root)
        self.menuregles_regles = Menu(self.menuregles, tearoff=0)
        self.menuregles_regles.add_command(label="Lister")
        self.menuregles_regles.add_command(label="Créer")   
        self.menuregles.add_cascade(label="Règles", menu=self.menuregles_regles)
        root.config(menu=self.menuregles)
      
    def labels(self):
        self.label_nomrepertoire = Label(self, text="Nom du répertoire", width=20, height=6)
        self.label_nomrepertoire.grid(row=5, column=1)

        self.label_renommerenlots = Label(self, text="Renommer en lots")
        self.label_renommerenlots.grid(row=4, column=2)

        self.label_amorce = Label(self, text="Amorce")
        self.label_amorce.grid(row=31, column=0)

        self.label_prefixe = Label(self, text="Préfixe")
        self.label_prefixe.grid(row=31, column=1)

        self.label_nomfichier = Label(self, text="Nom du fichier")
        self.label_nomfichier.grid(row=31, column=2)

        self.label_postfixe = Label(self, text="Postfixe", width=30)
        self.label_postfixe.grid(row=31, column=3)

        self.label_extension = Label(self, text="Extension Concernée")
        self.label_extension.grid(row=31, column=4)

        self.label_apartirde = Label(self, text="A partir de")
        self.label_apartirde.grid(row=50, column=0)

    
    def textfields(self):
        self.entry_repertoire = Entry(self)
        self.entry_repertoire.grid(row=5, column=2)

        self.entry_prefixe = Entry(self)
        self.entry_prefixe.grid(row=32, column=1)

        self.entry_postfixe = Entry(self)
        self.entry_postfixe.grid(row=32, column=3)

        self.entry_apartirde = Entry(self)
        self.entry_apartirde.grid()

        self.entry_nomfichier = Entry(self)
        self.entry_nomfichier.grid(row=34, column=2)

        self.entry_extension = Entry(self)
        self.entry_extension.grid(row=32, column=4)
        
    def recupere(self):
        print(self.entry_repertoire.get())
        print(self.entry_prefixe.get())
        print(self.entry_postfixe.get())
        print(self.entry_apartirde.get())
        print(self.entry_nomfichier.get())
        print(self.entry_extension.get())

if __name__ == '__main__':
    root = Tk()
    app = ApplicationRenommage()
    root.mainloop()
