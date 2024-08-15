/**
potentiometer is a variable resistor

The middle pin returns the current with the resistance of the potentiometer applied. 
Suppose you connect the + to 5 Volt, and connect the - to the GND. When we turn the potentiometer for 50% open the middle pin will be 2.5 Volts.
v= ir

baud is the unit of measure for symbol per second that can be send to a channel



*/

int potPin = A2;              // Potmeter pin
//int ledPin = LED_BUILTIN;     // Builtin LED pin
int potVal = 0;               // Potmeter's value (0 by default)

void setup() {
  Serial.begin(9600);         // Start the serial monitor at 9600 baud, This indicates that the Arduino is allowed to send back symbols to the computer at a rate of 9600 symbols per second. This number is called the Baud rate.
  pinMode(LED_BUILTIN, OUTPUT);    // Set ledPin as output
}

// The loop() function runs infinitely
void loop() {
  
  potVal = analogRead(potPin);       // Read the analog value of the potmeter (0-1023)
  Serial.println(potVal);            // Write the value to the serial monitor (computer - see menu tools -> serial monitor)
  
  digitalWrite(LED_BUILTIN, HIGH);   // Turn the built-in LED on
  delay(potVal);                     // Pause for the length of the potval value (0-1023) milliseconds
  
  digitalWrite(LED_BUILTIN, LOW);    // Turn the built-in LED off
  delay(potVal);                     // Pause for the length of the potval value (0-1023) milliseconds
  
}
