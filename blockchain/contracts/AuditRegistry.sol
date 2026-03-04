// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract AuditRegistry {

    struct Record {
        bytes32 hash;
        string dataType;
        uint256 timestamp;
    }

    Record[] private records;

    event RecordAdded(bytes32 hash, string dataType, uint256 timestamp);

    function addRecord(bytes32 _hash, string memory _type) public {
        Record memory newRecord = Record({
            hash: _hash,
            dataType: _type,
            timestamp: block.timestamp
        });

        records.push(newRecord);

        emit RecordAdded(_hash, _type, block.timestamp);
    }

    function getRecord(uint256 index)
        public
        view
        returns (bytes32, string memory, uint256)
    {
        require(index < records.length, "Invalid index");

        Record memory r = records[index];
        return (r.hash, r.dataType, r.timestamp);
    }

    function getRecordCount() public view returns (uint256) {
        return records.length;
    }
}