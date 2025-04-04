package Model.Places;

public class Place {
	private String name;
	private Place parentPlace;
	
	public Place(String n) {
		this.setName(n);
	}

	public String getName() {
		if (parentPlace != null) {
			return String.format("%s in %s", this.name, this.parentPlace.name);
		}
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public void setParentPlace(Place parentPlace) {
		this.parentPlace = parentPlace;
	}
}
