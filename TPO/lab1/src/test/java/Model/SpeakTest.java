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
public class SpeakTest {
	private Speak speak;
	private Subject speaker;
	private Place platform;
	
	@BeforeAll
	public void setUp() {
		this.speak = new Speak();
		this.platform = new Place("platform");
		this.speaker = new Subject("speaker", this.platform);
	}
	
    @Test
    void testOk() throws CommandNotFoundException {
        CommandResult result = this.speak.execute(this.speaker, this.platform);
        Assertions.assertEquals(result.getResult(), "speaker speak at platform");
        Assertions.assertEquals(result.getPlace(), this.platform);
        Assertions.assertEquals(result.getSubject(), this.speaker);
    }
}
