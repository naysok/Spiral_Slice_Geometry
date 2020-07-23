# Spiral_Slice_Geometry  


Cura 等の汎用のスライサには、花瓶モードや、スパイラルベースモードと呼ばれるスライスが実装されている。これは、入力された STL ファイルから、外周だけを取り出し、らせん状に積み上げるように 3D プリントする。形状によっては非常に有効。  

これを Grasshopper 上に、とりあえず目コピ実装する。  


### Ref  

- Special modes settings (Ultimaker Cura Support)
  [https://support.ultimaker.com/hc/en-us/articles/360012614279-Special-modes-settings](https://support.ultimaker.com/hc/en-us/articles/360012614279-Special-modes-settings)  


### RhinoCommon Memo  

- Intersection.MeshPlane Method (RhinoCommon)  
  [https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_Geometry_Intersect_Intersection_MeshPlane.htm](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_Geometry_Intersect_Intersection_MeshPlane.htm)  

- Plane.WorldXY Property (RhinoCommon)  
  [https://developer.rhino3d.com/api/RhinoCommon/html/P_Rhino_Geometry_Plane_WorldXY.htm](https://developer.rhino3d.com/api/RhinoCommon/html/P_Rhino_Geometry_Plane_WorldXY.htm)  

- Curve.Offset Method (RhinoCommon)  
  [https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_Geometry_Curve_Offset.htm](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_Geometry_Curve_Offset.htm)  