package Model.Commands;

import Model.Places.Place;
import Model.Subjects.Subject;

public class CommandResult {
	private Place place;
	private Subject subject;
	private String result;

	public CommandResult(Subject s, Place p, String r) {
		this.setSubject(s);
		this.setPlace(p);
		this.setResult(r);
	}

	public Place getPlace() {
		return place;
	}

	public void setPlace(Place place) {
		this.place = place;
	}

	public Subject getSubject() {
		return subject;
	}

	public void setSubject(Subject subject) {
		this.subject = subject;
	}

	public String getResult() {
		return result;
	}

	public void setResult(String result) {
		this.result = result;
	}
}
