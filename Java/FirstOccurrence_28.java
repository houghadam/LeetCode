class Solution {
    public int strStr(String haystack, String needle) {
        // If needle is longer than haystack, return not found
        if (needle.length() > haystack.length()) return -1;
        // Loop through every char in haystack
        for (int i = 0; i < haystack.length(); i++) {
            // Loop through every char in needle
            for (int j = 0; j < needle.length(); j++) {
                // Check that we have more remaining chars in haystack than needle
                if ((i + j) < haystack.length()) {
                    // If chars don't match, break loop to move on
                    if (!(needle.charAt(j) == haystack.charAt(i + j))) {
                    break;
                    // If all chars from needle match in haystack and we have zero or more chars remaining in haystack, return index of needle start
                    } else if (j == needle.length() - 1 && haystack.length() > (i+j)) {
                            return i;
                    }
                } 
            }    
        } 
        return -1;
    }
}