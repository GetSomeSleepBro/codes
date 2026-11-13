// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @notice Educational one-address-one-vote demo; NOT suitable for real elections.
contract Voting {
    enum Phase { Created, Open, Closed }
    struct Candidate { string name; uint256 votes; }

    address public immutable owner;
    Phase public phase;
    Candidate[] private candidates;
    mapping(address => bool) public hasVoted;
    uint256 public totalVotes;

    event ElectionOpened();
    event ElectionClosed();
    event VoteRecorded(address indexed voter, uint256 indexed candidateId);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only election administrator");
        _;
    }

    constructor(string[] memory candidateNames) {
        require(candidateNames.length >= 2, "Need at least 2 candidates");
        owner = msg.sender;
        for (uint256 i = 0; i < candidateNames.length; ++i) {
            require(bytes(candidateNames[i]).length != 0, "Empty name");
            candidates.push(Candidate(candidateNames[i], 0));
        }
    }

    function openElection() external onlyOwner {
        require(phase == Phase.Created, "Cannot open");
        phase = Phase.Open;
        emit ElectionOpened();
    }

    function closeElection() external onlyOwner {
        require(phase == Phase.Open, "Not open");
        phase = Phase.Closed;
        emit ElectionClosed();
    }

    function vote(uint256 candidateId) external {
        require(phase == Phase.Open, "Election not open");
        require(!hasVoted[msg.sender], "Address already voted");
        require(candidateId < candidates.length, "Invalid candidate");
        hasVoted[msg.sender] = true;
        ++candidates[candidateId].votes;
        ++totalVotes;
        emit VoteRecorded(msg.sender, candidateId);
    }

    function getCandidateCount() external view returns (uint256) {
        return candidates.length;
    }

    function getCandidate(uint256 candidateId) external view returns (string memory, uint256) {
        require(candidateId < candidates.length, "Invalid candidate");
        Candidate storage c = candidates[candidateId];
        return (c.name, c.votes);
    }
}
