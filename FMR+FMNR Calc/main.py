# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# False Match Rate(FMR) = the proportion of IMPOSTER scores greater than THRESHOLD
def FMR_calc(threshold, scores, name):

    total_scores = len(scores)
    greater_thresh = 0

    for val in scores:
        if val > threshold:
            greater_thresh += 1

    ratio = greater_thresh/total_scores
    print("The FMR is for", name, "is: ", ratio)

# False Non-Match Rate(FNMR) = the proportion of GENUINE scores lower than the THRESHOLD
def FNMR_calc(threshold, scores, name):

    total_scores = len(scores)
    lower_thresh = 0

    for val in scores:
        if val < threshold:
            lower_thresh += 1

    ratio = lower_thresh/total_scores
    print("The FNMR is for", name, "is: ", ratio)


with open('finger_genuine.txt', 'r') as fin_gen:
    contents = fin_gen.readlines()
    gen = []
    for num in contents:
        num.strip()
        #print(num)
        gen.append(float(num))
with open('finger_imposter.txt', 'r') as fin_imp:
    contents = fin_imp.readlines()
    imp = []
    for num in contents:
        num.strip()
        #print(num)
        imp.append(float(num))

print("Genuine Finger score Max is: ", max(gen))
print("Genuine Finger score Min is: ", min(gen))
print("Imposter Finger score Max is: ", max(imp))
print("Imposter Finger score Min is: ", min(imp))


with open('hand_genuine.txt', 'r') as hand_gen:
    contents = hand_gen.readlines()
    handgen = []
    for num in contents:
        num.strip()
        #print(num)
        handgen.append(float(num))
with open('hand_imposter.txt', 'r') as hand_imp:
    contents = hand_imp.readlines()
    handimp = []
    for num in contents:
        num.strip()
        #print(num)
        handimp.append(float(num))

print("Genuine hand score Max is: ", max(handgen))
print("Genuine hand score Min is: ", min(handgen))
print("Imposter hand score Max is: ", max(handimp))
print("Imposter hand score Min is: ", min(handimp))


# False Match Rate(FMR) = the proportion of IMPOSTER scores greater than THRESHOLD
# False Non-Match Rate(FNMR) = the proportion of GENUINE scores lower than the THRESHOLD
threshold = 45

FMR_calc(threshold, imp, "finger")  #finger imposter
FMR_calc(threshold, handimp, "hand") #hand imposter
FNMR_calc(threshold, gen, "finger")  #finger genuine
FNMR_calc(threshold, handgen, "hand") #hand genuine


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


