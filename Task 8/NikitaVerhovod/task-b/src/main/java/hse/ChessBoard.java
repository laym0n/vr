package hse;

import java.util.Arrays;

public class ChessBoard {
    private final int[] board;

    public ChessBoard(int size) {
        this.board = new int[size];
        Arrays.fill(board, -1);
    }

    public int getSize() {
        return board.length;
    }

    public void placeQueen(int row, int col) {
        board[row] = col;
    }

    public void removeQueen(int row) {
        board[row] = -1;
    }

    public boolean isSafe(int row, int col) {
        for (int r = 0; r < row; r++) {
            int c = board[r];
            if (c == col || Math.abs(c - col) == Math.abs(r - row)) {
                return false;
            }
        }
        return true;
    }

    public void print() {
        System.out.println("Board Configuration:");
        for (int k : board) {
            for (int j = 0; j < board.length; j++) {
                System.out.print((k == j ? "Q" : ".") + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
