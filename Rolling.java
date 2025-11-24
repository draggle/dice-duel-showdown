import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Rolling {
    protected Random random = new Random(); // For generating random rolls
    protected ArrayList<int[]> results = new ArrayList<>(); // Stores roll results

    // Roll a single die (1 to 6)
    public int rollDie() {
        return random.nextInt(6) + 1;
    }

    // Roll two dice, store the result, and return the outcome
    public int[] rollTwoDice(int rollNumber) {
        int die1 = rollDie();
        int die2 = rollDie();
        int[] rollResult = {rollNumber, die1, die2};
        results.add(rollResult);
        return rollResult;
    }

    // Retrieve all stored roll results
    public ArrayList<int[]> getResults() {
        return results;
    }

    // Run the game for 10 rounds and return the results
    public void playGame(PlayerRoll player, ComputerRoll computer, ArrayList<int[]> playerResults, ArrayList<int[]> computerResults) {
        int rollNumber = 1; // To track the number of rolls

        while (rollNumber <= 10) { // Game limited to 10 rolls
            System.out.println("\nRound " + rollNumber);

            // Player's turn
            System.out.println("Your turn! Type 'r' to roll or 's' to skip.");
            String input = new Scanner(System.in).nextLine();

            if (input.equalsIgnoreCase("s")) {
                if (player.getSkips() > 0 && player.getPoints() > 40) {
                    player.decrementSkips();
                    System.out.println("You skipped your turn! Remaining skips: " + player.getSkips());
                } else {
                    System.out.println("You cannot skip! Either you're out of skips or have less than 40 points.");
                    continue; // Retry player's turn
                }
            } else if (input.equalsIgnoreCase("r")) {
                int[] roll = player.rollTwoDice(rollNumber);
                System.out.println("You rolled: " + roll[1] + " and " + roll[2]);

                if (roll[1] == roll[2]) { // Player rolls doubles
                    System.out.println("Double rolled! Computer loses 10 points.");
                    computer.adjustPoints(-10);
                }
                player.adjustPoints(roll[1] + roll[2]); // Add points to player
                System.out.println("Your total points: " + player.getPoints());

                // Store player results
                playerResults.add(roll);

                // Check if player wins or loses
                if (player.getPoints() == 50) {
                    System.out.println("You hit 50 points! You win!");
                    return; // End the game immediately
                } else if (player.getPoints() > 50) {
                    System.out.println("You went over 50 points! You lose!");
                    return; // End the game immediately
                }
            } else {
                System.out.println("Invalid input. Please type 'r' to roll or 's' to skip.");
                continue; // Retry player's turn
            }

            // Computer's turn
            if (computer.getPoints() > 40 && Math.random() < 0.3) {
                System.out.println("Computer skipped its turn!");
            } else {
                int[] roll = computer.rollTwoDice(rollNumber);
                System.out.println("Computer rolled: " + roll[1] + " and " + roll[2]);

                if (roll[1] == roll[2]) { // Computer rolls doubles
                    System.out.println("Double rolled! Player loses 10 points.");
                    player.adjustPoints(-10);
                }
                computer.adjustPoints(roll[1] + roll[2]); // Add points to computer
                System.out.println("Computer's total points: " + computer.getPoints());

                // Store computer results
                computerResults.add(roll);

                // Check if computer wins or loses
                if (computer.getPoints() == 50) {
                    System.out.println("Computer hit 50 points! Computer wins!");
                    return; // End the game immediately
                } else if (computer.getPoints() > 50) {
                    System.out.println("Computer went over 50 points! Computer loses!");
                    return; // End the game immediately
                }
            }

            rollNumber++; // Increment roll count

            // Display current scores
            System.out.println("\nCurrent Scores:");
            System.out.println("Player: " + player.getPoints());
            System.out.println("Computer: " + computer.getPoints());
        }

        // Determine winner after 10 rolls (if no one hit 50)
        System.out.println("\nGame over! Final Scores:");
        System.out.println("Player: " + player.getPoints());
        System.out.println("Computer: " + computer.getPoints());

        if (player.getPoints() > computer.getPoints() && player.getPoints() <= 50) {
            System.out.println("Congratulations! You win!");
        } else if (computer.getPoints() > player.getPoints() && computer.getPoints() <= 50) {
            System.out.println("The Computer wins! Better luck next time!");
        } else if (player.getPoints() == computer.getPoints()) {
            System.out.println("It's a tie!");
        }
    }
}

class PlayerRoll extends Rolling {
    private int points = 0; // Player's points
    private int skips = 2;  // Remaining skips (adjusted as per original design)

    // Adjust player points
    public void adjustPoints(int adjustment) {
        points += adjustment;
    }

    // Get current points
    public int getPoints() {
        return points;
    }

    // Get remaining skips
    public int getSkips() {
        return skips;
    }

    // Reduce skips by 1
    public void decrementSkips() {
        skips--;
    }
}

class ComputerRoll extends Rolling {
    private int points = 0; // Computer's points

    // Adjust computer points
    public void adjustPoints(int adjustment) {
        points += adjustment;
    }

    // Get current points
    public int getPoints() {
        return points;
    }
}