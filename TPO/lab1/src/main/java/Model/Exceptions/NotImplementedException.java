package Model.Exceptions;

public class NotImplementedException extends UnsupportedOperationException {
    private static final long serialVersionUID = 1L;

	public NotImplementedException() {
        super("Not implemented yet.");
    }
}
