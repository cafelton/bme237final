
from matplotlib_venn import venn3
from matplotlib_venn import venn2
from matplotlib import pyplot as plt
a_all, a_csc_not_air, a_all_ext, a_csc_not_air_ext = [], [], [], []
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allFusions-arriba.txt"): a_all.append(line.strip())
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allDFusions-arriba.txt"): a_all_ext.append(line.strip())
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirFusions-arriba.txt"): a_csc_not_air.append(line.strip())
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirDFusions-arriba.txt"): a_csc_not_air_ext.append(line.strip())
k_all, k_csc_not_air, k_all_ext, k_csc_not_air_ext = [], [], [], []
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/allFusions.txt"): k_all.append(line.strip())
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/allDFusions.txt"): k_all_ext.append(line.strip())
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscNotAirFusions.txt"): k_csc_not_air.append(line.strip())
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscNotAirDFusions.txt"): k_csc_not_air_ext.append(line.strip())
s_all, s_csc_not_air, s_all_ext, s_csc_not_air_ext = [], [], [], []
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allFusions-star.txt"): s_all.append(line.strip())
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allDFusions-star.txt"): s_all_ext.append(line.strip())
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirFusions-star.txt"): s_csc_not_air.append(line.strip())
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirDFusions-star.txt"): s_csc_not_air_ext.append(line.strip())
# print("Star-arriba", set(s_all).intersection(a_all_ext))
# print("Star-kallisto", set(s_all).intersection(k_all_ext))
# print("arriba-star", set(a_all).intersection(s_all_ext))
# print("arriba-kallisto", set(a_all).intersection(k_all_ext))
print(len(s_all_ext), len(a_all_ext), len(k_all_ext))
clinical = []
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/gene-list-V2"): clinical.append(line.strip())
clinical = set(clinical)
clinical = {'ALK', 'RET', 'ROS1', 'NTRK1'}
#print(clinical)
c = 0
for a in s_all:
    b =  a.split('--')
    #print(b)
    if b[0] in clinical or b[1] in clinical:
        c += 1
        #print(a)
print("starClinical", c)
c = 0
for a in s_all_ext:
    b =  a.split('--')
    if b[0] in clinical or b[1] in clinical:
        c += 1
        #print(a)
print("starExtClinical", c)
c = 0
for a in a_all:
    b =  a.split('--')
    if b[0] in clinical or b[1] in clinical:
        c += 1
        #print(a)
print("arrClinical", c)
c = 0
for a in a_all_ext:
    b =  a.split('--')
    if b[0] in clinical or b[1] in clinical:
        c += 1
        #print(a)
print("arrExtClinical", c)
c = 0
for a in k_all_ext:
    b =  a.split('--')
    if b[0] in clinical or b[1] in clinical:
        c += 1
        #print(a)
print("kallExtClinical", c)


plt.figure(figsize=(4,4))
venn2([set(a_all), set(s_all)], set_labels=('Arriba', 'STAR-Fusion'))
plt.title("All Filtered Fusion Calls")
plt.savefig("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/filteredFusionOverlap.png")
plt.figure(figsize=(4,4))
venn3([set(a_all_ext), set(k_all_ext), set(s_all_ext)], set_labels=('Arriba', 'Kallisto', 'STAR-Fusion'))
plt.title("All Fusion Calls Pre-Filtering")
plt.savefig("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/notfilteredFusionOverlap.png")
