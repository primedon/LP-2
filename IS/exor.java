public class exor {

    public static void main(String[] args) {
        String str="Ajinkya raut";
        System.out.println("Character | ASCII | AND with 127 | Xor with 127 ");
        System.out.println("-------------------------------------------");

        for(char ch:str.toCharArray()){
            int asciiValue=(int) ch;
            int AndResult=ch & 127;
            int ExorResult=ch ^ 127;
            System.out.printf(  "   %c  |  %3d    |  %3d   |    %3d\n", ch,asciiValue,ExorResult,AndResult);
        }
    }
}