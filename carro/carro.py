class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        venta = self.session.get("venta")
        if not carro:
            self.session["carro"]={}
            self.carro = self.session["carro"]
        else:
            self.carro = carro

        if not venta:
            self.session["venta"] = {}
            self.venta = self.session["venta"]
        else:
            self.venta = venta

    def agregar_observacion_cliente(self,observacion,cliente):
        self.venta[0]={
            "cliente" : cliente.id,
            "nombreCliente": cliente.nombreCliente,
            "observacion": observacion,
        }
        self.guardar_observacion_cliente()

    def guardar_observacion_cliente(self):        
        self.session["venta"]=self.venta
        self.session.modified=True

    def agregar(self,producto,cantidad):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre" : producto.nombre ,
                "precio": str(producto.precioUnitario) ,
                "cantidad" : cantidad,
                "precioAcumulado": str(producto.precioUnitario*cantidad) ,
            }
        else:
            for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+cantidad
                    value["precioAcumulado"]=str(float(producto.precioUnitario)*float(value["cantidad"]))
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    def restar_producto(self,producto):
        for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    value["precioAcumulado"]=float(value["precioAcumulado"])-producto.precioUnitario
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"].clear()
        self.session["venta"].clear()
        self.session.modified=True    

          
