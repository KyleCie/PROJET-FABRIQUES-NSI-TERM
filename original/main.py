from time import sleep
from threading import Thread, Lock
from typing import Any
from random import randint

class Objet:
    def __init__(self, nom: str) -> None:
        """
        Class Objet, qui represente les objets des Consommateurs
        """

        self.nom_obj: str = nom
    
    def nom(self) -> str:
        """
        renvoie le nom de l'objet
        """

        return self.nom_obj

class File:
    def __init__(self) -> None:
        """
        Class File, gestion FIFO (First In, First Out)
        """

        self.accumulateur: list[Any] = []
        self.fin: int = -1

    def enfile(self, valeur: Any) -> None:
        """
        enfile un element dans la File

        entree = Any
        sortie = None
        """

        self.accumulateur.append(valeur)
        self.fin += 1
    
    def defile(self) -> Any | None:
        """
        defile un element de la File
        
        entree = None
        sortie = Any | None
        """

        if self.fin == -1:
            return None # vide

        valeur = self.accumulateur.pop(0)
        self.fin -= 1
        return valeur

    def est_vide(self) -> bool:
        """
        renvoie un booleen si la File est vide.

        entree = None
        sortie = bool
        """

        return self.fin == -1

class Consommateur:
    def __init__(self, commande: dict[str, int]) -> None:
        """
        class Consommateur, repesente les demandes des Consommateurs

        entree = dict[str, int] # represente les objet et leurs quantites
        sortie = None
        """

        self.commande: dict[str, int] = commande
        self.objets: File = File()
        self.lock: Lock = Lock()

    def __str__(self) -> str:
        """
        permet de faire un print(consommateur)

        entree = None
        sortie = str
        """

        return "Consommateur(" + str(self.commande) + ")"

    def avoir_commande(self) -> dict[str, int]:
        """
        Avoir la commande du consommateur.

        entree = None
        sortie = dict[str, int]
        """

        return self.commande
    
    def ajouter(self, objet: Objet) -> None:
        """
        ajoute l'objet dans son recu + actualise sa commande.

        entree = Objet
        sortie = None
        """

        with self.lock: # lock de Threads
            self.objets.enfile(objet)
            self.commande[objet.nom()] -= 1

    def bilan(self) -> dict[str, int]:
        """
        Renvoie les objets recu pour repondre a sa commande

        entree = None
        sortie = dict[str, int] # represente les objets/quantites
        """

        bilan: dict[str, int] = {}

        while not self.objets.est_vide():
            obj = self.objets.defile()

            if obj is None: # theoriquement impossible mais c'est gere
                raise ValueError("Aucune valeur de l'objet.")

            bilan[obj.nom()] = bilan.get(obj.nom(), 0) + 1
        
        return bilan

class Fabrique:
    def __init__(self, nom_objet: str, temps_fabriquation: float | int) -> None:
        """
        class Fabrique, represente les usines qui fabriquent les Objets.

        entree = nom_objet: str # nom de l'objet a fabriquer
                 temps_fabriquation: float | int # temps que prend a fabriquer
        sortie = None
        """
        self.nom: str = nom_objet
        self.temps: float | int = temps_fabriquation

    def fabriquer(self, consommateur: Consommateur, debug: bool) -> None:
        """
        Fabrique l'objet + le met dans le consommateur

        entree = consommateur: Consommateur
        sortie = None
        """
        if debug: print("--> Fabrique " + self.nom + " appelee.")
        sleep(temps_fabriquation)
        consommateur.ajouter(Objet(self.nom))
        if debug: print("--> Objet " + self.nom + " ajoute.")

class Commandes:
    def __init__(self) -> None:
        """
        Class Commandes, represente les commandes des consommateurs.
        """
        self.commandes: File = File()

    def creer_commandes(self, noms: tuple[str, ...], combien: int, nombre_maxi: int) -> File:
        """
        Faire des commandes.

        entree = noms: tuple[str] # les noms des objets
                 combien: int     # nombre de commandes
                 nombre_maxi: int # nombre maxi que peux avoir un objet
        sortie = File
        """
        for _ in range(combien):
            commande: dict[str, int] = {}

            for nom in noms:
                commande[nom] = randint(0, nombre_maxi)

            self.commandes.enfile(Consommateur(commande))
        
        return self.commandes
    
    def avoir_commandes(self) -> File:
        """
        renvoie la commande.

        entree = None
        sortie = File
        """
        return self.commandes

class Repartiteur:
    def __init__(self, noms_objets: tuple[str, ...], commandes: File, temps_fabriquation: float | int) -> None:
        """
        Class Repartiteur, represente le gestionnaire des commandes.

        entree = noms_objets: tuple[str] # les noms des objets
                 commandes: File # les commandes des consommateurs
                 temps_fabriquation: float | int # temps de fabriquation des objets
        sortie = None
        """

        self.noms_objets: tuple[str, ...] = noms_objets
        self.commandes: File = commandes
        self.temps_fabriquation: float | int = temps_fabriquation

        self.fabriques: dict[str, Fabrique] = {}
        self.__faire_fabriques() # faire les fabriques avec les noms des objets


    def __faire_fabriques(self) -> None:
        """
        uniquement pour la class ; creer les instances de fabriques
        """
        for nom_objet in self.noms_objets: # Dictionnairs de fabriques -> selon objet.
            self.fabriques[nom_objet] = Fabrique(nom_objet, self.temps_fabriquation)

    def faire_commandes(self, debug: bool = False) -> None:
        """
        Fait les commandes des consommateurs.

        entree = debug: bool (False) # pour les print
        sortie = None
        """
        
        print("Fabriquation des commandes.")

        while not self.commandes.est_vide(): # boucle de commandes
            consommateur: Consommateur | None = self.commandes.defile()

            if consommateur is None: #  theoriquement impossible mais c'est gere
                raise ValueError("Aucune valeur du consommateur.")

            if debug: print("> Nouvelle commande :" + str(consommateur))

            while True: # boucle de commande non terminee.
                

                if debug: print("-> " + str(consommateur))

                commande: dict[str, int] = consommateur.avoir_commande()
                fab_a_lancer: list[Fabrique] = []

                for nom_objet, quantite in commande.items():

                    if nom_objet not in self.noms_objets: # theoriquement impossible mais c'est gere
                        raise ValueError("Aucune fabrique pour l'objet : " + nom_objet)

                    if quantite > 0: # il faut faire l'objet
                        fab_a_lancer.append(self.fabriques[nom_objet])

                if fab_a_lancer == []: 
                    break # vide, commande terminee

                thread_a_lancer: list[Thread] = []

                for fab in fab_a_lancer:
                    thread_a_lancer.append(Thread(target=fab.fabriquer, args=(consommateur, debug)))

                for t in thread_a_lancer:
                    t.start()
                
                for t in thread_a_lancer:
                    t.join()

            if debug: print("> Commande terminee : " + str(consommateur))
            if debug: print("> bilan objets recu : " + str(consommateur.bilan()))
        print("Les commandes sont terminees.")


if __name__ == "__main__": # programme principal

    # --- parametres --- #
    noms_objets: tuple[str, ...] = ("chaise", "table", "banc")
    nombre_commandes: int = 2
    nombre_max_objet: int = 3
    temps_fabriquation: float | int = 0.5
    debug: bool = True
    # --- parametres --- #

    com = Commandes()
    commandes = com.creer_commandes(noms_objets, nombre_commandes, nombre_max_objet)

    rep = Repartiteur(noms_objets, commandes, temps_fabriquation)
    rep.faire_commandes(debug=debug)