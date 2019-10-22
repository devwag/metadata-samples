# DQ Profiling

Single Azure (Spring Boot) Function App with 2 Functions  

1 - Metrics (in SQL DB) -> Atlas  
2 - DQ Rules (in SQL DB) -> Atals

Relies on 3 App Settings configured in Azure Functions

- jdbc-username - configured with the username of the user in Azure SQL DB  
- jdbc-password - configured with a Key Vault reference pointing to a securely stored password for SQL DB
- jdbc-uri - configured with the SQL DB connection string (incl the databasename) 

