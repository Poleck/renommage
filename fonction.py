
class action():
    def __init__(self, nomdurepertoire, regle):
        self.nomdurepertoire = nomdurepertoire
        self.regle = regle
    
    def getNomRepertoire(self):
        return self.nomdurepertoire
    
    def setSimule(self):
        if regles.getNomFichier() is False:
            return "error"

 
class listregles():
    def __init__(self, regles):
        self.regles = regles
    
    def __str__(self):
        return "{}".format(self.regles)
    
    def getRegles(self):
        return self.regles
    
    def setSaveRegles(self):
        with open("save.ini", 'w') as fichier:
            for i in self.regles:
                fichier.write(i)     
    
    def setLoadRegles(self):
        self.regles = []
        with open("save.ini", 'r') as fichier:
            for line in fichier:
                line=line.split()
                self.regles.append(line)
        return self.regles
    
     
    
class regles ():
    def __init__(self, amorce, apartirde, prefixe, nomfichier, postfixe, extension):
        self.amorce = amorce
        self.apartirde = apartirde
        self.prefixe = prefixe
        self.nomfichier = nomfichier
        self.postfixe = postfixe
        self.extension = extension
    
    def __str___(self):
        return "{} {} {} {} {} {}".format(self.amorce, self.apartirde, self.prefixe, self.nomfichier, self.postfixe, self.extension)
    
    def getAmorce(self):
        return self.amorce
    
    def getApartirde(self):
        return self.apartirde
    
    def getPrefixe(self):
        return self.prefixe
    
    def getNomFichier(self, varfichier):
        if self.nomfichier is None:
            return False
        elif self.nomfichier == varfichier:
            return True
        else:
            self.nomfichier = varfichier
            return self.nomfichier
    
    def getPostfixe(self):
        return self.postfixe
    
    def getExtension(self):
        return self.extension
    
    
    
            
  
