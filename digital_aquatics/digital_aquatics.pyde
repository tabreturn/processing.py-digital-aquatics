size(600,600)

def supershape(theta, n1, n2, n3, m, a, b):
    t1 = pow( abs( (1/a) * cos(theta*m/4) ), n2 )
    t2 = pow( abs( (1/b) * sin(theta*m/4) ), n3 )
    t = pow(t1+t2, 1/n1)
    
    if t == 0:
        return 0

    return 1/t

translate(width/2, height/2)
angle = 0.0
radius = 100

beginShape()

while angle < TWO_PI:
    r = supershape(angle, 0.3, 2, 3, 7, 1, 1)
    x = r * cos(angle) * radius
    y = r * sin(angle) * radius
    vertex(x,y)
    angle += 0.1

endShape(CLOSE)
