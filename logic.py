from math import trunc

from PyQt6.QtWidgets import *
from project1 import *
import math
class Logic(QMainWindow, Ui_MainWindow):
    """
        Main logic that inherits from QMainWindow and Ui_MainWindow.
         connection between UI logic behind the calculator functions.
        """
    def __init__(self)-> None:
        super().__init__()
        self.setupUi(self)

        """
             Initializes the calculator's logic and connection of button for actions.
            Sets up initial values for first input, second input, and operator.
         """
        self.__First_input = ''
        self.__Second_input = ''
        self.__Operator = ""
        self.result.setText(self.__First_input)
        self.windowshow = False
        self.secondpage.hide()
        self.setFixedWidth(440)

        '''Connect buttons for actions'''
        self.zero_button.clicked.connect(lambda:self.update_input("0"))
        self.one_button.clicked.connect(lambda: self.update_input("1"))
        self.two_button.clicked.connect(lambda: self.update_input("2"))
        self.three_button.clicked.connect(lambda: self.update_input("3"))
        self.four_button.clicked.connect(lambda: self.update_input("4"))
        self.five_button.clicked.connect(lambda: self.update_input("5"))
        self.six_button.clicked.connect(lambda: self.update_input("6"))
        self.seven_button.clicked.connect(lambda: self.update_input("7"))
        self.eight_button.clicked.connect(lambda: self.update_input("8"))
        self.nine_button.clicked.connect(lambda: self.update_input("9"))
        '''Connect operator for actions'''
        self.add_button.clicked.connect(lambda: self.update_operator("+"))
        self.subtract_button.clicked.connect(lambda: self.update_operator("-"))
        self.multiply_button.clicked.connect(lambda: self.update_operator("*"))
        self.division_button.clicked.connect(lambda: self.update_operator("/"))
        self.percent_button.clicked.connect(lambda: self.update_operator("%"))
        self.squareroot_button.clicked.connect(lambda: self.update_operator("√"))
        self.square_button.clicked.connect(lambda: self.update_operator("x²"))
        self.cube_button.clicked.connect(lambda: self.update_operator("x³"))
        self.cube_root_button.clicked.connect(lambda: self.update_operator("∛"))
        '''Equal and the Clear button for actions'''
        self.equal_button.clicked.connect(self.calculate_result)
        self.clear_button.clicked.connect(self.clear_input)
        self.circle_button.clicked.connect(lambda:self.update_operator("circle"))
        self.square_button_2.clicked.connect(lambda: self.update_operator("square"))
        self.rectangle_button.clicked.connect(lambda: self.update_operator("rectangle"))
        self.triangle_button.clicked.connect(lambda: self.update_operator("triangle"))
        self.mode_button.clicked.connect(lambda: self.mode_input())




    def update_input(self,value)-> None:
        """
                Updating the current input value based on the button that will be clicked.
                """

        if self.__First_input == '':
            print("Made it")
            self.__First_input =value
        elif self.__First_input !='' and self.__Operator =='':
            self.__First_input = self.__First_input + value

        elif self.__Second_input =='' and self.__Operator !='':
            self.__Second_input = value
        elif self.__Second_input != '' and self.__Operator !='':
            self.__Second_input = self.__Second_input + value


        if self.__Second_input == '':
            print("First",self.__First_input)
            self.result.setText(self.__First_input)
        else:
            print("Second",self.__Second_input)
            self.result.setText(self.__Second_input)


    def update_operator(self,value) -> None:
        """
                Updates the operator(e.g., "+", "-", "*", "/", "%") based on the button clicked.

                """
        self.__Operator = value

    def mode_input(self)-> None:
        """
        this is for showing the second screen
        """

        if  self.windowshow:
            self.setFixedWidth(440)
            self.windowshow =False
            self.secondpage.hide()
        else:
            self.setFixedWidth(862)
            self.windowshow = True
            self.secondpage.show()




    def clear_input(self)-> None:
        """
        Clears all current inputs.
         """

        self.__First_input = ''
        self.__Second_input = ''
        self.__Operator = ""
        self.result.setText("0")

    def calculate_result(self)-> None:
        """
                 Calculates the result of the current operation.
                 """
        if self.__Operator == "+":
            result = int(self.__First_input) + int(self.__Second_input)

        elif self.__Operator == "-":
            result = int(self.__First_input) - int(self.__Second_input)


        elif self.__Operator == "*":
            result= int(self.__First_input) * int(self.__Second_input)

        elif self.__Operator == "/":
            result = int(self.__First_input) / int(self.__Second_input)

        elif self.__Operator == "%":
            result = int (self.__First_input) / 100
        elif self.__Operator == "x²":
            result = int(self.__First_input) ** 2
        elif self.__Operator == "x³":
            result = int(self.__First_input) ** 3
        elif self.__Operator == "√":
            result = math.sqrt(int(self.__First_input))
        elif self.__Operator == "∛":
            result = int(self.__First_input) ** (1/3)
        elif self.__Operator == "circle":
            result = self.circle(float(self.__First_input))
        elif self.__Operator == "square":
            result = self.square(float(self.__First_input))
        elif self.__Operator == "rectangle":
            result = self.rectangle(float(self.__First_input),float(self.__Second_input))
        elif self.__Operator == "triangle":
            result = self.triangle(float(self.__First_input),float(self.__Second_input))










        self.result.setText(str(result))
        self.__First_input = str(result)
        self.__Second_input = ''
        self.__Operator = ''




    def circle(self,radius) -> float:
        """
          Calculates the circle.
            """

        if radius <= 0:
             raise ValueError("Radius must be positive")
        return math.pi * radius ** 2

    def square(self,side)-> float:
        """
        Calculates the square.
        """

        side = float(side)
        if side <= 0:
         raise ValueError("Side must be positive")
        return side * side

    def rectangle(self,length, width)-> float:
        """
        Calculates the rectangle.
         """
        length = float(length)
        width = float(width)
        if length <= 0 or width <= 0:
             raise TypeError("length and width must be positive")
        return length * width



    def triangle(self,base, height)-> float:
        """
         Calculates the triangle.
        """
        base = float(base)
        height = float(height)
        if base <= 0 or height <= 0:
             raise TypeError("base and height must be positive")
        return 1 / 2 * base * height




