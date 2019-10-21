# rules-importer Function

This Java Function connects to an Azure SQL DB database and copies DQ Rules from *[tablename]* and copies them in to Atlas

## App Settings

***jdbc-user*** - the username used for Azure SQL DB database
***jdbc-password*** - the password for the *jdbc-user*
***jdbc-uri*** - the connection string for the Azure SQL DB, including the databasename.

E.g. = jdbc:sqlserver://*[sqldbname]*.database.windows.net:1433;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;database=*[databasename]*

Makes use of Kayvault References to retrieve the password from Azure Keyvault as per this documentation - 
https://docs.microsoft.com/en-us/azure/app-service/app-service-key-vault-references