import Rhino.Geometry as rg


class Slicing():

    def offset_curves(self, curves, offset_value):

        pass


    def slice_mesh(self, target_mesh, layer_height, offset_value):

        polylines = []

        slice_plane_count = int(1000 / layer_height) + 1

        for i in range(slice_plane_count):
            
            ### Create Slice Plane
            plane_xy = rg.Plane.WorldXY
            plane_vec = rg.Vector3d(0, 0, i * layer_height)
            rg.Plane.Translate(plane_xy, plane_vec)
            
            ### Create Intersect Mash X Plane
            ### Return >> Polyline Array
            result_polyline = rg.Intersect.Intersection.MeshPlane(target_mesh, plane_xy)
            
            ### Check None
            if result_polyline:
                ### Array to Item
                for j in xrange(len(result_polyline)):
                    polylines.append(result_polyline[j])
            
        return polylines
    

    def spiral_slicing(self, target_mesh, layer_height):
        
        pass
        