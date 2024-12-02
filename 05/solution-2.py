import sys
from collections import defaultdict

def get_score(update, rules):
    is_ordered = True
    for i in range(len(update)-1):
            for j in range(i+1, len(update)):
                if update[i] in rules[update[j]]:
                    # swap them
                    tmp = update[j]
                    update[j] = update[i]
                    update[i] = tmp
                    is_ordered = False
    return 0 if is_ordered else update[int(len(update)/2)]
    
with open(sys.argv[1]) as f:
    rules, updates = f.read().split("\n\n")

rules = [rule.split("|") for rule in rules.split("\n") ]
updates = [update.split(',') for update in [x for x in updates.split('\n')]]

rule_table = defaultdict(list)
for a,b in rules:
    rule_table[a].append(b)
    
result = sum(int(get_score(update, rule_table)) for update in updates)
print(result)