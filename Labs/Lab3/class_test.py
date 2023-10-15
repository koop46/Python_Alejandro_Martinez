from Lab_3 import *


def test_operator_overload():
    rec1 = Rectangle(x=0, y=0, side=5, side2=6)
    rec2 = Rectangle(x=1,y=1, side=2, side2=3)
    ci1 = Circle(x=0, y=0, radius=4)
    ci2 = Circle(x=1, y=1, radius=3)

    assert not rec1 == ci2
    assert rec2 > rec1
    assert ci1 < ci2

    sp1 = Sphere(1,1,1, radius=1)
    sp2 = Sphere(4,4,4, radius=4)
    cu1 = Cube(3,3,3, side=3)
    cu2 = Cube(2,2,2, side=2)

    assert not sp1 >= sp2
    assert not cu1 <= cu2


def test_area():

    ci2 = Circle(x=1, y=1, radius=5)
    assert round(ci2.area, 2) == 78.54

    ci2 = Circle(x=1, y=1, radius=-5)
    assert round(ci2.area, 2) == 78.54

    rec2 = Rectangle(x=1,y=1, side=2, side2=3)
    assert rec2.area == 6

    rec2 = Rectangle(x=1,y=1, side=2, side2=-3)
    assert rec2.area == 404 #Error

    rec2 = Rectangle(x=1,y=1, side=-2, side2=3)
    assert rec2.area == 404 #Error


def test_circumference():

    rec1 = Rectangle(x=0, y=0, side=5.4, side2=6.3)
    assert rec1.circumference == 23.4

    rec1 = Rectangle(x=0, y=0, side=5, side2=-6)
    assert rec1.circumference != 22

    rec1 = Rectangle(x=0, y=0, side=-5, side2=6)
    assert rec1.circumference == 404 #error

    ci1 = Circle(x=0, y=0, radius=4)
    assert round(ci1.circumference, 2) == 25.13

    ci1 = Circle(x=0, y=0, radius=-4)
    assert round(ci1.circumference, 2) == 404 #error


def test_volume():
    
    sp1 = Sphere(1,1,1, radius=3)
    assert round(sp1.volume, 2) == 113.10

    sp1 = Sphere(1,1,1, radius=-3)
    assert round(sp1.volume, 2) != 113.10


def test_is_inside_edge():
 
    rec1 = Rectangle(x=0, y=0, side=5, side2=6)
    assert rec1.is_inside_edge(0.5,0.5) == True
    rec1.translate(5,5)
    assert rec1.is_inside_edge(0.5,0.5) == False

    cu1 = Cube(x=0,y=0,z=0, side=3)
    assert cu1.is_inside_edge(-3,-3,3) == False
    assert cu1.is_inside_edge(1.5, 1.5, 1.4) == False


def test_is_inside_curve():

    ci1 = Circle(x=0, y=0, radius=4)
    assert ci1.is_inside_curve(4,4) == False
    assert ci1.is_inside_curve(-2.6,-3) == True

    sp1 = Sphere(x=0, y=0, z=0, radius=3)
    assert sp1.is_inside_curve(-3, -3, -3) == False
    assert sp1.is_inside_curve(1.5, 1.5, 1.4) == True
    sp1.translate(x=-1.5, y=-1.5, z=-1.5)
    assert sp1.is_inside_curve(1.5, 1.5, 1.4) == False


def test_is_square():
    sq = Rectangle(x=0, y=0, side=5, side2=5)
    assert sq.is_square() == True
    
    rec1 = Rectangle(x=0, y=0, side=5, side2=6)
    assert rec1.is_square() == False

    rec1 = Rectangle(x=0, y=0, side=6, side2=5)
    assert rec1.is_square() == False


def test_is_unit_circle():
    ci1 = Circle(x=0, y=0, radius=4)
    assert ci1.is_unit_circle() == False
    ci1.radius = 1
    assert ci1.is_unit_circle() == True
    

def test_value_error():

    rec2 = Rectangle(x=1,y=1, side=2, side2=3)
    assert rec2.is_inside_edge(1.5,1.7) == True    
    rec2.translate("7", 7)
    assert rec2.is_inside_edge(1.5,1.7) == False
    rec2.translate(1, "1")
    assert rec2.is_inside_edge(1.5,1.7) == True    
    rec2.translate("seven", "seven")
    assert rec2.is_inside_edge(1.5,1.7) == True
    x = rec2.x
    assert x == 1
    y = rec2.y
    assert y == 1


