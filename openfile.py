data_seq = open('C:\Documents and Settings\winxp\Desktop\DenP-S1_1.fastq.fa','r')

def analyse(seq):
    A_count = seq.count('A')
    T_count = seq.count('T')
    C_count = seq.count('C')
    G_count = seq.count('G')
    N_count = seq.count('N')

    CG_count=C_count+G_count
    total=A_count+T_count+C_count+G_count+N_count

    print "A:",A_count, "T:",T_count, "C:",C_count, "G:",G_count, "N:",N_count
    print "%%CG =%0.2f\n" %((CG_count*1.0/total)*100)

for line in data_seq:
    if line[0]!='>':
        analyse(line)
