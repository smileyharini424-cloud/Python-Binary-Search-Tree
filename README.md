# Python Binary Search Tree

## Explanation

A Binary Search Tree (BST) is a binary tree in which:

* Values smaller than the root are stored in the left subtree.
* Values greater than the root are stored in the right subtree.

This property makes searching and inserting elements efficient.

## Problem Statement

Write a Python program to implement a Binary Search Tree.

The program should support:

* Insertion
* Searching
* Inorder traversal

## Features

* Creates a Binary Search Tree
* Inserts elements according to BST rules
* Searches for an element
* Performs inorder traversal
* Displays elements in sorted order

## How It Works

1. A `Node` class is created to store data.
2. The `insert()` function places values according to BST rules.
3. The `search()` function searches for a specified value.
4. The `inorder()` function traverses the tree.
5. Inorder traversal displays BST elements in ascending order.

## Technologies Used

* Python 3

## Data Structure Used

* Binary Search Tree
* Nodes

## Methods Used

* `__init__()`
* `insert()`
* `search()`
* `inorder()`

## Program Flow

1. Create an empty BST.
2. Insert elements into the tree.
3. Display the inorder traversal.
4. Enter a value to search.
5. Search the tree.
6. Display whether the element was found.

## Sample Input

```text
Enter elements: 50 30 70 20 40 60 80
Enter element to search: 40
```

## Sample Output

```text
Inorder Traversal: 20 30 40 50 60 70 80
Element found in BST.
```

## Time Complexity

Average case:

* Insertion: O(log n)
* Search: O(log n)
* Inorder Traversal: O(n)

Worst case for an unbalanced BST:

* Insertion: O(n)
* Search: O(n)

## Space Complexity

* O(n)

## Key Learning

* Understanding Binary Search Trees
* Understanding BST properties
* Implementing insertion
* Implementing searching
* Performing inorder traversal
* Understanding balanced and unbalanced trees

## File Location

```text
Python-Binary-Search-Tree/binary_search_tree.py
```

## Repository Structure

```text
Python-Binary-Search-Tree/
│
├── binary_search_tree.py
└── README.md
```

## Author

V.Harini
