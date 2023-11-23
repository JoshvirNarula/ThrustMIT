#include <Servo.h>




#define SERVO_1_PIN 5 // Zpb3
#define SERVO_2_PIN 4 // Zpb2
#define SERVO_3_PIN 3 // Zpb1
#define servothree 120
Servo servo1;
Servo servo2;
Servo servo3;

int i = 1;
int delay1 = 1000;
int delay2 = 350;
void setup() 
{
    Serial.begin(9600);
    servo1.attach(SERVO_1_PIN);
    servo2.attach(SERVO_2_PIN);
    servo3.attach(SERVO_3_PIN);
    delay(50);
    Serial.println("Initialized servos...");
    servo1.write(70);
    servo2.write(10);
    servo3.write(50);
    Serial.println("!!! Servo's SET TO Mechanical 0 (zero) !!!");
    Serial.println("Starting loop...");


    
}

void loop()
{
    //LOOP 1
    //1ST
    servo1.write(180);
    servo2.write(0);
    servo3.write(0);
    delay(delay1);


    //2nd
    servo1.write(180);
    servo2.write(0);
    servo3.write(180);
    delay(delay1);

    servo1.write(0);
    servo2.write(0);
    servo3.write(0);
    delay(delay1);

    //3rd
    servo1.write(120);
    servo2.write(90);
    servo3.write(120);
    delay(delay1);

    servo1.write(0);
    servo2.write(0);
    servo3.write(0);
    delay(delay1);

    //4th
    servo1.write(180);
    servo2.write(0);
    servo3.write(0);
    delay(delay1);

    servo1.write(0);
    servo2.write(0);
    servo3.write(0);
    delay(delay1);

    //5th
    servo1.write(180);
    servo2.write(180);
    servo3.write(0);
    delay(delay1);

    servo1.write(0);
    servo2.write(0);
    servo3.write(0);
    delay(delay1);

    //6th
    servo1.write(0);
    servo2.write(180);
    servo3.write(0);
    delay(delay1);

    servo1.write(0);
    servo2.write(0);
    servo3.write(0);
    delay(delay1);

    //7th
    servo1.write(120);
    servo2.write(120);
    servo3.write(90);
    delay(delay1);

    servo1.write(0);
    servo2.write(0);
    servo3.write(0);
    delay(delay1);

    //8th
    servo1.write(0);
    servo2.write(180);
    servo3.write(180);
    delay(delay1);

    servo1.write(0);
    servo2.write(0);
    servo3.write(0);
    delay(delay1);


    //LOOP 2
    //1ST
    servo1.write(0);
    servo2.write(0);
    servo3.write(180);
    delay(delay2);

    //2nd
    servo1.write(180);
    servo2.write(0);
    servo3.write(180);
    delay(delay2);

    //3rd
    servo1.write(120);
    servo2.write(90);
    servo3.write(120);
    delay(delay2);

    //4th
    servo1.write(180);
    servo2.write(0);
    servo3.write(0);
    delay(delay2);

    //5th
    servo1.write(180);
    servo2.write(180);
    servo3.write(0);
    delay(delay2);

    //6th
    servo1.write(0);
    servo2.write(180);
    servo3.write(0);
    delay(delay2);


    //7th
    servo1.write(120);
    servo2.write(120);
    servo3.write(90);
    delay(delay2);

    //8th
    servo1.write(0);
    servo2.write(180);
    servo3.write(180);
    delay(delay2);

}
