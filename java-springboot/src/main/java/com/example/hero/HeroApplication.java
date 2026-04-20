package com.example.hero;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;
import java.util.HashMap;

@SpringBootApplication
@RestController
public class HeroApplication {

	public static void main(String[] args) {
		SpringApplication.run(HeroApplication.class, args);
	}

	@GetMapping("/healthz")
	public String health() {
		return "OK";
	}

	@GetMapping("/")
	public Map<String, String> hello() {
		Map<String, String> response = new HashMap<>();
		response.put("message", "Hello from Spring Boot!");
		response.put("platform", "Infra Heroes");
        response.put("log_level", System.getenv().getOrDefault("LOG_LEVEL", "info"));
		return response;
	}
}
