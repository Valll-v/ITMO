package Model.Commands;

import java.util.HashMap;

import Model.Exceptions.CommandNotFoundException;

public class CommandRepository {
	private HashMap<String, Command> CommandMap;

	public CommandRepository() {
		this.CommandMap = new HashMap<String, Command>();
	}
	
	public void addCommand(String s, Command c) {
		this.CommandMap.put(s, c);
	}
	
	public Command getCommand(String c) throws CommandNotFoundException {
		if (!this.CommandMap.containsKey(c)) {
			throw new CommandNotFoundException(String.format("Command %s not found!", c));
		}
		return this.CommandMap.get(c);
	}
}