import sys
sys.path.insert(0,"../")

from ctCNV.baseline.baseline import baseline

self_normalized_region_depth_files = ['data/result/YH2017Lcf07050386.self_normalized_region_depth.txt', 'data/result/YH2017Lcf07050384.self_normalized_region_depth.txt']
outdir = "data/result/"

def test_baseline():

    baseline(self_normalized_region_depth_files,outdir)

if __name__ == "__main__":
    test_baseline()
