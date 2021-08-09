package tp1;

import tp1.arquitecture.*;
import tp1.bodies.Grid;


public class Main {
    public static void main(String[] args){
        Config config = new Config(args[0], args[1], args[2], args[3]);
        //System.out.println(config);
        System.out.println("--------");
        config.grid.bruteForce();
        config.grid.CIM();
    }

}