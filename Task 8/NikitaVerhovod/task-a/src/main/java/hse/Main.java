package hse;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        KWICSystem kwic = new KWICSystem();

//        kwic.addLine("Design is the process");
//        kwic.addLine("Software engineering principles");
//        kwic.addLine("Structured programming methodology");

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(
                KWICSystem.class.getClassLoader().getResourceAsStream("input.txt")))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (!line.trim().isEmpty()) {
                    kwic.addLine(line.trim());
                }
            }
        } catch (IOException e) {
            System.out.println("Ошибка при чтении файла: " + e.getMessage());
        }

        kwic.generateCircularShifts();
        kwic.sortShifts();
        kwic.printShifts();
    }
}

