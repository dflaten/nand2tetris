// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@R2    //Initialize Sum to zero
M=0
@R1    //Getting second digit to be used as a counter for the loop
D=M
@ZERO  //Jump to Zero if R1 Zero
D;JEQ
@R3    //Storing counter
M=D
@R1    //checking first digit for zero
D=M
@ZERO  //Jump to Zero if R1 Zero
D;JEQ
(LOOP)
@R0
D=M    // D=R0
@R2
M=D+M  // D=R2+R0
@R3    // Reducing Counter
D=M
@END   // Checking for zero
D;JEQ
@R3
M=M-1
D=M
@END
D;JEQ
@LOOP
0;JMP  // Goto LOOP
@ZERO
@R2
M=0
D=M
@END   // Checking for zero
D;JEQ
(END)
@END
0;JMP  // Infinite loop
