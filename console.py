#!/usr/bin/python3
""" console """ 


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ TODO: document """
    prompt = "(hbnb) "
    __list_of_class = ["BaseModel"]

    def do_create(self, arg):
        """ TODO: document """
        try:
            args = arg.split()
            if not args:
                print ("** class name missing **")
            else:
                if args[0] in HBNBCommand.__list_of_class:
                    instance = globals()[args[0]]()
                    instance.save()
                    print (instance.id)
                else:
                    print ("** class doesn't exist **")
        except ValueError:
            print ("** class name missing **")

    def do_show(self, arg):
        """ TODO: document """
        storage_objects = storage.all()
        try:
            args = arg.split()
            if not args:
                print ("** class name missing **")
            elif not args[0]:
                print ("** class name missing **")
            elif len(args) == 1:
                print ("** instance id missing **")
            else:
                if args[0] not in HBNBCommand.__list_of_class:
                    print ("** class doesn't exist **")
                else:
                    if f"{args[0]}.{args[1]}" not in storage_objects:
                        print ("** no instance found **")
                    else:
                        print(storage_objects[f"{args[0]}.{args[1]}"])
        except ValueError:
            print ("** class name missing **")

    def do_destroy(self, arg):
        """ TODO: document """
        storage_objects = storage.all()
        try:
            args = arg.split()
            if not args:
                print ("** class name missing **")
            elif not args[0]:
                print ("** class name missing **")
            elif len(args) == 1:
                print ("** instance id missing **")
            else:
                if args[0] not in HBNBCommand.__list_of_class:
                    print ("** class doesn't exist **")
                else:
                    if f"{args[0]}.{args[1]}" not in storage_objects:
                        print ("** no instance found **")
                    else:
                        del storage_objects[f"{args[0]}.{args[1]}"]
                        storage.save()
        except ValueError:
            print ("** class name missing **")

    def do_all(self, arg):
        """ TODO: Document """
        storage_objects = storage.all()
        try:
            args = arg.split()
            if args[1] in HBNBCommand.__list_of_class:
                all_arg_obj = []
                for value in storage_objects.values():
                    if value.__class.__name__ == args[0]:
                        all_arg_obj.append(value.__str__())
                print(all_arg_obj)
                        
            else:
                print ("** class doesn't exist **")
        except IndexError:
            print ([value.__str__() for value in storage_objects.values()])
        

    def do_quit(self, arg):
        """ Quit the cmd """
        return True

    def do_EOF(self, arg):
        """ exit when signal End Of File """
        print("")
        return True

    def help_quit(self):
        """ document  quit command """
        print("Quit command to exit the program")

    def help_EOF(self):
        """ document EXIT THE CMD """
        print("quit due to CTRL+D")

    def emptyline(self):
        """ do nothing when empty string """
        pass







if __name__ == '__main__':
    HBNBCommand().cmdloop()

