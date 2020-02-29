package main
import "fmt"
func main(){
	var num int
	fmt.Println("Enter Number")
	fmt.Scan(&num)
	if num%2==0{
		fmt.Println(num,"is a Even Number")
	}else{
		fmt.Println(num,"is an Odd Number")
	}
}