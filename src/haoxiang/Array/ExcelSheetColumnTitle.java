package haoxiang.Array;

import java.util.HashMap;

/**
 * Created by haoxiang on 16/2/19.
 */
public class ExcelSheetColumnTitle {
    public String convertToTitle(int n) {

        int num = n;
        String res = "";
        HashMap<Integer,String> map = new HashMap<Integer,String>();
        map.put(1,"A");
        map.put(2,"B");
        map.put(3,"C");
        map.put(4,"D");
        map.put(5,"E");
        map.put(6,"F");
        map.put(7,"G");
        map.put(8,"H");
        map.put(9,"I");
        map.put(10,"J");
        map.put(11,"K");
        map.put(12,"L");
        map.put(13,"M");
        map.put(14,"N");
        map.put(15,"O");
        map.put(16,"P");
        map.put(17,"Q");
        map.put(18,"R");
        map.put(19,"S");
        map.put(20,"T");
        map.put(21,"U");
        map.put(22,"V");
        map.put(23,"W");
        map.put(24,"X");
        map.put(25,"Y");
        map.put(26,"Z");
        while(num > 0 ){
            int tmp = num%26;
            res+=map.get(tmp);
            num/=26;
        }
        StringBuilder sb = new StringBuilder(res);
        return sb.reverse().toString();

    }
}
