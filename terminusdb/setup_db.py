from terminusdb import Client
from terminusdb_client.errors import DatabaseError


def main() -> None:
    server_url = "http://127.0.0.1:6363/"
    team = "admin"
    dbid = "Pavements"
    label = "Pavements"
    description = "Pavements database"
    prefixes = {
        "@base": "iri:///pavements/",
        "@schema": "iri:///pavements#",
    }

    client = Client(server_url)
    client.connect(team=team, user="admin", key="terminus")

    try:
        client.get_database(dbid, team)
        print(f"Database '{dbid}' already exists.")
    except DatabaseError:
        client.create_database(
            dbid,
            team,
            label=label,
            description=description,
            prefixes=prefixes,
        )
        print(f"Database '{dbid}' created successfully.")


if __name__ == "__main__":
    main()
