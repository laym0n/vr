package com.victor.kochnev.a.filters;

import java.io.EOFException;
import java.util.concurrent.ConcurrentSkipListSet;

public class SortList extends Filter {

    private final ConcurrentSkipListSet<String> buffer = new ConcurrentSkipListSet<>(String.CASE_INSENSITIVE_ORDER);

    @Override
    public void run() {
        while (true) {
            try {
                String s = read();
                buffer.add(s);
            } catch (EOFException e) {
                break;
            }
        }

        while (!buffer.isEmpty())
            write(buffer.pollFirst());

        write(null);
    }

}
