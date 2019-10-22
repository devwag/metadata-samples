package com.ms.cse.dqprofileapp.models;

import com.ms.cse.dqprofileapp.extensions.TimestampExtension;
import org.json.JSONObject;

import java.sql.Timestamp;

public class ScheduleStatus {
    private Timestamp last;
    private Timestamp next;
    private Timestamp lastUpdated;

    public Timestamp getLast() {
        return last;
    }

    public Timestamp getNext() {
        return next;
    }

    public Timestamp getLastUpdated() {
        return lastUpdated;
    }

    public void setLast(Timestamp last) {
        this.last = last;
    }

    public void setNext(Timestamp next) {
        this.next = next;
    }

    public void setLastUpdated(Timestamp lastUpdated) {
        this.lastUpdated = lastUpdated;
    }

    public static ScheduleStatus Deserialize(String json) {
        if(json != null && !json.isEmpty()) {
            JSONObject jo = new JSONObject(json);
            JSONObject scheduleStatusRoot = (JSONObject) jo.get("ScheduleStatus");

            ScheduleStatus scheduleStatus = new ScheduleStatus();
            scheduleStatus.setLast(TimestampExtension.fromISO8601(scheduleStatusRoot.get("Last").toString()));
            scheduleStatus.setNext(TimestampExtension.fromISO8601(scheduleStatusRoot.get("Next").toString()));
            scheduleStatus.setLastUpdated(TimestampExtension.fromISO8601(scheduleStatusRoot.get("LastUpdated").toString()));
            return scheduleStatus;
        } else {
            return new ScheduleStatus();
        }
    }
}
