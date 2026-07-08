# Getting Started with TerminusDB

## Prerequisites
A docker environment is configured on your machine

## Server installation steps
clone the terminusdb repository to a local "terminusdb" directory

```
cd terminusdb
```

setup the environment variable in your shell:
```
export TERMINUSDB_ADMIN_PASS=terminus
```

create a .env file with your text editor
```
cat .env
OPENAI_KEY=not-required
BUFFER_AMOUNT=120000
```

run the following command:
```
docker compose up
```

In another window:
## Server installation steps
Install the terminusdb python client with pip

run the setup_db.py script

Expected result:
```
Database 'Pavements' created successfully.
```