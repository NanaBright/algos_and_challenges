// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;
contract SimpSearchAlgo {
    // Function to search for a value in an array and return its index
    function search(uint256[] memory arr, uint256 value) public pure returns (int256) {
        for (uint256 i = 0; i < arr.length; i++) {
            if (arr[i] == value) {
                return int256(i);
            }
        }
        // If value not found, return -1
        return -1;
    }
}
