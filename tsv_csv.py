with open("policyinfo.tsv", "r", encoding='gb18030') as input_file:
    for line in input_file:
        with open("policyinfo.csv", "a", encoding='gb18030', errors='ignore') as output:
            line = line.replace("\t", ",")
            output.write(line)
