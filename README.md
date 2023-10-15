Design a Priority Message Queue that satisfy the requirements below:

- Priority value is integer. Message will be consumed from the highest priority
- The Queue must be thread-safety and able for multiple producer, consumer to send and retrieve the message concurrently
- When the queue is almost full (90%), "High-water-mark" event will be created (this can be changed in configuration). Writer thread can use this event to suspend writting to the queue
- When the queue is almost empty (10%), "Low-water-mark" event will be created (this can be changed in configuration)
- Add some unit test to prove the solution works
