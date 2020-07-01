// This is a Processing.py adaption of the Nodebox script:
// "Aquatics!" by Lieven Menschaert (using Johan Gielis' Superformula equations)
// https://www.nodebox.net/code/index.php/Aquatics

function setup() {
  createCanvas(500, 500);
  
  let fillcolor = color(random(255),
                        random(255),
                        random(255),
                        random(128,230));
  
  // remove bubble and bgcolor arguments for a transparent perimeter
  let aquatic = new Aquatic(width/2, height/2, random(80, 130),
                            fillcolor, bubble=true, bgcolor='#D7E1FA');
  aquatic.drawAquatic();
  
}

class Aquatic {
  
  constructor(x ,y, size, fillcolor, bubble=False, bgcolor=None) {
    this.x = x;
  }
  
  drawAquatic() {
    circle(this.x, 250, 50);
  }
  
}
