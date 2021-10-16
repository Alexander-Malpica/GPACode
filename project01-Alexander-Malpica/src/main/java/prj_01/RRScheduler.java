package prj_01;

public class RRScheduler {
    public static void main(String[] args){
        int termination_limit = 50;
        int no_threads = 5;
        int project_step = 1;
        for (int i=0; i<args.length; i++) {
            if (args[i].equals("-t") || args[i].equals("--termination")) {
                termination_limit = Integer.valueOf(args[++i]);
            }
            else if (args[i].equals("-p") || args[i].equals("--processes")) {
                no_threads = Integer.valueOf(args[++i]);
            }
            else if (args[i].equals("-s") || args[i].equals("--prjstep")) {
                project_step = Integer.valueOf(args[++i]);
                if (project_step!=1 && project_step!=2) {
                    System.out.println("Project Step value is 1 or 2 (" + project_step + " given).");
                    System.exit(1);
                }
            }
        }

        System.out.println("Starting Program...");


        RoundRobinCLL roundRobine = null;
        if (project_step==2) {
            roundRobine =  new RoundRobinCLL(12, termination_limit);
        }

        ThreadRunnable rrRunnable = new ThreadRunnable(roundRobine);
        Threads threads = new Threads(no_threads, rrRunnable);

        for (int i=0; i<threads.threads.size(); i++) {
            threads.threads.get(i).start();
        }

        if (roundRobine!=null) roundRobine.findFilledSlot() ;

        System.out.println("Main Finished ... Bye Bye");

        if (roundRobine!=null) roundRobine.stopLoop = true;

    }
}
