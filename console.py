#!/usr/bin/python3
"""Command Interprete for Airbnb Porject."""

import cmd


class HBHBCommand(cmd.Cmd):
    """ Class for command."""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exit to the program.
           Args: 
               args: argument for the command.   
        """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program.
           Args:
               args: argument for the command.
        """
        print("")
        return True

    def emptyline(self):
        """ An empty line doesn't execute anything. """   
     pass

if __name__ == '__main__':
    interprete = HBHBCommand()
    interprete.cmdloop()
