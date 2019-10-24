# Metadata - Lineage - DQ  framework

The meta-data manager built on Apache Atlas (ADC V2 compatible) will store the following information:
1.	Business metadata: These are business terms and glossaries that will be defined by the data stewards in Walmart Inc in Collibra. A third party software purchased by Walmart and deployed on premise.
2.	Technical metadata: Technical metadata will be used by devs and applications to discover & explore datasets and will consist of the following hierarchy of information:
    1. Table name/Dataset names
        1. Description
        2. Entity Details
        3. Columns
            - Description
            - DQ Rules
            - DQ Metrics
	        - Tags: Storing information like Classification, ODS zone
    2. Last updated date timestamp
    
3.	Lineage – use the Apache Atlas Lineage structure to:
    1.	Lineage of each of the datasets created or copied over from source
    2.	Include the lineage on KPIs , with details around which specific columns/processes go into calculation of the KPI
    3.	Store the PBI dashboard details that the KPIs are displayed
    
### Architecture diagram:

![Image of Architecture](https://github.com/devwag/metadata-samples/blob/master/images/GBS-ODS-MetaDataFramework.JPG)
