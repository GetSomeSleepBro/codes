import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Banking system demonstration written in Java, mirroring the Group-C C++
 * assignment but fully object-oriented in Java.
 */
public class gB_BankingSystem {

    private static final Scanner scanner = new Scanner(System.in);

    /* -------------------------- Model classes -------------------------- */

    private static class Transaction {
        LocalDateTime timestamp;
        String type;
        double amount;
        double balanceAfter;

        Transaction(String type, double amount, double balanceAfter) {
            this.timestamp = LocalDateTime.now();
            this.type = type;
            this.amount = amount;
            this.balanceAfter = balanceAfter;
        }
    }

    private static class Account {
        private static final double DAILY_LIMIT = 5_000;
        private static final AtomicInteger NEXT_ACC_NO = new AtomicInteger(1001);

        private final int accNo;
        private final String holder;
        private double balance;
        private final List<Transaction> passbook = new ArrayList<>();

        /* Tracking daily withdrawal */
        private LocalDate lastWithdrawDate = null;
        private double withdrawnToday = 0;

        Account(String holder, double initial) {
            this.accNo = NEXT_ACC_NO.getAndIncrement();
            this.holder = holder;
            this.balance = initial;
            addTxn("OPEN", initial);
        }

        void deposit(double amt) {
            balance += amt;
            addTxn("DEPOSIT", amt);
        }

        boolean withdraw(double amt) {
            LocalDate today = LocalDate.now();
            if (!today.equals(lastWithdrawDate)) {
                withdrawnToday = 0;
                lastWithdrawDate = today;
            }

            if (amt > balance) {
                System.out.println("Insufficient balance.");
                return false;
            }
            if (withdrawnToday + amt > DAILY_LIMIT) {
                System.out.println("Daily withdrawal limit exceeded.");
                return false;
            }

            balance -= amt;
            withdrawnToday += amt;
            addTxn("WITHDRAW", amt);
            return true;
        }

        double getBalance() { return balance; }

        void printInfo() {
            System.out.printf("Account No : %d%nName       : %s%nBalance    : $%.2f%n", accNo, holder, balance);
        }

        void printPassbook() {
            printPassbook(LocalDateTime.MIN, LocalDateTime.MAX);
        }

        void printPassbook(LocalDateTime from, LocalDateTime to) {
            DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
            System.out.println("\n--- Passbook ---");
            passbook.stream()
                    .filter(t -> !t.timestamp.isBefore(from) && !t.timestamp.isAfter(to))
                    .forEach(t -> System.out.printf("%s | %8s | %10.2f | Bal: %.2f%n",
                            t.timestamp.format(fmt), t.type, t.amount, t.balanceAfter));
        }

        private void addTxn(String type, double amt) {
            passbook.add(new Transaction(type, amt, balance));
        }
    }

    /* --------------------------- Main driver --------------------------- */

    public static void main(String[] args) {
        Account account = null;
        while (true) {
            System.out.println("\n===== Banking System =====");
            System.out.println("1. Create account\n2. Deposit\n3. Withdraw\n4. Check balance\n5. Display account info\n6. Passbook print\n0. Exit");
            System.out.print("Select: ");
            int choice = readInt();

            if (choice == 0) break;

            if (account == null && choice != 1) {
                System.out.println("Please create an account first.");
                continue;
            }

            switch (choice) {
                case 1 -> account = createAccount();
                case 2 -> {
                    System.out.print("Deposit amount: $");
                    double amt = readDouble();
                    account.deposit(amt);
                }
                case 3 -> {
                    System.out.print("Withdraw amount: $");
                    double amt = readDouble();
                    account.withdraw(amt);
                }
                case 4 -> System.out.printf("Current balance: $%.2f%n", account.getBalance());
                case 5 -> account.printInfo();
                case 6 -> printPassbookMenu(account);
                default -> System.out.println("Invalid option.");
            }
        }
        System.out.println("Good-bye!");
    }

    private static Account createAccount() {
        System.out.print("Enter name: ");
        String name = scanner.nextLine();
        if (name.isEmpty()) name = scanner.nextLine(); // flush if earlier newline
        System.out.print("Initial deposit: $");
        double initial = readDouble();
        System.out.println("Account created successfully!");
        return new Account(name, initial);
    }

    private static void printPassbookMenu(Account account) {
        System.out.print("Print full passbook? (y/n): ");
        String yn = scanner.next();
        if (yn.equalsIgnoreCase("y")) {
            account.printPassbook();
        } else {
            System.out.print("From (yyyy-MM-dd HH:mm): ");
            LocalDateTime from = readDateTime();
            System.out.print("To   (yyyy-MM-dd HH:mm): ");
            LocalDateTime to = readDateTime();
            account.printPassbook(from, to);
        }
    }

    /* ------------------------- Helper methods ------------------------- */

    private static int readInt() {
        while (!scanner.hasNextInt()) {
            System.out.print("Invalid, re-enter: ");
            scanner.next();
        }
        return scanner.nextInt();
    }

    private static double readDouble() {
        while (!scanner.hasNextDouble()) {
            System.out.print("Invalid, re-enter: $");
            scanner.next();
        }
        return scanner.nextDouble();
    }

    private static LocalDateTime readDateTime() {
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        while (true) {
            String s = scanner.next() + (scanner.hasNext() ? " " + scanner.next() : "");
            try {
                return LocalDateTime.parse(s, fmt);
            } catch (Exception e) {
                System.out.print("Invalid format, try again: ");
            }
        }
    }
}
