import java.util.Scanner;
import java.util.Random;

public class telephone {
    private boolean isMakingCall;
    private boolean isDialToneRinging;
    private boolean isConnecting;
    private boolean isRinging;
    private boolean isConnected;
    private boolean isTalking;
    private String phoneNumber;

    public telephone() {
        this.isMakingCall = false;          //On Hook
        this.isDialToneRinging = false;     //Dial Tone and Dialling
        this.isConnecting = false;          //Connecting
        this.isConnected = false;           //Connected
        this.isRinging = false;             //Ringing
        this.isTalking = false;             //Talking
        this.phoneNumber = "";
    }

    public void start() {
        Scanner input = new Scanner(System.in);
        System.out.println("Do you want to make a call? (Y/N)");
        String choice = input.nextLine();

        if (choice.equalsIgnoreCase("Y")) {
            this.isMakingCall = true;                           // Telephone is off hook now
            System.out.println("Dial Tone Ringing...");       // Dial tone ringing
            System.out.println("Please enter the number you want to call (3 digits max):");
            // Scanner phoneNumber = new Scanner(System.in);
            while (this.phoneNumber.length() < 3) {
                char digit = input.next().charAt(0);
                if (Character.isDigit(digit)) {
                    this.phoneNumber += digit;
                }
            }            

            System.out.println("Connecting...");
            this.isDialToneRinging = false; // After user input all digit, dial tone stops.
            this.isConnecting = true;       // Telephone is now connecting.
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println("Ringing...");
            this.isConnecting = false;      // Telephone is now connected.
            this.isRinging = true;          // Receiver telephone now ringing.

            try {
                Thread.sleep(4000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            Random rand = new Random(); // Randomizes whether the receiver will pick up or not.

            if (rand.nextBoolean()) {
                System.out.println("Receiver picked up. Talking...");
                this.isRinging = false;
                this.isConnected = true;
                this.isTalking = true;

            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            if (this.phoneNumber.equals("911")) {
                System.out.println("911, What's your emergency?"); // Just an easter egg :P
            }

            System.out.println("Do you want to end call? (Yes/No)");
            System.out.println("Talking...");

            Scanner callInput = new Scanner(System.in); // Asks if user wants to end the call.
            while (this.isConnected && callInput.hasNextLine()) {
                String callChoice = callInput.nextLine();
                if (callChoice.equalsIgnoreCase("yes")) {
                    endCall();
                    hangUp();
                }
                else {
                    System.out.println("Continue talking...");
                    try {
                        Thread.sleep(2500);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println("Receiver hanged up.");
                    endCall();
                    hangUp();
                }
            }

            } else {
                System.out.println("Receiver did not pick up.");
                this.isRinging = false;
                this.isConnecting = false;
                this.isDialToneRinging = true;
            }
        } else {
            System.out.println("Ok, goodbye."); // If user doesn't wanna make a call.
        }
    }

    public void endCall() {
        if (this.isConnected) {
            this.isConnected = false;
            this.isTalking = false;
            System.out.println("Call ended.");
        }
    }

    public void hangUp() {
        if (this.isMakingCall) {
            this.isMakingCall = false;
            this.isDialToneRinging = false;
            this.isConnecting = false;
            this.isRinging = false;
            this.isConnected = false;
            this.isTalking = false;
            this.phoneNumber = "";
            System.out.println("Phone hung up.");
        }
    }

    public static void main(String[] args) {
        Telephone3 phone = new Telephone3();
        phone.start();
        phone.endCall();
        phone.hangUp();
    }

}
