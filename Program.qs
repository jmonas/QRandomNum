namespace Qrng {
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    
    operation SampleQuantumRandomNumberGenerator() : Result {
        // Allocate a qubit        
        use q = Qubit();  
        // Put the qubit to superposition
        // It now has a 50% chance of being measured 0 or 1  
        H(q);      
        // Measure the qubit value            
        return M(q); 
    }
}