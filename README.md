This is the code for Compsci342 Above and Beyond 3

The algorithm works by first completely shuffling the groups so that the order is arbitrary (fair). It then goes down the list of groups and attempts to give the first group their first choice. It does this by looking for the next group below it with the same first preference. If this group exists, they will both be added to the results (they both get their top choice). If not, it looks for the group below it with the same second choice as it's first, and similarly if this isn't found it looks for a group with the third-choice equal to its first. If none of these are found, the first group attempts to match its second and third preferences respectively. If none of these are found, the group will get added to the unmatchables array, which will be dealt with later.

The above was hard to explain in words, essentially you move down the list of groups and try to match group i with any group j where j > i in this order:  
Pref 1 for i & Pref 1 for j (obviously ideal scenario)  
Pref 1 for i & Pref 2 for j (give priority to i because it comes first in the random order)  
Pref 1 for i & Pref 3 for j  
Pref 2 for i & Pref 1 for j  
Pref 2 for i & Pref 2 for j  
Pref 2 for i & Pref 3 for j  
Pref 3 for i & Pref 1 for j... etc.  

I also included a MAX_THRESHOLD constant that can be set to mandate that their cannot be more than N groups for a given project. This will stop the case where 90% of the groups choose 1 topic. 

Finally, we deal with the unmatchables. It is rare that a group will even be included in this array, unless the threshold is very small. For the unmatchable groups, we simply pair them together and put them in the topics that currently have the fewest students -- we're trying to balance out the groups again. This may seem unfair for a given group, but really the only way you can get on the unmatcheable list is if you were low in the random order -- some groups have to take a topic that isn't their preference if we want to have balanced topics, and this is determined by the random order, so every group is just as likely. It is also likely that there will be no groups in the unmatchable array. Also, if there is an odd number of groups, one group will be in the unmatcheable array that will have to go by themselves -- there's no way around this, but groups of 2 are favored.

I generated random netids and group preferences for the purposes of testing. See netids.txt and preferences.txt
