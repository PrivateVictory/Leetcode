package haoxiang.Array;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by haoxiang on 16/2/11.
 */
public class AddDigits {
    public int addDigits(int num) {
        if(num/10 == 0)return num;
        List<Integer> list = new ArrayList<Integer>();
        int tmp = num;
        while(tmp!=0){
            int temp = num%10;
            list.add(temp);
            tmp /=10;
        }
        int sum = 0;
        for(int j =0;j<list.size();j++){
            sum+=list.get(j);
        }
        return addDigits(sum);
    }
}
