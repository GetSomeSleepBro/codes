# Sample Java & C++ Programs – Groups A & B

This repository contains a small collection of console–based example programs that cover fundamental OOP, multi-threading, exception handling and data-structure concepts.  The source files are grouped and prefixed as follows:

* **Group A (`gA_*`) – Java**  
  Assignment-style exercises demonstrating calculators, 2-D arrays, multiple inheritance via interfaces, exception handling with an ATM simulation, and basic multithreading.
* **Group B (`gB_*`) – C++ & Java**  
  Object-oriented “mini-projects” for a Banking System and an Inventory Management System provided *both* in C++ and Java for comparison.

## Directory Structure

```
java-codes/
├── gA_ATMSimulator.java              # ATM with robust exception handling
├── gA_Calculator.java                # Console calculator (+ – × ÷ %)
├── gA_HotelBookingSystem.java        # 2-D array room-booking demo
├── gA_MultiThreadedSimulation.java   # Multithreaded file-download mock-up
├── gA_MultipleInheritanceDemo.java   # Interfaces & polymorphism example
├── gB_BankingSystem.cpp              # Banking System in C++
├── gB_BankingSystem.java             # Banking System in Java
├── gB_InventoryManagementSystem.cpp  # Inventory System in C++
└── gB_InventoryManagementSystem.java # Inventory System in Java
```

## Prerequisites

* **Java 17+** – any recent JDK that supports `switch` expressions.  
* **C++17 compiler** – e.g. `g++` or `clang++`.

macOS users can install the command-line developer tools (`xcode-select --install`) to obtain `clang++`.  AdoptOpenJDK or Temurin provide free JDK builds.

## Building & Running

### Compile all Java sources

```bash
cd java-codes
javac *.java
```

Run a program (example: Calculator):

```bash
java gA_Calculator
```

Tip: compile/run only what you need, e.g. `javac gB_BankingSystem.java && java gB_BankingSystem`.

### Build the C++ programs

```bash
g++ -std=c++17 java-codes/gB_BankingSystem.cpp -o BankingSystem
g++ -std=c++17 java-codes/gB_InventoryManagementSystem.cpp -o InventorySystem
```

Execute them:

```bash
./BankingSystem
./InventorySystem
```

## Short Descriptions

### Group A

| Program | Purpose |
|---------|---------|
| `gA_Calculator` | Demonstrates user input parsing, looping, conditional logic, and exception handling for invalid input & divide-by-zero. |
| `gA_HotelBookingSystem` | Uses a 2-dimensional boolean array to manage room bookings across floors, with a simple menu. |
| `gA_MultipleInheritanceDemo` | Shows multiple-inheritance-style behaviour through Java interfaces (`Singer`, `Dancer`). |
| `gA_ATMSimulator` | ATM menu supporting balance check, withdraw & deposit. Uses `try–catch–finally`; throws `ArithmeticException` on insufficient funds, `IllegalArgumentException` on bad menu choice. |
| `gA_MultiThreadedSimulation` | Spawns worker threads that mimic downloading files and prints progress concurrently. |

### Group B

| Program | Key Features |
|---------|--------------|
| `gB_BankingSystem` (Java & C++) | • Account creation with auto-increment account number  
• Deposit / Withdraw with daily withdrawal limit  
• Passbook printing for full history or date-range  |
| `gB_InventoryManagementSystem` (Java & C++) | • Maintain product list with cost & sell price  
• Purchase (stock-in) & Shipping (stock-out)  
• Real-time profit calculation |

## License

These examples are provided for educational use and released into the **public domain** – feel free to copy or modify for your own learning.
