# import os module 
import os 

# Get the value of 'HOME' 
key = 'HOME'
value = os.getenv(key) 

# Print the value of 'HOME' 
# environment variable 
print("Value of 'HOME' environment variable :", value) 

# Get the value of 'JAVA_HOME' 
# environment variable 
key = 'JAVA_HOME'
value = os.getenv(key) 

# Print the value of 'JAVA_HOME' 
# environment variable 
print("Value of 'JAVA_HOME' environment variable :", value)