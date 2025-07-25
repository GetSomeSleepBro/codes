import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * A robust console-based calculator that repeatedly prompts the user for two
 * operands and an operator until they decide to quit.  It demonstrates the
 * use of conditional branching, looping constructs and basic exception
 * handling.
 */
public class Calculator {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("===== Simple Java Calculator =====\n" +
                "Enter expressions in the form: <number> <operator> <number>." +
                "\nSupported operators: +  -  *  /  %\nType 'exit' at any time to quit.\n");

        while (true) {
            try {
                System.out.print("First operand  : ");
                String firstToken = scanner.next();
                if (firstToken.equalsIgnoreCase("exit")) {
                    break;
                }
                double a = Double.parseDouble(firstToken);

                System.out.print("Operator (+,-,*,/,%) : ");
                String op = scanner.next();
                if (op.equalsIgnoreCase("exit")) {
                    break;
                }

                System.out.print("Second operand : ");
                String secondToken = scanner.next();
                if (secondToken.equalsIgnoreCase("exit")) {
                    break;
                }
                double b = Double.parseDouble(secondToken);

                double result = calculate(a, b, op);
                System.out.printf("Result         : %.4f%n", result);
            } catch (NumberFormatException e) {
                System.err.println("Invalid number entered. Please try again.\n");
            } catch (IllegalArgumentException e) {
                System.err.println(e.getMessage() + "\n");
            } catch (ArithmeticException e) {
                System.err.println("Math error: " + e.getMessage() + "\n");
            }
        }

        System.out.println("Good-bye!");
    }

    private static double calculate(double a, double b, String op) {
        return switch (op) {
            case "+" -> a + b;
            case "-" -> a - b;
            case "*" -> a * b;
            case "/" -> {
                if (b == 0) throw new ArithmeticException("Division by zero");
                yield a / b;
            }
            case "%" -> {
                if (b == 0) throw new ArithmeticException("Division by zero");
                yield a % b;
            }
            default -> throw new IllegalArgumentException("Unsupported operator: " + op);
        };
    }
}
