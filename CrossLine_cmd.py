import rhinoscriptsyntax as rs
import Rhino.Geometry as geo
import scriptcontext

__commandname__ = "CrossLine"

def RunCommand( is_interactive ):
  # Get centre point and lengths of cross
  centre = rs.GetPoint("Centre of cross", 0)
  if( centre == None ):
      return 1

  lengths = rs.GetReal("Size of cross", 1.0, 0)
  if( lengths == None ):
      return 1
  
  # Define line distances around centre point
  distX = (rs.CreatePoint(-lengths/2, 0, 0), rs.CreatePoint(lengths/2, 0, 0))
  distY = (rs.CreatePoint(0, -lengths/2, 0), rs.CreatePoint(0, lengths/2, 0))
  
  
  # Create rotation transformation to keep cross in the active plane
  plane = rs.ViewCameraPlane()
  xform = rs.XformRotation1(rs.WorldXYPlane(),plane)
  
  for i in range(0,3):
      xform[i, 3] = 0
      
  # Rotate line definition
  distX = rs.LineTransform(distX, xform)
  distY = rs.LineTransform(distY, xform)
  
  # Build lines around centre and draw
  
  rs.AddLine(distX[0]+centre, distX[1]+centre)
  rs.AddLine(distY[0]+centre, distY[1]+centre)

  
  return 0