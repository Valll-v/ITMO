package Model.Subjects;

import Model.Places.Place;

public class Subject {
	private String name;
	private Place place;
	
	public Subject(String n, Place p) {
		this.name = n;
		this.place = p;
	}
	
	public String getName() {
		return name;
	}
}
