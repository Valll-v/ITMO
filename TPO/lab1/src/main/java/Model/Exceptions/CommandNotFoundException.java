package Model.Exceptions;

public class CommandNotFoundException extends Exception {
	private static final long serialVersionUID = 1L;
	
	public CommandNotFoundException(String errorMessage) {
        super(errorMessage);
    }
}
