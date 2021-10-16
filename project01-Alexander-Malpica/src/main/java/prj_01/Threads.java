package prj_01;
import java.util.*;
public class Threads {
    public ArrayList<Thread> threads = new ArrayList<Thread>();
    public Threads(int noThreads){
       for (int i=0; i<noThreads; i++){
           ThreadRunnable runnable = new ThreadRunnable();
           System.out.println("Creating Thread " + (i+1));
           threads.add(new Thread(runnable, ""+i));
       }
    }
    public Threads(int noThreads, ThreadRunnable runnable){
        for (int i=0; i<noThreads; i++){
            System.out.println("Creating Thread " + (i+1));
            threads.add(new Thread(runnable, ""+i));
        }
    }
}
