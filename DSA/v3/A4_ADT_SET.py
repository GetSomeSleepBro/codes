'''
OUESTION:
   To create ADT that implement the "set" concept.
   a. Add (newElement) -Place a value into the set
   b. Remove (element) Remove the value
   c. Contains (element) Return true if element is in collection
   d. Size () Return number of values in collection Iterator () 
      Return an iterator used to loop over collection
   e. Intersection of two sets
   f. Union of two sets
   g. Difference between two sets
   h. Subset

OUTPUT:
  Create Set 1:
  Enter the number of elements in the set: 3
  Enter an element: 1
  Enter an element: 2
  Enter an element: 3
  
  Create Set 2:
  Enter the number of elements in the set: 3
  Enter an element: 3
  Enter an element: 4
  Enter an element: 5
  
  Set 1: [1, 2, 3]
  Set 2: [3, 4, 5]
  
  Choose an operation:
  1. Intersection
  2. Union
  3. Difference (Set 1 - Set 2)
  4. Check Subset
  5. Exit
  Enter your choice (1/2/3/4/5): 1
  
  Intersection: [3]
  
  Choose an operation:
  1. Intersection
  2. Union
  3. Difference (Set 1 - Set 2)
  4. Check Subset
  5. Exit
  Enter your choice (1/2/3/4/5): 3
  
  Difference (Set 1 - Set 2): [1, 2]
'''

class Set:
    def __init__(self):
        self.elements = []

    def add(self, newElement):
        if newElement not in self.elements:
            self.elements.append(newElement)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def contains(self, element):
        return element in self.elements

    def size(self):
        return len(self.elements)

    def iterator(self):
        return iter(self.elements)

    def intersection(self, otherSet):
        intersectionSet = Set()
        for element in self.elements:
            if otherSet.contains(element):
                intersectionSet.add(element)
        return intersectionSet

    def union(self, otherSet):
        unionSet = Set()
        unionSet.elements = self.elements.copy()
        for element in otherSet.elements:
            unionSet.add(element)
        return unionSet

    def difference(self, otherSet):
        differenceSet = Set()
        for element in self.elements:
            if not otherSet.contains(element):
                differenceSet.add(element)
        return differenceSet

    def subset(self, otherSet):
        for element in self.elements:
            if not otherSet.contains(element):
                return "Set 1 is Not a Subset of Set 2"
        return "Set 1 is a Subset of Set 2"

    def display(self):
        print("Current Set:", self.elements)



def create_set_from_input():
    s = Set()
    num_elements = int(input("Enter the number of elements in the set: "))
    for _ in range(num_elements):
        element = int(input("Enter an element: "))
        s.add(element)
    return s


def main():
  print("Create Set 1:")
  set1 = create_set_from_input()
  
  print("Create Set 2:")
  set2 = create_set_from_input()
  
  print("Set 1:", list(set1.iterator()))
  print("Set 2:", list(set2.iterator()))
  
  while True:
      print("\nChoose an operation:")
      print("1. Intersection")
      print("2. Union")
      print("3. Difference (Set 1 - Set 2)")
      print("4. Check Subset")
      print("5. Exit")
      choice = input("Enter your choice (1/2/3/4/5): ")
  
      if choice == "1":
          print("Intersection:", list(set1.intersection(set2).iterator()))
      elif choice == "2":
          print("Union:", list(set1.union(set2).iterator()))
      elif choice == "3":
          print("Difference (Set 1 - Set 2):", list(set1.difference(set2).iterator()))
      elif choice == "4":
          print(set1.subset(set2))
      elif choice == "5":
          print("Exiting...")
          break
      else:
          print("Invalid choice! Please enter a valid option (1/2/3/4/5).")

if __name__ == "__main__":
  main()
