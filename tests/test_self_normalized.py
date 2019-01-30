import sys
sys.path.insert(0,"../")

from ctCNV.self_normalize.self_normalize import self_normalize

region_depth = "data/result/YH2017Lcf07050386.sambamba_region_depth.txt"
outdir = "data/result/"

def test_self_normalize():

    self_normalize(region_depth,outdir)

if __name__ == "__main__":
    test_self_normalize()
