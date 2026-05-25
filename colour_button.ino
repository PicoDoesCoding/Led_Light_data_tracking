  const int green = 8;
  const int yellow =9;
  const int red =10;

  const int Rbutton = 4;
  const int Ybutton = 3;
  const int Gbutton = 2;

  const int buzzer = 5;
  int buzzerCount = 0;
  bool lastAllOn = false;

  bool GState = false;
  bool YState = false;
  bool RState = false;

  bool lastG = HIGH;
  bool lastY = HIGH;
  bool lastR = HIGH;


  void setup() {
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);

  pinMode(Rbutton, INPUT_PULLUP);
  pinMode(Ybutton, INPUT_PULLUP);
  pinMode(Gbutton, INPUT_PULLUP);

  pinMode(buzzer, OUTPUT);

  Serial.begin(9600);

  }

  void loop() {
    bool currentG = digitalRead(Gbutton);

    if(lastG == HIGH && currentG == LOW)
    { GState = !GState;
      digitalWrite(green, GState);
      Serial.println("G_PRESS"); }

    lastG = currentG;

    bool currentY = digitalRead(Ybutton);

    if(lastY == HIGH && currentY == LOW)
    { YState = !YState;
      digitalWrite(yellow, YState); 
      Serial.println("Y_PRESS"); }

    lastY = currentY;

    bool currentR = digitalRead(Rbutton);

    if(lastR == HIGH && currentR == LOW)
    { RState = !RState;
      digitalWrite(red, RState);
      Serial.println("R_PRESS"); }

    lastR = currentR;

    bool allOn = (GState == true && YState == true && RState == true);

    if (allOn)
    { digitalWrite(buzzer, HIGH);

    if (!lastAllOn)
    { buzzerCount++;
      Serial.println("BUZZER"); } }
    else
    { digitalWrite(buzzer, LOW); }

    lastAllOn = allOn; }
