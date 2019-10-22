package com.ms.cse.dqprofileapp.cloudfunctions;

import com.ms.cse.dqprofileapp.extensions.TimestampExtension;
import com.ms.cse.dqprofileapp.models.EntityScore;
import com.ms.cse.dqprofileapp.repositories.EntityScoreRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

import java.sql.Timestamp;
import java.util.List;
import java.util.function.Function;

@Component
public class GetCurrentEntityScores {
    @Autowired
    private EntityScoreRepository entityScoreRepository;

    @Bean
    public Function<Timestamp, List<EntityScore>> getCurrentEntityScores() {
        return waterMarkDate -> {
            List<EntityScore> entityScores = entityScoreRepository.findByUpdatedBetweenOrderByUpdatedDesc(waterMarkDate, TimestampExtension.now());
            return entityScores;
        };
    }
}
