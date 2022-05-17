import static cTools.KernelWrapper.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class simple_shell {

    private String PATH = System.getenv("PATH");

    public static void main(String[] args) throws IOException {
        simple_shell ss = new simple_shell();

        Boolean runn_var = true;

        while (runn_var) {
            print_prompt();
            String[] input = ss.handle_input();

            check_running_condition(input[0], runn_var);

            String path = ss.get_executable_file_path(input);
            // improve following line
            if (path == null) {
                System.err.println("Kein ausführbares Programm gefunden!");
            } else {
                execute(path, input);

            }

        }
    }

    private static void execute(String path, String[] input) {
        int child_pid = fork();

        if (child_pid == 0) { // Kindprozess
            execv(path, input);
            exit(0);
        } else if (child_pid == -1) { // Fehler
            System.err.println("Starten der Anwendung fehlgeschlagen");
            exit(1);
        } else {
            int[] status = new int[1];
            waitpid(child_pid, status, 0);

        }
    }

    private static void check_running_condition(String input_cmd, Boolean runn_var) {
        if (input_cmd.equals("exit")) {
            runn_var = false;
            exit(0);
        }
    }

    private String[] handle_input() throws IOException {
        BufferedReader b_reader = new BufferedReader(
                new InputStreamReader(System.in));
        return b_reader.readLine().split("\\/|\\\\|\\s+");
    }

    private static void print_prompt() {
        System.out.print("Input>>");
    }

    private String get_executable_file_path(String[] input) {

        String path = null;
        String[] pathArray = PATH.split(":");
        File file;
        // remove
        for (String elem : pathArray) {
            System.out.println(elem);
        }
        for (int i = 0; i < pathArray.length; i++) {
            file = new File(pathArray[i] + "/" + input[0]);

            if (file.isFile() && file.canExecute()) {
                path = pathArray[i] + "/" + input[0];
                break;
            }
        }
        // remove
        System.out.println("path was : " + path);
        return path;
    }

}
