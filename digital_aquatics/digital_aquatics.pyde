# This is a Processing.py port of a Nodebox script:
# "Aquatics!" by Lieven Menschaert 
# https://www.nodebox.net/code/index.php/Aquatics

class Aquatic:

    def __init__(self, x ,y, size, fillcolor):
        # main variables
        self.x = x
        self.y = y
        self.s = size
        self.f = fillcolor
        self.r = red(self.f)
        self.g = green(self.f)
        self.b = blue(self.f)
        self.a = alpha(self.f)
        self.eyelist = []
        #self.backpad = ellipse(10,10,0,0)
        #self.backpadintern = []
        #self.backpadextern = []

    def drawIrisPupil(self, x, y, size):
        s = size/4 + random(size/3)

        # iris
        fill(self.r*2, self.g, self.b, self.a/2)
        stroke(self.r, self.g/2, self.b, 140)
        strokeWeight(2)
        ellipse(x, y, s*2, s*2)

        # pupil
        fill(1)
        stroke(0)
        strokeWeight(5)
        ellipse(x, y, s/2, s/2)
    
    def drawEyeLid(self, x, y, size):
        fill(self.f)
        stroke(self.r/2, self.g/2, self.b/2)
        strokeWeight(1)
        arc(x, y, size*2, size*2, PI, TWO_PI, CHORD);

    def drawEyes(self, eyex, eyey, eyesize):
        stroke(self.r/2, self.g/2, self.b/2)

        # eyelashes
        if random(1) > 0.3:
            strokeWeight(3)
        
            for eyelash in range( int(random(8)) ):

                if random(1) > 0.5:
                    lashx = random(-eyesize*1.5, 0)
                else:
                    lashx = random( eyesize*1.5, 0)

                lashy = random(-eyesize*2, eyesize/2)
                line(eyex, eyey, eyex+lashx, eyey+lashy)

        # eye
        fill(255)
        strokeWeight(2)
        ellipse(eyex, eyey, eyesize*2, eyesize*2)
        self.drawIrisPupil(eyex, eyey, eyesize)
        # eyelid
        if random(1) > 0.5:
            cover = self.drawEyeLid(eyex, eyey, eyesize)
    
    '''
    def linedash(self, path, segment, gap):
        path._nsBezierPath.setLineDash_count_phase_([segment,gap],2,0)
        return path
    '''

    def superShapeVertices(self, m, n1, n2, n3, a, b, radius, start, stop, 
                           xoff=0, yoff=0, xdistort=1, cw=True):
        
        def superShapeVertex(theta):
            t1 = pow( abs( (1.0/a) * cos(theta*m/4) ), n2 )
            t2 = pow( abs( (1.0/b) * sin(theta*m/4) ), n3 )
            t3 = pow(t1+t2, 1.0/n1)
            x = (t3 * cos(theta) * xdistort * radius) + xoff
            y = (t3 * sin(theta) * radius) + yoff
            vertex(x,y)

        # plot supershape clock/counter-clockwise
        if cw:
            theta = start
            while theta < stop:
                superShapeVertex(theta)
                theta += 0.1
        else:
            theta = start
            while theta > stop:
                superShapeVertex(theta)
                theta -= 0.1

    def drawAquatic(self):

        # outline/mouth variables
        m = int( random(1,30) )
        if random(1) > 0.5:
            n1 = -0.8-random(5)
        else:
            n1 =  0.8+random(5)
        n2 = 0.5+random(5)
        n3 = 0.5+random(0.5,-1.5)

        # outline/mouth properties
        fill(self.f)
        stroke(self.r/2, self.g/2, self.b/2) 
        strokeWeight(self.s/22.5)
        r = random(HALF_PI-0.2, HALF_PI+0.2)

        # supershapes
        translate(self.x, self.y); rotate(r)
        # body
        beginShape()
        a = random(0.7, 1.2)
        b = 1
        self.superShapeVertices(m, n1, n2, n3, a, b, self.s, 
                                0.5, TWO_PI-0.5)
        #mouth
        m = 4+random(20)
        n3 = 0.81+random(-0.8,0.8)
        a = random(0.9, 1.1)
        b = random(0.9, 1.1)
        radius = self.s*random(0.2,0.4)
        xoff = self.s/(random(0.9,1.1))
        self.superShapeVertices(m, 0.98, 3.0, n3, a, b, radius, 
                                PI+HALF_PI, HALF_PI, 
                                xoff=xoff, xdistort=1.5, cw=False)
        endShape(CLOSE)
        # lips
        noFill()
        strokeWeight(self.s/12.0)
        beginShape()
        self.superShapeVertices(m, 0.98, 3.0, n3, a, b, radius, 
                                PI+HALF_PI, HALF_PI, 
                                xoff=xoff, xdistort=1.5, cw=False)
        endShape()
        stroke((self.r+self.g)*0.8,
               (self.g+self.b)*0.8,
               (self.b+self.r)*0.8,
               128)
        strokeWeight(self.s/22.5)
        beginShape()
        self.superShapeVertices(m, 0.98, 3.0, n3, a, b, radius, 
                                PI+HALF_PI, HALF_PI, 
                                xoff=xoff, xdistort=1.5, cw=False)
        endShape()
        rotate(-r); translate(-self.x, -self.y)

        # eye locations
        eyex = self.x - self.s

        for i in range( 3+int(random(10)) ):
            
            if eyex < self.x + self.s - self.s/2:
                eyex = eyex + random(-10, 10)
                eyex += random(30, 50)
                eyey = self.y + random(-self.s/2)
                eyesize = 5+random(self.s/5.0)
                
                tup = (eyex, eyey, eyesize)
                self.eyelist.append(tup)
        
        for eye in self.eyelist:
            self.drawEyes(eye[0], eye[1], eye[2])
        

        '''
        self.geefpad()
        
        def geefpad(self):
            return self.p
        '''

size(500,500)
background('#D7E1FA')
fillcolor = color(random(255), random(255), random(255))
aquatic = Aquatic(width/2, height/2, 100, fillcolor)
aquatic.drawAquatic()
