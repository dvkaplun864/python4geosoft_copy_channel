import geosoft.gxapi as gxapi
import geosoft.gxpy as gxpy
import numpy as np

import geosoft.gxpy.utility as gxu

def rungx():
   
    ret = gxapi.GXSYS.run_gx("copych_gui.gx")
   
    if ret == -1:
        gxapi.GXSYS.cancel_()
    

    parms = gxu.get_parameters("COPYCHGUI")

    print(parms)

    inch=parms.get("IN"),
    outch=parms.get("OUT"),


    # get the current database
    
    db = gxpy.gdb.Geosoft_gdb.open()

    lines = db.list_lines()
    
    soutch=''.join(outch)
    print(soutch)
 
    db.new_channel(soutch)
    
    for l in lines:

        data, ch, fid = db.read_line(l, channels=inch)

        out=data
        db.write_channel(l, soutch, out, fid)

   
if __name__ == "__main__":
    print('Hello {}'.format(gxpy.gx.GXpy().gid))


