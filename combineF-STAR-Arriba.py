allFusions, airFusions, cscFusions, allDFusions, airDFusions, cscDFusions = [], [], [], [], [], []
out1 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allFusions-arriba.txt", 'w')
out2 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allDFusions-arriba.txt", 'w')
out3 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/airFusions-arriba.txt", 'w')
out4 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/airDFusions-arriba.txt", 'w')
out5 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscFusions-arriba.txt", 'w')
out6 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscDFusions-arriba.txt", 'w')
out7 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirFusions-arriba.txt", 'w')
out8 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirDFusions-arriba.txt", 'w')
for a in ['92', '93', '94', '95', '96', '97']:
    for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/" + a + "-fusions.discarded.tsv"):
        if line[0] != '#':
            line = line.split('\t')
            if ',' in line[0] and ',' in line[1]:
                temp = line[0].split(',')[0].split('(')[0] + '--' + line[0].split(',')[1].split('(')[0]
            elif ',' in line[0]:
                i = [line[0].split(',')[0].split('(')[0], line[0].split(',')[1].split('(')[0]]
                if i[0] != line[1]: temp = i[0] + '--' + line[1]
                else: temp = i[1] + "--" + line[1]
            elif ',' in line[1]:
                i = [line[1].split(',')[0].split('(')[0], line[1].split(',')[1].split('(')[0]]
                if i[0] != line[1]: temp = line[0] + '--' + i[0]
                else: temp = line[0] + "--" + i[1]
            else: temp = line[0] + '--' + line[1]
            allDFusions.append(temp)
            if a in ['92', '93', '94']: airDFusions.append(temp)
            else: cscDFusions.append(temp)
    for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/" + a + "-fusions.tsv"):
        if line[0] != '#':
            line = line.split('\t')
            if ',' in line[0] and ',' in line[1]:
                temp = line[0].split(',')[0].split('(')[0] + '--' + line[0].split(',')[1].split('(')[0]
            elif ',' in line[0]:
                i = [line[0].split(',')[0].split('(')[0], line[0].split(',')[1].split('(')[0]]
                if i[0] != line[1]: temp = i[0] + '--' + line[1]
                else: temp = i[1] + "--" + line[1]
            elif ',' in line[1]:
                i = [line[1].split(',')[0].split('(')[0], line[1].split(',')[1].split('(')[0]]
                if i[0] != line[1]: temp = line[0] + '--' + i[0]
                else: temp = line[0] + "--" + i[1]
            else: temp = line[0] + '--' + line[1]
            allFusions.append(temp)
            allDFusions.append(temp)
            if a in ['92', '93', '94']:
                airFusions.append(temp)
                airDFusions.append(temp)
            else:
                cscFusions.append(temp)
                cscDFusions.append(temp)
for a in set(allFusions): out1.write(a + '\n')
for a in set(allDFusions): out2.write(a + '\n')
for a in set(airFusions): out3.write(a + '\n')
for a in set(airDFusions): out4.write(a + '\n')
for a in set(cscFusions): out5.write(a + '\n')
for a in set(cscDFusions): out6.write(a + '\n')
airFusions = set(airFusions)
airDFusions = set(airDFusions)
for a in set(cscFusions):
    if a not in airFusions: out7.write(a + '\n')
for a in set(cscDFusions):
    if a not in airDFusions: out8.write(a + '\n')
out1.close()
out2.close()
out3.close()
out4.close()
out5.close()
out6.close()
out7.close()
out8.close()

allFusions, airFusions, cscFusions, allDFusions, airDFusions, cscDFusions = [], [], [], [], [], []
out1 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allFusions-star.txt", 'w')
out2 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/allDFusions-star.txt", 'w')
out3 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/airFusions-star.txt", 'w')
out4 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/airDFusions-star.txt", 'w')
out5 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscFusions-star.txt", 'w')
out6 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscDFusions-star.txt", 'w')
out7 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirFusions-star.txt", 'w')
out8 = open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/cscNotAirDFusions-star.txt", 'w')
for a in ['92', '93', '94', '95', '96', '97']:
    for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/SRR63478" + a + "-star-fusion/star-fusion.fusion_predictions.tsv"):
        if line[0] != '#':
            line = line.split('\t')
            allFusions.append(line[0])
            allDFusions.append(line[0])
            if a in ['92', '93', '94']:
                airFusions.append(line[0])
                airDFusions.append(line[0])
            else:
                cscFusions.append(line[0])
                cscDFusions.append(line[0])
    for line in open("/private/groups/brookslab/cafelton/rnaInfoClass/final-proj-2/SRR63478" + a + "-star-fusion/star-fusion.preliminary/star-fusion.fusion_candidates.preliminary"):
        if line[0] != '#':
            line = line.split('\t')
            allDFusions.append(line[0])
            if a in ['92', '93', '94']: airDFusions.append(line[0])
            else: cscDFusions.append(line[0])
for a in set(allFusions): out1.write(a + '\n')
for a in set(allDFusions): out2.write(a + '\n')
for a in set(airFusions): out3.write(a + '\n')
for a in set(airDFusions): out4.write(a + '\n')
for a in set(cscFusions): out5.write(a + '\n')
for a in set(cscDFusions): out6.write(a + '\n')
airFusions = set(airFusions)
airDFusions = set(airDFusions)
for a in set(cscFusions):
    if a not in airFusions: out7.write(a + '\n')
for a in set(cscDFusions):
    if a not in airDFusions: out8.write(a + '\n')