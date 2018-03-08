### Youbin 2017/06/23
### 371 Sum of Two Integers

class Solution {
public:
    int getSum(int a, int b) {
        int sum = a^b;
        int carry = a&b;
        int buff;
        while (carry!=0){
            carry = carry<<1;
            buff = carry^sum;
            carry = carry&sum;
            sum = buff;
        }
        return sum;
        
    }
};