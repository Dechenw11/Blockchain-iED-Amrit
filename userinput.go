package main
import "fmt"
func main(){
	var num int 
	fmt.Println("Enter one number")
	fmt.Scan(&num)
	if num%2==0{
	fmt.Println("Even")
	}else{
		fmt.Println("Odd")
	}
}