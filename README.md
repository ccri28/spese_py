# Tracciatore di Spese Python

Questo script Python permette di collegarsi a un database MySQL per gestire e registrare le spese finanziarie.

## 📋 Descrizione del Database

Lo script interagisce con un database contenente una tabella chiamata `spese`. La tabella è strutturata con i seguenti campi:

* `id`: Identificativo univoco (Chiave primaria).
* `euro`: Importo della spesa.
* `causale`: Descrizione o motivo della spesa.
* `data`: Data in cui è stata effettuata la spesa.

## 🛠️ Requisiti e Installazione

Per poter eseguire lo script, è necessario installare la libreria di connessione MySQL per Python.

Esegui i seguenti comandi nel tuo terminale per installare la dipendenze richieste:

```bash
pip install mysql-connector-python
```

```bash
pip install pyinstaller
```

## ⚙️ Configurazione del Database

Lo script legge le credenziali di accesso al database da un file esterno chiamato `dbconfig.json` tramite la funzione `json.loads`. 

Crea un file chiamato `dbconfig.json` nella stessa cartella dello script con la seguente struttura:

```json
{
  "host": "localhost",
  "user": "il_tuo_utente",
  "passwd": "la_tua_password",
  "database": "nome_del_tuo_db"
}
```

## 🚀 Come Utilizzare lo Script

1. Assicurati che il tuo server MySQL sia attivo e che la tabella `spese` sia presente.
2. Configura il file `dbconfig.json` come mostrato sopra.
3. Avvia lo script dal terminale:

```bash
python nome_del_tuo_script.py
```

## ⚙️ Eseguibile .exe per Windows

E' stato realizzato un eseguibile spese.exe nella cartella `dist` 
Nota: bisogna mettere il file `dbconfig.json` nella cartella `dist` per far funzionare l'eseguibile

## 📋 Istruzioni realizzazione .exe per Windows

Per poter creare l'eseguibile, bisogna assicurarsi di aver installato `pyinstaller`:

```bash
pip install pyinstaller
```

Una volta installato `pyinstaller`, e con l'ambiente venv attivo, lanciare il seguente comando:

```bash
pyinstaller --onefile --hidden-import=mysql.connector.plugins.mysql_native_password --copy-metadata=mysql-connector-python spese.py
```

Una volta creato l'esegubile, sarà possibile trovarlo nella cartella `dist`