# Exaplination

<br><hr><br>

## A1 - Telephone, Hash Table

The code you provided implements a `TelephoneBook` class that uses a hash table for storing key-value pairs (in this case, a telephone book where the key is a phone number and the value is the name of the person). The class handles collisions in two different ways: **chaining** and **linear probing**. Let me explain the theory and logic behind the code step by step.

### Key Components of the Code:

1. **Constructor (`__init__`)**:

   * The constructor initializes the hash table with a given size (`size`) and a collision-handling method (`collision_handling`).
   * It creates an internal table (list) of the specified size, initialized with `None` to represent empty slots.
   * `self.size`: The size of the hash table.
   * `self.collision_handling`: Specifies the method used for handling collisions ('chaining' or 'linear\_probing').
   * `self.table`: A list of size `size` to hold the data.

2. **Hash Function (`hash_function`)**:

   * The hash function takes a key and returns an index within the bounds of the hash table (`key % self.size`).
   * This ensures that the key is mapped to an index in the table that is between 0 and `self.size - 1`.
   * In this case, the key is a telephone number, and the modulus operation ensures that the hash table's size is respected.

3. **Insert Method (`insert`)**:

   * **Chaining**: When a collision occurs (i.e., when two keys map to the same index), the method creates a list at that index and appends the key-value pair as a tuple `(key, value)`. Multiple values with the same hash can coexist in the list at the same index.
   * **Linear Probing**: When a collision occurs, the method uses linear probing, i.e., it checks the next index (index + 1) in the table, wrapping around to the beginning of the table if needed, until it finds an empty slot.
   * The method keeps trying to insert the key-value pair until it finds an available slot, then stores the pair there.

4. **Search Method (`search`)**:

   * **Chaining**: The method first calculates the index for the key. If there is no entry at the calculated index, it returns `None`. If there is a list, it searches through the list of key-value pairs, checking if the given key exists, and returns the corresponding value.
   * **Linear Probing**: The method calculates the index for the key. If the slot is not `None` and the key matches, it returns the corresponding value. If not, it continues to check the next index (index + 1) in a linear fashion until it finds the key or encounters an empty slot.

5. **Example Usage**:

   * Two instances of the `TelephoneBook` class are created: one with chaining and one with linear probing.
   * Phone numbers and corresponding names are inserted into both telephone books.
   * A `while` loop is used to ask the user for a key (telephone number) to search for, with validation to ensure that the input is an integer.
   * Finally, the code searches for the user-entered key in both telephone books (using chaining and linear probing) and prints the results.

### Detailed Walkthrough of Collision Handling Techniques

#### 1. **Chaining**:

* **What is it?** In chaining, each index in the hash table points to a list (or another data structure). If multiple keys hash to the same index, they are stored in that list.
* **How is it implemented?**:

  * When inserting, if the slot is empty (`None`), we initialize an empty list at that index. If it's not empty, we append the new key-value pair to the list at that index.
  * When searching, if the slot contains a list, we iterate through the list of key-value pairs and check for the matching key.

#### 2. **Linear Probing**:

* **What is it?** In linear probing, if a collision occurs (i.e., two keys hash to the same index), the algorithm checks subsequent indices in the hash table until it finds an empty slot. It "probes" the next available index in a linear manner (index + 1, wrapping around if necessary).
* **How is it implemented?**:

  * When inserting, if the index is already occupied, we continue to check the next indices until an empty slot is found.
  * When searching, if the slot contains a key, it is compared with the target key. If they match, we return the value. If not, we move to the next index and continue the search.

### Example of Code Execution

1. **Creating Telephone Books**:

   ```python
   telephone_book_chaining = TelephoneBook(10, 'chaining')
   telephone_book_linear_probing = TelephoneBook(10, 'linear_probing')
   ```

2. **Inserting Data**:

   * Both books store 3 entries:

     ```python
     telephone_book_chaining.insert(123456, 'John Doe')
     telephone_book_chaining.insert(789012, 'Jane Smith')
     telephone_book_chaining.insert(345678, 'Michael Johnson')
     ```

     In the chaining table, each phone number is placed at the index computed by the hash function. If there are collisions, the key-value pairs are added to the list at that index.

3. **Searching for a Key**:

   * The user is prompted to enter a key to search for:

     ```python
     key = int(input("Enter the key you want to search for: "))
     ```
   * Based on the selected collision-handling method, the search is performed:

     * **Chaining**: Searches the list at the computed index for the key.
     * **Linear Probing**: Probes subsequent indices until the key is found or an empty slot is encountered.

4. **Printing Results**:

   * The search results are printed for both chaining and linear probing methods:

     ```python
     if chaining_result is not None:
         print("Chaining - Telephone number for key", key, ":", chaining_result)
     else:
         print("Chaining - Key", key, "not found.")
     if linear_probing_result is not None:
         print("Linear Probing - Telephone number for key", key, ":", linear_probing_result)
     else:
         print("Linear Probing - Key", key, "not found.")
     ```

### Example Output

If the user enters `123456`, the output could look like this:

```
Enter the key you want to search for: 123456
Chaining - Telephone number for key 123456 : John Doe
Linear Probing - Telephone number for key 123456 : John Doe
```

If the key is not found, it would print something like:

```
Chaining - Key 111111 not found.
Linear Probing - Key 111111 not found.
```

### Summary

* This code simulates a telephone book using a hash table and handles collisions with two different strategies: **chaining** and **linear probing**.
* It allows for the efficient storage and retrieval of key-value pairs (phone numbers and names) with support for collision management.
* It includes a simple user interface to search for a phone number by key and demonstrates how different collision-handling strategies affect the performance of insertions and lookups.



<br><hr><br>


