package Model.Commands;

import Model.Places.Place;
import Model.Subjects.Subject;

public class Speak implements Command {
	@Override
	public CommandResult execute(Subject s, Place p) {
		String result = String.format("%s speak at %s", s.getName(), p.getName());
		return new CommandResult(s, p, result);
	}
}
