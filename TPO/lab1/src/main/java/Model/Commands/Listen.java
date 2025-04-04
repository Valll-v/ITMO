package Model.Commands;

import Model.Places.Place;
import Model.Subjects.Subject;

public class Listen implements Command {
	@Override
	public CommandResult execute(Subject s, Place p) {
		String result = String.format("%s listen at %s", s.getName(), p.getName());
		return new CommandResult(s, p, result);
	}
}
