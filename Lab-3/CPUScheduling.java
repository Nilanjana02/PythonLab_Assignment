import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class Process {
    int pid;        // Process ID
    int arrival;    // Arrival Time
    int burst;      // Burst Time
    int priority;   // Priority (only for Priority scheduling)
    int waiting;    // Waiting Time
    int turnaround; // Turnaround Time

    public Process(int pid, int arrival, int burst, int priority) {
        this.pid = pid;
        this.arrival = arrival;
        this.burst = burst;
        this.priority = priority;
    }
}

public class CPUScheduling {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of processes: ");
        int n = scanner.nextInt();
        
        Process[] processes = new Process[n];

        System.out.println("Enter the arrival time, burst time, and priority for each process:");
        for (int i = 0; i < n; i++) {
            System.out.print("Process " + (i + 1) + ": ");
            int arrival = scanner.nextInt();
            int burst = scanner.nextInt();
            int priority = scanner.nextInt();
            processes[i] = new Process(i + 1, arrival, burst, priority);
        }

        System.out.println("Choose the scheduling algorithm:\n1. FCFS\n2. SJF\n3. Priority");
        int choice = scanner.nextInt();

        switch (choice) {
            case 1:
                fcfs(processes);
                break;
            case 2:
                sjf(processes);
                break;
            case 3:
                priorityScheduling(processes);
                break;
            default:
                System.out.println("Invalid choice!");
                scanner.close();
                return;
        }

        calculateTimes(processes);
        printProcesses(processes);
        printAverageTimes(processes);

        scanner.close();
    }

    public static void calculateTimes(Process[] processes) {
        int currentTime = 0;
        for (Process process : processes) {
            process.waiting = currentTime - process.arrival;
            process.turnaround = process.waiting + process.burst;
            currentTime += process.burst;
        }
    }

    public static void printProcesses(Process[] processes) {
        System.out.println("\nPID\tArrival\tBurst\tPriority\tWaiting\tTurnaround");
        for (Process process : processes) {
            System.out.printf("%d\t%d\t%d\t%d\t\t%d\t%d\n",
                    process.pid,
                    process.arrival,
                    process.burst,
                    process.priority,
                    process.waiting,
                    process.turnaround);
        }
    }

    public static void printAverageTimes(Process[] processes) {
        double totalWaiting = 0, totalTurnaround = 0;
        for (Process process : processes) {
            totalWaiting += process.waiting;
            totalTurnaround += process.turnaround;
        }
        double avgWaiting = totalWaiting / processes.length;
        double avgTurnaround = totalTurnaround / processes.length;
        
        System.out.printf("\nAverage Waiting Time: %.2f\n", avgWaiting);
        System.out.printf("Average Turnaround Time: %.2f\n", avgTurnaround);
    }

    public static void fcfs(Process[] processes) {
        Arrays.sort(processes, Comparator.comparingInt(p -> p.arrival));
    }

    public static void sjf(Process[] processes) {
        Arrays.sort(processes, Comparator.comparingInt(p -> p.burst));
    }

    public static void priorityScheduling(Process[] processes) {
        Arrays.sort(processes, Comparator.comparingInt(p -> p.priority));
    }
}

