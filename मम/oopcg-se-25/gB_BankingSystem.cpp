#include <iostream>
#include <iomanip>
#include <limits>
#include <string>
#include <vector>
#include <ctime>

struct Transaction {
    std::time_t ts;
    std::string type;
    double amount;
    double balance_after;
};

class Account {
  private:
    static constexpr double kDailyLimit = 5000.0; // Daily withdrawal limit
    int account_no_;
    std::string holder_name_;
    double balance_{};
    std::vector<Transaction> passbook_;

    double withdrawn_today_{};
    std::time_t last_withdraw_day_{};

    static int generateAccountNo() {
        static int next = 1001;
        return next++;
    }

    void addTransaction(const std::string &type, double amount) {
        passbook_.push_back({std::time(nullptr), type, amount, balance_});
    }

    static bool isSameDay(std::time_t a, std::time_t b) {
        std::tm tm_a = *std::localtime(&a);
        std::tm tm_b = *std::localtime(&b);
        return tm_a.tm_year == tm_b.tm_year && tm_a.tm_yday == tm_b.tm_yday;
    }

  public:
    Account(std::string name, double initial) : account_no_(generateAccountNo()), holder_name_(std::move(name)), balance_(initial) {
        addTransaction("OPEN", initial);
    }

    void deposit(double amt) {
        balance_ += amt;
        addTransaction("DEPOSIT", amt);
    }

    bool withdraw(double amt) {
        std::time_t now = std::time(nullptr);
        if (!isSameDay(now, last_withdraw_day_)) {
            withdrawn_today_ = 0;
            last_withdraw_day_ = now;
        }

        if (amt > balance_) {
            std::cerr << "Insufficient balance.\n";
            return false;
        }
        if (withdrawn_today_ + amt > kDailyLimit) {
            std::cerr << "Daily withdrawal limit exceeded.\n";
            return false;
        }

        balance_ -= amt;
        withdrawn_today_ += amt;
        addTransaction("WITHDRAW", amt);
        return true;
    }

    double balance() const { return balance_; }

    void printInfo() const {
        std::cout << "Account No : " << account_no_ << "\nName       : " << holder_name_ << "\nBalance    : $" << std::fixed << std::setprecision(2) << balance_ << "\n";
    }

    void printPassbook() const {
        std::cout << "\n--- Passbook ---\n";
        for (const auto &t : passbook_) {
            std::tm tm = *std::localtime(&t.ts);
            char buf[25];
            std::strftime(buf, sizeof(buf), "%Y-%m-%d %H:%M:%S", &tm);
            std::cout << buf << " | " << std::setw(8) << t.type << " | " << std::setw(10) << t.amount << " | Bal: " << t.balance_after << "\n";
        }
    }

    void printPassbook(std::time_t from, std::time_t to) const {
        std::cout << "\n--- Passbook from to ---\n";
        for (const auto &t : passbook_) {
            if (t.ts >= from && t.ts <= to) {
                std::tm tm = *std::localtime(&t.ts);
                char buf[25];
                std::strftime(buf, sizeof(buf), "%Y-%m-%d %H:%M:%S", &tm);
                std::cout << buf << " | " << std::setw(8) << t.type << " | " << std::setw(10) << t.amount << " | Bal: " << t.balance_after << "\n";
            }
        }
    }
};

static void clearCin() {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

int main() {
    Account *account = nullptr;
    int option;
    while (true) {
        std::cout << "\n===== Banking System =====\n";
        std::cout << "1. Create account\n2. Deposit\n3. Withdraw\n4. Check balance\n5. Display account info\n6. Passbook print\n0. Exit\nSelect: ";
        if (!(std::cin >> option)) {
            clearCin();
            continue;
        }

        if (option == 0)
            break;

        if (!account && option != 1) {
            std::cout << "Please create an account first.\n";
            continue;
        }

        switch (option) {
            case 1: {
                std::string name;
                double initial;
                std::cout << "Enter name: ";
                clearCin();
                std::getline(std::cin, name);
                std::cout << "Initial deposit: $";
                std::cin >> initial;
                account = new Account(name, initial);
                std::cout << "Account created successfully!\n";
                break;
            }
            case 2: {
                double amt;
                std::cout << "Deposit amount: $";
                std::cin >> amt;
                account->deposit(amt);
                std::cout << "Deposited successfully.\n";
                break;
            }
            case 3: {
                double amt;
                std::cout << "Withdraw amount: $";
                std::cin >> amt;
                account->withdraw(amt);
                break;
            }
            case 4: {
                std::cout << "Current balance: $" << std::fixed << std::setprecision(2) << account->balance() << "\n";
                break;
            }
            case 5: {
                account->printInfo();
                break;
            }
            case 6: {
                std::cout << "Print full passbook? (y/n): ";
                char yn;
                std::cin >> yn;
                if (yn == 'y' || yn == 'Y') {
                    account->printPassbook();
                } else {
                    std::cout << "Enter 'from' timestamp (epoch): ";
                    std::time_t from, to;
                    std::cin >> from;
                    std::cout << "Enter 'to' timestamp (epoch): ";
                    std::cin >> to;
                    account->printPassbook(from, to);
                }
                break;
            }
            default:
                std::cout << "Invalid option.\n";
        }
    }

    delete account;
    return 0;
}
