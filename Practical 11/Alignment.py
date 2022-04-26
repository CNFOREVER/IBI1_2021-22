genedictionary = {}

human = open("DLX5_human.fa")
for line in human:
    if not line.startswith(">"):
        genedictionary ["human"] = line

mouse = open("DLX5_mouse.fa")
for line in mouse:
    if not line.startswith(">"):
        genedictionary ["mouse"] = line

random = open("RandomSeq.fa")
for line in random:
    if not line.startswith(">"):
        genedictionary ["random"] = line

human_mouse_ct=0
for i in range(len(genedictionary["human"])):
    if genedictionary["human"][i] == genedictionary["mouse"][i]:
        human_mouse_ct = human_mouse_ct + 1

mouse_random_ct=0
for i in range(len(genedictionary["mouse"])):
    if genedictionary["mouse"][i] == genedictionary["random"][i]:
        mouse_random_ct = mouse_random_ct + 1

random_human_ct=0
for i in range(len(genedictionary["random"])):
    if genedictionary["random"][i] == genedictionary["human"][i]:
        random_human_ct = random_human_ct + 1

human_mouse_per=human_mouse_ct/len(genedictionary["human"])
mouse_random_per=mouse_random_ct/len(genedictionary["mouse"])
random_human_per=random_human_ct/len(genedictionary["random"])

print(human_mouse_ct,mouse_random_ct,random_human_ct)
print(human_mouse_per,mouse_random_per,random_human_per)
