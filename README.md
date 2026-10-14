
# Social Network Adjacency Matrix

## 1. Introduction
A social network connects users through friendship
relationships. An adjacency matrix represents these
connections using a two-dimensional array.

## 2. Objective
To represent friendship connections between users
using an adjacency matrix.

## 3. Data Structure
Two-Dimensional Array (Matrix)

## 4. Algorithm
1. Store the names of users.
2. Create an adjacency matrix.
3. Use 1 for friendship and 0 for no friendship.
4. Display the matrix.
5. Display each friendship connection.

## 5. Input
Users: Amit, Rahul, Sneha, Priya

## 6. Output
A matrix showing friendship connections between users.

## 7. Time Complexity
Displaying the matrix: O(n^2)

## 8. Advantages
- Simple representation of connections.
- Checking a friendship takes O(1) time.
- Easy to understand and implement.

## 9. Limitation
An adjacency matrix requires O(n^2) space,
so it is inefficient for networks with millions
of users when most users have few friends.

## 10. Conclusion
An adjacency matrix represents friendship connections
clearly. However, large sparse social networks often
use adjacency lists to save memory.
