import requests
import psutil


def end_point_status():

    try:
        status_render_connectivity = psutil.net_connections()
        status_cpu = psutil.cpu_times()
        status_ram = psutil.swap_memory()
    
        connectivity = str(status_render_connectivity[0][3])
        
        # mensaje 
        mensaje = f"tu estatus son ram : {status_ram}, cpu {status_cpu}, conectivity {connectivity}"

    except Exception as e:
        return {"error": e.args[0]}, 400
    else:
        if type(connectivity) == str:
            return mensaje
        else:
            return {"strig": False}, 200
