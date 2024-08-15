/*
Reading temp sensor value. no resistor. reading from analog pin a0
you can also use a transistor as a heat sensor https://circuitdigest.com/electronic-circuits/heat-sensor#:~:text=As%20the%20temperature%20of%20PN,it%20as%20a%20heat%20sensor.
I used transistors 2n 2222 4338 




*/
void setup() 
{
   Serial.begin(9600);
}

void loop()
{
   // read the input on analog pin 0:
   int analogueValue = analogRead(A0); 
   delay(2000);
   Serial.print("raw read:");
   Serial.print(analogueValue);
   Serial.print(" to celcious: ");

   Serial.println((analogueValue - 32 )* 0.5556 );
}
