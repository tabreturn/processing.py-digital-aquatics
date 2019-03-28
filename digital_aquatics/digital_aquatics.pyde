# This is a Processing.py adaption of the Nodebox script:
# "Aquatics!" by Lieven Menschaert (using Johan Gielis' Superformula equations)
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
        self.currentx = random(-self.s/8, self.s/8)
        self.currenty = random(-self.s/8, self.s/8)
        strokeJoin(ROUND)

    def drawIrisPupil(self, pupilx, pupily, pupilsize):
        s = pupilsize/4 + random(pupilsize/3)

        # iris
        fill(self.r*2, self.g, self.b, self.a/2)
        stroke(self.r, self.g/2, self.b, 140)
        strokeWeight(2)
        ellipse(pupilx, pupily, s*2, s*2)

        # pupil
        fill(1)
        stroke(0)
        strokeWeight(5)
        ellipse(pupilx, pupily, s/2, s/2)

    def drawEyeLid(self, eyex, eyey, eyesize):
        fill(self.r, self.g, self.b, random(200, 240))
        stroke(self.r/2, self.g/2, self.b/2)
        strokeWeight(1)
        arc(eyex, eyey, eyesize*2, eyesize*2, PI, TWO_PI, CHORD)

    def drawEyes(self, eyex, eyey, eyesize):
        stroke(self.r/2, self.g/2, self.b/2)

        # eyelashes
        if random(1) > .3:
            strokeWeight(2)
            translate(eyex, eyey)
            rot = 0

            for eyelash in range( int(random(3, 8)) ):
                randomrot = random(.2, .7)
                rot += randomrot
                rotate(randomrot)
                line(0, 0, random(-eyesize*2, -eyesize*1.2), 0)

            rotate(-rot)
            translate(-eyex, -eyey)

        # eye
        fill(255)
        strokeWeight(2)
        ellipse(eyex, eyey, eyesize*2, eyesize*2)
        self.drawIrisPupil(eyex, eyey, eyesize)

        # eyelid
        if random(1) > .5:
            cover = self.drawEyeLid(eyex, eyey, eyesize)

    def drawHair(self, hairx, hairy, hairlength, angle):
        tipx = cos(angle) * hairlength
        tipy = sin(angle) * hairlength
        curve(hairx-random(-100, 100), hairy+random(-100, 100),
              hairx, hairy,
              tipx+self.currentx, tipy+self.currenty,
              tipx-random(-100, 100), tipy+random(-100, 100))

    def superShape(self, m, n1, n2, n3, a, b, radius, start, stop,
                   xoff=0, yoff=0, xdistort=1, cw=True, mode='vertex'):
        # https://en.wikipedia.org/wiki/Superformula
        def superShapeVertex(angle):
            t1 = pow( abs( (1.0/a) * cos(angle*m/4) ), n2 )
            t2 = pow( abs( (1.0/b) * sin(angle*m/4) ), n3 )
            t3 = pow(t1+t2, 1.0/n1)
            x = (t3 * cos(angle) * xdistort * radius) + xoff
            y = (t3 * sin(angle) * radius) + yoff
            return [x, y]

        # plot supershape clock/counter-clockwise
        # drawing hairs only works with cw=True
        angle = start
        tuftstart = random(0, PI)
        tuftend = random(PI, TWO_PI)

        if cw:
            while angle < stop:
                xy = superShapeVertex(angle)
                if mode == 'vertex':
                    vertex(xy[0], xy[1])
                elif mode == 'hair':
                    noFill()
                    stroke(self.r/2, self.g/2, self.b/2, 200)
                    strokeWeight(.8)
                    self.drawHair(xy[0], xy[1], radius*random(1.1, 1.2), angle)
                    if angle > tuftstart and angle < tuftend:
                        strokeWeight(2)
                        hairlength = radius*random(1.3, 1.5)
                        self.drawHair(xy[0], xy[1], hairlength, angle)
                angle += .05
        else:
            while angle > stop:
                xy = superShapeVertex(angle)
                vertex(xy[0], xy[1])
                angle -= .05

    def drawAquatic(self):
        # outline/mouth variables
        # b_ for body; m_ for mouth
        n1 = (-.8-random(5) if random(1) < .5 else .8+random(5))
        n2 = .5 + random(5)
        ba = random(.7, 1.2)
        bb = 1
        bm = int( random(1, 30) )
        bn3 = .5 + random(.5, -1.5)
        ma = random(.9, 1.1)
        mb = random(.9, 1.1)
        mm = 4 + random(20)
        mn3 = .81 + random(-.8, .8)
        mradius = self.s * random(.2, .4)
        mxoff = self.s / random(.9, 1.1)

        # nucleus
        rot = random(-PI, PI)
        xoff = self.x-self.s/3 * (1 if random(1) < .5 else -1)
        yoff = self.y-self.s / random(1.5, 20)
        translate(xoff, yoff)
        rotate(rot)
        fill(self.r/2, self.g/2, self.b/2, 80)
        noStroke()
        ellipse(0, 0, self.s/random(1.5, 5), self.s/random(1.5, 5))
        fill(self.r/3, self.g/3, self.b/3, 120)
        ellipse(0, 0, self.s/6, self.s/6)
        rotate(-rot)
        translate(-xoff, -yoff)

        # supershapes
        rot = random(HALF_PI-.3, HALF_PI+.3)
        translate(self.x, self.y)
        rotate(rot)
        #hairs
        if random(1) > .3:
            self.superShape(bm, n1, n2, bn3, ba, bb, self.s, .5, TWO_PI-.5,
                            mode='hair')
        # ectoplasm
        noFill()
        stroke(255, 255, 255, 180)
        strokeWeight(self.s/8)
        beginShape()
        self.superShape(bm, n1, n2, bn3, ba, bb, self.s-self.s/12, .5, TWO_PI-.5)
        endShape()
        # s's
        fill(self.r/2, self.g/2, self.b/2, 40)
        for i in range( int(random(2,5)) ):
            play = self.s/4
            textSize( random(self.s/4, play) )
            rot = random(TWO_PI)
            rotate(rot)
            text('S', random(-play,play), random(-play,play))
            rotate(-rot)
        # body
        fill(self.r, self.g, self.b, 120)
        stroke(self.r/2, self.g/2, self.b/2)
        strokeWeight(self.s/22.5)
        beginShape()
        self.superShape(bm, n1, n2, bn3, ba, bb, self.s, .5, TWO_PI-.5)
        # mouth
        self.superShape(bm, .98, 3, bn3, ma, mb, mradius, PI+HALF_PI, HALF_PI,
                        xoff=mxoff, xdistort=1.5, cw=False)
        endShape(CLOSE)
        # freckles
        fill(self.r*1.8, self.g*1.8, self.b*1.8, 200)
        noStroke()
        for i in range(80):
            freckx = i/self.s*40 * sin(i*15) + random(1, 10)
            frecky = i/self.s*90 * cos(i*15) + random(1, 10)
            dotsize = random(1, 6)
            ellipse(freckx, frecky, dotsize, dotsize)
        # lips
        noFill()
        stroke(self.r/2, self.g/2, self.b/2)
        strokeWeight(self.s/12.0)
        beginShape()
        self.superShape(bm, .98, 3, bn3, ma, mb, mradius, PI+HALF_PI, HALF_PI,
                        xoff=mxoff, xdistort=1.5, cw=False)
        endShape()
        stroke((self.r + self.g) * .8,
               (self.g + self.b) * .8,
               (self.b + self.r) * .8,
               128)
        strokeWeight(self.s/22.5)
        beginShape()
        self.superShape(bm, .98, 3, bn3, ma, mb, mradius, PI+HALF_PI, HALF_PI,
                        xoff=mxoff, xdistort=1.5, cw=False)
        endShape()
        rotate(-rot)
        translate(-self.x, -self.y)

        # eye locations
        eyex = self.x-self.s-random(self.s/10)

        for i in range( 3+int(random(10)) ):

            if eyex < self.x+self.s-self.s/2:
                eyex = eyex + random(-10, 10)
                eyex += random(30, 50)
                eyey = self.y + random(-self.s/2)
                eyesize = 8 + random(self.s/5.0)

                tup = (eyex, eyey, eyesize)
                self.eyelist.append(tup)

        for eye in self.eyelist:
            self.drawEyes(eye[0], eye[1], eye[2])

# setup sketch and spawn an aquatic
size(500, 500)
background('#D7E1FA')
fillcolor = color(random(255),
                  random(255),
                  random(255),
                  random(128,230))
aquatic = Aquatic(width/2, height/2, random(80, 150), fillcolor)
aquatic.drawAquatic()
