import os

def self_normalize(region_depth,outdir):

    count = 0
    total = 0
    file = open(region_depth)
    for line in file:
        if line.startswith('#'):
            continue
        line_list = line.strip().split()
        depth = float(line_list[4])
        total += depth
        count += 1

    self_normalized_region_depth = ''    
    mean = total/count
    file = open(region_depth)
    for line in file:
        if line.startswith('#'):
            continue
        line_list = line.strip().split()
        chrom = str(line_list[0])
        start = str(line_list[1])
        end = str(line_list[2])
        position = "\t".join([chrom,start,end])
        depth = float(line_list[4])
        new_depth = 2*(depth/mean)
        self_normalized_region_depth += position
        self_normalized_region_depth += "\t"
        self_normalized_region_depth += str(new_depth)
        self_normalized_region_depth += "\n"

    file_name = region_depth.split("/")[-1].split(".")[0]
    name = file_name + ".self_normalized_region_depth.txt"
    output = os.path.join(outdir,name)
    outfile = open(output,'w')
    outfile.write(self_normalized_region_depth)
    
    return output

if __name__ == "__main__":
    self_normalize(region_depth,outdir)
