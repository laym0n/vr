package com.victor.kochnev.a.filters;

import java.io.EOFException;

public abstract class Filter implements Runnable {

    protected Pipe in;
    protected Pipe out;

    protected void setIn(Pipe p) {
        in = p;
    }

    protected void setOut(Pipe p) {
        out = p;
    }

    protected void write(String s) {
        if (s == null) {
            out.close();
            return;
        }
        out.write(s);
    }

    protected String read() throws EOFException {
        return in.read();
    }

}
