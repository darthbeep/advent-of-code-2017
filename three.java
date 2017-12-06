import java.util.Arrays;

public class three {

    public static int ring(int n) {
        double sqr = Math.sqrt(n);
        return (int) Math.ceil(sqr/2.0);
    }

    public static void printArray(int[][] arr) {
        for (Integer i = 0; i < arr.length; i++) {
            for (Integer j = 0; j < arr[0].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static int sumFriends(int[][] arr, int x, int y) {
        int sum = 0;
        sum += arr[x+1][y];
        sum += arr[x-1][y];
        sum += arr[x+1][y+1];
        sum += arr[x][y+1];
        sum += arr[x-1][y+1];
        sum += arr[x+1][y-1];
        sum += arr[x][y-1];
        sum += arr[x-1][y-1];
        if(sum == 0) {
            return 1;
        }
        return sum;
    }

    public static void main(String[] args) {
        int n = 265149;
        int place = 1;
        int steps = 1;
        int add = 0;
        int ring = ring(n);
        //System.out.println(ring);
        int grid[][] = new int[ring*2+1][ring*2+1];
        int direction = 0;
        int recent = -1;

        int x =ring/1, y=ring/1;
        while (place <= n && recent < n) {

            for (Integer i = 0; i < steps; i++) {
                if(recent >= n) {
                //printArray(grid);
                System.out.println(recent);
                break;
            }
                grid[x][y]=sumFriends(grid, x, y);
                recent = grid[x][y];
                if(direction == 0) {
                    x++;
                }
                if(direction == 1) {
                    y--;
                }
                if(direction == 2) {
                    x--;
                }
                if(direction == 3) {
                    y++;
                }

                place++;
                //printArray(grid);
            }
            add++;
            if(add == 2) {
                steps++;
                add = 0;
            }
            direction = (direction + 1) % 4;
        }
    }
}
