# AdventOfCode_2020

### Code snippets from Advent of Code 2020. Using as an excuse to drag myself out of R where I am pretty comfortable and get some daily work in with Python.

### Notes:  
- Day 1: Not too bad some quick nested for loops and we're off to the races. 
- Day 2: Got frustrated with pandas, too used to the tidyverse - ended up doing some in excel due to time constraints (got a late start) and the simple frustration of knowing what I wanted to do but struggling to implement it in code.  
- Day 3: Back on track - pretty simple breakdown, follow the instructions, no major snags in this one.
- Day 4: That was a doozy. Had to watch my regex. Been a while since I've used and spent a while debugging why I was off on the final count (by 1!) . Starting to remember to use functions to my advantage.
- Day 5: Went pretty smooth - sure my code could be cleaned up but pulled through this one in a decent time. *Note to self: remember to clear the new line character from text data when parsing... 
- Day 6: Def need to figure out a cleaner way to deal with last line of text files when breaking up groups, but short and sweet.
- Day 7: This was another tough one. My code's a mess, but it does the job for now. Half the challenge was just wrapping mind around the problem and how to solve it. This was the first day I didn't immediately have a good idea how to get to a solution. The recursiveness took a while to wrap my mind around and figure out how to handle. First attempt writting everything to a variable gave memory error. Whoops. Lesson learned. Massive tree structure of suitcases inside of suitcases inside of suitcases... you get it. Besides the mindwarp hit a few snags forgetting that Python will edit a list in place - defining a new list from an old one can get dangerous. But good to break out the dictionaries and experiment with them. Definitly going to look up other solutions to this one as I'm fairly confident the approach I took is not the most efficient.
- Day 8: Phew. Short and sweet, no major roadblocks on this one. Some fairly simple functions to define what should happen at each line and while loops to control the flow. Part 2 was fun, get to use the index to find the solution.
- Day 9: Another relatively easy day. Reused a bit of code from day one to check for the sum in the first part. Second part iterativly approach summing up the rows. There may be a faster way to do this, but the dataset is small enough brute force works just fine.
- Day 10: Part 1: Cakewalk! Just sort and find the differences. Part 2: Ugh, It was a trap! Finally managed to brute force some code that worked on the test files, but main file was too long. Ended up having to look to others for the solution to this one. Included my favorite solution I found (and reference) in the code at the end.
- Day 11: Part 1: This one took a little bit of effort but all in wasn't too bad. Part 2. Checking for edge conditions got much trickier with the new rules and it took me a while to figure out how to handle them. Also got mixed up on some variables referencing rows vs columns and got hung up in some endless loops for a bit. Finally got the code to run, but definatly not the most elegant solution. A bit slow as well. But it does the job.
- Day 12: Phew. Finally a relatively easy day again. Made some good use of Dicts to make solving this one short and sweet. Set up of part 1 made part 2 pretty easy, just had to add in an extra function to handle rotation of the waypoint, everything else was simply redefining which point was moving and where. I needed this one, was close to getting burned out over the last couple of days.
- Day 13: Part 1 was relatively straight forward. Part 2, due to the size of the problem proved to be quite tricky. Was able to build brute force code that would work on the example file but obviously wouldn't work on the real data. Tried playing around with a least common multiple type solution, but the offsets made it tricky. Finally gave up and looked to the interwebs for inspiration and found an approach that clicked. There's also an approach using the Chinese Remainder Theorem, but this approach made more intuitive sense to me.
- Day 14: Had to brush up on binary numbers, but this one was pretty straightforward. Trickiest part was just reading the problem, particuarlly part 2 where the problem becomes how you map the data to memory. I liked this one, some interesting twists to it and it was satisfying to solve.
- Day 15: For some reason I spent way too much time trying to parse the first 3 starting values in, rather than just starting my counter at 4 and being done with it. Once I cleared this hurdle was pretty straightforward. Had to optimize the code a bit to run faster for the 30M row case. Was unnecessarily writing all the outputs to a list which I really didn't need to. Need to work on keeping code clean of unnessesary junk.
- Day 16: A bit involved today but no major hiccups. Trickiest part was actually matching the ticket fields to their values, since there were so many duplicates. But I noticed each had one more than another in the set, so by iteratively selecting them, then removing the lowest value, can parse out which ticket value goes to which field. Quickly learning to love dictionaries for these challenges.
- Day 17: Careful planning paid off in this one. The intial problem revolves around 3 dimensional space. By setting this part up propperly using a dictionary to track the positions, it was relatively trivial to add the fourth dimension to part 2. That being said, part 2 dramatically increases the runtime of the code, so overall I'm sure there is a more efficient way to approach this, but all in all, I'm pleased that this worked as well as it did.
- Day 18: Non standard order of operations calculator. Worked thorugh part 1, not too bad, got stuck on part 2. Had to look once again to the solutions thread for an answer that made sense to me.
- Day 19: The late nights caught up to me. Passed out on the couch. So didn't get a chance to look at the problem till the morning. Gave it a shot with some recursion and nested lists before fairly quickly realizing that was going to blow up in my face. From the hints threads, regex seems to be the key and regex's are... not my particular strength. Didn't have a lot of time to devote to this today, so unabashedly borrowed some code from the solutions thread and worked my way though to understand it. This is a learning process afterall. Definatly going to add regex refresher to my todo list.
- Day 20: I came to the realization early on in part 1 that I didn't actually need to solve and arrange the entire picture for part 1 - I just needed to determine which 4 pieces were the corners, which was much more straightforward. Just find which pieces only matched on 2 edges with any other pieces and those 4 would be the answer. Of course, part 2 still requires I figure out the arrangement...TBD at a later date...
- Day 21: Woohoo! Much simpler problem tonight. Even was able to reuse some of the recursive matching from Day 16 for getting to the answer on part 2. Not bad at all tonight.