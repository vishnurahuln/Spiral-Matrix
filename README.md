# SpiralMatrix
Given an m x n matrix, return all elements of the matrix in spiral order.


This is a simple python recursive code. We use the helper function to recurse through the matrix and append the elements onto the matrix.

The helper has two base conditions,

If the row or columns are within the boundary, or if value = '#'
If the length of the result hits the total number of elements in the matrix
Then we append the element onto the matrix and set the matrix value to #. We do this to avoid revisiting the nodes.

The if statement controls when the cursor needs to start going right. Else it will recurse in the wrong direction as shown in the image below.

Finally, the four recursive statements basically goes all the way right, all the way down, all the way left and all the way up. Given that we are at (row, col), where row is the row index, and col is the column index.
move right: (row, col + 1)
move downwards: (row + 1, col)
move left: (row, col - 1)
move upwards: (row - 1, col)

![WhatsApp Image 2022-01-26 at 9 55 24 AM](https://user-images.githubusercontent.com/89628033/151204779-23e895e8-042f-45b6-8988-a56a848aef32.jpeg)

PS: Please go easy on me, I just started problem solving coding a month back. I might be inefficient.
