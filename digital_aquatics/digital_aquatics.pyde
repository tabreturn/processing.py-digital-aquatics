# This is a Processing.py port of a Nodebox script:
# "Aquatics!" by Lieven Menschaert 
# https://www.nodebox.net/code/index.php/Aquatics

size(800,600)

class Aquatic:
    
    def __init__(self,x ,y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.r = red(self.c)
        self.g = green(self.c)
        self.b = blue(self.c)
        self.a = alpha(self.c)
        self.eyelist = []
        #self.backpad = ellipse(10,10,0,0)
        #self.backpadintern = []
        #self.backpadextern = []

    def pupil(self, x, y, g):
        # normal
        if not random(1) > .85:
            s = g/4 + random(g/3)
            fill(self.c.r*2.0, self.c.g, self.c.b, self.c.a/2.0)
            stroke(self.c.r, self.c.g/2, self.c.b,.6)
            strokeWeight(2.0)
            ran = random(s/2, -s/2)
            ellipse(x-s+ran, y-s+ran, s*2, s*2)
            fill(1)
            strokeWeight(5.0)
            stroke(0)
            ellipse(x-s/4+ran, y-s/4+ran, s/2, s/2)
        # spiral
        else:
            l = random(1)
            fill(0)
            stroke(self.c.r, self.c.g/2, self.c.b, 1.0)
            strokewidth(0.5)
            
            for i in range(100):
                v = x+i/5.0 * sin(i*l)
                w = y+i/5.0 * cos(i*l)
                ellipse(v, w, 2, 2)

    def pupil(self, x, y, g):

        if not random(1) > .85:
            # normal
            s = g/4 + random(g/3)
            fill(self.r*2.0, self.g, self.b, self.a/2.0)
            stroke(self.r, self.g/2, self.b, 0.6)
            strokeWeight(2.0)
            ran = random(s/2, -s/2)
            ellipse(x-s+ran, y-s+ran, s*2, s*2)
            fill(1)
            strokeWeight(5.0)
            stroke(0)
            ellipse(x-s/4+ran, y-s/4+ran, s/2, s/2)
        else:
            # spiral
            l = random(1)
            fill(0)
            stroke(self.r, self.g/2, self.b, 1.0)
            strokeWeight(0.5)
            for i in range(100):
                v = x+i/5.0 * sin(i*l)
                w = y+i/5.0 * cos(i*l)
                ellipse(v,w,2,2)
    
    '''
    def shield(self, x, y, g):
        seg = ellipse(x-g, y-g, g*2, g*2, draw = False)
        pad = rect(x-g,y-random(10.0,-4.0),g*2,g*2,draw = False)
        pc = pad
        pad = pad.union(seg)
        pad = pad.difference(pc,False)
        fill(self.c.r,self.c.g,self.c.b,1.0)
        stroke(0);strokewidth(1.0)
        drawpath(pad)
        return(pad)
    '''            
    def eyes(self, xx, yy, g):
        fill(1)
        stroke(0)
        strokeWeight(2.0)
        ellipse(xx-g, yy-g, g*2, g*2)
        self.pupil(xx, yy, g)
        
        if random(1) > 0.5:
            #cover = self.shield(xx, yy, g)
            f = [xx, yy]
            stroke(self.r/2, self.g/2, self.b/2, 1.0)
            strokeWeight(3.0)
            
            '''
            for eyelash in cover:
                if random(1) > 0.5:
                    x = eyelash.x-f[0]
                    y = eyelash.y-f[1]
                    lx = random(x)
                    ly = random(y)
                    line(eyelash.x, eyelash.y, eyelash.x+lx, eyelash.y+ly)
            '''        
    '''
    def linedash(self, path, segment, gap):
        path._nsBezierPath.setLineDash_count_phase_([segment,gap],2,0)
        return path
    '''
    
    def superShape(self, m, n1, n2, n3, a, b, radius, start, stop, xoff=0, yoff=0, xdistort=1, cw=True):
        
        def drawVertex(theta):
            t1 = pow( abs( (1.0/a) * cos(theta*m/4) ), n2 )
            t2 = pow( abs( (1.0/b) * sin(theta*m/4) ), n3 )
            t3 = pow(t1+t2, 1.0/n1)
            
            x = (t3 * cos(theta) * xdistort * radius) + xoff
            y = (t3 * sin(theta) * radius) + yoff
            vertex(x,y)
        
        if cw:
            theta = start
            while theta < stop:
                drawVertex(theta)
                theta += 0.1
        
        else:
            theta = start
            while theta > stop:
                drawVertex(theta)
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
        fill(self.c)
        stroke(self.r/2, self.g/2, self.b/2) 
        strokeWeight(self.w/20)
        rotate(HALF_PI)
        beginShape()
        a = random(0.7, 1.2); b = 1
        self.superShape(m, n1, n2, n3, a, b, self.h, 0.5, TWO_PI-0.5)
        a = random(0.9, 1.1); b = random(0.9, 1.1)
        radius = self.h*random(0.2,0.5)
        m = 4+random(20)
        n3 = 0.81+random(-0.8,0.8)
        xoff = self.h/(random(1, 1.5))
        self.superShape(m, 0.98, 3.0, n3, a, b, radius, PI+HALF_PI, HALF_PI, 
                        xoff=xoff, xdistort=1.5, cw=False)
        endShape(CLOSE)
        rotate(-HALF_PI)
        
        # eye locations
        for i in range( 2+int(random(10)) ):
            xx = self.x+random(-self.w, self.w)
            yy = self.y+random(-self.h)
            g = 5+random(self.w/5.0)
            
            tup = xx, yy, g
            self.eyelist.append(tup)
        
        for eye in self.eyelist:
            self.eyes(eye[0], eye[1], eye[2])
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
                if random() < .01 and p.y < (self.h*4.8):
                    fill(1);strokewidth(5)
                    k = (-45,0,45)
                    # teeth __ not to pleased about them
                    stroke(self.c.r/2,self.c.g/2,self.c.b/2,1.0)
                    si = 10+random(self.w*.1)
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

translate(width/2, height/2)
orange = color(255,153,0)
#(3.7, 4.8, 1.7, 5, 1, 1, 100)
a = Aquatic(width/2, height/2, 100, 200, orange)
a.draw()
