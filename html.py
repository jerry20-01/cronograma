# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:38:32 2024

@author: jreyes
"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Cronograma de Actividades PWA">
    <title>Cronograma de Actividades</title>
    <link rel="manifest" href="manifest.json">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Cronograma de Actividades</h1>

    <!-- Cargar el archivo Excel -->
    <input type="file" id="fileInput" accept=".xlsx, .xls">
    <button id="checkActivities">Verificar actividades</button>

    <!-- Área donde se mostrarán las alertas -->
    <div id="alerts"></div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.17.0/xlsx.full.min.js"></script>
    <script src="app.js"></script>

    <!-- Registrar el service worker -->
    <script>
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('sw.js').then(function() {
                console.log('Service Worker registrado con éxito');
            });
        }
    </script>
</body>
</html>
