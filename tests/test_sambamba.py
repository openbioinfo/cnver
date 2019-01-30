import sys
sys.path.insert(0,"../")

from ctCNV.sambamba.sambamba import sambamba

bed = "data/104gene_best.bed"
bam = "data/YH2017Lcf07050386_3rongyu.sorted.bam"
outdir = "data/result"
def test_sambamba():

    sambamba(bam,bed,outdir)

if __name__ == "__main__":
    test_sambamba()
