# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

class TimeMap:

    # initialize object as dict
    def __init__(self):
        self.store = {}

    # set function
    def set(self, key, value, timestamp):

        # intialize new array if key not already in use
        if key not in self.store:
            self.store[key] = []
        # add value and timestamp as array to the array with the given key
        self.store[key].append([value, timestamp])
    
    # get function
    def get(self, key, timestamp):
        # result for get func as "" to start
        res = ""
        # get the list of values associated with key, if none get new array
        values = self.store.get(key, [])

        # binary search based on second index of these list of arrays
        l,r = 0, len(values) - 1
        
        while l <= r:
            mid = ( l + r ) // 2

            # valid timestamp, update res and try to find a higher timestamp that is also valid (search right half)
            if values [mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            # same as top but time stamp is too high so search left half instead 
            else:
                r = mid - 1
        # return res as "" or the closest time stamp value from binary search
        return res
    
            