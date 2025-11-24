import java.util.ArrayList;
import java.util.Scanner;

public class GameRunner {

    // Display the menu and return user's choice
    public static int menu() {
        Scanner userChoice = new Scanner(System.in);
        while (true) {
            System.out.println("""
    ╔══╦╗    ╔══╗      ╔══╦╗      ╔╗
    ╚╗╗╠╬═╦═╗╚╗╗╠╦╦═╦╗ ║══╣╚╦═╦╦╦╦╝╠═╦╦╦╦═╦╗
    ╔╩╝║║═╣╩╣╔╩╝║║║╩╣╚╗╠══║║║╬║║║║╬║╬║║║║║║║
    ╚══╩╩═╩═╝╚══╩═╩═╩═╝╚══╩╩╩═╩══╩═╩═╩══╩╩═╝

        ╔══╦╦══╦══╦═╦╗     ╔══╦╦╦══╦══╗      
    ╔══╗║═╦╬╣═╦╩╗╔╩╗║║╔═╦╦╗║╔╗║║║══╬╗╔╝╔══╗
    ╚══╝║╔╝║║╔╝ ║║╔╩╗║║╬║╔╝║╔╗║║╠══║║║ ╚══╝
        ╚╝ ╚╩╝  ╚╝╚══╝╚═╩╝ ╚══╩═╩══╝╚╝


                1. Play
                2. How to Play
                3. Quit
                """);
            System.out.print("Please enter your choice (1-3): ");
            try {
                int intChoice = userChoice.nextInt();
                if (intChoice >= 1 && intChoice <= 3) { // Validate input
                    return intChoice;
                } else {
                    System.out.println("Invalid choice. Please enter a number between 1 and 3.");
                }
            } catch (Exception e) {
                System.out.println("Invalid input. Please enter a valid number.");
                userChoice.next(); // Clear invalid input
            }
        }
    }

    // Display "How to Play" instructions
    public static void howToPlay() {
        System.out.println("""
                Welcome to Dice Duel Showdown - Fifty or Bust.

                In this game, your goal is to roll two dice and get the closest to 50 points within 10 turns without going over 50 points.
                While you are rolling, you are competing against a computer. If either you or the computer rolls the same number twice (e.g., roll a 5 and 5),
                the opposite player will lose 10 points.
                If you have more than 40 points, you will have 2 skips where you can skip your roll if you choose to. If the computer is over 40 points,
                they have a 30% chance of skipping their turn and have infinite skips.
                If you go over 50 points, the computer will automatically win, and if the computer goes over 50 points, you will automatically win.
                In case there is no winner after the 10 turns, the party with the most points will be victorious (same points is a tie).
                If a party hits exactly 50 points, they will automatically win.

                Good luck and have fun!
                """);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        PlayerRoll player = new PlayerRoll();
        ComputerRoll computer = new ComputerRoll();
        Rolling game = new Rolling();

        // These lists will hold the results of each round for statistics
        ArrayList<int[]> playerResults = new ArrayList<>();
        ArrayList<int[]> computerResults = new ArrayList<>();

        while (true) {
            int choice = menu(); // Display menu and get user choice

            if (choice == 2) {
                howToPlay(); // Show "How to Play"
            } else if (choice == 3) {
                System.out.println("Thanks for playing! Goodbye!");
                break; // Exit the program
            } else if (choice == 1) {
                // Reset for new game
                player = new PlayerRoll();
                computer = new ComputerRoll();
                playerResults.clear();
                computerResults.clear();
                
                game.playGame(player, computer, playerResults, computerResults); // Call the playGame method for 10 rounds
                GameStatistics.displayStats(playerResults, computerResults); // Display game statistics
                
                // We don't break here, so the user goes back to the menu after playing
            }
        }
        scanner.close(); // Close scanner
    }
}