package com.ms.cse.dqprofileapp.models;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.sql.Timestamp;

@Entity
@Table(name = "dqscore")
public class EntityScore {
    @Id
    private int entityId;
    private int successfulRowCount;
    private int failureRowCount;
    private int totalRowCount;
    private Timestamp updated;

    public int getEntityId(){ return this.entityId; }
    public int getSuccessfulRowCount() { return this.successfulRowCount; }
    public int getFailureRowCount() { return this.failureRowCount; }
    public int getTotalRowCount() { return this.totalRowCount; }

    public Timestamp getUpdated() {
        return updated;
    }

    public void setEntityId(int entityId){
        this.entityId = entityId;
    }

    public void setSuccessfulRowCount(int successfulRowCount) {
        this.successfulRowCount = successfulRowCount;
    }

    public void setFailureRowCount(int failureRowCount) {
        this.failureRowCount = failureRowCount;
    }

    public void setTotalRowCount(int totalRowCount) {
        this.totalRowCount = totalRowCount;
    }

    public void setUpdated(Timestamp updated) {
        this.updated = updated;
    }
}
