import os
import numpy as np

def baseline(self_normalized_region_depth_files,outdir):
   
    matrix = dict()
    samples = self_normalized_region_depth_files
    for sample in samples:
        file = open(sample)
        for line in file:
            if line.startswith("#"):
                continue
            line = line.strip()
            line_list = line.split()
            chrom = str(line_list[0])
            start = str(line_list[1])
            end = str(line_list[2])
            depth = str(line_list[3])
            key = "\t".join([chrom,start,end])
            if key not in matrix:
                matrix[key] = depth
                matrix[key] += "\t"
            else:
                matrix[key] += depth
                matrix[key] += "\t"       

    baseline_file = ''
    for k in sorted(matrix):
        depth_list = []
        value = matrix[k]
        values = value.split()
        for dep in values:
            dep = float(dep)
            depth_list.append(dep)
        sd = np.std(depth_list,ddof = 1)
        mean = np.mean(depth_list)
        sd_mean = float(sd)/mean
        new_list = "\t".join([k,str(mean),str(sd),str(sd_mean)])
        baseline_file += new_list
        baseline_file += "\n"
    
    cmd = "mkdir -p %s" % outdir
    os.system(cmd)
    output = os.path.join(outdir,"baseline.txt")
    outfile = open(output,'w')
    outfile.write(baseline_file)

    return baseline_file

if __name__ == "__main__":
    baseline(self_normalized_region_depth_files,outdir)
