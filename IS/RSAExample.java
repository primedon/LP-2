import java.math.BigInteger;
import java.util.Scanner;

public class RSAExample {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        BigInteger p = new BigInteger("61");
        BigInteger q = new BigInteger("53");

        BigInteger n = p.multiply(q);
        BigInteger phi = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));
        BigInteger e = new BigInteger("17");
        BigInteger d = e.modInverse(phi);

        System.out.println("Public Key (e, n): (" + e + ", " + n + ")");
        System.out.println("Private Key (d, n): (" + d + ", " + n + ")");

        System.out.print("Enter a message (as a number): ");
        BigInteger message = sc.nextBigInteger();

        BigInteger encrypted = message.modPow(e, n);
        System.out.println("Encrypted message: " + encrypted);

        BigInteger decrypted = encrypted.modPow(d, n);
        System.out.println("Decrypted message: " + decrypted);

        sc.close();
    }
}
