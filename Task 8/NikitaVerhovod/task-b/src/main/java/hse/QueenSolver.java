package hse;

public class QueenSolver {
    private final ChessBoard board;

    public QueenSolver(ChessBoard board) {
        this.board = board;
    }

    public void solve() {
        if (placeQueen(0)) {
            board.print();
        } else {
            System.out.println("No solution. Fail.");
        }
    }

    private boolean placeQueen(int row) {
        if (row == board.getSize()) {
            return true;
        }

        for (int col = 0; col < board.getSize(); col++) {
            if (board.isSafe(row, col)) {
                board.placeQueen(row, col);
                if (placeQueen(row + 1)) {
                    return true;
                }
                board.removeQueen(row);
            }
        }
        return false;
    }
}
