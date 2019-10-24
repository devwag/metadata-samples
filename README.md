# Metadata - Lineage - DQ  framework

The meta-data manager built on Apache Atlas (ADC V2 compatible) will store the following information:
1.	Business metadata: These are business terms and glossaries that will be defined by the data stewards in Walmart Inc in Collibra. A third party software purchased by Walmart and deployed on premise.
2.	Technical metadata: Technical metadata will be used by devs and applications to discover & explore datasets and will consist of the following hierarchy of information:
a.	Table name/Dataset names 
    i.	Description 
    ii.	Entity Details
    iii.	Columns
          - Description
          - DQ Rules
          - DQ Metrics
4.	Tags: Storing information like Classification, ODS zone
iv.	Last updated date timestamp
v.	Cold/Hot (to be explored if this can be excluded from Milestone 1) 
3.	Lineage – use the Apache Atlas Lineage structure to:

a.	Lineage of each of the datasets created or copied over from source
b.	Include the lineage on KPIs , with details around which specific columns/processes go into calculation of the KPI
c.	Store the PBI dashboard details that the KPIs are displayed
