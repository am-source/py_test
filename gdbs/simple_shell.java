import static cTools.KernelWrapper.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class simple_shell {

    public static void main(String[] args) throws IOException {
        while (true) {
            System.out.print("Input>>");
            BufferedReader b_reader = new BufferedReader(
                    new InputStreamReader(System.in));
            String[] input = b_reader.readLine().split("\\/|\\s+");

        }
    }

}
