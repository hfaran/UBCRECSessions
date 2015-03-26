# ubcrecdb

## Setup

### Bootstrapping Database

```bash
$ sqlite3 project.db < bootstrapdb.sql
```

### Documentation

```bash
sudo pip install mkdocs
mkdocs serve
```

### Running `ubcrecdb`

```bash
sudo pip install -r requirements.txt
cd src/
./ubcrec_server.py --port 8888 --db ../project.db --cookie-secret cookies
```
