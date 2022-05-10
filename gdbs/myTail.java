import static cTools.KernelWrapper.*;

import java.util.ArrayList;
import java.util.List;

public class myTail {

	public static void main(String[] args) throws Exception {

		int tailLines = 10; // standard
		int start = 0;
		boolean startAt = false;

		for (int i = 0; i < args.length; i++) {
			// args containing "--help"?
			if (args[i].equals("--help")) {
				System.out.println("Auflistung der Kommandos?");
				exit(0);
			}
			// -n (+)K in "args"?
			if (args[i].equals("-n")) {
				if (args.length == i + 1) { // sonst index out of bounds exception
					System.out.println("falsche Eingabe");
					exit(1);
				} else if (args[i + 1].matches("[+]\\d+")) {
					startAt = true;
					start = Integer.parseInt(args[i + 1]) - 1;
				} else if (args[i + 1].matches("\\d+")) {
					tailLines = Integer.parseInt(args[i + 1]);
				} else {
					System.out.println("something went wrong");
					exit(1);
				}

				// now remove -n (+)K and save back as args
				List<String> list = new ArrayList<String>();
				for (int j = 0; j < args.length; j++) {
					list.add(args[j]);
				}
				list.remove(i);
				list.remove(i);
				args = list.toArray(new String[list.size()]);
				break;
			}
		}

		// open and read file
		for (String file : args) {
			int fd = open(file, O_RDONLY);
			if (fd == -1) {
				System.err.println("Fehler beim oeffnen der Datei" + file);
				exit(1);
			}
			int byteCount = lseek(fd, 0, SEEK_END);
			lseek(fd, 0, SEEK_SET);
			byte[] buffer = new byte[byteCount];
			read(fd, buffer, byteCount);
			close(fd);
			String content = new String(buffer);
			String[] contentLines = content.split("\n");

			// print tail
			if (startAt) {
				System.out.println(file + ":");
				for (int i = start; i < contentLines.length; i++) {
					System.out.println(contentLines[i]);
				}
				System.out.println();
			} else {
				System.out.println(file + ":");
				for (int i = contentLines.length - tailLines; i < contentLines.length; i++) {
					System.out.println(contentLines[i]);
				}
				System.out.println();
			}
		}
	}
}
