

//GATT Services UUIDs: https://www.bluetooth.com/specifications/gatt/services/
//GATT Characteristic UUIDs: https://www.bluetooth.com/specifications/gatt/characteristics/


let chosenBleService = null;

function myFunction() {	
  navigator.bluetooth.requestDevice({
      filters: [
        { services: [0x180D] }, //heart rate UUID
        {name: 'Bluefruit52'} //this is required on web ble  but not chrome
      ]
    })
  .then(device => device.gatt.connect())
  .then(document.getElementById("mytext").value = "connected")
  .then(server => server.getPrimaryService(0x180D)) //heart rate uuid
  .then(document.getElementById("mytext").value = "got primary service")
  .then(service => {
    //console.log("connected, got primary service");
    document.getElementById("mytext").value = "connected got primary service";
    return Promise.all([
      service.getCharacteristic(0x2A37) //fat burn upper limit UUID
        .then(handleBleCharacteristic),
    ]);
  });
}

function handleBleCharacteristic(characteristic) {
  document.getElementById("mytext").value = "handling ble characteristics";
  return characteristic.startNotifications()
  .then(char => {

    characteristic.addEventListener('characteristicvaluechanged',
                                    onDataChanged);
  });
}

function onDataChanged(event) {
  document.getElementById("mytext").value = "data changed";
  let characteristic = event.target;
  
  parseData(characteristic.value);
  updateChart(characteristic.value);
}



function parseData(data) {
  let result = {};
  //console.log("receiving 10 bytes");

  //console.log("x: " + data.getUint8(0) + "y: " + data.getUint8(1) + "z: " + data.getUint8(2));

  //document.getElementById("mytext").value = data.getUint8(2);
  //result.bitOne = data.getUint8(2);
  //return result;
}
