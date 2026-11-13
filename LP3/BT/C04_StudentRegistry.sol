// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @notice SPPU Lab Group C #4: struct, array, receive and fallback examples.
contract StudentRegistry {
    struct Student {
        string name;
        uint256 age;
    }

    Student[] private students;
    uint256 public totalEtherReceived;
    event StudentAdded(uint256 indexed index, string name, uint256 age);
    event EtherReceived(address indexed sender, uint256 amount, bool viaFallback);

    function addStudent(string calldata name, uint256 age) external {
        require(bytes(name).length != 0, "Name required");
        require(age > 0, "Age must be positive");
        students.push(Student(name, age));
        emit StudentAdded(students.length - 1, name, age);
    }

    function getStudent(uint256 index) external view returns (string memory, uint256) {
        require(index < students.length, "Invalid student index");
        Student storage student = students[index];
        return (student.name, student.age);
    }

    function getStudentCount() external view returns (uint256) {
        return students.length;
    }

    receive() external payable {
        totalEtherReceived += msg.value;
        emit EtherReceived(msg.sender, msg.value, false);
    }

    fallback() external payable {
        totalEtherReceived += msg.value;
        emit EtherReceived(msg.sender, msg.value, true);
    }
}
