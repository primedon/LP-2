import java.util.Scanner;

public class Pract_2_SimpleTranspositionCipher {

    // Encrypt the message
    public static String encrypt(String message, int key) {
        StringBuilder cipher = new StringBuilder();

        for (int i = 0; i < key; i++) {
            for (int j = i; j < message.length(); j += key) {
                cipher.append(message.charAt(j));
            }
        }

        return cipher.toString();
    }

    // Decrypt the message
    public static String decrypt(String cipherText, int key) {
        int length = cipherText.length();
        int rows = (int) Math.ceil((double) length / key);
        char[] decrypted = new char[length];

        int index = 0;
        for (int i = 0; i < key; i++) {
            for (int j = i; j < length; j += key) {
                if (index < length) {
                    decrypted[j] = cipherText.charAt(index++);
                }
            }
        }

        return new String(decrypted);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the message: ");
        String message = sc.nextLine();

        System.out.print("Enter the key (number): ");
        int key = sc.nextInt();

        String encrypted = encrypt(message, key);
        System.out.println("Encrypted: " + encrypted);

        String decrypted = decrypt(encrypted, key);
        System.out.println("Decrypted: " + decrypted);
    }
}
