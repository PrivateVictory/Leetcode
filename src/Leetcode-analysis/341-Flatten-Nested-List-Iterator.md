# [341. Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/)

> Given a nested list of integers, implement an iterator to flatten it.

> Each element is either an integer, or a list -- whose elements may also be integers or other lists.

> Example 1:Given the list [[1,1],2,[1,1]],

> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

> Example 2:Given the list [1,[4,[6]]],

> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

题目的要求是要把一个嵌套的list给变成一个普通的list，用iterator遍历其中所有的整数。但是在list之中可能有list，层层嵌套，要想取得其中的整数，需要层层递归下去。可以使用栈来实现。


	/**
	 // This is the interface that allows for creating nested lists.
	 // You should not implement it, or speculate about its implementation
	 public interface NestedInteger {
	 *
	     // @return true if this NestedInteger holds a single integer, rather than a nested list.
	     public boolean isInteger();
	 *
	     // @return the single integer that this NestedInteger holds, if it holds a single integer
	     // Return null if this NestedInteger holds a nested list
	     public Integer getInteger();
	 *
	     // @return the nested list that this NestedInteger holds, if it holds a nested list
	     // Return null if this NestedInteger holds a single integer
	     public List<NestedInteger> getList();
	 }
	 */
	public class NestedIterator implements Iterator<Integer> {

		private Stack<Integer> nestedStack = new Stack<Integer>();
		private Iterator<Integer> iterator;
		
	    public NestedIterator(List<NestedInteger> nestedList) {
	    	if(nestedList==null) return;
	    	recursion(nestedList);
	    	iterator = nestedStack.iterator();
	    }
	    
	    private void recursion(List<NestedInteger> nestedList){
	    	if(nestedList==null) return;
	    	Iterator<NestedInteger> it = nestedList.iterator();
	    	while(it.hasNext()){
	    		NestedInteger ni = it.next();
	    		if(ni.isInteger()) nestedStack.push(ni.getInteger());
	    		else{
	    			recursion(ni.getList());
	    		}
	    	}
	    }

	    @Override
	    public Integer next() {
	    	return iterator.next();
	    }

	    @Override
	    public boolean hasNext() {
	    	return iterator.hasNext();
	    }
	}



