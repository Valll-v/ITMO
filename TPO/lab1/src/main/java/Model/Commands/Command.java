package Model.Commands;

import Model.Places.Place;
import Model.Subjects.Subject;

public interface Command {
	public CommandResult execute(Subject s, Place p);
}