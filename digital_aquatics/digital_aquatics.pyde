// This is a p5.js adaption of the Nodebox script:
// "Aquatics!" by Lieven Menschaert (using Johan Gielis' Superformula equations)
// https://www.nodebox.net/code/index.php/Aquatics

function setup() {
  createCanvas(500, 500);
background('#D7E1FA')
  let fillcolor = color(random(255), 
                        random(255), 
                        random(255), 
                        random(128, 230));

  // remove bubble and bgcolor arguments for a transparent perimeter
  let aquatic = new Aquatic(width/2, height/2, random(80, 130), fillcolor, 
                            true, '#D7E1FA');
  aquatic.drawAquatic();
}


function keyPressed() {
  if (key === 's') {
    let timestamp = (`${hour()}-${minute()}-${second()}`);
    save(timestamp+'.png');
  }
}


class Aquatic {

  constructor(x, y, size, fillcolor, bubble, bgcolor) {
    this.x = x;
    this.y = y;
    this.s = size;
    this.f = fillcolor;
    this.r = red(this.f);
    this.g = green(this.f);
    this.b = blue(this.f);
    this.a = alpha(this.f);
    this.bubble = bubble;
    this.bg = bgcolor;
    this.eyelist = [];
    this.currentx = random(-this.s/8, this.s/8);
    this.currenty = random(-this.s/8, this.s/8);
    strokeJoin(ROUND)
  }
  /*
  drawIrisPupil(pupilx, pupily, pupilsize) {
    let s = pupilsize/4 + random(pupilsize/3);

    // iris
    if (random(1) < 0.7) {
      fill(255-this.r, 255-this.g, 255-this.b, this.a/1.5);
      stroke(255-this.r, 255-this.g/2, 255-this.b, 140);
    } else {
      fill(this.r*2, this.g, this.b, this.a/2);
      stroke(this.r, this.g/2, this.b, 140);
    }

    strokeWeight(2);
    ellipse(10, 10, s*2, s*2);//ellipse(pupilx, pupily, s*2, s*2);

    // pupil
    fill(1)
    stroke(0);
    strokeWeight(5);
    ellipse(10, 10, s/2, s/2);//ellipse(pupilx, pupily, s/2, s/2);
  }

  drawEyeLid(eyex, eyey, eyesize) {
    fill('#000000');//fill(self.r, self.g, self.b, random(200, 240));
    stroke(self.r/2, self.g/2, self.b/2);
    strokeWeight(1);
    //arc(eyex, eyey, eyesize*2, eyesize*2, PI, TWO_PI, CHORD);
    arc(1,1,1,1,1,1)
  }
  
  drawEyes(eyex, eyey, eyesize) {
    stroke(self.r/2, self.g/2, self.b/2, 220)

    // eyelashes
    if (random(1) > 0.3) {
      strokeWeight(2.5);
      //translate(eyex, eyey);
      translate(10, 10)
      let rot = 0;
      let eyelashes = int(random(3, 8));
          
      for (let eyelash=0; eyelash<eyelashes; eyelash++) {
        let randomrot = random(0.2, 0.7);
        rot += randomrot;
        rotate(randomrot);
        line(0, 0, random(-eyesize*2, -eyesize*1.2), 0);
      }

      rotate(-rot);
      translate(-eyex, -eyey);
    }

    // eye
    //fill(255);
    fill('#000000');
    strokeWeight(2);
    //ellipse(eyex, eyey, eyesize*2, eyesize*2);
    ellipse(10, 10, 10, 10);
    this.drawIrisPupil(eyex, eyey, eyesize);
    // eye shine
    //fill(255);
    fill('#000000');
    noStroke();
    let shinexy = eyesize/4;
    let shinesize = eyesize/2.5;
    //ellipse(eyex-shinexy, eyey-shinexy, shinesize, shinesize);
    ellipse(10, 10, 10, 10);

    // eyelid
    if (random(1) > 0.5) {
      let cover = this.drawEyeLid(eyex, eyey, eyesize);
    }
  }
  
  drawHair(hairx, hairy, hairlength, angle) {
    let tipx = cos(angle) * hairlength;
    let tipy = sin(angle) * hairlength;
    curve(hairx-random(-100, 100), hairy+random(-100, 100), hairx, hairy,
          tipx+self.currentx, tipy+self.currenty, tipx-random(-100, 100), 
          tipy+random(-100, 100));
  }
  */
  superShape(m, n1, n2, n3, a, b, radius, start, stop, xoff, yoff, 
             xdistort, cw, mode) {
    // https://en.wikipedia.org/wiki/Superformula
    function superShapeVertex(angle) {
      let t1 = pow( abs( (1.0/a) * cos(angle*m/4) ), n2 );
      let t2 = pow( abs( (1.0/b) * sin(angle*m/4) ), n3 );
      let t3 = pow(t1+t2, 1.0/n1);
      let x = (t3 * cos(angle) * xdistort * radius) + xoff;
      let y = (t3 * sin(angle) * radius) + yoff;
      return [x, y];
    }
    // plot supershape clock/counter-clockwise
    // drawing hairs only works with cw=True
    let angle = start;
    let tuftstart = random(0, PI);
    let tuftend = random(PI, TWO_PI);

    if (cw) {
      while (angle < stop) {
        let xy = superShapeVertex(angle)
        if (mode === 'vertex') {
          vertex(xy[0], xy[1]);
        }
        else if (mode === 'hair') {
          noFill();
          stroke(this.r/2, this.g/2, this.b/2, 200);
          strokeWeight(0.8);
          this.drawHair(xy[0], xy[1], radius*random(1.1, 1.2), angle)
          if (angle > tuftstart && angle < tuftend) {
            strokeWeight(2);
            let hairlength = radius*random(1.3, 1.5);
            this.drawHair(xy[0], xy[1], hairlength, angle);
          }
        }
        angle += 0.05;
      }
    }
    else {
      while (angle > stop) {
        let xy = superShapeVertex(angle);
        vertex(xy[0], xy[1]);
        angle -= 0.05;
      }
    }
  }

  drawAquatic() {
    // outline / mouth variables
    // b_ for body; m_ for mouth
    let n1 = random(1) < 0.5 ? -0.8-random(5) : 0.8+random(5);
    let n2 = 0.5 + random(5);
    let ba = random(0.7, 1.2);
    let bb = 1;
    let bm = int(random(1, 30));
    let bn3 = 0.5 + random(0.5, -1.5);
    let ma = random(0.9, 1.1);
    let mb = random(0.9, 1.1);
    let mm = 4 + random(20);
    let mn3 = 0.81 + random(-0.8, 0.8);
    let mradius = this.s * random(0.2, 0.4);
    let mxoff = this.s / random(0.9, 1.1);
    
    // bubbles
    if (this.bubble) {
      noStroke();
      fill(255, 255, 255);
      let bs = this.s * 0.8;
      ellipse(this.x + random(-bs, bs), this.y+random(-bs, bs), bs, bs);
      ellipse(this.x + random(-bs, bs), this.y+random(-bs, bs), this.s/2, this.s/2);
    }
    
    // nucleus
    let rot = random(-PI, PI);
    let xoff = this.x-this.s/3 * (random(1) < 0.5 ? 1 : -1);
    let yoff = this.y+this.s / random(1.5, 20);
    translate(xoff, yoff);
    rotate(rot);
    fill(this.r/2, this.g/2, this.b/2, 80);
    stroke(this.r/2, this.g/2, this.b/2, 80);
    ellipse(0, 0, this.s/random(1, 3), this.s/random(1, 3));
    fill(this.r/3, this.g/3, this.b/3, 120);
    ellipse(0, 0, this.s/6, this.s/6);
    rotate(-rot);
    translate(-xoff, -yoff);
    
    // supershapes
    rot = random(HALF_PI-0.3, HALF_PI+0.3);
    translate(this.x, this.y)
    rotate(rot);
    // ectoplasm
    noFill();
    stroke(255, 255, 255);
    strokeWeight(self.s/8);
    beginShape();
    this.superShape(bm, n1, n2, bn3, ba, bb, this.s-this.s/12, 0.5, TWO_PI-0.5, 
                   0, 0, 1, true, 'vertex');
    endShape();
    // body
    fill(this.r, this.g, this.b, 120);
    stroke(this.r/2, this.g/2, this.b/2, 220);
    strokeWeight(self.s/12);
    beginShape();
    this.superShape(bm, n1, n2, bn3, ba, bb, this.s, 0.5, TWO_PI-0.5);
    // mouth
    this.superShape(bm, 0.98, 3, bn3, ma, mb, mradius, PI+HALF_PI, HALF_PI, 
                    mxoff, 0, 1.5, true, 'vertex');
    endShape(CLOSE);
    /*
    // freckles
    fill(this.r*1.8, this.g*1.8, this.b*1.8, 150);
    noStroke();
    for (let i=10; i<200; i++) {
      let freckx = i/this.s*150 * sin(i*15) + random(1, 10);
      let frecky = i/self.s*150 * cos(i*15) + random(1, 10);
      let dotsize = random(1, 10);
      ellipse(freckx, frecky, dotsize, dotsize);
    }
    // characters
    var chars = 's*.~_.)`:;*"-';
    [...chars].forEach(c => {
      fill(self.r/2, self.g/2, self.b/2, 70);
      let play = self.s/2;
      textSize( random(play/3, play/1.5) );
      text(char, random(-play, play/2), random(-play*1.5, play*1.5));
    });
    // background-colored mask
    
    fill(this.bg);
    noStroke();
    beginShape();
    vertex(-width*2, -height*2);
    vertex(-width*2, height*4);
    vertex(width*4, height*4);
    vertex(width*4, -height*2);
    beginContour();
    this.superShape(bm, n1, n2, bn3, ba, bb, this.s, 0.5, TWO_PI-0.5, 0, 0, 1, 
                    true, 'vertex');
    this.superShape(bm, 0.98, 3, bn3, ma, mb, mradius, PI+HALF_PI, HALF_PI,
                    mxoff, 0, 1.5, false, 'vertex');
    endContour();
    endShape(CLOSE);
    
    // lips
    noFill();
    stroke(this.r/2, this.g/2, this.b/2);
    strokeWeight(self.s/12.0);
    beginShape();
    this.superShape(bm, 0.98, 3, bn3, ma, mb, mradius, PI+HALF_PI, HALF_PI,
                    mxoff, 0, 1.5, false, 'vertex');
    endShape();
    stroke((this.r + this.g) * 0.8, (this.g + this.b) * 0.8, (this.b + this.r) * 0.8, 128);
    strokeWeight(self.s/22.5);
    beginShape();
    this.superShape(bm, 0.98, 3, bn3, ma, mb, mradius, PI+HALF_PI, HALF_PI,
                    mxoff, 0, 1.5, false, 'vertex');
    endShape();
    // hairs
    if (random(1) > 0.3) {
      this.superShape(bm, n1, n2, bn3, ba, bb, self.s, 0.5, TWO_PI-0.5,
                      0, 0, 1, true, 'hair')
      rotate(-rot);
      translate(-self.x, -self.y);
    }
    */
    /*
    // eye locations
    let eyex = this.x-this.s-random(this.s/10);
    let eyes = 3+int(random(10));
    
    for (let i=0; i<eyes; i++) {

      if (eyex < this.x+this.s-this.s/2) {
        eyex = eyex + random(-10, 10);
        eyex += random(30, 50);
        let eyey = self.y + random(-self.s/1.5, self.s/5);
        let eyesize = 8 + random(this.s/5.0);
        
        let tup = (eyex, eyey, eyesize);
        this.eyelist.push(tup);
      }
    }
    
    this.eyelist.forEach(eye => {
      this.drawEyes(eye[0], eye[1], eye[2]);
    });
  */
  }

}
