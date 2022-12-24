#include <AccelStepper.h>

#define dirPin 2
#define stepPin 3
#define motorInterfaceType 1

int speed = 5;
int data;

void setup() {
  Serial.begin(9600);

  pinMode(dirPin, OUTPUT);
  pinMode(stepPin, OUTPUT);

  digitalWrite(stepPin, HIGH);
  digitalWrite(dirPin, LOW);
}

void loop() {
  digitalWrite(stepPin, HIGH);
  delay(speed);
  digitalWrite(stepPin, LOW);
  delay(speed);
}

void serialEvent() {
  while (Serial.available()) {
    data = Serial.read();
    Serial.println(speed);
    speed = data;
    Serial.println("<");
  }
}