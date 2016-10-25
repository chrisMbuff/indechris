void setup()
{
Serial.begin(9600);
pinMode(13, OUTPUT);
}

void loop(){
    if(Serial.available() > 0) {
    String value = Serial.readStringUntil('\n');
    if  (value == "ON"){
      digitalWrite(13, HIGH);
      }
      if (value == "OFF"){
        digitalWrite(13, LOW);
        }
}
}


