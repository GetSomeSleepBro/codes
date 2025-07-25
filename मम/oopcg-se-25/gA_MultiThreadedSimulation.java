/**
 * A simple multi-threaded simulation that spawns multiple worker threads which
 * mimic downloading files.  Progress is printed in real-time.
 */
public class MultiThreadedSimulation {

    private static class Downloader implements Runnable {
        private final int id;

        Downloader(int id) {
            this.id = id;
        }

        @Override
        public void run() {
            for (int progress = 0; progress <= 100; progress += 10) {
                System.out.printf("[Thread-%d] Download progress: %d%%%n", id, progress);
                try {
                    Thread.sleep((long) (Math.random() * 400 + 100));
                } catch (InterruptedException ignored) {
                    Thread.currentThread().interrupt();
                }
            }
            System.out.printf("[Thread-%d] Download complete!%n", id);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("Launching multi-threaded download simulation...\n");

        Thread[] threads = new Thread[3];
        for (int i = 0; i < threads.length; i++) {
            threads[i] = new Thread(new Downloader(i + 1));
            threads[i].start();
        }

        // Wait for all downloads to finish
        for (Thread t : threads) {
            t.join();
        }

        System.out.println("All downloads finished successfully.");
    }
}
