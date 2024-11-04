package com.victor.kochnev.a.filters;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;

public class Pump extends Filter {

    private final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    @Override
    public void run() {
        try {
            String read;
            while (true) {
                read = reader.readLine();
                if (Objects.equals(read, "")) {
                    write(null);
                    break;
                }
                write(read + "\n");
            }
        } catch (IOException e) {
            System.err.println("IOException caught in Filter::StandardIn");
        }
    }

}
