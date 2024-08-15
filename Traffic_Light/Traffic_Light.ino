int red = 3;
int yellow = 5;
int green = 6;
int buzz = 9;
int wait = 1000;
int repeat = 5;


void setup() {
  Serial.begin(9600);
  pinMode(red , OUTPUT);    
  pinMode(yellow , OUTPUT);    
  pinMode(green , OUTPUT);    
  pinMode(buzz , OUTPUT);  

}

void loop() {
  for(int i = 0; i < repeat ; i++){

    //RED
    digitalWrite(red, HIGH);   
    delay(wait);

    //YELLOW
    digitalWrite(red, LOW);   
    digitalWrite(yellow, HIGH);   
    delay(wait);

    //GREEN and BUZZ
    digitalWrite(yellow, LOW);   
    digitalWrite(green, HIGH);   
    tone(buzz, 1000);   
    delay(wait);

    //OFF
    digitalWrite(yellow, LOW);   
    digitalWrite(green, LOW);   
    digitalWrite(buzz, LOW);   
    noTone(buzz);
  }

  exit(0);

}
