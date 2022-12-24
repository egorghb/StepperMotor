#include <AccelStepper.h>

#define dirPin 2
#define stepPin 3
#define motorInterFaceType 1

AccelStepper stepper(motorInterFaceType, stepPin, dirPin);

int speed;
bool dir = true;
int data;

void setup() {
  stepper.setMaxSpeed(1000);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(dirPin, dir);
  stepper.setSpeed(speed);
  stepper.run();
}

void serialEvent() {
  while (Serial.available()) {
    data = Serial.read();
    Serial.println(speed);
    speed = data;
    Serial.println("<");
  }
}

//