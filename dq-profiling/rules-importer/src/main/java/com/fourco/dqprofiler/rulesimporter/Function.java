package com.fourco.dqprofiler.rulesimporter;

import java.util.Optional;
import java.util.logging.Logger;

import com.microsoft.azure.functions.ExecutionContext;
import com.microsoft.azure.functions.HttpMethod;
import com.microsoft.azure.functions.HttpRequestMessage;
import com.microsoft.azure.functions.HttpResponseMessage;
import com.microsoft.azure.functions.HttpStatus;
import com.microsoft.azure.functions.annotation.AuthorizationLevel;
import com.microsoft.azure.functions.annotation.FunctionName;
import com.microsoft.azure.functions.annotation.HttpTrigger;

public class Function {
    @FunctionName("UpdateDQRules")
    public HttpResponseMessage run(
            @HttpTrigger(name = "req", methods = {HttpMethod.GET, HttpMethod.POST}, authLevel = AuthorizationLevel.ANONYMOUS) HttpRequestMessage<Optional<String>> request,
            final ExecutionContext context) {
            
        Logger logger = context.getLogger();

        logger.info("Update DQ Rules processed a request");
        
        //get app settings
        String username=System.getenv("jdbc-user");
        logger.info("jdbc-user: " + username);
        
        String password=System.getenv("jdbc-password");
        logger.info("jdbc-password: " + password);
        
        String jdbcUri=System.getenv("jdbc-uri");
        logger.info("jdbc-uri: " + jdbcUri);
        
        String connString = jdbcUri + ";user=" + username + ";password=" + password;
        
        return request.createResponseBuilder(HttpStatus.OK).body("Hello, " + connString).build();
    }    
}
