#include <ArduinoJson.h> // Instalar biblioteca: arduinojson

int temp = 0, umid = 2;

DynamicJsonDocument dados(1024);

void setup() {
  Serial.begin(9600);
}

void loop() {
  dados["Temperatura"] = temp;
  dados["Umidade"] = umid;

  serializeJson(dados, Serial);

  Serial.println();
  delay(5000);
  temp++;
  umid++;
}