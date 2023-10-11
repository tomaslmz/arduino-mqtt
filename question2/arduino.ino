#include <ArduinoJson.h> // Instalar biblioteca: arduinojson

DynamicJsonDocument data(1024);

int count = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  data["count"] = count;
  serializeJson(data, Serial);
  Serial.println();
  delay(2000);
  count++;
  // Serial.println();
}