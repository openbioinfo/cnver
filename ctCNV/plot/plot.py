import os
import matplotlib.pyplot as plt


def plot(baseline_normalized_region_depth,outdir):
    
    x = []
    y = []
    i = 1
    file = open(baseline_normalized_region_depth)
    name = baseline_normalized_region_depth.split("/")[-1].split('.')[0]
    for line in file:
        line_list = line.strip().split()
        dep = float(line_list[3])
        if dep > 4 :
            dep = 4
        x.append(i)
        y.append(dep)
        i += 1

    plt.figure(figsize=(20,10))

    plt.plot([0,3500],[2,2],linewidth = '3',color = 'black')
    plt.scatter(x,y,s=5)
    
    plt.xlim((0,i))
    plt.ylim((0,4))


    cmd = "mkdir -p %s" % outdir
    os.system(cmd)
    new_name = name + ".cnv.png"
    output = os.path.join(outdir,new_name)
    plt.savefig(output)

if __name__ == "__main__":
    plot(baseline_normalized_region_depth,outdir)
