# This is a Processing.py port of a Nodebox script:
# "Aquatics!" by Lieven Menschaert 
# https://www.nodebox.net/code/index.php/Aquatics

class Aquatic:

    def __init__(self, x ,y, size, fillcolor):
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

    def pupil(self, x, y, g):
        # normal
        if not random(1) > .85:
            s = g/4 + random(g/3)
            fill(self.r*2.0, self.g, self.b, self.a/2.0)
            stroke(self.r, self.g/2, self.b,.6)
            strokeWeight(2.0)
            ran = random(s/2, -s/2)
            ellipse(x, y, s*2, s*2)
            fill(1)
            strokeWeight(5.0)
            stroke(0)
            ellipse(x-s/4+ran, y-s/4+ran, s/2, s/2)
        # spiral
        else:
            l = random(1)
            fill(0)
            stroke(self.r, self.g/2, self.b, 1.0)
            strokeWeight(0.5)
            
            for i in range(100):
                v = x+i/5.0 * sin(i*l)
                w = y+i/5.0 * cos(i*l)
                ellipse(v, w, 2, 2)

    def shield(self, x, y, g):
        seg = ellipse(x-g, y-g, g*2, g*2, draw = False)
        pad = rect(x-g,y-random(10.0,-4.0),g*2,g*2,draw = False)
        pc = pad
        pad = pad.union(seg)
        pad = pad.difference(pc,False)
        fill(self.r,self.g,self.b,1.0)
        stroke(0);strokewidth(1.0)
        drawpath(pad)
        return(pad)

    def drawEyes(self, eyex, eyey, eyesize):

        if random(1) > 0.5:
            stroke(self.r/2, self.g/2, self.b/2, 255)
            strokeWeight(3.0)
        
            for eyelash in range( 2, int(random(10)) ):
                lashx = random(-eyesize*1.5, eyesize*1.5)
                lashy = random(-eyesize*1.5, eyesize/2)
                line(eyex, eyey, eyex+lashx, eyey+lashy)

        fill(255)
        stroke(0)
        strokeWeight(2)
        ellipse(eyex, eyey, eyesize*2, eyesize*2)
        self.pupil(eyex, eyey, eyesize)
    
    '''
    def linedash(self, path, segment, gap):
        path._nsBezierPath.setLineDash_count_phase_([segment,gap],2,0)
        return path
    '''

    def superShape(self, m, n1, n2, n3, a, b, radius, start, stop, 
                   xoff=0, yoff=0, xdistort=1, cw=True):
        
        def superShapeVertex(theta):
            t1 = pow( abs( (1.0/a) * cos(theta*m/4) ), n2 )
            t2 = pow( abs( (1.0/b) * sin(theta*m/4) ), n3 )
            t3 = pow(t1+t2, 1.0/n1)
            x = (t3 * cos(theta) * xdistort * radius) + xoff
            y = (t3 * sin(theta) * radius) + yoff
            vertex(x,y)
        
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

    def draw(self):
        
        # outline and mouth
        m = int(random(1,30))
        if random(1) > 0.5:
            n1 = -.8-random(5.0)
        else:
            n1 = .8+random(5.0)
        n2 = .5+random(5.0)
        n3 = .5+random(.5,-1.5)
        fill(self.f)
        stroke(self.r/2, self.g/2, self.b/2) 
        strokeWeight(self.s/20)

        rotate(HALF_PI)
        translate(self.x, -self.y)

        beginShape()
        a = random(0.7, 1.2); b = 1
        self.superShape(m, n1, n2, n3, a, b, self.s, 0.5, TWO_PI-0.5)
        a = random(0.9, 1.1); b = random(0.9, 1.1)
        radius = self.s*random(0.2,0.5)
        m = 4+random(20)
        n3 = 0.81+random(-0.8,0.8)
        xoff = self.s/(random(1, 1.5))
        self.superShape(m, 0.98, 3.0, n3, a, b, radius, PI+HALF_PI, HALF_PI, 
                        xoff=xoff, xdistort=1.5, cw=False)
        endShape(CLOSE)

        rotate(-HALF_PI)
        translate(-self.x, -self.y)

        # eye locations
        for i in range( 2+int(random(6)) ):
            eyex = self.x + random(-self.s, self.s)
            eyey = self.y + random(-self.s/2)
            g = 5+random(self.s/5.0)
            
            tup = (eyex, eyey, g)
            self.eyelist.append(tup)
        
        for eye in self.eyelist:
            self.drawEyes(eye[0], eye[1], eye[2])
            '''
            if header.p.contains(xx, yy):
                tup = xx, yy, g
                self.eyelist.append(tup)
            '''
        mouth = []
        '''
        for p in l:
            if self.p.contains(p.x,p.y):
                loc = p.x,p.y
                mouth.append(loc)
                if random() < .01 and p.y < (self.s*4.8):
                    fill(1);strokewidth(5)
                    k = (-45,0,45)
                    # teeth __ not to pleased about them
                    stroke(self.r/2,self.g/2,self.b/2,1.0)
                    si = 10+random(self.s*.1)
                    if not p.x < self.x:
                        skew(choice(k))
                        rect(p.x+si/2,p.y,-si,-si)
                        reset()
                    else:
                        skew(choice(k))
                        rect(p.x-si/2,p.y,si,si)
                        reset()
        '''
        #drawpath(self.p)
        # lips
        for o in mouth:
            s = 1.5
            fill( (self.r+self.g)*0.8, (self.g+self.b)*0.8, (self.b+self.r)*0.8, 0.5 )
            noStroke()
            ellipse(o[0]-s, o[1]-s, s*2, s*2)
        '''
        self.geefpad()
        
        def geefpad(self):
            return self.p
        '''

size(500,500)
background('#D7E1FA')
fillcolor = color(random(255), random(255), random(255))
aquatic = Aquatic(width/2, height/2, 100, fillcolor)
aquatic.draw()
