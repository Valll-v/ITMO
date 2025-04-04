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
public class ListenTest {
	private Listen listen;
	private Subject crowd;
	private Place area;
	
	@BeforeAll
	public void setUp() {
		this.listen = new Listen();
		this.area = new Place("area");
		this.crowd = new Subject("crowd", area);
	}
	
    @Test
    void testOk() throws CommandNotFoundException {
        CommandResult result = listen.execute(this.crowd, this.area);
        Assertions.assertEquals(result.getResult(), "crowd listen at area");
        Assertions.assertEquals(result.getPlace(), this.area);
        Assertions.assertEquals(result.getSubject(), this.crowd);
    }
}
