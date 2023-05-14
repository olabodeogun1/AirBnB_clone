#!/usr/bin/python3

"""
HBNB CMD
"""

from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.amenity import Amenity
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "
    classes = {
        'BaseModel': BaseModel,
        'State': State,
        'Place': Place,
        'User': User,
        'Amenity': Amenity,
        'City': City,
        'Review': Review
    }

    def do_create(self, args):
        """
        A command for creating new object through the command line
        """
        if not args:
            print("** class name missing **")
            return
        else:
            if args not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                model = HBNBCommand.classes[args]()
                model.save()
                print(model.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
        name and id.
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key not in objects.keys():
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key not in objects.keys():
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
            based or not on the class name.
        """
        if '.' in args:
            arg = args.split('.')
        else:
            arg = args.split()
        objects = storage.all()
        result = []

        if hasattr(self.classes[arg[1]], 'all'):
            result = self.classses[arg[0]].all()
 
        elif len(arg) == 0:
            for obj in objects.values():
                result.append(str(obj))
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for obj in objects.values():
                if type(obj).__name__ == arg[0]:
                    result.append(str(obj))
        print(result)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """

        my_list = parse(args)
        key = my_obj(args)
        if key:
            if len(my_list) > 4:
                print("Usage:update <class name> <id>\
                         <aittribute name> \"<attribute value>\"")
            elif len(my_list) == 3:
                print("** value missing **")
            elif len(my_list) == 2:
                print("** attribute name missing **")
            else:
                my_dict = storage.all()
                my_in = my_dict[key]
                val = my_list[3][1:-1]
                try:
                    if "." in val:
                        val = float(val)
                    else:
                        val = int(val)
                except ValueError:
                    pass
                setattr(my_in, my_list[2], val)
                storage.save()

    def do_quit(self, args):
        """
        Command to exit program
        """
        return True

    def do_EOF(self, args):
        """
        Command to exit program using end of file
        """
        quit
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass


def parse(arg):
    '''
    Splits and returns command line arguments
    '''
    return arg.split()


def my_obj(my_line):

    """returns key of an object
    """

    my_list = parse(my_line)
    if len(my_list) == 0:
        print("** class name missing **")
    elif len(my_list) == 1:
        if my_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print("** instance id missing **")
    elif len(my_list) >= 2:
        if my_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            key = f"{my_list[0]}.{my_list[1]}"
            file_dict = storage.all()
            if key in file_dict:
                return key
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
