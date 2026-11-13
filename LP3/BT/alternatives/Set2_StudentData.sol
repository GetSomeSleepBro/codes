// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 BT Assignment 4
 Write a program in solidity to create Student data. Use the following constructs:
   - Structures
   - Arrays
   - Fallback
 Deploy this as smart contract on Ethereum and observe the transaction fee and Gas values.

 After every transaction, open the Remix terminal (bottom) -> click the transaction ->
 note "gas", "transaction cost" and "execution cost". On Sepolia, open the tx on
 sepolia.etherscan.io to see Gas Used, Gas Price and Transaction Fee.
*/

contract StudentData {
    // Structure
    struct Student {
        uint256 rollNo;
        string name;
        string department;
        uint256 marks;
    }

    // Array of structures
    Student[] public students;

    event StudentAdded(uint256 rollNo, string name);
    event FallbackCalled(address sender, uint256 value, bytes data);
    event EtherReceived(address sender, uint256 value);

    function addStudent(uint256 _rollNo, string memory _name, string memory _department, uint256 _marks) public {
        for (uint256 i = 0; i < students.length; i++) {
            require(students[i].rollNo != _rollNo, "Roll number already exists");
        }
        students.push(Student(_rollNo, _name, _department, _marks));
        emit StudentAdded(_rollNo, _name);
    }

    function getStudent(uint256 _rollNo) public view returns (string memory, string memory, uint256) {
        for (uint256 i = 0; i < students.length; i++) {
            if (students[i].rollNo == _rollNo) {
                return (students[i].name, students[i].department, students[i].marks);
            }
        }
        revert("Student not found");
    }

    function getStudentCount() public view returns (uint256) {
        return students.length;
    }

    function getAllStudents() public view returns (Student[] memory) {
        return students;
    }

    // Fallback: runs when a function that does not exist is called (or calldata is sent)
    fallback() external payable {
        emit FallbackCalled(msg.sender, msg.value, msg.data);
    }

    // Receive: runs when plain Ether is sent with empty calldata
    receive() external payable {
        emit EtherReceived(msg.sender, msg.value);
    }
}
