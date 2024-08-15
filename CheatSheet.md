
### Arduino Programming Cheat Sheet

#### Basic Structure

```cpp
void setup() {
  // Initialization code here
}

void loop() {
  // Main code here
}
```

- **setup()**: Runs once when the Arduino is powered on or reset. Use it to initialize variables, pin modes, start using libraries, etc.
- **loop()**: Runs repeatedly after setup(). Use it to actively control the Arduino board.

#### Comments
- Single-line comment: `// This is a comment`
- Multi-line comment: `/* This is a multi-line comment */`

#### Variables and Data Types

```cpp
int a = 13;            // Integer
float b = 4.56;        // Floating-point number
char c = 'A';          // Character
char str[] = "Hello";  // String
boolean flag = true;   // Boolean
```

#### Pin Modes

```cpp
pinMode(pin, mode);
```
- `pin`: The pin number.
- `mode`: `INPUT`, `OUTPUT`, or `INPUT_PULLUP`.

#### Digital I/O

```cpp
digitalWrite(pin, value);   // Write HIGH or LOW to a digital pin
int val = digitalRead(pin); // Read value from a digital pin
```

#### Analog I/O

```cpp
analogWrite(pin, value);     // Write PWM value (0-255) to a pin
int sensorValue = analogRead(pin); // Read value (0-1023) from an analog pin
```

#### Time Functions

```cpp
delay(milliseconds);           // Pause for specified milliseconds
unsigned long time = millis(); // Return number of milliseconds since program started
```

#### Serial Communication

```cpp
Serial.begin(baud_rate);     // Start serial communication at given baud rate
Serial.print(data);          // Print data to the serial port
Serial.println(data);        // Print data with a new line
int val = Serial.read();     // Read incoming serial data
```

#### Control Structures

- **if Statement**

  ```cpp
  if (condition) {
    // Code to execute if condition is true
  } else {
    // Code to execute if condition is false
  }
  ```

- **for Loop**

  ```cpp
  for (initialization; condition; increment) {
    // Code to execute in the loop
  }
  ```

- **while Loop**

  ```cpp
  while (condition) {
    // Code to execute while condition is true
  }
  ```

- **do-while Loop**

  ```cpp
  do {
    // Code to execute at least once
  } while (condition);
  ```

#### Functions

```cpp
returnType functionName(parameters) {
  // Function code
  return value; // if returnType is not void
}
```

#### Libraries

```cpp
#include <LibraryName.h>
```
- Include external libraries at the beginning of your code.

#### Built-in Functions

- Lots of maths functions such as abs(), constrain(), map(), max(), min(), pow(), sq(), sqrt(), etc. Example:

- **random()**

  ```cpp
  long randNumber = random(max);        // Generate random number from 0 to max-1
  long randNumber = random(min, max);   // Generate random number from min to max-1
  ```

#### Example: Blink an LED

```cpp
const int ledPin = 13; // Pin number for the LED

void setup() {
  pinMode(ledPin, OUTPUT); // Set pin mode to OUTPUT
}

void loop() {
  digitalWrite(ledPin, HIGH); // Turn the LED on
  delay(1000);                // Wait for 1 second
  digitalWrite(ledPin, LOW);  // Turn the LED off
  delay(1000);                // Wait for 1 second
}
```

more info here https://www.arduino.cc/reference/en/
