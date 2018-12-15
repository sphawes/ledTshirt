/*
 *  Written by Stephen Hawes December 2018 for Tom's Hardware 
 *  stephenhawes.com
 *  
 */

#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>

#define PIN 6

Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(8, 8, 3, 1, PIN,
  NEO_TILE_TOP   + NEO_TILE_LEFT   + NEO_TILE_ROWS   + NEO_TILE_ZIGZAG +
  NEO_MATRIX_TOP + NEO_MATRIX_LEFT + NEO_MATRIX_ROWS + NEO_MATRIX_PROGRESSIVE,
  NEO_GRB + NEO_KHZ800);

const uint16_t colors[] = {
    matrix.Color(250, 250, 250)};

const byte numChars = 128;
char receivedChars[numChars]; // an array to store the received data
boolean newData = false;
String data;
int x = matrix.width();

void setup() {
  Serial.begin(9600);
  matrix.begin();
  matrix.setTextWrap(false);
  matrix.setBrightness(80);
  matrix.setTextColor(colors[0]);
  matrix.fillScreen(0);
  matrix.show();
}

void loop() {
  recvWithEndMarker();
  showNewData();
}

void recvWithEndMarker() {
  static byte ndx = 0;
  char endMarker = '\n';
  char rc;
  
  while (Serial.available() > 0 && newData == false) {
    rc = Serial.read();
    if (rc != endMarker) {
      receivedChars[ndx] = rc;
      ndx++;
      if (ndx >= numChars) {
        ndx = numChars - 1;
      }
    }
    else {
      receivedChars[ndx] = '\0'; // terminate the string
      ndx = 0;
      newData = true;
    }
  }
}

void scroll(String text){
  //scrolling text
  matrix.setTextColor(colors[0]);
  int len = text.length();
  for(int i=24;i>(len*(-6));i--){
    matrix.fillScreen(0);
    matrix.setCursor(i, 0);
    matrix.print(text);
    matrix.show();
    delay(30);
  }
}

void showNewData() {
 if (newData == true) {
   Serial.print("Just received: ");
   Serial.println(receivedChars);
   data = receivedChars;
   newData = false;
   scroll(data);
 }
}


