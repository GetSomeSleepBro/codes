// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 BT Mini Project
 Develop a Blockchain based application dApp (de-centralized app) for e-voting system.

 Flow: admin (deployer) adds candidates -> registers voters -> starts voting ->
 each registered voter votes once -> admin ends voting -> anyone can see the winner.
*/

contract Voting {
    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    address public admin;
    bool public votingOpen;
    bool public hasStarted;
    bool public hasEnded;
    Candidate[] public candidates;
    mapping(address => bool) public isRegistered;
    mapping(address => bool) public hasVoted;

    event CandidateAdded(uint256 id, string name);
    event VoterRegistered(address voter);
    event Voted(address voter, uint256 candidateId);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can do this");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    function addCandidate(string memory _name) public onlyAdmin {
        require(!hasStarted, "Cannot add candidates after election starts");
        require(bytes(_name).length > 0, "Candidate name required");
        candidates.push(Candidate(candidates.length, _name, 0));
        emit CandidateAdded(candidates.length - 1, _name);
    }

    function registerVoter(address _voter) public onlyAdmin {
        require(!hasStarted, "Registration closed");
        require(_voter != address(0), "Invalid voter");
        require(!isRegistered[_voter], "Voter already registered");
        isRegistered[_voter] = true;
        emit VoterRegistered(_voter);
    }

    function startVoting() public onlyAdmin {
        require(!hasStarted, "Election already started");
        require(candidates.length >= 2, "Need at least 2 candidates");
        hasStarted = true;
        votingOpen = true;
    }

    function endVoting() public onlyAdmin {
        require(votingOpen && !hasEnded, "Election not open");
        votingOpen = false;
        hasEnded = true;
    }

    function vote(uint256 _candidateId) public {
        require(votingOpen, "Voting is not open");
        require(isRegistered[msg.sender], "You are not a registered voter");
        require(!hasVoted[msg.sender], "You have already voted");
        require(_candidateId < candidates.length, "Invalid candidate");
        hasVoted[msg.sender] = true;
        candidates[_candidateId].voteCount++;
        emit Voted(msg.sender, _candidateId);
    }

    function getCandidateCount() public view returns (uint256) {
        return candidates.length;
    }

    function getAllCandidates() public view returns (Candidate[] memory) {
        return candidates;
    }

    function getWinner() public view returns (string memory name, uint256 votes) {
        require(hasEnded, "Election is not closed");
        require(candidates.length > 0, "No candidates");
        uint256 winner = 0;
        for (uint256 i = 1; i < candidates.length; i++) {
            if (candidates[i].voteCount > candidates[winner].voteCount) winner = i;
        }
        return (candidates[winner].name, candidates[winner].voteCount);
    }
}
