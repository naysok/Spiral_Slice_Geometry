import math

import Rhino.Geometry as rg
from scriptcontext import doc

import ghpythonlib.components as ghcp


class Utill():

    pass


class Slicing():


    def offset_curve(self, curve, offset_value):

        ### SLOW !!
        ### Offset Curve

        ### Offset Tolerance
        off_tolerance = doc.ModelAbsoluteTolerance

        ### Offset Type
        ### https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_CurveOffsetCornerStyle.htm
        off_type = 0

        ### Offset Curve
        ### Polyline >>> PolylineCurve
        new_crv = rg.Polyline.ToNurbsCurve(curve)
        # print(new_crv)
        # print(type(new_crv))

        ### Offset Vector
        vec_z = rg.Vector3d(0, 0, 1)

        ### Offset Point
        ### Move the start-point in a 90-degree vector of both plus and minus with respect to the tangent line.
        pt_start = rg.Curve.PointAt(new_crv, 0)

        vec_start = rg.Vector3d.Multiply(rg.Curve.TangentAt(new_crv, 0), 1)
        rg.Vector3d.Rotate(vec_start, math.pi * 0.5, vec_z)
        pt_a = rg.Point3d.Add(pt_start, vec_start)

        vec_start = rg.Vector3d.Multiply(rg.Curve.TangentAt(new_crv, 0), 1)
        rg.Vector3d.Rotate(vec_start, -1 * math.pi * 0.5, vec_z)
        pt_b = rg.Point3d.Add(pt_start, vec_start)
        
        ### And select the inner one via Point_in_Curve.
        tf_a = rg.Curve.Contains(new_crv, pt_a)
        tf_b = rg.Curve.Contains(new_crv, pt_a)

        if tf_a == rg.PointContainment.Inside:
            pt_base = pt_a
        
        elif tf_b == rg.PointContainment.Inside:
            pt_base = pt_b

        ### Offset
        ### Curve.Offset Method (Point3d, Vector3d, Double, Double, CurveOffsetCornerStyle)
        off_crv = new_crv.Offset(pt_base, vec_z, offset_value, off_tolerance, off_type)

        print(off_crv)

        if off_crv != None:
            return off_crv


    def offset_curves(self, curves, offset_value):

        ### SLOW !!
        ### Offset
        # offs = []
        # for i in xrange(len(curves)):
        #     tmp_crv = curves[i]
        #     offs.append(self.offset_curve(tmp_crv, offset_value))

        ### FAST !!
        ### Offset with ghpythonlib.components
        offs = self.offset_curve_ghcp(curves, (-1) * offset_value)

        return offs


    def slice_mesh(self, target_mesh, layer_height):

        polylines = []
        polylines_flatten = []

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
            if result_polyline != None:

                if len(result_polyline) == 1:
                    
                    tmp_crv = result_polyline[0]
                    # print(tmp_crv)
                    polylines.append(tmp_crv)

        return polylines
    

    def spiral_slicing(self, curves):

        pass
        