import sys
src_directory = '../../../'
sys.path.append(src_directory)

import scipy.io
import scipy.interpolate

from src.helper        import *
from src.utilities     import DataInput, DataOutput
from dolfin            import *
from pylab             import arange

set_log_active(True)

parameters['allow_extrapolation'] = True

# load a mesh :
mesh = Mesh("meshes/mesh.xml")

dbv  = DataInput('results/', ('Ubmag.mat',), mesh=mesh)

dbv.set_data_min('Ubmag', 0.0, 0.0)

U    = dbv.get_spline_expression('Ubmag')

ref_iso              = IsotropicMeshRefiner(mesh, U)
smoothing_iterations = 0
refine_ratios        = [0.5, 0.25, 0.125]#, 0.0625, 0.03125]

for ratio in refine_ratios:
  ref_iso.refine(ratio,1000.,40000.)
  ref_ani = AnisotropicMeshRefiner(ref_iso.mesh,U)
  for j in range(smoothing_iterations):
    edge_errors = ref_ani.get_edge_errors()
    new_x,new_y = ref_ani.weighted_smoothing(edge_errors,omega=0.5)
    ref_iso.mesh.coordinates()[:,0] = new_x
    ref_iso.mesh.coordinates()[:,1] = new_y

dolfin.File('./results/meshes/2dmesh.xml') << ref_iso.mesh
#write_gmsh(ref_iso.mesh,'./results/meshes/2dmesh.msh')

ref_iso.extrude(10, workspace_path="results/meshes", n_processors=16)