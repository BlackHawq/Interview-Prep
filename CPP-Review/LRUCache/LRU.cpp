#include <unordered_map>
#include <deque>

using namespace std;

class Solution {
    public:
        class LRUCache {
            private:
                int capacity;
                unordered_map<int, int> cache;
                deque<int> usage;
            public:
                LRUCache(int capacity){
                    this->capacity = capacity;
                }

                int get(int key){
                    return cache.find(key) != cache.end() ? cache[key] : -1;
                }

                void put(int key, int value);




        };
};