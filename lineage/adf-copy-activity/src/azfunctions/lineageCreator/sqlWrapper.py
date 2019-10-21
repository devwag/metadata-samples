import logging
import pyodbc
import os

class SqlWrapper:
    def __init__(self, config):
        self.connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=%s;Database=%s;uid=%s;pwd=%s;" % 
                            (
                                config['sql_server'],
                                config['sql_database'],
                                config['sql_login'], 
                                config['sql_password']
                            ))
        
    def getModifiedDatasets(self):

        selectStatement = """
            SELECT 
                r.clm_int_id as request_id,
				clm_varchar_datafactory_name as datafactory_name,
				clm_varchar_pipeline_name as pipeline_name,
				clm_varchar_activity_name as activity_name,
                clm_varchar_execution_start_time as execution_start_time,
                clm_varchar_execution_end_time as execution_end_time,
                d.clm_int_id as dataset_id,
                d.clm_varchar_dataset as dataset,
                d.clm_varchar_direction as direction,
                d.clm_varchar_type as type,
                d.clm_varchar_azure_resource as azure_resource
            FROM [dbo].[tbl_lineage_request] as r
            JOIN [dbo].[tbl_datasets] d on d.clm_int_lineage_request_id = r.clm_int_id
            """

        cursor = self.connection.cursor()

        cursor.execute(selectStatement)

        results = [dict(zip([column[0] for column in cursor.description], row))
                for row in cursor.fetchall()]

        return results
        
    def deleteRequests(self, requestIds):

        parameters = ', '.join('?' * len(requestIds))

        deleteStatement = """
            DELETE FROM [dbo].[tbl_lineage_request]
            WHERE clm_int_id in (%s)
            """ % parameters

        cursor = self.connection.cursor()
        cursor.execute(deleteStatement, requestIds)

        self.connection.commit()