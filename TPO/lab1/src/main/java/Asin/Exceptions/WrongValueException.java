package Asin.Exceptions;

public class WrongValueException extends Exception {
    private static final long serialVersionUID = 1L;

	public WrongValueException(String errorMessage) {
        super(errorMessage);
    }
}