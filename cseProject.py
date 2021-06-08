
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/1air_fusion-short.txt", "w")
# types = []
# for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/1air_fusion.txt", "r"):
#     line = line.split('\t')
#     if line[0] != "TYPE":
#         side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
#         # print(side1, side2)
#         types.append(side1[-2])
#         types.append(side2[-2])
#         out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
# out.close()
# print(set(types))
#
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/2air_fusion-short.txt", "w")
# for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/2air_fusion.txt", "r"):
#     line = line.split('\t')
#     if line[0] != "TYPE":
#         side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
#         # print(side1, side2)
#         out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
# out.close()
#
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/3air_fusion-short.txt", "w")
# for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/3air_fusion.txt", "r"):
#     line = line.split('\t')
#     if line[0] != "TYPE":
#         side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
#         out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
# out.close()
#
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/1csc_fusion-short.txt", "w")
# for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/1csc_fusion.txt", "r"):
#     line = line.split('\t')
#     if line[0] != "TYPE":
#         side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
#         out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
# out.close()
#
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/2csc_fusion-short.txt", "w")
# for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/2csc_fusion.txt", "r"):
#     line = line.split('\t')
#     if line[0] != "TYPE":
#         side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
#         out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
# out.close()
#
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/3csc_fusion-short.txt", "w")
# for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/3csc_fusion.txt", "r"):
#     line = line.split('\t')
#     if line[0] != "TYPE":
#         side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
#         out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
# out.close()


# allTypes = {'TEC', 'unitary_pseudogene', 'Mt_tRNA', 'retained_intron', 'scaRNA', 'scRNA', 'transcribed_processed_pseudogene', 'misc_RNA', 'protein_coding', 'polymorphic_pseudogene', 'processed_transcript', 'lncRNA', 'unprocessed_pseudogene', 'rRNA_pseudogene', 'snRNA', 'pseudogene', 'rRNA', 'transcribed_unprocessed_pseudogene', 'translated_processed_pseudogene', 'transcribed_unitary_pseudogene', 'processed_pseudogene', 'non_stop_decay', 'miRNA', 'snoRNA', 'Mt_rRNA', 'nonsense_mediated_decay'}
# goodTypes = {'retained_intron', 'transcribed_processed_pseudogene', 'protein_coding', 'processed_transcript', 'lncRNA'}
# allFusions = []
# airF, cscF = [], []
# allGFusions, airGF, cscGF = [], [], []
# for a in ["1air", '2air', '3air', '1csc', '2csc', '3csc']:
#     out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/" + a + "_fusion-filtered.txt", "w")
#     outS = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/" + a + "_fusion-strenuous.txt", "w")
#     outF = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/" + a + "_fusion-names.txt", "w")
#     for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/" + a + "_fusion-short.txt", "r"):
#         temp = line.split('\t')
#         if temp[2][:3] != "MT-" and temp[4][:3] != "MT-":
#             if temp[3] in goodTypes and temp[5] in goodTypes:
#                 out.write(line)
#             if temp[3] == 'protein_coding' and temp[5] == 'protein_coding':
#                 outS.write(line)
#                 allGFusions.append(temp[2] + '--' + temp[4])
#                 if a[1:] == 'air': airGF.append(temp[2] + '--' + temp[4])
#                 if a[1:] == 'csc': cscGF.append(temp[2] + '--' + temp[4])
#         outF.write(temp[2] + '--' + temp[4] + '\n')
#         allFusions.append(temp[2] + '--' + temp[4])
#         if a[1:] == 'air': airF.append(temp[2] + '--' + temp[4])
#         if a[1:] == 'csc': cscF.append(temp[2] + '--' + temp[4])
#     out.close()
#     outS.close()
#     outF.close()
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/allDFusions.txt", "w")
# for a in set(allFusions): out.write(a + '\n')
# out.close()
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/airDFusions.txt", "w")
# for a in set(airF): out.write(a + '\n')
# out.close()
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscDFusions.txt", "w")
# for a in set(cscF): out.write(a + '\n')
# out.close()
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/allFusions.txt", "w")
# for a in set(allGFusions): out.write(a + '\n')
# out.close()
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/airFusions.txt", "w")
# for a in set(airGF): out.write(a + '\n')
# out.close()
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscFusions.txt", "w")
# for a in set(cscGF): out.write(a + '\n')
# out.close()
# print('cscNotAir')
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscNotAirFusions.txt", 'w')
# airGF = set(airGF)
# airF = set(airF)
# for a in set(cscGF):
#     if a not in airGF:
#         out.write(a + '\n')
# out.close()
# print('cscNotAir')
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscNotAirDFusions.txt", 'w')
# for a in set(cscF):
#     if a not in airF:
#         out.write(a + '\n')
# out.close()
#
# # airF = []
# # out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscNotAirFusions.txt", 'w')
# # for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/airFusions.txt", 'r'):
# #     airF.append(line.strip())
# # airF = set(airF)
# # for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscFusions.txt", 'r'):
# #     if line.strip() not in airF:
# #         out.write(line)
# # out.close()


# allFusions, airFusions, cscFusions, allDFusions, airDFusions, cscDFusions = [], [], [], [], [], []
# out1 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allFusions-arriba.txt", 'w')
# out2 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allDFusions-arriba.txt", 'w')
# out3 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/airFusions-arriba.txt", 'w')
# out4 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/airDFusions-arriba.txt", 'w')
# out5 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscFusions-arriba.txt", 'w')
# out6 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscDFusions-arriba.txt", 'w')
# out7 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirFusions-arriba.txt", 'w')
# out8 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirDFusions-arriba.txt", 'w')
# for a in ['92', '93', '94', '95', '96', '97']:
#     for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/" + a + "-fusions.discarded.tsv"):
#         if line[0] != '#':
#             line = line.split('\t')
#             if ',' in line[0] and ',' in line[1]:
#                 temp = line[0].split(',')[0].split('(')[0] + '--' + line[0].split(',')[1].split('(')[0]
#             elif ',' in line[0]:
#                 i = [line[0].split(',')[0].split('(')[0], line[0].split(',')[1].split('(')[0]]
#                 if i[0] != line[1]: temp = i[0] + '--' + line[1]
#                 else: temp = i[1] + "--" + line[1]
#             elif ',' in line[1]:
#                 i = [line[1].split(',')[0].split('(')[0], line[1].split(',')[1].split('(')[0]]
#                 if i[0] != line[1]: temp = line[0] + '--' + i[0]
#                 else: temp = line[0] + "--" + i[1]
#             else: temp = line[0] + '--' + line[1]
#             allDFusions.append(temp)
#             if a in ['92', '93', '94']: airDFusions.append(temp)
#             else: cscDFusions.append(temp)
#     for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/" + a + "-fusions.tsv"):
#         if line[0] != '#':
#             line = line.split('\t')
#             if ',' in line[0] and ',' in line[1]:
#                 temp = line[0].split(',')[0].split('(')[0] + '--' + line[0].split(',')[1].split('(')[0]
#             elif ',' in line[0]:
#                 i = [line[0].split(',')[0].split('(')[0], line[0].split(',')[1].split('(')[0]]
#                 if i[0] != line[1]: temp = i[0] + '--' + line[1]
#                 else: temp = i[1] + "--" + line[1]
#             elif ',' in line[1]:
#                 i = [line[1].split(',')[0].split('(')[0], line[1].split(',')[1].split('(')[0]]
#                 if i[0] != line[1]: temp = line[0] + '--' + i[0]
#                 else: temp = line[0] + "--" + i[1]
#             else: temp = line[0] + '--' + line[1]
#             allFusions.append(temp)
#             allDFusions.append(temp)
#             if a in ['92', '93', '94']:
#                 airFusions.append(temp)
#                 airDFusions.append(temp)
#             else:
#                 cscFusions.append(temp)
#                 cscDFusions.append(temp)
# for a in set(allFusions): out1.write(a + '\n')
# for a in set(allDFusions): out2.write(a + '\n')
# for a in set(airFusions): out3.write(a + '\n')
# for a in set(airDFusions): out4.write(a + '\n')
# for a in set(cscFusions): out5.write(a + '\n')
# for a in set(cscDFusions): out6.write(a + '\n')
# airFusions = set(airFusions)
# airDFusions = set(airDFusions)
# for a in set(cscFusions):
#     if a not in airFusions: out7.write(a + '\n')
# for a in set(cscDFusions):
#     if a not in airDFusions: out8.write(a + '\n')

# allFusions, airFusions, cscFusions, allDFusions, airDFusions, cscDFusions = [], [], [], [], [], []
# out1 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allFusions-star.txt", 'w')
# out2 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allDFusions-star.txt", 'w')
# out3 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/airFusions-star.txt", 'w')
# out4 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/airDFusions-star.txt", 'w')
# out5 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscFusions-star.txt", 'w')
# out6 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscDFusions-star.txt", 'w')
# out7 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirFusions-star.txt", 'w')
# out8 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirDFusions-star.txt", 'w')
# for a in ['92', '93', '94', '95', '96', '97']:
#     for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/SRR63478" + a + "-star-fusion/star-fusion.fusion_predictions.tsv"):
#         if line[0] != '#':
#             line = line.split('\t')
#             allFusions.append(line[0])
#             allDFusions.append(line[0])
#             if a in ['92', '93', '94']:
#                 airFusions.append(line[0])
#                 airDFusions.append(line[0])
#             else:
#                 cscFusions.append(line[0])
#                 cscDFusions.append(line[0])
#     for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/SRR63478" + a + "-star-fusion/star-fusion.preliminary/star-fusion.fusion_candidates.preliminary"):
#         if line[0] != '#':
#             line = line.split('\t')
#             allDFusions.append(line[0])
#             if a in ['92', '93', '94']: airDFusions.append(line[0])
#             else: cscDFusions.append(line[0])
# for a in set(allFusions): out1.write(a + '\n')
# for a in set(allDFusions): out2.write(a + '\n')
# for a in set(airFusions): out3.write(a + '\n')
# for a in set(airDFusions): out4.write(a + '\n')
# for a in set(cscFusions): out5.write(a + '\n')
# for a in set(cscDFusions): out6.write(a + '\n')
# airFusions = set(airFusions)
# airDFusions = set(airDFusions)
# for a in set(cscFusions):
#     if a not in airFusions: out7.write(a + '\n')
# for a in set(cscDFusions):
#     if a not in airDFusions: out8.write(a + '\n')

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
# plt.figure(figsize=(4,4))
# venn2([set(a_all), set(s_all)], set_labels=('Arriba', 'STAR-Fusion'))
# plt.title("All Filtered Fusion Calls")
# plt.savefig("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/filteredFusionOverlap.png")
# plt.figure(figsize=(4,4))
# venn3([set(a_all_ext), set(k_all_ext), set(s_all_ext)], set_labels=('Arriba', 'Kallisto', 'STAR-Fusion'))
# plt.title("All Fusion Calls Pre-Filtering")
# plt.savefig("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/notfilteredFusionOverlap.png")
