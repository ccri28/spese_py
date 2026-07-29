
import mysql.connector
import sys
import json

class Spese:
    def __init__(self):
        self.totale_spesa = 0

    def connectDb(self):
        # leggo il file di configurazione per il database
        dbconfig = open("dbconfig.json").read()
        dbconfig = json.loads(dbconfig)
        # mi collego al database
        mydb = mysql.connector.connect(
            host=dbconfig['host'],
            user=dbconfig['user'],
            passwd=dbconfig['passwd'],
            database=dbconfig['database']
        )
        return mydb

    def listaSpese(self, flag_stampa = True):
        # di default il flag_stampa vale true quindi stampo le spese man mano e infine il totale
        # quando calcolo la rimanenza, mi server soltanto il valore aggiornato di self.totale_spesa senza stampare le spese 
        # quindi per questo in caso di calcolo rimanenza, devo passare il flag_stampa a False come parametro
        db = self.connectDb()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM spese")
        lista_spese = cursor.fetchall()
        self.totale_spesa = 0
        for spesa in lista_spese:
            self.totale_spesa += spesa[1]
            if flag_stampa == True:
                print(f"Spesa: {spesa[1]} € | Causale: {spesa[2]} \n")
        if flag_stampa == True:
            print(f"Totale speso: {self.totale_spesa} €")

    def inserisciSpesa(self, cifra, causale):
        db = self.connectDb()
        cursor = db.cursor()
        sql = "INSERT INTO spese (euro, causale) VALUES (%s, %s)"
        val = (cifra, causale)
        cursor.execute(sql, val)
        db.commit()
        print(cursor.rowcount, "Spesa inserita con successo.")

    def calcolaRimanenza(self, stipendio):
        self.listaSpese(False)
        rimanenza = float(stipendio) - self.totale_spesa
        print(f"Rimanenza: {rimanenza} €")

    def menu(self):
        menu = """
        --- MENU SPESE ---
        1. Visualizza spese
        2. Inserire spesa
        3. Calcola rimanenza
        4. Esci
        """

        while True:
            scelta = input(menu)
            if scelta == "1":
                s.listaSpese()
            elif scelta == "2":
                cifra = input("Inserire spesa: ")
                try:    
                    cifra = float(cifra)
                except ValueError:
                    print("Errore: non hai inserito un numero valido.")
                    self.menu()
                causale = input("Inserire causale: ")
                s.inserisciSpesa(cifra, causale)
            elif scelta == "3":
                stipendio = input("Inserire stipendio: ")
                try:    
                    stipendio = float(stipendio)
                except ValueError:
                    print("Errore: non hai inserito un numero valido.")
                    self.menu()
                s.calcolaRimanenza(stipendio)
            elif scelta == "4":
                print("Sto uscendo")
                sys.exit(0)
            else:
                print("Scelta non valida. Riprova.")
                self.menu()
    
s = Spese()
s.menu()