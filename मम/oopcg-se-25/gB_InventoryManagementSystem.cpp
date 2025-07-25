#include <iostream>
#include <iomanip>
#include <limits>
#include <string>
#include <vector>

struct Product {
    int id;
    std::string name;
    double cost_price;
    double sell_price;
    int stock;
};

class Inventory {
    std::vector<Product> products_;
    double profit_{};

  public:
    void addProduct(const Product &p) { products_.push_back(p); }

    Product *getProductById(int id) {
        for (auto &p : products_)
            if (p.id == id) return &p;
        return nullptr;
    }

    void listProducts() const {
        std::cout << "\nID  Name                Cost  Sell  Stock\n";
        for (const auto &p : products_) {
            std::cout << std::setw(3) << p.id << "  " << std::setw(18) << p.name << "  "
                      << std::setw(5) << p.cost_price << "  " << std::setw(5) << p.sell_price << "  "
                      << std::setw(5) << p.stock << "\n";
        }
    }

    void purchase(int id, int qty) {
        auto *p = getProductById(id);
        if (!p) {
            std::cout << "Product not found.\n";
            return;
        }
        p->stock += qty;
        profit_ -= p->cost_price * qty; // Spending reduces profit
        std::cout << "Purchased and stocked " << qty << " units.\n";
    }

    void ship(int id, int qty) {
        auto *p = getProductById(id);
        if (!p || p->stock < qty) {
            std::cout << "Not enough stock.\n";
            return;
        }
        p->stock -= qty;
        profit_ += p->sell_price * qty - p->cost_price * qty;
        std::cout << "Shipped " << qty << " units.\n";
    }

    void showProduct(int id) const {
        for (const auto &p : products_) {
            if (p.id == id) {
                std::cout << "\nProduct details:\nID           : " << p.id << "\nName         : " << p.name
                          << "\nCost price   : $" << p.cost_price << "\nSell price   : $" << p.sell_price
                          << "\nCurrent stock: " << p.stock << "\n";
                return;
            }
        }
        std::cout << "Product not found.\n";
    }

    void showProfit() const { std::cout << "Current net profit: $" << profit_ << "\n"; }
};

static void clearCin() {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

int main() {
    Inventory inv;
    // Seed with some products
    inv.addProduct({1, "Laptop", 500, 700, 10});
    inv.addProduct({2, "Phone", 200, 350, 25});
    inv.addProduct({3, "Headphones", 20, 30, 50});

    int choice;
    while (true) {
        std::cout << "\n===== Inventory Management =====\n";
        std::cout << "1. List all products\n2. Display product info\n3. Purchase (stock in)\n4. Shipping (stock out)\n5. Display net profit\n0. Exit\nSelect: ";
        if (!(std::cin >> choice)) {
            clearCin();
            continue;
        }

        if (choice == 0) break;

        switch (choice) {
            case 1:
                inv.listProducts();
                break;
            case 2: {
                int id;
                std::cout << "Enter product ID: ";
                std::cin >> id;
                inv.showProduct(id);
                break;
            }
            case 3: {
                int id, qty;
                std::cout << "Enter product ID: ";
                std::cin >> id;
                std::cout << "Quantity: ";
                std::cin >> qty;
                inv.purchase(id, qty);
                break;
            }
            case 4: {
                int id, qty;
                std::cout << "Enter product ID: ";
                std::cin >> id;
                std::cout << "Quantity: ";
                std::cin >> qty;
                inv.ship(id, qty);
                break;
            }
            case 5:
                inv.showProfit();
                break;
            default:
                std::cout << "Invalid option.\n";
        }
    }

    return 0;
}
