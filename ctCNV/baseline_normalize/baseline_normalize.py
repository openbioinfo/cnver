import os

def baseline_normalize(baseline,self_normalized_region_depth,outdir):

    ### processing baseline
    mean_dict = dict()
    sd_dict = dict()
    sd_mean_dict = dict()
    baseline = open(baseline)
    for line in baseline:
        if line.startswith("chr"):
            continue
        line = line.strip()
        line_list = line.split()
        chrom = str(line_list[0])
        start = str(line_list[1])
        end = str(line_list[2])
        mean = float(line_list[3])
        sd = float(line_list[4])
        sd_mean = float(line_list[5])
        key = "\t".join([chrom,start,end])
        mean_dict[key] = mean
        sd_dict[key] = sd
        sd_mean_dict[key] = sd_mean        

    ### normalize by baseline
    multiple = 3
    baseline_normalized_region_depth = ''
    snrd = open(self_normalized_region_depth)
    for line in snrd:
        line_list = line.strip().split()
        chrom =str(line_list[0])
        start = str(line_list[1])
        end = str(line_list[2])
        depth = float(line_list[3])
        key = "\t".join([chrom,start,end])
        new_depth = 2*(depth/mean_dict[key])
        if new_depth >= 2:
            new_depth = new_depth - (multiple * sd_mean_dict[key])
        else:
            new_depth = new_depth + (multiple * sd_mean_dict[key])

        baseline_normalized_region_depth += key
        baseline_normalized_region_depth += "\t"
        baseline_normalized_region_depth += str(new_depth)
        baseline_normalized_region_depth += "\n"

    
    cmd = "mkdir -p %s" % outdir
    os.system(cmd)
    file_name = self_normalized_region_depth.split("/")[-1].split(".")[0]
    name = file_name + ".finally_normalized_depth.txt"
    output = os.path.join(outdir,name)
    outfile = open(output,'w')
    outfile.write(baseline_normalized_region_depth)
    
    return output

if __name__ == "__main__":
    baseline_normalizenormalize(baseline,self_normalized_region_depth,outdir)
