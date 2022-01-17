import qsharp
# Import the quantum operation from the namespace defined in the program.qs file 
from Qrng import SampleQuantumRandomNumberGenerator 
# Set the maximum range
max = 50 
# Variable to store the output
output = max + 1 
while output > max:
    # Initialize a list to store the bits that will define the random integer
    bit_string = [] 
    # Call the quantum operation as many times as there are bits
    # needed to define the maximum of the range. For example, if max=7, you need three bits
    # to generate all the numbers from 0 to 7.
    for i in range(0, max.bit_length()):  
        # Call the quantum operation and store the random bit in the list
        bit_string.append(SampleQuantumRandomNumberGenerator.simulate()) 
    # Transform bit string to integer
    output = int("".join(str(x) for x in bit_string), 2) 
# Print the random number
print("The random number generated is " + str(output))