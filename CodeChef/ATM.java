import java.util.Scanner;
//https://www.codechef.com/problems/HS08TEST
class ATM
{
    public static void main (String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int withdraw;
        double balance;
        withdraw = sc.nextInt();
        balance = sc.nextDouble();
        double dwithdraw = withdraw;
        if(dwithdraw+0.5 > balance || dwithdraw%5 != 0)
            System.out.println(balance);
        else
            System.out.println(balance-dwithdraw-0.5);
    }
}