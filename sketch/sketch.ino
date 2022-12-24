/*
  Получаем пачку значений: скорость, угол, направление.
  Раскидываем значения в целочисленный массив.
  PARSE_AMOUNT - количество значений, которое мы хотим принять.
  Пакет на прием должен быть вида:
    Начало - символ $
    Разделитель - пробел
    Заверщающий символ - ;
    Пример пакета: $200 20 1;
*/
#include <AccelStepper.h>

#define PARSE_AMOUNT 3

#define dirPin 2
#define stepPin 3
#define motorInterFaceType 1

AccelStepper stepper(motorInterFaceType, stepPin, dirPin);

int intData[PARSE_AMOUNT];
bool recievedFlag;
bool getStarted;
byte index;
String string_convert = "";

void parsing() {
  if (Serial.available()) {
    char incomingByte = Serial.read();
    if (getStarted) {                         // если приняли $
      if (incomingByte != ' ' && incomingByte != ';') {
        string_convert += incomingByte;       // складываем в строку
      } else {                                
        intData[index] = string_convert.toInt();  // преобразуем строку в int и кладём в массив
        string_convert = "";                  // очищаем строку
        index++;                              // переходим к парсингу следующего элемента массива
      }
    }
    if (incomingByte == '$') {                // если это $
      getStarted = true;                      // поднимаем флаг, что можно парсить
      index = 0;                              // сбрасываем индекс
      string_convert = "";                    // очищаем строку
    }
    if (incomingByte == ';') {                // если конец
      getStarted = false;                     // конец парсинга
      recievedFlag = true;                    // флаг на принятие
    }
  }
}

void setup() {
  stepper.setMaxSpeed(1000);
  stepper.setSpeed(0);
  Serial.begin(9600);
}

void loop() {
  parsing();
  if (recievedFlag){
    for (byte i = 0; i < PARSE_AMOUNT; i++){
      Serial.println(intData[i]);
    }
    Serial.println('<');

    stepper.setSpeed(intData[0]);
    digitalWrite(dirPin, intData[2]);
  }

  stepper.runSpeed();
}