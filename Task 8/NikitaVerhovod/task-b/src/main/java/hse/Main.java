package hse;

public class Main {
    public static void main(String[] args) {
        int boardSize = 8;
        ChessBoard board = new ChessBoard(boardSize);
        QueenSolver solver = new QueenSolver(board);

        solver.solve();
    }
}
