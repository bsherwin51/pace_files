import yt
import h5py as h

yt.enable_parallelism()

ds = h.File('catalog.h5')
fns = ['/storage/home/hcoda1/0/jw254/data/RS-RP/RD%04d/RedshiftOutput%04d' % (i,i) for i in range(2,42)]

for (idx, fn) in yt.parallel_objects(enumerate(fns[::-1])):     
    data_ds = yt.load(fn)
    centers_i = []
    rvir_i = []
    for halo in ds.keys():
    fesc_list = list(ds[halo]['fesc'])
        if fesc_list[idx] >= 1e-5 and idx < len(fesc_list):
            centers_i.append(ds[halo]['center'][idx])
            rvir_i.append(ds[halo]['rvir'][idx]) 
    p = yt.ProjectionPlot(data_ds, "z", ("gas", "density"), width = data_ds.domain_width/10)
    p.annotate_title(f'RP Simulation Density Projection Over All Redshifts')
    for i in range(len(centers_i)):
        p.annotate_sphere(centers_i[i], rvir_i[i])
    p.set_cmap('density', 'viridis')
    p.set_zlim('density', 0.01, 0.05)
    p.save('RP%02d.png' % idx)