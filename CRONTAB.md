
# Configuración de Crontab

Para ejecutar el script de transformación cada 15 minutos en un servidor Linux, agrega la siguiente línea a tu crontab:

```bash
*/15 * * * * /usr/bin/python3 /ruta/al/script/transform_data.py
```
Ejemplo en mi proyecto:
```bash
*/15 * * * * /usr/bin/python3 /home/victor/Documentos/Challenge-main/challenge2/scripts/csv_process.py
```