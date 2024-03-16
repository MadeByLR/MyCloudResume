{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "name": "req",
      "authLevel": "anonymous",
      "type": "httpTrigger",
      "direction": "in",
      "methods": ["get"]
    },
    {
      "name": "documents",
      "type": "cosmosDBTrigger",
      "direction": "in",
      "leaseCollectionName": "leases",
      "connectionStringSetting": "AccountEndpoint=https://visitorcountcosdb.documents.azure.com:443/;AccountKey=McLARE3IlXyfGZZlL5xCiaAUHrVGWeKd7lchtfmYWN5LuaT0Kf8b8DkNfpQgJkrTTGeqaePrkWBwACDbxkZf3Q==;",
      "databaseName": "visitorcount-db",
      "collectionName": "count-container",
      "createLeaseCollectionIfNotExists": "true"
    }
  ]
}
