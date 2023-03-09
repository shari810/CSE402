import matplotlib
import matplotlib.pyplot as plt
import sns as sns

matplotlib.use('TkAgg')
import numpy as np
from decimal import Decimal
import math
import seaborn as sns

# False Match Rate(FMR) = the proportion of IMPOSTER scores greater than THRESHOLD
def FMR_calc(threshold, scores, name=""):

    total_scores = len(scores)
    greater_thresh = 0

    for val in scores:
        if val > threshold:
            greater_thresh += 1

    ratio = greater_thresh/total_scores
    return ratio
    #print("The FMR is for", name, "is: ", ratio)

# False Non-Match Rate(FNMR) = the proportion of GENUINE scores lower than the THRESHOLD
def FNMR_calc(threshold, scores, name=""):

    total_scores = len(scores)
    lower_thresh = 0

    for val in scores:
        if val < threshold:
            lower_thresh += 1

    ratio = lower_thresh/total_scores
    #print("The FNMR is for", name, "is: ", ratio)
    return ratio

def FMR_values(fmr_array, min_thresh, max_thresh, scores):

    print(1+int(((max_thresh-min_thresh)/100)))
    for x in range(min_thresh, max_thresh, 1+int(((max_thresh-min_thresh)/100))):
        fmr = FMR_calc(x, scores)
        fmr_array.append(fmr)

def FMNR_values(fnmr_array, min_thresh, max_thresh, scores):

    print(1+int(((max_thresh-min_thresh)/100)))
    for x in range(min_thresh, max_thresh, 1+int(((max_thresh-min_thresh)/100))):
        fnmr = FNMR_calc(x, scores)
        fnmr_array.append(fnmr)



def dprime(mean_gen,var_gen, mean_imp, var_imp):
    result = ( math.sqrt(2) * abs(mean_gen-mean_imp) ) / ( math.sqrt( (var_gen**2) + (var_imp**2) ) )
    return result

with open('proj01_q1_match_scores/finger_genuine.txt', 'r') as fin_gen:
    contents = fin_gen.readlines()
    gen = []
    for num in contents:
        num.strip()
        #print(num)
        gen.append(float(num))
with open('proj01_q1_match_scores/finger_impostor.txt', 'r') as fin_imp:
    contents = fin_imp.readlines()
    imp = []
    for num in contents:
        num.strip()
        #print(num)
        imp.append(float(num))
with open('proj01_q1_match_scores/hand_genuine.txt', 'r') as hand_gen:
    contents = hand_gen.readlines()
    handgen = []
    for num in contents:
        num.strip()
        #print(num)
        handgen.append(float(num))
with open('proj01_q1_match_scores/hand_impostor.txt', 'r') as hand_imp:
    contents = hand_imp.readlines()
    handimp = []
    for num in contents:
        num.strip()
        #print(num)
        handimp.append(float(num))

fg_mean = np.mean(gen)
fg_var = np.var(gen)
fi_mean = np.mean(imp)
fi_var = np.var(imp)
hg_mean = np.mean(handgen)
hg_var = np.var(handgen)
hi_mean = np.mean(handimp)
hi_var = np.var(handimp)

#print("Finger-genuine mean is: ", fg_mean)
#print("Finger-genuine variance is: ", fg_var)
#print("Finger-impostor mean is: ", fi_mean)
#print("Finger-impostor variance is: ", fi_var)
#print("Hand-genuine mean is: ", hg_mean)
#print("Hand-genuine variance is: ", hg_var)
#print("Hand-impostor mean is: ", hi_mean)
#print("Hand-impostor variance is: ", hi_var)


#finger_dprime = dprime(fg_mean,fg_var,fi_mean,fi_var)
#print("Finger matcher d-prime is: ", finger_dprime)
#hand_dprime = dprime(hg_mean,hg_var,hi_mean,hi_var)
#print("Hand matcher d-prime is: ", hand_dprime)


gen_floats = [int(x) for x in gen]
imp_floats = [int(x) for x in imp]
handgen_floats = [int(x) for x in handgen]
handimp_floats = [int(x) for x in handimp]
#print(gen_floats)
# #sns.distplot(handgen_floats, hist=False, kde=True,
#              bins=int(180/5), color = 'darkblue',
#              hist_kws={'edgecolor':'black'},
#              kde_kws={'linewidth': 1})
# sns.distplot(handimp_floats, hist=False, kde=True,
#              bins=int(180/5), color = 'darkblue',
#              hist_kws={'edgecolor':'black'},
#              kde_kws={'linewidth': 1})
#
# plt.xlabel('score')
# plt.ylabel('probability')
# plt.show()

finger_threshold = 500
hand_threshold = 300

FMR_calc(finger_threshold, imp, "finger")  #finger imposter
FMR_calc(hand_threshold, handimp, "hand") #hand imposter
FNMR_calc(finger_threshold, gen, "finger")  #finger genuine
FNMR_calc(hand_threshold, handgen, "hand") #hand genuine


finger_fmr_points = []   #x-axis
finger_fmnr_points = []    #y-axis

max_gen = max(gen_floats)
min_gen = min(gen_floats)
max_imp = max(imp_floats)
min_imp = min(imp_floats)




FMR_values(finger_fmr_points, min_imp, max_imp, imp_floats)
print(finger_fmr_points)
FMNR_values(finger_fmnr_points, min_gen, max_gen, gen_floats)
print(finger_fmnr_points)

plt.plot(finger_fmr_points[0:70], finger_fmnr_points[:70])
plt.xlabel('FMR')
plt.ylabel('FMNR')
plt.title('Fingerprint')
plt.show()


hand_fmr_points = []   #x-axis
hand_fmnr_points = []    #y-axis

max_handgen = max(handgen_floats)
min_handgen = min(handgen_floats)
max_handimp = max(handimp_floats)
min_handimp = min(handimp_floats)

FMR_values(hand_fmr_points, min_handimp, max_handimp, handimp_floats)
print(hand_fmr_points)
FMNR_values(hand_fmnr_points, min_handgen, max_handgen, handgen_floats)
print(hand_fmnr_points)

plt.plot(hand_fmr_points[0:70], hand_fmnr_points[:70])
plt.xlabel('FMR')
plt.ylabel('FMNR')
plt.title('Hand')
plt.show()



