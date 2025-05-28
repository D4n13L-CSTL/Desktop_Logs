import win32evtlog

def buscar_eventos_5145_debug():
    servidor = 'localhost'
    log_type = 'Security'
    EVENT_ID_ACCESO_COMPARTIDO = 5145

    hand = win32evtlog.OpenEventLog(servidor, log_type)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    count = 0

    while True:
        eventos_chunk = win32evtlog.ReadEventLog(hand, flags, 0)
        if not eventos_chunk:
            break
        
        for event in eventos_chunk:
            if event.EventID == EVENT_ID_ACCESO_COMPARTIDO:
                print("\n======= Evento 5145 detectado =======\n")
                print(f"Fecha: {event.TimeGenerated.Format()}\n")
                print(f"Fuente:{event.SourceName}\n")
                print(f"Mensaje completo:{event.StringInserts}\n")
                ip = event.StringInserts[5]
                if ip == '::1':
                    ip = 'LOCAL'
                else:
                    ip = event.StringInserts[5]
                print(ip)
                mascara_acceso = event.StringInserts[11] if len(event.StringInserts) > 11 else "Desconocida"
                accesos = event.StringInserts[12] if len(event.StringInserts) > 12 else "Desconocidos"
                
                print('Accesos', accesos)
                print(mascara_acceso)
                count += 1
                if count >= 10:
                    return

buscar_eventos_5145_debug()
