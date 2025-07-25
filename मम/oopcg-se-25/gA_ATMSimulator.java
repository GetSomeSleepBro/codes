import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * A console ATM simulator demonstrating custom exception handling using
 * standard exceptions.  ArithmeticException denotes insufficient funds, while
 * IllegalArgumentException denotes invalid user input.
 */
public class ATMSimulator {

    private static final Scanner scanner = new Scanner(System.in);
    private static double balance = 1_000.00;  // Initial balance

    public static void main(String[] args) {
        System.out.println("===== ATM Simulator =====");
        boolean exit = false;
        while (!exit) {
            printMenu();
            try {
                int choice = Integer.parseInt(scanner.next());
                switch (choice) {
                    case 1 -> showBalance();
                    case 2 -> withdraw();
                    case 3 -> deposit();
                    case 0 -> exit = true;
                    default -> throw new IllegalArgumentException("Invalid menu option");
                }
            } catch (IllegalArgumentException e) {
                System.err.println("Error: " + e.getMessage());
            } finally {
                System.out.println();
            }
        }
        System.out.println("Thank you for banking with us!");
    }

    private static void printMenu() {
        System.out.println("1. Check balance");
        System.out.println("2. Withdraw cash");
        System.out.println("3. Deposit cash");
        System.out.println("0. Exit");
        System.out.print("Select: ");
    }

    private static void showBalance() {
        System.out.printf("Current balance: $%.2f%n", balance);
    }

    private static void withdraw() {
        System.out.print("Enter amount to withdraw: $");
        double amount = readDouble();
        try {
            if (amount <= 0) {
                throw new IllegalArgumentException("Amount must be positive");
            }
            if (amount > balance) {
                throw new ArithmeticException("Insufficient funds");
            }
            balance -= amount;
            System.out.printf("Please take your cash. New balance: $%.2f%n", balance);
        } catch (ArithmeticException | IllegalArgumentException e) {
            System.err.println("Transaction failed: " + e.getMessage());
        }
    }

    private static void deposit() {
        System.out.print("Enter amount to deposit: $");
        double amount = readDouble();
        try {
            if (amount <= 0) {
                throw new IllegalArgumentException("Amount must be positive");
            }
            balance += amount;
            System.out.printf("Deposit successful. New balance: $%.2f%n", balance);
        } catch (IllegalArgumentException e) {
            System.err.println("Transaction failed: " + e.getMessage());
        }
    }

    private static double readDouble() {
        while (true) {
            try {
                return Double.parseDouble(scanner.next());
            } catch (NumberFormatException e) {
                System.err.print("Invalid number, please try again: $");
            }
        }
    }
}
