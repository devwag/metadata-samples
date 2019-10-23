# DQ Profiling

Single Azure (Spring Boot) Function App with 2 Functions  

1 - Metrics (in SQL DB) -> Atlas  
2 - DQ Rules (in SQL DB) -> Atals

Relies on 3 App Settings configured in Azure Functions

- jdbc-username - configured with the username of the user in Azure SQL DB  
- jdbc-password - configured with a Key Vault reference pointing to a securely stored password for SQL DB
- jdbc-uri - configured with the SQL DB connection string (incl the databasename)


CREATE TABLE DQ_RULESINFO (
	RULEID VARCHAR PRIMARY KEY,
	RULENAME VARCHAR,
	DIMENSION VARCHAR,
	COLUMNNAME VARCHAR,
	[Rule Description] VARCHAR,
	[Business Rule Name] VARCHAR,
	[Update Timestamp] DATETIME,
	RULETYPE VARCHAR,
	TABLE_FQDN VARCHAR,
	COLUMN_FQDN VARCHAR,
	TABLENAME VARCHAR,
	RULEDEFINITION VARCHAR,
	RULEPRIORITY VARCHAR
);


CREATE TABLE DQ_RUNINFO (
	RUNID VARCHAR PRIMARY KEY,
	ENTITYID VARCHAR,
	STARTTIME VARCHAR,
	ENDTIME VARCHAR,
	STATUS VARCHAR,
	RUNBY VARCHAR,
	[TOTAL ROWS] INT,
	[ROWS PASSED] INT,
	[ROWS FAILED] INT
);


CREATE VIEW VW_ENTITYSCORE
AS
SELECT 
    ENTITYID, 
    MAX([ENDTIME]) as [Update Timestamp],
    SUM([TOTAL ROWS]) as [TOTAL ROWS],
    SUM([ROWS PASSED]) AS [ROWS PASSED],
    SUM([ROWS FAILED]) AS [ROWS FAILED]
FROM DQ_RUNINFO
GROUP BY ENTITYID

