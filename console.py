#!/usr/bin/python3
""" console """ 


import cmd 


class HBNBCommand(cmd.Cmd):
    """ TODO: document """
    prompt = "(hbnb) "

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

