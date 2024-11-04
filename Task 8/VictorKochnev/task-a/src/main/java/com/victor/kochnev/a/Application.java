package com.victor.kochnev.a;

import com.victor.kochnev.a.filters.*;

public class Application {
    public static void main(String[] args) {
        (new Pipeline(
                new Pump(),
                new CircularShifter(),
                new NoiseWordRemoval(),
                new SortList(),
                new Sink()
        )).run();
    }
}
