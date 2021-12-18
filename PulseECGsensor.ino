
int PulseSensorPurplePin = A1;
int LED13 = 13;   

int Signal;               
int threshold = 0;            

unsigned long time1=0;
unsigned long time2=0;
    

void setup() {
//  pinMode(LED13,OUTPUT);         
  Serial.begin(9600);         

}


void loop() {

  for(int i=0;i<200;i++)
  {
    delay(10);
  }

  threshold=analogRead(A1);
  
  for(int i=0;i<50;i++)
  {
    int x=analogRead(A1);
    if(threshold<x)
    {
      threshold=x;
    }

    delay(10);
  }

  Serial.println(threshold);
  
  delay(1000);
  
  int count=0;
                                              
  for(int i=0;i<6000;i++)
  {
    
    Signal = analogRead(A1);
    Serial.println(Signal);
    time2=millis();
    
    if(Signal>threshold*0.98 && (time2-time1)>500)
    {
      count++;
      Serial.print("c=");
      Serial.println(count);
      time1=millis();
    }
   
    delay(10);                   
  }

   Serial.print("BPM=");
   Serial.println(count);
   
delay(5000);


}
