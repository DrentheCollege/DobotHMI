let socket;

window.addEventListener("load", function (){
  document.getElementById('connect').onclick = function(){
    connectSocket();
  };
  document.getElementById('home').addEventListener("click", function(){
    var data = "{" +
       "\"command\": \"home\"" +
    "}";
    socket.send(data);
  });

  document.getElementById('save').addEventListener("click", function(){
    var data = `{
      "command": "save",
      "position" : {
        "name" : "${document.getElementById("name").value}",
        "x" : ${document.getElementById("x").value},
        "y" : ${document.getElementById("y").value},
        "z" : ${document.getElementById("z").value},
        "r" : ${document.getElementById("r").value}
      }
    }`;
    console.log(data);
    socket.send(data);
  });

  document.getElementById("get").addEventListener("click" , function(){
    var data = `{
      "command": "get",
      "position" : {
        "name" : "harmen",
        "linenumber" : 1
      }
    }`;
    socket.send(data);
  });

});

function connectSocket(){
  if(socket == undefined || socket.readyState != 1){
    console.log("Trying to connect to websocket");
    socket = new WebSocket("ws://192.168.137.208:8765");

    socket.onmessage = function(event) {
      var data = JSON.parse(event.data);
      if( data["result"] == "connected"){
        console.log("green");
        document.getElementById("connect").style.backgroundColor = 'green';
      }
      if( data["result"] == "position"){
        var result = "";
        result += "x: " + data["position"]["x"] + ", ";
        result += "y: " + data["position"]["y"] + ", ";
        result += "z: " + data["position"]["z"] + ", ";
        result += "r: " + data["position"]["r"];
        document.getElementById("result").innerHTML = result;
        document.getElementById("x").value = data["position"]["x"];
        document.getElementById("y").value = data["position"]["y"];
        document.getElementById("z").value = data["position"]["z"];
        document.getElementById("r").value = data["position"]["r"];
      }
      console.log(`[message] Data received from server: ${event.data}`);
    };

    socket.onopen = function(e) {
      socket.onclose = function(event) {
        if (event.wasClean) {
          console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
        } else {
          console.log('[close] Connection died');
        }
        document.getElementById("connect").style.backgroundColor = 'red';
      };
      socket.onerror = function(error) {
        console.log(`[error] ${error.message}`);
        document.getElementById("connect").style.backgroundColor = 'red';
      };
      var data = "{" +
        "\"command\": \"connect\"" +
      "}"
      socket.send(data);
    };
  }
}
