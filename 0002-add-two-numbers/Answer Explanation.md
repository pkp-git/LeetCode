The Question gives us two linked lists. Their elements are to be added up from left to right.

This is unlike normal addition which goes from right to left. (ones place to tens place to hundreds place and so on) 

![Sum two numbers](https://github.com/user-attachments/assets/bf5923a9-2475-465b-9a83-29a8585ab6c7)

Common errors in interpreting the question include: 
1. "We have to reverse and add it" (i'm guilty of this)
2. Ignoring the carry in the end. (say if last addition ie; the sum of the last two elements is 11 or 10. The carry 1 gets ignored.

Approach: 
1. Run a while loop as long as l1 or l2 have elements in them, or carry exists (to mitigate Error 2)
2. Get respective values from both linked lists. If due to a length diffference like in the picture above we encounter missing values fill the missing value with 0.
3. Add the two values and carry (which initially is 0). 
4. From the sum obtained, separate the carry and append the ones place digit to Final linked list (The solution linked list)
5. Go to next node (l.next)
6. repeat 2,3,4,5 till no more elements or carry remains. 
