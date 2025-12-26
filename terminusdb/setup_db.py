from terminusdb_client import Client

if __name__ == '__main__':
    client = Client("http://127.0.0.1:6364/")
    team="admin"
    client.connect(team="admin")
    dbid="Pavements"
    label="Pavements"
    description="Pavements database"
    prefixes = {'@base' : 'iri:///pavements/',
                '@schema' : 'iri:///pavements#'}
    team="admin"
    client.create_database(
        dbid,
        team,
        label=label,
        description=description,
        prefixes=prefixes)
