#!/usr/bin/env python3
"""Command Interprete for Airbnb Porject."""


import cmd

class HBHBCommand(cmd.Cmd):
    """ Class for command."""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exit to the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    
if __name__ == '__main__':
    interprete = HBHBCommand()
    interprete.cmdloop()
