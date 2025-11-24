# dsa-assignment-2
# 📚 DSA Assignment 2 - Library Book Management System

**Name:** Manjeet Yadav  
**Roll No:** 2401420045
**Course:** B-Tech CSE Data  
**Assignment:** 02  
**Submission Filename:** `045Assignment-2.py`

## 🧠 Problem Statement

Develop a **Library Book Management System** using:
- **Singly Linked List** to maintain a collection of books.
- **Stack** to maintain transaction history (issue/return) and enable **Undo** operation.

The system should support:
- Inserting new books  
- Deleting a book  
- Searching for a book by ID  
- Displaying all books  
- Issuing and returning books  
- Undoing the last transaction using stack operations

## ⚙️ Implementation Files

| File Name | Description |
|------------|-------------|
| `linkedlist.py` | Defines `Book` and `BookLinkedList` classes (insert, delete, search, display). |
| `stack.py` | Defines `Transaction` and `TransactionStack` classes (push, pop, view transactions). |
| `main.py` | Demonstrates the system: adds books, issues, returns, and performs undo operation. |
| `045Assignment-2.pdf` | PDF report formatted for submission. |

## 🧩 Data Structures Used

### 🔹 Singly Linked List
- Each node represents a `Book` object.
- Links all books in sequence.
- Enables traversal, insertion, and deletion.

### 🔹 Stack
- Used to record transactions (ISSUE or RETURN).
- Supports **LIFO** (Last In First Out) behavior for Undo operation.
