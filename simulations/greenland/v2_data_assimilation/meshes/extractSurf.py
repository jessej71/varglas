from dolfin import *

"""
mesh = UnitSquareMesh(10,10)
V = FunctionSpace(mesh, "CG", 1)
u = Function(V)
u.vector()[:] = 1.5

bmesh = BoundaryMesh(mesh, "exterior")
mapping = bmesh.entity_map(1) 
part_of_boundary = CellFunction("size_t", bmesh, 0)
for cell in cells(bmesh):
  if Facet(mesh, mapping[cell.index()]).normal().x() < 0:
      part_of_boundary[cell] = 1

submesh_of_boundary = SubMesh(bmesh, part_of_boundary, 1)
Vb = FunctionSpace(submesh_of_boundary, "CG", 1)
ub = Function(V)
ub.interpolate(u)
File("ub.pvd") << ub
"""

mesh = Mesh('mesh.xml')
V    = FunctionSpace(mesh, "CG", 1)
u    = Function(V)
File('../results_sq/00/beta2_opt.xml') >> u

bmesh   = BoundaryMesh(mesh, "exterior")
mapping = bmesh.entity_map(1)
part_of_boundary = CellFunction("size_t", bmesh, 0)

for cell in cells(bmesh):
  if Facet(mesh, mapping[cell.index()]).normal().x() < -1e-3:
    part_of_boundary[cell] = 1

submesh_of_boundary = SubMesh(bmesh, part_of_boundary, 1)
Vb = FunctionSpace(submesh_of_boundary, "CG", 1)
ub = Function(V)
ub.interpolate(u)
File("ub.pvd") << ub

