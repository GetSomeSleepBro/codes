// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    
    // 1. Structure to define Student properties
    struct Student {
        uint id;
        string name;
        uint age;
        bool enrolled;
    }

    // 2. Array to store multiple Student structures dynamically
    Student[] public students;

    // Event to log when a student is added
    event StudentAdded(uint id, string name, uint age);

    // Function to add a new student to the array
    function addStudent(uint _id, string memory _name, uint _age) public {
        students.push(Student({
            id: _id,
            name: _name,
            age: _age,
            enrolled: true
        }));
        
        emit StudentAdded(_id, _name, _age);
    }

    // Function to retrieve total student count
    function getStudentCount() public view returns (uint) {
        return students.length;
    }

    // 3. Fallback function: triggered when ether is sent with invalid data or function selector
    fallback() external payable {
        // Custom logic or state changes can go here
    }

    // Receive function for plain Ether transfers (recommended best practice alongside fallback)
    receive() external payable {
        // Accepts direct ETH transfers to the contract
    }
}
