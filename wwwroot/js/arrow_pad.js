var mapping = {
  "x+": {"bounderies" : [26,235,153, 330], "movement" : [10,0,0,0]},
  "x-": {"bounderies" : [275, 240, 395, 330], "movement" : [-10,0,0,0]},
  "y+": {"bounderies" : [150, 175, 270,265], "movement" : [0,10,0,0]},
  "y-": {"bounderies" : [150,335,270, 440], "movement" : [0,-10,0,0]},
  "z+": {"bounderies" : [35,0,150, 125], "movement" : [0,0,10,0]},
  "z-": {"bounderies" : [35,125,150,240], "movement" : [0,0,-10,0]},
  "r+": {"bounderies" : [11, 325, 140, 430], "movement" : [0,0,0,10]},
  "r-": {"bounderies" : [280,135,415,430], "movement" : [0,0,0,-10]}
}

window.addEventListener("load", function(){
  document.getElementById("arrow_pad").addEventListener("click", function(){
    x = event.offsetX;
    y = event.offsetY;
    for (const arrow in mapping){
      if( mapping[arrow]["bounderies"][0] < x &&
          mapping[arrow]["bounderies"][2] > x &&
          mapping[arrow]["bounderies"][1] < y &&
          mapping[arrow]["bounderies"][3] > y)
      {
         data = `{
           "command":"move",
           "movement": "${mapping[arrow]["movement"]}"
          }`
          socket.send(data);
      }
    }
  });
});
