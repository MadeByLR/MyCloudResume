import os
import json
from azure.cosmos import CosmosClient
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Get Cosmos DB connection details from environment variables
        cosmos_uri = os.environ["https://visitorcountcosdb.documents.azure.com:443/"]
        cosmos_key = os.environ["McLARE3IlXyfGZZlL5xCiaAUHrVGWeKd7lchtfmYWN5LuaT0Kf8b8DkNfpQgJkrTTGeqaePrkWBwACDbxkZf3Q=="]
        database_name = os.environ["visitorcount-db"]
        collection_name = os.environ["count-container"]

        # Create Cosmos DB client with the authorization token
        connection_policy = documents.ConnectionPolicy()
        connection_policy.SslConfig.SslOptions = documents.SslOptions(EnabledProtocols="TLSv1_2")
        client = CosmosClient(cosmos_uri, {'masterKey': cosmos_key}, connection_policy=connection_policy)
        
        # Use the Cosmos DB client to interact with the database and container
        database = client.get_database_client(database_name)
        container = database.get_container_client(collection_name)

        # Retrieve existing visitor count from Cosmos DB
        existing_count = container.read_item(item="visitor_count", partition_key="visitor_count")["count"]

        # Increment the visitor count
        new_count = existing_count + 1

        # Update the visitor count in Cosmos DB
        container.upsert_item(
            {
                "id": "visitor_count",
                "count": new_count
            }
        )

        # Prepare response
        response_message = {"count": new_count}
        return func.HttpResponse(json.dumps(response_message), mimetype="application/json", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
