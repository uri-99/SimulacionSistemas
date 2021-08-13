package tp1;

import tp1.arquitecture.*;

import java.time.Clock;
import java.util.Random;


public class Main {
    private static long Tinicio, Tfinal, Tiempo;
    private static Config config;

    public static void main(String[] args){
        config = new Config("150", "5", "10", "1");
        config.grid.CIMP();
        config.exportToLAMMPSFile("test", 3);
//        ej1a("100", "2", "10", "2");
//        ej1b("100", "2", "10", "2");
//        ej2("100", "5");
//        ej3("100", "2");
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

    //COMPLETO
    private static void ej1b(String cantParticulas, String matrix, String planeLength, String radioInteraccion){
        config = new Config(cantParticulas, matrix, planeLength, radioInteraccion);
        System.out.println("\n\nCOMIENZO DEL EJ 1B"); //
        Tinicio = System.currentTimeMillis();
        config.grid.bruteForce();
        config.grid.CIMP();
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
            Random rand = new Random();
            int N = rand.nextInt(5000-500) + 500; //100 (excluyente) es el maximo y 1 (incluido) es el minimo
            String cantParticulas = Integer.toString(N);
            resultados[i][0] = N;
            // GUARDO EN EL LUGAR 1 DE LA MATRIZ LA CANT DE CELDAS
            rand = new Random();
            int MxM = rand.nextInt(20-1) + 1;
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
                if(j == 0){
                    System.out.println("Numero de particulas: ");
                }
                else if(j == 1){
                    System.out.println("El tamaño de la matrix MxM es: ");
                }
                else if(j == 2){
                    System.out.println("Tiempo del Brute Force (en ms): ");
                }
                else if(j == 3){
                    System.out.println("Tiempo del CIM (en ms): ");
                }
                System.out.println(resultados[i][j] + " ");
            }
            System.out.println();
        }
    }

    //COMPLETO
    private static void ej3(String planeLength, String radioInteraccion){
        Clock clock = Clock.systemDefaultZone();
        Random rand = new Random();
        int N = rand.nextInt(1000-1) + 1; //100 (excluyente) es el maximo y 1 (incluido) es el minimo
        String cantParticulas = Integer.toString(N);
        double L = Double.parseDouble(planeLength);
        double R = Double.parseDouble(radioInteraccion);
        int MxM = (int)Math.floor(L/R);
        String matrix = Integer.toString(MxM);
        config = new Config(cantParticulas, matrix, planeLength, radioInteraccion);
        //config = new Config("100", "10", "10", "1");
        System.out.println("\n\nCOMIENZO DEL EJ 3 con un M: " + MxM);
        Tinicio = clock.millis();
        config.grid.bruteForce();
        config.grid.CIM();
        Tfinal = clock.millis();
        Tiempo = Tfinal - Tinicio;
        long TiempoM = Tiempo;


        System.out.println("\n\nOtro tamaño de matrix para ver su tiempo");
        rand = new Random();
        int MxM2 = rand.nextInt(MxM-1) + 1;
        matrix = Integer.toString(MxM2);
        Config config2 = new Config(cantParticulas, matrix, planeLength, radioInteraccion);
        //Config config2 = new Config("1000", "10", "10", "1");
        Tinicio = clock.millis();
        config2.grid.bruteForce();
        config2.grid.CIM();
        Tfinal = clock.millis();
        Tiempo = Tfinal - Tinicio;






        System.out.println("El tiempo tardado con un M optimo es: " + TiempoM  + "ms. " + "M es igual a: " + MxM);
        System.out.println("El tiempo tardado con un M aleatorio es: " + Tiempo +  "ms. "+ "M es igual a: " + MxM2);

    }

}