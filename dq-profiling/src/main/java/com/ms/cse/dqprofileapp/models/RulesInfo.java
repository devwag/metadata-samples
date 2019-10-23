package com.ms.cse.dqprofileapp.models;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.sql.Timestamp;

@Entity
@Table(name = "DQ_RULESINFO")
public class RulesInfo {

    @Id
    private String ruleId;
    private String ruleName;
    private String dimension;
    private String columnName;

    @Column(name = "Rule Description")
    private String ruleDescription;

    @Column(name = "Business Rule Name")
    private String businessRuleName;

    @Column(name = "Update Timestamp")
    private Timestamp updateTimestamp;
    private String ruleType;

    @Column(name = "TABLE_FQDN")
    private String tableFQDN;

    @Column(name = "COLUMN_FQDN")
    private String columnFQDN;
    private String tableName;
    private String ruleDefinition;
    private String rulePriority;


    public String getRuleId() {
        return ruleId;
    }

    public void setRuleId(String ruleId) {
        this.ruleId = ruleId;
    }

    public String getRuleName() {
        return ruleName;
    }

    public void setRuleName(String ruleName) {
        this.ruleName = ruleName;
    }

    public String getDimension() {
        return dimension;
    }

    public void setDimension(String dimension) {
        this.dimension = dimension;
    }

    public String getColumnName() {
        return columnName;
    }

    public void setColumnName(String columnName) {
        this.columnName = columnName;
    }

    public String getRuleDefinition() {
        return ruleDefinition;
    }

    public void setRuleDefinition(String ruleDefinition) {
        this.ruleDefinition = ruleDefinition;
    }

    public String getRuleDescription() {
        return ruleDescription;
    }

    public void setRuleDescription(String ruleDescription) {
        this.ruleDescription = ruleDescription;
    }

    public String getBusinessRuleName() {
        return businessRuleName;
    }

    public void setBusinessRuleName(String businessRuleName) {
        this.businessRuleName = businessRuleName;
    }

    public Timestamp getUpdateTimestamp() {
        return updateTimestamp;
    }

    public void setUpdateTimestamp(Timestamp updateTimestamp) {
        this.updateTimestamp = updateTimestamp;
    }

    public String getRuleType() {
        return ruleType;
    }

    public void setRuleType(String ruleType) {
        this.ruleType = ruleType;
    }

    public String getTableFQDN() {
        return tableFQDN;
    }

    public void setTableFQDN(String tableFQDN) {
        this.tableFQDN = tableFQDN;
    }

    public String getColumnFQDN() {
        return columnFQDN;
    }

    public void setColumnFQDN(String columnFQDN) {
        this.columnFQDN = columnFQDN;
    }

    public String getTableName() {
        return tableName;
    }

    public void setTableName(String tableName) {
        this.tableName = tableName;
    }

    public String getRulePriority() {
        return rulePriority;
    }

    public void setRulePriority(String rulePriority) {
        this.rulePriority = rulePriority;
    }
}

