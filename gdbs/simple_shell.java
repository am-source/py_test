import static cTools.KernelWrapper.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class simple_shell {

    private String PATH = System.getenv("PATH");
    private static Integer old_fd_in;
    private static Integer old_fd_out;

    public static void main(String[] args) throws IOException {
        simple_shell ss = new simple_shell();

        Boolean runn_var = true;

        while (runn_var) {
            print_prompt();
            String[] input = ss.handle_input();
            // exit?
            check_running_condition(input[0], runn_var);
            // "<" or ">" ?
            boolean redirected = check_std_redirection(input);
            if (redirected == true) {
                input = crop_input_for_redirect(input);
            }
            String path = ss.get_executable_file_path(input);
            // improve following line
            if (path == null) {
                System.err.println("Kein ausführbares Programm gefunden!");
            } else {
                execute(path, input, redirected);

            }

        }
    }

    private static boolean check_std_redirection(String[] input) {
        boolean redirected = false;
        for (int i = 0; i < input.length; i++) {
            if (input[i].equals("<")) {
                old_fd_in = dup2(STDIN_FILENO, 1000);
                close(STDIN_FILENO);
                open(input[i + 1], O_RDONLY);
                redirected = true;
            }
            if (input[i].equals(">")) {
                old_fd_out = dup2(STDOUT_FILENO, 1001);
                close(STDOUT_FILENO);
                open(input[i + 1], O_WRONLY);
                redirected = true;
            }
        }
        return redirected;
    }

    private static void execute(String path, String[] input, boolean redirected) {
        int child_pid = fork();

        if (child_pid == 0) { // child process
            execv(path, input);
            exit(0);
        } else if (child_pid == -1) { // error
            System.err.println("Starten der Anwendung fehlgeschlagen");
            exit(1);
        } else { // parent process
            int[] status = new int[1];
            waitpid(child_pid, status, 0);
            // check if redirect was used, to restore status
            if (redirected) {
                if (old_fd_in != null) {
                    close(STDIN_FILENO);
                    dup2(old_fd_in, STDIN_FILENO);
                    close(old_fd_in);
                    old_fd_in = null;
                } else {
                    close(STDOUT_FILENO);
                    dup2(old_fd_out, STDOUT_FILENO);
                    close(old_fd_out);
                    old_fd_out = null;
                }
            }
        }
    }

    private static void check_running_condition(String input_cmd, Boolean runn_var) {
        if (input_cmd.equals("exit")) {
            runn_var = false;
            exit(0);
        }
    }

    // remove "<"/">" and filename
    private static String[] crop_input_for_redirect(String[] input) {
        String[] tmp_input = new String[input.length - 2];
        System.arraycopy(input, 0, tmp_input, 0, input.length - 2);
        return tmp_input;
    }

    private String[] handle_input() throws IOException {
        BufferedReader b_reader = new BufferedReader(
                new InputStreamReader(System.in));
        return b_reader.readLine().split("\\/|\\\\|\\s+"); // \s represents " "
    }

    private static void print_prompt() {
        System.out.print("Input>>");
    }

    private String get_executable_file_path(String[] input) {

        String path = null;
        String[] pathArray = PATH.split(":");
        File file;
        // remove
        // for (String elem : pathArray) {
        // System.out.println(elem);
        // }
        for (int i = 0; i < pathArray.length; i++) {
            String tmp_path = pathArray[i] + "/" + input[0];
            file = new File(tmp_path);

            if (file.isFile() && file.canExecute()) {
                path = tmp_path;
                break;
            }
        }
        // remove
        // System.out.println("path was : " + path);
        return path;
    }

}
