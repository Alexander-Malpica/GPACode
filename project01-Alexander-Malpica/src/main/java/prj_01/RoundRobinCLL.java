// Alexander Malpica alexander.malpica@uprm.edu

package prj_01;
import java.util.concurrent.ThreadLocalRandom;

class Node {
    public int id;
    public Node next;
    public Node previous;
    public Boolean processed_flag;

    public Node (int id) {
        this.id = id;
        processed_flag = true;
    }
}

interface RoundRobinCLLInterface {
    abstract void findEmptySlot();
    abstract void findFilledSlot();
}

public class RoundRobinCLL implements RoundRobinCLLInterface {
    private int num_nodes = 5;
    public Node head = null;
    public Node tail = null;
    public Boolean stopLoop = false;
    private int termination_limit;

    private void holdon() {
        try{
            Thread.currentThread();
			Thread.sleep(ThreadLocalRandom.current().nextInt(500, 3000));
        }
        catch(Exception e){
            System.out.println("Something went wrong.");
        }
    }

    @Override
    public String toString () {
        String s = new String(""+ Thread.currentThread().getName() + " ");
        Node node = head;
        s+= "(Node-1: " + node.processed_flag + ")";
        s+= " ==> ";

        for (int i=1; i<num_nodes; i++) {
            node = node.next;
            s+= "(Node-"+(i+1)+": "+node.processed_flag + ")";
            if (i<num_nodes-1)
                s+= " ==> ";
        }
        return s;
    }

    private synchronized void holdRR(Node node, Boolean set_slot) {
        System.out.println("Thread " + Thread.currentThread().getName() + " Holding Resources");
        node.processed_flag = set_slot ;
        System.out.println("Thread " + Thread.currentThread().getName() + " Releasing Resources");
        if (set_slot) holdon();
    }

    public void findEmptySlot() {
        holdon();
        Node checking = head;
        while (checking.next != head) {
            if (checking.processed_flag) {
                holdRR(checking, false);
            } else {
                checking = checking.next;
            }
        }
        if (checking.processed_flag) {
            holdRR(checking, true);
        }
        /* PUT YOUR CODE HERE TO FIND AN EMPTY SLOT */
        /* STARTING FROM THE FIRST NODE IN THE LINKED LIST */
        /*** IMPORTANT:: USE THE holdRR() METHODE TO ACCESS THE LINKED LIST ***/
        /*** TO AVOID RACE CONDITION ***/
    }

    public void findFilledSlot() {
        /* PUT YOUR CODE HERE TO FIND THE FILLED SLOTS */
        /* FOR THE MAIN PROCESS                        */
        /*** IMPORTANT:: USE THE holdRR() METHODE TO ACCESS THE LINKED LIST ***/
        holdon();
        int count = 0;
        Node curNode = head;
        while (!stopLoop) {
            /* PUT YOUR CODE HERE TO FIND THE FILLED SLOTS */
            if (count>termination_limit) break;
            else if (!curNode.processed_flag) {
                holdRR(curNode, true);
            }
            curNode = curNode.next;
            System.out.println("- - - - - - - - - - - - - - - - - -");
            System.out.println(count);
            System.out.println(num_nodes);
            System.out.println(termination_limit);
            System.out.println("- - - - - - - - - - - - - - - - - -");
            System.out.println("Main Move No.: " + count%num_nodes + "\t" + toString());
            count++;
        }
    }

    private void fillRoundRubin () {
        /* PUT YOUR CODE HERE INITIATE THE CIRCULAR LINKED LIST */
        /* WITH DESIRED NUMBER OF NODES BASED TO THE PROGRAM   */
        if (num_nodes>0) {
            head = new Node(0);
            Node tempNode = head;
            for (int i = 1; i < num_nodes; i++) {
                Node add = new Node(i);
                tempNode.next = add;
                add.previous = tempNode;
                tempNode = tempNode.next;
            }
            tail = tempNode;
            head.previous = tail;
            tail.next = head;
        }
    }

    public RoundRobinCLL(int num_nodes, int termination_limit) {
        this.num_nodes = num_nodes;
        this.termination_limit = termination_limit;
        fillRoundRubin();
    }
    public RoundRobinCLL(int num_nodes) {
        this.num_nodes = num_nodes;
        fillRoundRubin();
    }

    public RoundRobinCLL() {
        fillRoundRubin();
    }

}
