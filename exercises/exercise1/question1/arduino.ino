#include <ArduinoJson.h> // Instalar biblioteca: arduinojson
#define BTN 13

DynamicJsonDocument data(1024);

void setup() {
  pinMode(BTN, INPUT);
  Serial.begin(9600);
}

void loop() {
    if(digitalRead(BTN)) {
        data["message"] = "button pressed!";
    //        Serial.println("button pressed");
    }
    serializeJson(data, Serial);
    Serial.println();
    delay(2000);
}