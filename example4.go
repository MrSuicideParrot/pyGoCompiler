package main

import "fmt"

func main() {
<<<<<<< Updated upstream
    fmt.Scan(a);
    b:=0;
    c:=1;
=======
	fmt.Scan(a);
	b:=0;
	c:=1;
>>>>>>> Stashed changes
    temp:=0;

    fmt.Print(b);
    fmt.Print(c);
<<<<<<< Updated upstream
    for i:=0; i<a; i++ {
        temp=c;
        c=c+b;
        b=temp;
        fmt.Print(c);
    }
}

=======
	for i:=0; i<a; i++ {
	    temp=c;
	    c=c+b;
	    b=temp;
	    fmt.Print(c);
	}
}
>>>>>>> Stashed changes
