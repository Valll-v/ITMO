package Model;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.TestInstance.Lifecycle;

import Model.Exceptions.CommandNotFoundException;
import Model.Places.Place;
import Model.Subjects.Subject;
import Model.Commands.*;


@TestInstance(Lifecycle.PER_CLASS)
public class SlideTest {
	private Slide slide;
	private Subject arthur;
	private Place window;
	
	@BeforeAll
	public void setUp() {
		this.slide = new Slide();
		this.window = new Place("Great window");
		this.window.setParentPlace(new Place("second floor"));
		this.arthur = new Subject("Arthur", this.window);
	}
	
    @Test
    void testOk() throws CommandNotFoundException {
        CommandResult result = this.slide.execute(this.arthur, this.window);
        Assertions.assertEquals(result.getResult(), "Arthur slides at Great window in second floor");
        Assertions.assertEquals(result.getPlace(), this.window);
        Assertions.assertEquals(result.getSubject(), this.arthur);
    }
}
