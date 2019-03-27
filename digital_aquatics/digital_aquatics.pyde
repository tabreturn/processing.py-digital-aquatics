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
        self.current = [random(-self.s/8,self.s/8), 
                        random(-self.s/8,self.s/8)]
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
        fill(self.r, self.g, self.b, random(200,240))
        stroke(self.r/2, self.g/2, self.b/2)
        strokeWeight(1)
        arc(x, y, size*2, size*2, PI, TWO_PI, CHORD);

    def drawEyes(self, eyex, eyey, eyesize):
        stroke(self.r/2, self.g/2, self.b/2)

        # eyelashes
        if random(1) > 0.3:
            strokeWeight(2)
            translate(eyex,eyey)
            rot = 0

            for eyelash in range( int(random(3,8)) ):
                randomrot = random(0.2,0.7)
                rot += randomrot
                rotate(randomrot)
                line(0, 0, random(-eyesize*2,-eyesize*1.2), 0)

            rotate(-rot)
            translate(-eyex,-eyey)

        # eye
        fill(255)
        strokeWeight(2)
        ellipse(eyex, eyey, eyesize*2, eyesize*2)
        self.drawIrisPupil(eyex, eyey, eyesize)

        # eyelid
        if random(1) > 0.5:
            cover = self.drawEyeLid(eyex, eyey, eyesize)

    def drawHair(self, hairx, hairy, hairlength, angle):
        tipx = cos(angle) * hairlength
        tipy = sin(angle) * hairlength
        curve(hairx-random(-100,100), hairy+random(-100,100), 
              hairx, hairy, 
              tipx+self.current[0], tipy+self.current[1], 
              tipx-random(-100,100), tipy+random(-100,100))

    def superShape(self, m, n1, n2, n3, a, b, radius, start, stop, 
                   xoff=0, yoff=0, xdistort=1, cw=True, drawhairs=False):
        
        def superShapeVertex(angle):
            t1 = pow( abs( (1.0/a) * cos(angle*m/4) ), n2 )
            t2 = pow( abs( (1.0/b) * sin(angle*m/4) ), n3 )
            t3 = pow(t1+t2, 1.0/n1)
            x = (t3 * cos(angle) * xdistort * radius) + xoff
            y = (t3 * sin(angle) * radius) + yoff
            return [x,y]

        # plot supershape clock/counter-clockwise
        # drawing hairs only works on clockwise
        angle = start
        tuftstart = random(0,PI)
        tuftend = random(PI,TWO_PI)

        if cw:
            while angle < stop:
                xy = superShapeVertex(angle)
                if not drawhairs:
                    vertex(xy[0],xy[1])
                else:
                    noFill()
                    stroke(self.r/2, self.g/2, self.b/2, 200) 
                    strokeWeight(0.8)
                    self.drawHair(xy[0],xy[1], radius*random(1.1,1.2), angle)
                    if angle > tuftstart and angle < tuftend:
                        strokeWeight(2)
                        self.drawHair(xy[0],xy[1], radius*random(1.3,1.5), angle)
                angle += 0.05
        else:
            while angle > stop:
                xy = superShapeVertex(angle)
                vertex(xy[0],xy[1])
                angle -= 0.05

    def drawAquatic(self):
        # outline/mouth variables
        m = int( random(1,30) )

        if random(1) > 0.5:
            n1 = -0.8-random(5)
        else:
            n1 = 0.8+random(5)

        n2 = 0.5+random(5)
        n3 = 0.5+random(0.5,-1.5)

        # nucleus
        rot = random(-PI,PI)
        xoff = self.x-self.s/3 * (1 if random(1) < 0.5 else -1)
        yoff = self.y-self.s/random(1.5,20)
        translate(xoff, yoff)
        rotate(rot)
        fill(self.r/2, self.g/2, self.b/2, 80)
        noStroke()
        ellipse(0, 0, self.s/random(1.5,5), self.s/random(1.5,5))
        fill(self.r/3, self.g/3, self.b/3, 120)
        ellipse(0, 0, self.s/6, self.s/6)
        rotate(-rot)
        translate(-xoff, -yoff)

        # supershapes
        rot = random(HALF_PI-0.2, HALF_PI+0.2)
        translate(self.x,self.y)
        rotate(rot)
        #hairs
        a = random(0.7,1.2)
        b = 1
        if random(1) > 0.3:
            self.superShape(m, n1, n2, n3, a, b, self.s, 0.5, TWO_PI-0.5, 
                            drawhairs=True)
        # body
        fill(self.f)
        stroke(self.r/2, self.g/2, self.b/2) 
        strokeWeight(self.s/22.5)
        beginShape()
        self.superShape(m, n1, n2, n3, a, b, self.s, 0.5, TWO_PI-0.5)
        #mouth
        m = 4+random(20)
        n3 = 0.81+random(-0.8,0.8)
        a = random(0.9,1.1)
        b = random(0.9,1.1)
        radius = self.s*random(0.2,0.4)
        xoff = self.s/(random(0.9,1.1))
        self.superShape(m, 0.98, 3.0, n3, a, b, radius, PI+HALF_PI, HALF_PI, 
                        xoff=xoff, xdistort=1.5, cw=False)
        endShape(CLOSE)
        # freckles
        fill(self.r*1.8, self.g*1.8, self.b*1.8, 200)
        noStroke()
        for i in range(80):
            freckx = i/self.s*40 * sin(i*15)+random(1,10)
            frecky = i/self.s*90 * cos(i*15)+random(1,10)
            dotsize = random(1,6)
            ellipse(freckx,frecky, dotsize,dotsize)
        # lips
        noFill()
        stroke(self.r/2, self.g/2, self.b/2) 
        strokeWeight(self.s/12.0)
        beginShape()
        self.superShape(m, 0.98, 3.0, n3, a, b, radius, PI+HALF_PI, HALF_PI, 
                        xoff=xoff, xdistort=1.5, cw=False)
        endShape()
        stroke((self.r+self.g)*0.8,
               (self.g+self.b)*0.8,
               (self.b+self.r)*0.8,
               128)
        strokeWeight(self.s/22.5)
        beginShape()
        self.superShape(m, 0.98, 3.0, n3, a, b, radius, PI+HALF_PI, HALF_PI, 
                        xoff=xoff, xdistort=1.5, cw=False)
        endShape()
        rotate(-rot); translate(-self.x,-self.y)

        # eye locations
        eyex = self.x-self.s-random(self.s/10)

        for i in range( 3+int(random(10)) ):
            
            if eyex < self.x+self.s-self.s/2:
                eyex = eyex+random(-10,10)
                eyex += random(30,50)
                eyey = self.y+random(-self.s/2)
                eyesize = 8+random(self.s/5.0)
                
                tup = (eyex, eyey, eyesize)
                self.eyelist.append(tup)
        
        for eye in self.eyelist:
            self.drawEyes(eye[0], eye[1], eye[2])

size(500,500)
background('#D7E1FA')
fillcolor = color(random(255), 
                  random(255), 
                  random(255),
                  random(128,230))

aquatic = Aquatic(width/2, height/2, random(80,150), fillcolor)
aquatic.drawAquatic()
