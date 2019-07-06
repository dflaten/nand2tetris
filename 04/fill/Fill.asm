// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

@24576      //Check for keyboard press  
D=M
@BLACK
D;JNE
@WHITE
0;JMP

(BLACK)
  @8192
  D=A
  @screenposition
  M=D
  (BLOOP)
    @24576       //Check for keyboard press
    D=M
    @WHITE
    D;JEQ
    @screenposition
    D=M
    @SCREEN      //Marking Screen Black 
    A=A+D
    M=-1
    @screenposition
    M=M-1
    D=M
    @BLACK       //End of screen?
    D;JLT
    @BLOOP
    0;JMP

 (WHITE)
   @8192
   D=A
   @screenposition
   M=D
   (WLOOP)
     @24576       //Check for keyboard press
     D=M
     @BLACK
     D;JNE
     @screenposition
     D=M
     @SCREEN      //Marking Screen White 
     A=A+D
     M=0
     @screenposition
     M=M-1
     D=M
     @WHITE       //End of screen?
     D;JLT
     @WLOOP
     0;JMP
 
