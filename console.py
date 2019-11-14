#!/usr/bin/python3
"""Command Interprete for Airbnb Porject."""

import cmd
import shlex
import re
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State


class HBHBCommand(cmd.Cmd):
    """ Class for command."""
    prompt = "(hbnb) "

    __classes = (
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            )

    __restricted_attrs = (
            "created_at",
            "updated_at",
            "id"
            )

    __operations = (
            "all",
            "count"
            )

    __args_operations = (
            "show",
            "update",
            "destroy"
            )

    def default(self, line):
        for c in HBHBCommand.__classes:
            for o in HBHBCommand.__operations:
                if re.search(r'^%s\.%s\(\)' % (c, o), line):
                    if o == "all":
                        self.do_all(c)
                    elif o == "count":
                        self.count(c)

        for c in HBHBCommand.__classes:
            for o in HBHBCommand.__args_operations:
                if re.search(r'^%s\.%s\(.*\)' % (c, o), line):
                    args = re.findall(r'^%s\.%s\((.*)\)' % (c, o), line)[0]
                    if args:
                        if o == "show":
                            args = args.strip('"')
                            self.do_show("{} {}".format(c, args))
                        elif o == "destroy":
                            args = args.strip('"')
                            self.do_destroy("{} {}".format(c, args))
                        elif o == "update":
                            args = args.split(", ")
                            if len(args) == 3:
                                args[0:2] = [s.strip(", \"")
                                             for s in args[0:2]]
                                self.do_update(
                                    "{} {} {} {}".format(c,
                                                         args[0],
                                                         args[1],
                                                         args[2]))
                            elif len(args) == 2:
                                print(args)
                                if (args[1][0] == "{"
                                        and args[1][-1] == "}"):
                                    args[1] = args[1].replace("'", "\"")
                                    args[1] = json.loads(args[1])
                                    args[0] = args[0].strip(", \"")
                                    self.update_with_dict(args[0], args[1])


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

    def do_create(self, args):
        """Command to create an instance of a class."""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBHBCommand.__classes:
            print("** class doesn't exist **")
        else:
            models.storage.reload()
            new = eval(args[0])()
            new.save()
            print(new.id)

    def do_show(self, args):
        """Prints the string representation of an instance."""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBHBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            for ins, obj in models.storage.all().items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    print(obj.__str__())
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBHBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            current_objs = models.storage.all()
            for ins, obj in current_objs.items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    del(current_objs[ins])
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """Command to print the string representation of all instances."""
        args = shlex.split(args)
        if args == []:
            models.storage.reload()
            new_list = []
            for ins, obj in models.storage.all().items():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBHBCommand.__classes:
            print("** class doesn't exist **")
        else:
            models.storage.reload()
            new_list = []
            for ins, obj in models.storage.all().items():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id."""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBHBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            current_objs = models.storage.all()
            for _, obj in current_objs.items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:

                    if len(args) == 2:
                        print("** attribute name missing **")
                        return
                    if len(args) == 3:
                        print("** value missing **")
                        return
                    if args[2] in HBHBCommand.__restricted_attrs:
                        return

                    if args[3][0] and args[3][-1] != '"':
                        try:
                            args[3] = int(args[3])
                        except ValueError:
                            try:
                                args[3] = float(args[3])
                            except ValueError:
                                pass

                    setattr(obj,
                            args[2],
                            type(getattr(obj, args[2], args[3]))(args[3]))
                    models.storage.save()
                    return
            print("** no instance found **")

    def update_with_dict(self, id, dic):
        """Updates an instance based on the class name and id."""
        models.storage.reload()
        current_objs = models.storage.all()
        for _, obj in current_objs.items():
            if obj.id == id:
                for k, v in dic.items():
                    if k not in HBHBCommand.__restricted_attrs:
                        setattr(obj,
                                k,
                                type(getattr(obj, k, v))(v))
                models.storage.save()
                return
        print("** no instance found **")

    def count(self, cls):
        count = 0

        for _, o in models.storage.all().items():
            if o.__class__.__name__ == cls:
                count += 1

        print(count)

    def emptyline(self):
        """ An empty line doesn't execute anything. """


if __name__ == '__main__':
    interpreter = HBHBCommand()
    interpreter.cmdloop()
