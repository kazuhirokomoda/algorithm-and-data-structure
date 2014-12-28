/*
DP_recursive.go
http://www.itmedia.co.jp/enterprise/articles/1003/06/news002_5.html

Given n, p, q, x and y, return the n-th element of A (index is 0-based).
*/

package main
import "fmt"
import "time"

const Limit int = 1e6
var values = map[int]int{}

func infinite_sequence(n, p, q, x, y int) (res int){
    
    // initial condition
    if n <= 0 {
        return 1
    }

    // ok represents whether the key n is used in values
    _, ok := values[n]
    if n < Limit && ok{
        return values[n]
    }
    
    res = infinite_sequence(n/p - x, p, q, x, y) + infinite_sequence(n/q - y, p, q, x, y)
    
    // memorize value if n is small enough
    if n < Limit{
        values[n] = res
    }
        
    return
}

func main(){
    start := time.Now()
    answer := infinite_sequence(1e13, 2, 2, 0, 123456)
    fmt.Println(answer)
    end := time.Now()
    
    fmt.Println("elapsed_time:", end.Sub(start).Seconds(), "s")
}
