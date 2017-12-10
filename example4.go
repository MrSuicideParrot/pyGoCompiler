package main

import "fmt"

func main() {
    fmt.Scan(a);
    b:=0;
    c:=1;
    temp:=0;

    fmt.Print(b);
    fmt.Print(c);
    for i:=0; i<a; i++ {
        temp=c;
        c=c+b;
        b=temp;
        fmt.Print(c);
    }
}

