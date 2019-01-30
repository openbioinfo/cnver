import glob
import os
import sys

scr_dir = os.path.dirname(os.path.realpath(__file__))
mod_dir = os.path.join(scr_dir,"../")
sys.path.insert(0,mod_dir)

from ctCNV.sambamba.sambamba import sambamba
from ctCNV.self_normalize.self_normalize import self_normalize
from ctCNV.baseline_normalize.baseline_normalize import baseline_normalize
from ctCNV.plot.plot import plot


def main(bam,bed,baseline,outdir):
    
    dp = sambamba(bam,bed,outdir)
    snrd = self_normalize(dp,outdir)
    os.remove(dp)
    bnrd = baseline_normalize(baseline,snrd,outdir)
    os.remove(snrd)
    plot(bnrd,outdir)


if __name__ == "__main__":
    from docopt import docopt
    usage = """
    Usage:
        ctCNV.py [options] -i <bam> -b <bed_file> -l <baseline> -o <outdir>
    
    Options:
        -i,--input=input_bam                              
        -b,--bed=bed_file
        -l,--line=baseline
        -o,--output=output_directory

    """
    args = docopt(usage)
    print args
    bam = args["--input"]
    bed = args["--bed"]
    baseline = args["--line"]
    outdir = args["--output"]
    main(bam,bed,baseline,outdir)
