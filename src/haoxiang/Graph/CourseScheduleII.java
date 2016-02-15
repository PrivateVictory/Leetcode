package haoxiang.Graph;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by haoxiang on 16/2/15.
 */
public class CourseScheduleII {

    public  int[] findOrder(int numCourses, int[][] prerequisites) {
        if (numCourses <= 0)
            return new int[0];
        Queue<Integer> queue = new LinkedList<Integer>();
        int[] outDegree = new int[numCourses];
        int count = 0;
        int[] result = new int[numCourses];
        for (int i = 0; i < prerequisites.length; i++) {
            outDegree[prerequisites[i][0]]++;
        }
        for (int i = 0; i < outDegree.length; i++) {
            if (outDegree[i] == 0)
                queue.offer(i);
        }
        while (!queue.isEmpty()) {
            int x = queue.poll();
            result[count++] = x;
            for (int i = 0; i < prerequisites.length; i++) {
                if (x == prerequisites[i][1]) {
                    outDegree[prerequisites[i][0]]--;
                    if (outDegree[prerequisites[i][0]] == 0)
                        queue.offer(prerequisites[i][0]);
                }
            }
        }
        int i = 0;
        for (i = 0; i < outDegree.length; i++) {
            if (outDegree[i] != 0)
                break;
        }
        if (i < outDegree.length)
            return new int[0];
        else
            return result;

    }
}
