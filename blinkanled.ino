// LED pin to be blinked
const pin_t MY_LED = D7;


// allows code to run before connecting cloud
SYSTEM_THREAD(ENABLED);

void setup()
{
// 	pin is an output pin
	pinMode(MY_LED, OUTPUT);
}

void loop()
{
    // morse code for 'Betty' is -... . - - -.--'
    
    String betty = "-... . - - -.--";
    
    int index = 0;
    
    while (index < strlen(betty))
    {
        if (betty[index] == '-')
        {
            // Turn on the LED
        	digitalWrite(MY_LED, HIGH);
        
        	// Leave it on for three time units
        	delay(1500ms);
        
        	// Turn it off
        	digitalWrite(MY_LED, LOW);
        
        	// Wait for one time unit as interval between symbols
        	delay(500ms);
        }
        else if (betty[index] == '.')
        {
            // Turn on the LED
        	digitalWrite(MY_LED, HIGH);
        
        	// Leave it on for one time unit
        	delay(500ms);
        
        	// Turn it off
        	digitalWrite(MY_LED, LOW);
        
        	// Wait for one time unit as interval between symbols
        	delay(500ms);
        }
        //interval between letters
        else
        {
            // Turn it off
        	digitalWrite(MY_LED, LOW);
        
        	// Wait for three time units as interval between letters
        	delay(1500ms);
        }
        index++;
    }
}