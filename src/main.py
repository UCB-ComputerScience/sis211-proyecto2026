from sistema_taxis import SistemaTaxis
 
s = SistemaTaxis()
s.registrar_conductor("C1", "Ana")
s.registrar_conductor("C2", "Luis")
 
s.recibir_pedido(1, "Marta", "Plaza 25 de Mayo", "Terminal")
s.recibir_pedido(2, "Jorge", "Mercado", "Hospital")
s.recibir_pedido(3, "Rosa", "Universidad", "Aeropuerto")
 
print("Buscar C2:", s.buscar_conductor("C2"))
 
print("\n-- Asignaciones (sale el pedido más antiguo) --")
print(s.asignar_siguiente("C1"))
print(s.asignar_siguiente("C2"))
 
print("\n-- El operador se equivocó: deshacer la más reciente --")
pedido, conductor = s.deshacer_ultima_asignacion()
print("Revertido:", pedido, "|", conductor)
 
print("\n-- Pendientes ahora (el pedido 2 vuelve al frente) --")
for p in s.pedidos_pendientes:
    print(p)

print("\n-- V3: rutas con el grafo del mapa --")
s.registrar_calle("Plaza 25 de Mayo", "Mercado")
s.registrar_calle("Mercado", "Hospital")
s.registrar_calle("Hospital", "Plaza 25 de Mayo")  # ciclo: anillo de calles
s.registrar_calle("Plaza 25 de Mayo", "Terminal")
s.registrar_calle("Terminal", "Universidad")
s.registrar_lugar("Aeropuerto")  # todavía sin calles: no se llega

print("Ruta Plaza 25 de Mayo -> Universidad:",
      s.calcular_ruta("Plaza 25 de Mayo", "Universidad"))
print("Ruta Plaza 25 de Mayo -> Aeropuerto:",
      s.calcular_ruta("Plaza 25 de Mayo", "Aeropuerto"),
      "(sin ruta: caso límite)")
