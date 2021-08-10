package tp1;

import tp1.arquitecture.*;
import tp1.bodies.Grid;


public class Main {
    private static long Tinicio, Tfinal, Tiempo;
    private static Config config;

    public static void main(String[] args){
        ej1a("30", "10", "10", "0.5");
        ej1b("30", "10", "10", "0.5");
        ej2("20", "1");
//        ej3("20", "1");
    }

    // COMPLETADO
    private static void ej1a(String cantParticulas, String matrix, String planeLength, String radioInteraccion){
        config = new Config(cantParticulas, matrix, planeLength, radioInteraccion);
        System.out.println("\n\nCOMIENZO DEL EJ 1A");
        Tinicio = System.currentTimeMillis();
        config.grid.bruteForce();
        config.grid.CIM();
        Tfinal = System.currentTimeMillis();
        Tiempo = Tfinal - Tinicio;
        System.out.println("El tiempo tardado es: " + Tiempo);
    }

    //INCOMPLETO
    private static void ej1b(String cantParticulas, String matrix, String planeLength, String radioInteraccion){
        config = new Config(cantParticulas, matrix, planeLength, radioInteraccion);
        System.out.println("\n\nCOMIENZO DEL EJ 1B"); // TODO falta editar para que sea con condiciones periodicas
        Tinicio = System.currentTimeMillis();
        config.grid.bruteForce();
        config.grid.CIM();
        Tfinal = System.currentTimeMillis();
        Tiempo = Tfinal - Tinicio;
        System.out.println("El tiempo tardado es: " + Tiempo);
    }

    // COMPLETO
    private static void ej2(String planeLength, String radioInteraccion){
        System.out.println("\n\nCOMIENZO DEL EJ 2");
        int cantDePruebas = 10;
        // ACA GUARDO TODOS LOS RESULTADOS DE TODAS LAS PRUEBAS
        long[][] resultados = new long[10][4];
        for(int i = 0; i < cantDePruebas; i++){
            // GUARDO EN EL LUGAR 0 DE LA MATRIZ LA CANT DE PARTICULAS
            int N = (int)(Math.random() * 30);
            String cantParticulas = Integer.toString(N);
            resultados[i][0] = N;
            // GUARDO EN EL LUGAR 1 DE LA MATRIZ LA CANT DE CELDAS
            int MxM = (int)(Math.random() * 20);
            String matrix = Integer.toString(MxM);
            resultados[i][1] = MxM;
            // CREO LA CONFIG
            config = new Config(cantParticulas, matrix, planeLength, radioInteraccion);
            // GUARDO EN EL LUGAR 2 DE LA MATRIZ LA CANT DE TIEMPO DEL BRUTE FORCE
            Tinicio = System.currentTimeMillis();
            config.grid.bruteForce();
            Tfinal = System.currentTimeMillis();
            Tiempo = Tfinal - Tinicio;
            resultados[i][2] = Tiempo;
            // GUARDO EN EL LUGAR 3 DE LA MATRIZ LA CANT DE TIEMPO DEL CIM
            Tinicio = System.currentTimeMillis();
            config.grid.CIM();
            Tfinal = System.currentTimeMillis();
            Tiempo = Tfinal - Tinicio;
            resultados[i][3] = Tiempo;
        }
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 4; j++) {
                System.out.println(resultados[i][j] + " ");
            }
            System.out.println();
        }
    }

//    //INCOMPLETO
//    private static void ej3(String planeLength, String radioInteraccion){
//        config = new Config(cantParticulas, matrix, planeLength, radioInteraccion);
//        System.out.println("\n\nCOMIENZO DE Ej 1b");
//        Tinicio = System.currentTimeMillis();
//        config.grid.bruteForce();
//        config.grid.CIM();
//        Tfinal = System.currentTimeMillis();
//        Tiempo = Tfinal - Tinicio;
//        System.out.println("El tiempo tardado es: " + Tiempo);
//    }

//    30 10 10 0.5

}