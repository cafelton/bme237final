out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/1air_fusion-short.txt", "w")
types = []
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/1air_fusion.txt", "r"):
    line = line.split('\t')
    if line[0] != "TYPE":
        side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
        # print(side1, side2)
        types.append(side1[-2])
        types.append(side2[-2])
        out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
out.close()
print(set(types))

out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/2air_fusion-short.txt", "w")
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/2air_fusion.txt", "r"):
    line = line.split('\t')
    if line[0] != "TYPE":
        side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
        # print(side1, side2)
        out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
out.close()

out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/3air_fusion-short.txt", "w")
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/3air_fusion.txt", "r"):
    line = line.split('\t')
    if line[0] != "TYPE":
        side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
        out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
out.close()

out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/1csc_fusion-short.txt", "w")
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/1csc_fusion.txt", "r"):
    line = line.split('\t')
    if line[0] != "TYPE":
        side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
        out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
out.close()

out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/2csc_fusion-short.txt", "w")
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/2csc_fusion.txt", "r"):
    line = line.split('\t')
    if line[0] != "TYPE":
        side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
        out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
out.close()

out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/3csc_fusion-short.txt", "w")
for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/3csc_fusion.txt", "r"):
    line = line.split('\t')
    if line[0] != "TYPE":
        side1, side2 = line[-2].split(';')[0].split('|'), line[-1].split(';')[0].split('|')
        out.write("\t".join([line[0], line[-3], side1[-4], side1[-2], side2[-4], side2[-2], '\n']))
out.close()

allTypes = {'TEC', 'unitary_pseudogene', 'Mt_tRNA', 'retained_intron', 'scaRNA', 'scRNA', 'transcribed_processed_pseudogene', 'misc_RNA', 'protein_coding', 'polymorphic_pseudogene', 'processed_transcript', 'lncRNA', 'unprocessed_pseudogene', 'rRNA_pseudogene', 'snRNA', 'pseudogene', 'rRNA', 'transcribed_unprocessed_pseudogene', 'translated_processed_pseudogene', 'transcribed_unitary_pseudogene', 'processed_pseudogene', 'non_stop_decay', 'miRNA', 'snoRNA', 'Mt_rRNA', 'nonsense_mediated_decay'}
goodTypes = {'retained_intron', 'transcribed_processed_pseudogene', 'protein_coding', 'processed_transcript', 'lncRNA'}
allFusions = []
airF, cscF = [], []
allGFusions, airGF, cscGF = [], [], []
for a in ["1air", '2air', '3air', '1csc', '2csc', '3csc']:
    out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/" + a + "_fusion-filtered.txt", "w")
    outS = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/" + a + "_fusion-strenuous.txt", "w")
    outF = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/" + a + "_fusion-names.txt", "w")
    for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/" + a + "_fusion-short.txt", "r"):
        temp = line.split('\t')
        if temp[2][:3] != "MT-" and temp[4][:3] != "MT-":
            if temp[3] in goodTypes and temp[5] in goodTypes:
                out.write(line)
            if temp[3] == 'protein_coding' and temp[5] == 'protein_coding':
                outS.write(line)
                allGFusions.append(temp[2] + '--' + temp[4])
                if a[1:] == 'air': airGF.append(temp[2] + '--' + temp[4])
                if a[1:] == 'csc': cscGF.append(temp[2] + '--' + temp[4])
        outF.write(temp[2] + '--' + temp[4] + '\n')
        allFusions.append(temp[2] + '--' + temp[4])
        if a[1:] == 'air': airF.append(temp[2] + '--' + temp[4])
        if a[1:] == 'csc': cscF.append(temp[2] + '--' + temp[4])
    out.close()
    outS.close()
    outF.close()
out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/allDFusions.txt", "w")
for a in set(allFusions): out.write(a + '\n')
out.close()
out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/airDFusions.txt", "w")
for a in set(airF): out.write(a + '\n')
out.close()
out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscDFusions.txt", "w")
for a in set(cscF): out.write(a + '\n')
out.close()
out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/allFusions.txt", "w")
for a in set(allGFusions): out.write(a + '\n')
out.close()
out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/airFusions.txt", "w")
for a in set(airGF): out.write(a + '\n')
out.close()
out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscFusions.txt", "w")
for a in set(cscGF): out.write(a + '\n')
out.close()
print('cscNotAir')
out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscNotAirFusions.txt", 'w')
airGF = set(airGF)
airF = set(airF)
for a in set(cscGF):
    if a not in airGF:
        out.write(a + '\n')
out.close()
print('cscNotAir')
out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscNotAirDFusions.txt", 'w')
for a in set(cscF):
    if a not in airF:
        out.write(a + '\n')
out.close()

# airF = []
# out = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscNotAirFusions.txt", 'w')
# for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/airFusions.txt", 'r'):
#     airF.append(line.strip())
# airF = set(airF)
# for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/kallisto_fusions/cscFusions.txt", 'r'):
#     if line.strip() not in airF:
#         out.write(line)
# out.close()