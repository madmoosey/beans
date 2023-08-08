public class Numbers {
    public static void main(String[] args) {
        exerciseFour(16);
        exerciseFour(12);
        exerciseFour(21);
        exerciseFour(5);
    }

    public static void exerciseFour(int number) {
        if (number == 16) {
            System.out.println("16!");
        } else if (number >= 20) {
            System.out.println("20 or greater!");
        } else if (number <= 10) {
            System.out.println("10 or less!");
        } else {
            System.out.println("Between 10 and 20!");
        }
    }

}
