section .data
    num1 db 5
    num2 db 10
    result db 0

section .text
    global _start

_start:
    mov al, [num1]  ; Load num1 into AL
    add al, [num2]  ; Add num2 to AL
    mov [result], al ; Store the result

    ; Exit the program
    mov eax, 60     ; syscall: exit
    xor edi, edi    ; status: 0
    syscall