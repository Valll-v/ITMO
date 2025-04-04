package Model;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.TestInstance.Lifecycle;

import Model.Commands.CommandRepository;
import Model.Exceptions.CommandNotFoundException;
import Model.Commands.*;


@TestInstance(Lifecycle.PER_CLASS)
public class CommandRepositoryTest {
	private CommandRepository repo;
	
	@BeforeAll
	public void setUp() {
		repo = new CommandRepository();
		repo.addCommand("listen", new Listen());
		repo.addCommand("speak", new Speak());
		repo.addCommand("slide", new Slide());
		repo.addCommand("scream", new Scream());
	}

	@Test
	void testException() throws CommandNotFoundException {
		Assertions.assertThrows(CommandNotFoundException.class, () -> this.repo.getCommand("Do labs"));
	}
	
    @Test
    void testOk() throws CommandNotFoundException {
        assertTrue(repo.getCommand("listen") instanceof Listen);
        assertTrue(repo.getCommand("speak") instanceof Speak);
        assertTrue(repo.getCommand("slide") instanceof Slide);
        assertTrue(repo.getCommand("scream") instanceof Scream);
    }
}
