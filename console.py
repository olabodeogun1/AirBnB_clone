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
            """Prints all string representation of all instances based or not on the
            class name.
            """
            args = args.split()
            objects = storage.all()
            result = []
            if len(args) == 0:
                for obj in objects.values():
                    result.append(str(obj))
            elif args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                for obj in objects.values():
                    if type(obj).__name__ == args[0]:
                        result.append(str(obj))
            print(result)

        def do_update(self, args):
            """Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
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
                    return
                elif len(args) < 4:
                    print("** value missing **")
                    return

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
