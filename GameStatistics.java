import java.util.ArrayList;

public class GameStatistics {

    // Find the player's highest scoring round recursively
    public static int[] findMaxPlayerScore(ArrayList<int[]> playerResults, int index, int[] maxScore) {
        if (index >= playerResults.size()) {
            return maxScore; // Base case: return maxScore when done
        }
        int roundScore = playerResults.get(index)[1] + playerResults.get(index)[2];
        if (roundScore > maxScore[1]) { // Update maxScore if current round is higher
            maxScore[0] = playerResults.get(index)[0];
            maxScore[1] = roundScore;
        }
        return findMaxPlayerScore(playerResults, index + 1, maxScore); // Move to the next round
    }

    // Find the computer's highest scoring round recursively
    public static int[] findMaxComputerScore(ArrayList<int[]> computerResults, int index, int[] maxScore) {
        if (index >= computerResults.size()) {
            return maxScore; // Base case: return maxScore when done
        }
        int roundScore = computerResults.get(index)[1] + computerResults.get(index)[2];
        if (roundScore > maxScore[1]) { // Update maxScore if current round is higher
            maxScore[0] = computerResults.get(index)[0];
            maxScore[1] = roundScore;
        }
        return findMaxComputerScore(computerResults, index + 1, maxScore); // Move to the next round
    }

    // Display the highest scoring rounds for both player and computer
    public static void displayStats(ArrayList<int[]> playerResults, ArrayList<int[]> computerResults) {
        int[] playerMax = findMaxPlayerScore(playerResults, 0, new int[]{-1, 0});
        int[] computerMax = findMaxComputerScore(computerResults, 0, new int[]{-1, 0});

        System.out.println("\nGame Statistics:");
        System.out.println("Player's highest scoring round: Round " + playerMax[0] + " with " + playerMax[1] + " points.");
        System.out.println("Computer's highest scoring round: Round " + computerMax[0] + " with " + computerMax[1] + " points.");
    }
}