Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for j in range(len(my_list)):
        print("{:d}".format(my_list[j]))