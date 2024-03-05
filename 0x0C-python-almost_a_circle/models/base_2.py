#!/usr/bin/python3

"""
This module describes the class  Base
this is a  modular representation for the whole
project
"""

import json
import os.path
import csv


class Base:

    __nb_objects = 0

    """
    Class Representation of the base
    """

    def __init__(self, id=None):
        """
        Instance of the class
        """
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns string representation of an object
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """

        json_file = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass

        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

            lists = cls.to_json_string(list_dic)

            with open(json_file, 'w') as f:
                f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """
        that returns the list of the JSON string representation json_string
        """

        if json_string is None or len(json_string) == 0:
            return []

        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        that returns an instance with all attributes already set:
        **dictionary can be thought of as a double pointer to a dictionary
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)

        if cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns an instance of list
        """

        json_file = "{}.json".format(cls.__name__)

        if os.path.exists(json_file) is False:
            return []

        with open(json_file, 'r') as f:
            list_atr = f.read()

        list_cls = cls.from_json_string(list_atr)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        that serializes and deserializes in CSV
        """

        json_file = cls.__name__ + ".csv"

        with open(json_file, 'w', newline="") as f:
            csv_content = csv.writer(f)

            if cls.__name__ == "Rectangle":
                for i in list_objs:
                    csv_content.writerow([i.id, i.width, i.height, i.x, i.y])

            elif cls.__name__ == "Square":
                for i in list_objs:
                    csv_content.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of rectangles or squares in csv.

        Args:
            cls (any): class.
        """
        json_file = cls.__name__ + ".csv"
        my_obj = []
        try:
            with open(json_file, 'r') as f:
                csv_reader = csv.reader(f)
                for elm in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(elm[0]), "width": int(elm[1]),
                                      "height": int(elm[2]), "x": int(elm[3]),
                                      "y": int(elm[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(elm[0]), "size": int(elm[1]),
                                      "x": int(elm[2]), "y": int(elm[3])}
                    obj = cls.create(**dictionary)
                    my_obj.append(obj)
        except(Exception):
            pass
        return(my_obj)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a window and draws all the Rectangles and Squares

        NOT COMPLETE!!!!!!

        """
        window = turtle.Screen()
        turtle.speed(5)
        turtle.pensize(5)
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.color("black")
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for colors in ["red", "yellow", "purple", "blue"]:
                turtle.color(colors)
                turtle.forward(square.size)
                turtle.left(90)
        turtle.penup()

        window.exitonclick()
