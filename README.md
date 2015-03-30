# UBC REC Sessions

An application that allows UBC REC players to sign-up for drop-in sessions in
 advance to gauge interest!

## Setup

### Bootstrapping Database

```bash
$ sqlite3 project.db < bootstrapdb.sql
```

### Installing Dependencies

```bash
sudo pip install -r requirements.txt
# For documentation
sudo pip install mkdocs
```


## Running the Application

```bash
cd src/
./ubcrec_server.py --port 8888 --db ../project.db --cookie-secret cookies
```


## Web API Documentation

Using `mkdocs`:

```bash
mkdocs serve
```

Or you can just view `docs/API_documentation.md`.
