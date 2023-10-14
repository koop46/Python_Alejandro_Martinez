from Lab_3 import *


#def test_value_error():
 #   assert str(rec2.translate("sju", 7)) ==   "Sorry, you can only input numbers."

def test_operator_overload():

    assert not rec1 == ci2
    assert ci1 < ci2
    assert rec2 > rec1
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
    assert rec2.area == 404

    rec2 = Rectangle(x=1,y=1, side=-2, side2=3)
    assert rec2.area == 404


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


# def test_is_inside_edge():
#     ...

# def test_is_inside_curve():
#     ...

# def test_is_square():
# def test_is_unit_circle()


rec1 = Rectangle(x=0, y=0, side=5, side2=6)
rec2 = Rectangle(x=1,y=1, side=2, side2=3)
ci1 = Circle(x=0, y=0, radius=4)
ci2 = Circle(x=1, y=1, radius=3)
sp1 = Sphere(1,1,1, radius=1)
sp2 = Sphere(4,4,4, radius=4)
cu1 = Cube(3,3,3, side=3)
cu2 = Cube(2,2,2, side=2)

