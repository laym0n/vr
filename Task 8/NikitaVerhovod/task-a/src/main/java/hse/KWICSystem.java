package hse;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class KWICSystem {
    private final List<String> lines;
    private final List<String> circularShifts;

    public KWICSystem() {
        this.lines = new ArrayList<>();
        this.circularShifts = new ArrayList<>();
    }

    public void loadLinesFromFile(String filename) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (!line.trim().isEmpty()) { // Игнорируем пустые строки
                    addLine(line.trim());
                }
            }
        }
    }

    public void addLine(String line) {
        lines.add(line);
    }

    public void generateCircularShifts() {
        for (String line : lines) {
            createCircularShifts(line);
        }
    }

    private void createCircularShifts(String line) {
        String[] words = line.split(" ");
        int wordCount = words.length;

        for (int i = 0; i < wordCount; i++) {
            StringBuilder shift = new StringBuilder();
            for (int j = 0; j < wordCount; j++) {
                shift.append(words[(i + j) % wordCount]).append(" ");
            }
            circularShifts.add(shift.toString().trim());
        }
    }

    public void sortShifts() {
        Collections.sort(circularShifts);
    }

    public void printShifts() {
        System.out.println("KWIC Index:");
        for (String shift : circularShifts) {
            System.out.println(shift);
        }
    }
}
