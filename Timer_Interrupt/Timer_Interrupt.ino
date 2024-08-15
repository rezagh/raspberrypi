/*

  Lab 6 Task 4 Timer interrupts
  https://www.instructables.com/Arduino-Timer-Interrupts/
  https://electronoobs.com/eng_arduino_tut140.php

  see notes in onenote

*/

int led = LED_BUILTIN;
bool LED_STATE = true;


void setup() 
{
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  cli();                      //stop interrupts for till we make the settings
  
  /* reset the control register to make sure we start with everything disabled.*/
  TCCR1A = 0;                 // Reset entire TCCR1A to 0 
  TCCR1B = 0;                 // Reset entire TCCR1B to 0
 
  /* set the prescalar to 256 by changing the CS10 CS11 and CS12 bits. in this case CS12=1,CS10=0,CS11=0 */  
  TCCR1B |= B00000100;        //Set CS12 to 1 so we set prescalar to 256  
  
  /* enable compare match mode on register A*/
  TIMSK1 |= B00000010;        //Set OCIE1A bit to 1 so we enable compare match A 
  
  /* Set the value of register A to 31250, that is the number of pulses that counts to 500ms  */
  OCR1A = 31250;             //set compare register A to this value  
  sei();                     //Enable back the interrupts
}

void loop() {
  // put your main code here
}

//With the settings above, this IRS will trigger each 1000ms.
ISR(TIMER1_COMPA_vect){
  TCNT1  = 0;                  //First, set the timer back to 0 so it resets for next interrupt
  //int analogueValue = analogRead(A0); 
  LED_STATE = !LED_STATE;
  digitalWrite(led,LED_STATE);
}