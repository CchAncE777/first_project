import math



def Circle(radius):
    Perimeter_Circle_Cm = 2 * radius * math.pi 
    Perimeter_Circle_M = Perimeter_Circle_Cm * 0.01 
    print(f'Периметр круга в сантиметрах: {Perimeter_Circle_Cm } См') 
    print(f'Периметр круга в метрах: {Perimeter_Circle_M} М')

def Quadrate(radius):
    Quadrate_Side_Entered_Cm =  radius * math.sqrt(2) 
    Quadrate_Side_Entered_M = Quadrate_Side_Entered_Cm * 0.01 
    print(f'Сторона вписанного квадрата в сантиметрах: {Quadrate_Side_Entered_Cm} См') 
    print(f'Сторона вписанного квадрата в метрах: {Quadrate_Side_Entered_M} М') 

def Triangle(radius):
    Triangle_Side_Entered_Cm = radius * math.sqrt(3) 
    Triangle_Side_Entered_M = Triangle_Side_Entered_Cm * 0.01 
    print(f'Сторона вписанного равностороннего треугольника в сантиметрах: {Triangle_Side_Entered_Cm} См') 
    print(f'Сторона вписанного равностороннего треугольника в метрах: {Triangle_Side_Entered_M} М')

def Octagon(radius):
    Octagon_Side_Described_Cm = radius * 2 * math.tan(22.5) 
    Octagon_Side_Described_M = Octagon_Side_Described_Cm * 0.01 
    print(f'Сторона описанного восьмиугольника в сантиметрах: {Octagon_Side_Described_Cm} См') 
    print(f'Сторона описанного восьмиугольника в метрах: {Octagon_Side_Described_M} М') 

def main():
    Circle(5)
    Quadrate(5)
    Triangle(5)
    Octagon(5)

if __name__ == '__main__':
    main()