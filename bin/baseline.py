import glob
import os
import sys

scr_dir = os.path.dirname(os.path.realpath(__file__))
mod_dir = os.path.join(scr_dir,"../")
sys.path.insert(0,mod_dir)

from ctCNV.sambamba.sambamba import sambamba
from ctCNV.self_normalize.self_normalize import self_normalize
from ctCNV.baseline.baseline import baseline
from multiprocessing import Pool


def get_self_normlized_region_depth(bam,bed,outdir):
    
    dp = sambamba(bam,bed,outdir)
    norm = self_normalize(dp,outdir)
    os.remove(dp)

    return norm


def main(indir,bed,threads,outdir):
    
    comstr = os.path.join(indir,"*.bam")
    bams = glob.glob(comstr)

    pools = Pool(threads)

    ps = []
    for bam in bams:
        p = pools.apply_async(get_self_normlized_region_depth,(bam,bed,outdir))
        ps.append(p)
    pools.close()
    pools.join()

    norms = [ p.get() for p in ps ]
    print norms
    baseline(norms,outdir)
    
    for each_norm in norms:
        os.remove(each_norm)
   
if __name__ == "__main__":
    from docopt import docopt
    usage = """
    Usage:
        baseline.py [options] -d <bam_directory> -b <bed_file> -o <outdir>
    
      Options:
        -d,--dir=input_directory             bam directory path. bams should be sorted and indexed                
        -b,--bed=bed                         bed file
        -t,--threads=threads_num             threads num [default: 4]
        -o,--output=output_directory         output directory

    """
    args = docopt(usage)
    print args
    indir = args["--dir"]
    bed = args["--bed"]
    threads = int(args["--threads"])
    outdir = args["--output"]
    main(indir,bed,threads,outdir)

