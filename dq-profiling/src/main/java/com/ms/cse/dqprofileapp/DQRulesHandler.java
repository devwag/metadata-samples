package com.ms.cse.dqprofileapp;

import com.microsoft.azure.functions.ExecutionContext;
import com.microsoft.azure.functions.annotation.FunctionName;
import com.microsoft.azure.functions.annotation.TimerTrigger;
import com.ms.cse.dqprofileapp.extensions.TimestampExtension;
import com.ms.cse.dqprofileapp.models.EntityScore;
import com.ms.cse.dqprofileapp.models.ScheduleStatus;
import org.springframework.cloud.function.adapter.azure.AzureSpringBootRequestHandler;
import org.springframework.context.annotation.ComponentScan;

import java.sql.Timestamp;
import java.util.List;

@ComponentScan(basePackages={"com.ms.cse.dqprofileapp"})
public class DQRulesHandler extends AzureSpringBootRequestHandler<Integer, Integer> {

    @FunctionName("getDQRules")
    public Integer execute(
            @TimerTrigger(name = "getDQRulesTrigger", schedule = "0 */2 * * * *") String timerInfo,
            ExecutionContext context) {

        // Use getLast() from scheduleStatus
        ScheduleStatus scheduleStatus = ScheduleStatus.Deserialize(timerInfo);

        return 0;
    }
}