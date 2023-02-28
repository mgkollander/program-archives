import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class RegexChecker {
    public static void main (String[] args) {

        // Gather user regex
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a regular expression (Ex: \"(a+ba)*1*\"): ");
        String regex_input = scanner.nextLine();

        // Gather user string
        System.out.print("Enter a string (L = {a,b}): ");
        String string_input = scanner.nextLine();

        // Loop until 'q'
        while (true) {

            // Match
            Matcher regex_input_match = Pattern.compile(regex_input).matcher(string_input);

            // Print results
            System.out.println("\n" + regex_input + " : " + regex_input_match.matches());

            // Get new user string unless 'q'
            System.out.print("\nType q to quit or enter another string: ");
            string_input = scanner.nextLine();
            if (string_input.equals("q")) {
                break;
            }

        }
    }
}