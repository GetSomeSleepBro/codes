import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Inventory Management System in Java (mirror of Group-C assignment).
 */
public class gB_InventoryManagementSystem {

    /* -------------------------- Model classes -------------------------- */

    private static class Product {
        int id;
        String name;
        double costPrice;
        double sellPrice;
        int stock;

        Product(int id, String name, double costPrice, double sellPrice, int stock) {
            this.id = id;
            this.name = name;
            this.costPrice = costPrice;
            this.sellPrice = sellPrice;
            this.stock = stock;
        }
    }

    private static class Inventory {
        private final List<Product> products = new ArrayList<>();
        private double profit = 0;

        void addProduct(Product p) { products.add(p); }

        Product find(int id) {
            return products.stream().filter(p -> p.id == id).findFirst().orElse(null);
        }

        void listProducts() {
            System.out.printf("%n%-4s %-18s %-6s %-6s %-6s%n", "ID", "Name", "Cost", "Sell", "Stock");
            for (Product p : products) {
                System.out.printf("%-4d %-18s %-6.2f %-6.2f %-6d%n", p.id, p.name, p.costPrice, p.sellPrice, p.stock);
            }
        }

        void showProduct(int id) {
            Product p = find(id);
            if (p == null) {
                System.out.println("Product not found.");
                return;
            }
            System.out.printf("%nProduct details:%nID           : %d%nName         : %s%nCost price   : $%.2f%nSell price   : $%.2f%nCurrent stock: %d%n", p.id, p.name, p.costPrice, p.sellPrice, p.stock);
        }

        void purchase(int id, int qty) {
            Product p = find(id);
            if (p == null) {
                System.out.println("Product not found.");
                return;
            }
            p.stock += qty;
            profit -= p.costPrice * qty;
            System.out.println("Purchased and stocked " + qty + " units.");
        }

        void ship(int id, int qty) {
            Product p = find(id);
            if (p == null || p.stock < qty) {
                System.out.println("Not enough stock.");
                return;
            }
            p.stock -= qty;
            profit += (p.sellPrice - p.costPrice) * qty;
            System.out.println("Shipped " + qty + " units.");
        }

        void showProfit() {
            System.out.printf("Current net profit: $%.2f%n", profit);
        }
    }

    /* --------------------------- Main driver -------------------------- */

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Inventory inv = new Inventory();
        // Seed initial products
        inv.addProduct(new Product(1, "Laptop", 500, 700, 10));
        inv.addProduct(new Product(2, "Phone", 200, 350, 25));
        inv.addProduct(new Product(3, "Headphones", 20, 30, 50));

        while (true) {
            System.out.println("\n===== Inventory Management =====");
            System.out.println("1. List all products\n2. Display product info\n3. Purchase (stock in)\n4. Shipping (stock out)\n5. Display net profit\n0. Exit");
            System.out.print("Select: ");
            int choice = readInt();

            if (choice == 0) break;

            switch (choice) {
                case 1 -> inv.listProducts();
                case 2 -> {
                    System.out.print("Enter product ID: ");
                    inv.showProduct(readInt());
                }
                case 3 -> {
                    System.out.print("Enter product ID: ");
                    int id = readInt();
                    System.out.print("Quantity: ");
                    int qty = readInt();
                    inv.purchase(id, qty);
                }
                case 4 -> {
                    System.out.print("Enter product ID: ");
                    int id = readInt();
                    System.out.print("Quantity: ");
                    int qty = readInt();
                    inv.ship(id, qty);
                }
                case 5 -> inv.showProfit();
                default -> System.out.println("Invalid option.");
            }
        }
        System.out.println("Good-bye!");
    }

    /* ------------------------- Helper method ------------------------- */
    private static int readInt() {
        while (!scanner.hasNextInt()) {
            System.out.print("Invalid, re-enter: ");
            scanner.next();
        }
        return scanner.nextInt();
    }
}
