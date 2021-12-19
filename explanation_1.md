LRU Cache

- Design
    - A doubly linked list along with hash map is used to implement lru cache.
      Using a doubly linked list allows to easily move the nodes around
      depending on the access frequency. Hash map maps the keys to nodes in the
      doubly linked list. The least frequently accessed node is present at the
      beginning of the list.
- Time Complexity
    - O(1) for get
    - O(1) for put
- Space Complexity
    - O(n) if there are n elements in the cache
