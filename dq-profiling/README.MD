# DQ Profiling

Single Azure (Spring Boot) Function App with 2 Functions  

1 - Metrics (in SQL DB) -> Atlas  
2 - DQ Rules (in SQL DB) -> Atals

Relies on 3 App Settings configured in Azure Functions

- jdbc-username - configured with the username of the user in Azure SQL DB  
- jdbc-password - configured with a Key Vault reference pointing to a securely stored password for SQL DB
- jdbc-uri - configured with the SQL DB connection string (incl the databasename)


CREATE TABLE DQ_RULESINFO (
	RULEID VARCHAR(50) PRIMARY KEY,
	RULENAME VARCHAR(100),
	DIMENSION VARCHAR(50),
	COLUMNNAME VARCHAR(50),
	[Rule Description] VARCHAR(255),
	[Business Rule Name] VARCHAR(255),
	[Update Timestamp] DATETIME,
	RULETYPE VARCHAR(255),
	TABLE_FQDN VARCHAR(255),
	COLUMN_FQDN VARCHAR(255),
	TABLENAME VARCHAR(255),
	RULEDEFINITION VARCHAR(255),
	RULEPRIORITY VARCHAR(255)
);


CREATE TABLE DQ_RUNINFO (
	RUNID VARCHAR(36) PRIMARY KEY,
	ENTITYID VARCHAR(50),
	STARTTIME DATETIME,
	ENDTIME DATETIME,
	STATUS VARCHAR(50),
	RUNBY VARCHAR(10),
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

