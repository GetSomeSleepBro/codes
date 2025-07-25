import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * A simple hotel room booking system backed by a 2-D boolean array.
 * true  -> booked
 * false -> available
 *
 * The hotel layout is configured via "FLOORS" and "ROOMS_PER_FLOOR" constants.
 */
public class HotelBookingSystem {

    private static final int FLOORS = 5;
    private static final int ROOMS_PER_FLOOR = 10;
    private static final boolean[][] rooms = new boolean[FLOORS][ROOMS_PER_FLOOR];

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("======= Hotel Booking System =======");
        boolean exit = false;
        while (!exit) {
            printMenu();
            int choice = readInt("Enter choice: ");
            switch (choice) {
                case 1 -> displayRooms();
                case 2 -> bookRoom();
                case 0 -> exit = true;
                default -> System.out.println("Invalid choice, please try again.\n");
            }
        }
        System.out.println("Thank you for using the system. Goodbye!");
    }

    private static void printMenu() {
        System.out.println("\n1. View room availability");
        System.out.println("2. Book a room");
        System.out.println("0. Exit\n");
    }

    private static void displayRooms() {
        System.out.println("\nRoom Status (A=Available, B=Booked):");
        for (int i = 0; i < FLOORS; i++) {
            System.out.printf("Floor %d : ", i + 1);
            for (int j = 0; j < ROOMS_PER_FLOOR; j++) {
                System.out.print(rooms[i][j] ? " B" : " A");
            }
            System.out.println();
        }
    }

    private static void bookRoom() {
        int floor = readInt("Enter floor number (1-" + FLOORS + "): ") - 1;
        int room = readInt("Enter room number (1-" + ROOMS_PER_FLOOR + "): ") - 1;

        if (isValid(floor, room)) {
            if (!rooms[floor][room]) {
                rooms[floor][room] = true;
                System.out.println("Room successfully booked!\n");
            } else {
                System.out.println("Sorry, that room is already booked.\n");
            }
        } else {
            System.out.println("Invalid floor or room number.\n");
        }
    }

    private static boolean isValid(int floor, int room) {
        return floor >= 0 && floor < FLOORS && room >= 0 && room < ROOMS_PER_FLOOR;
    }

    private static int readInt(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                return Integer.parseInt(scanner.next());
            } catch (NumberFormatException e) {
                System.out.println("Invalid number, please try again.");
            }
        }
    }
}
