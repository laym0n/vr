package com.victor.kochnev.a.filters;

import java.io.EOFException;
import java.util.Arrays;

public class NoiseWordRemoval extends Filter {

    protected static final String[] noise = {"the", "and", "a", "to", "of", "in",
            "i", "is", "that", "it", "on", "you", "this", "for", "but", "with",
            "are", "have", "be", "at", "or", "as", "was", "so", "if", "out",
            "not",};

    @Override
    public void run() {
        while (true) {
            try {
                String s = read();
                String[] tokens = s.split("\\s");

                if (Arrays.asList(noise).contains(tokens[0].toLowerCase()))
                    continue;

                write(s);

            } catch (EOFException e) {
                write(null);
                break;
            }
        }
    }

}
