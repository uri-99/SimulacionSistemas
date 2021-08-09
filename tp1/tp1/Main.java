package tp1;

import tp1.arquitecture.*;


public class Main {
    public static void main(String[] args){
        Config config = new Config(args[0], args[1], args[2], args[3]);
        System.out.println("chau mundo");
        System.out.println(config);
    }

}