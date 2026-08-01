class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a map with defaultdict to have values
        # before the list actually is assigned
        map = defaultdict(list)

        # iterate through each word in the array
        for word in strs:
            # Create the 26 buckets for each letter
            count = [0] * 26
            
            # for every letter in the word we subtract the letter's
            # ASCII from a and add it to the bucket it is in
            for letter in word:
                count[ord(letter) - ord("a")] += 1

            # then we append it to the maps values and
            # we have to use tuple because a dicts keys are
            # immutable
            map[tuple(count)].append(word)
        
        # then return a LIST of the map values
        return list(map.values())
