import os


def sambamba(bam,bed,outdir):

    name = bam.split("/")[-1].split(".")[0].split("_")[0]
    cmd = "mkdir -p %s" % outdir
    os.system(cmd) 
    region_depth = str(name) + ".sambamba_region_depth.txt"
    output = os.path.join(outdir,region_depth)
    cmd1 = "sambamba depth region -L %s %s -o %s" % (bed,bam,output)
    print cmd1
    os.system(cmd1)

    return output

if __name__ == "__main__":
    sambamba(bam,bed,outdir)
