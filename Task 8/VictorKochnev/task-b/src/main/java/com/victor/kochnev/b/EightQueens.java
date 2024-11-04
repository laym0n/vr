package com.victor.kochnev.b;

import java.util.Arrays;

public class EightQueens {
    private static final int SIZE = 8;
    private final int[] queens = new int[SIZE];

    public EightQueens() {
        Arrays.fill(queens, -1);
    }

    public void solve() {
        if (placeQueens(0)) {
            printBoard();
        } else {
            System.out.println("Нет решений.");
        }
    }

    private boolean placeQueens(int row) {
        if (row == SIZE) {
            return true;
        }
        for (int col = 0; col < SIZE; col++) {
            if (isSafe(row, col)) {
                queens[row] = col;
                if (placeQueens(row + 1)) {
                    return true;
                }
                queens[row] = -1;
            }
        }
        return false;
    }

    private boolean isSafe(int row, int col) {
        for (int i = 0; i < row; i++) {
            if (queens[i] == col || Math.abs(queens[i] - col) == Math.abs(i - row)) {
                return false;
            }
        }
        return true;
    }

    private void printBoard() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (queens[i] == j) {
                    System.out.print("Q ");
                } else {
                    System.out.print(". ");
                }
            }
            System.out.println();
        }
    }
}
