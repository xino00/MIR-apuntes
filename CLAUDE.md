# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Contexto

Vault de Obsidian de un residente de Medicina de Familia en Madrid. Rotaciones por todos los servicios del hospital + guardias de urgencias de puerta. Uso principal: referencia clínica durante rotaciones, protocolos de guardia y registro de casos clínicos anónimos.

## Estructura del Vault

```
10_Patologias/          Patología crónica/electiva por especialidad
  01_Cardio/            02_Neuro/  03_Infecciosas/  04_Digestivo/
  05_Neumologia/        06_Nefrologia/  07_Reumatologia/

20_farmacos/            128 fichas de fármacos (una por archivo)

30_Urgencias/           Hub central de guardia
  Patologia_Aguda/      Shock, SDRA, IRA, Dolor torácico, Disnea
  Ionico_AcidoBase/     Iones, equilibrio ácido-base
  Exploracion_Fisica/   Exploración de Rodilla, Tobillo y Antepié

40_Casos clinicos/      Casos clínicos anónimos (vacío, plantilla disponible)
50_Guardias/            Registros de guardia por fecha
60_Pase de planta/      Notas de pase (vacío, plantilla disponible)
90_MOCs/                Índices de navegación por especialidad
99_Plantillas/          Plantillas Templater
Libros y referencias/   PDFs (Manual 12 Octubre, KDIGO 2024, Sepsis 2026, etc.)
```

El **MOC - Urgencias** actúa como vista transversal: agrega las urgencias de cada especialidad (que siguen viviendo en `10_Patologias/`) más el contenido propio de `30_Urgencias/`.

## Obsidian Local REST API

El vault tiene el plugin **Local REST API** activo. Mientras Obsidian esté abierto, se puede interactuar con él:

```bash
# Leer nota activa
curl http://localhost:27123/active/ -H "Authorization: Bearer c33f71c026877f5fd8f2a0588a7b94ca8f732eb68654d81a93ebe92064241d95"

# Abrir una nota
curl -X POST "http://localhost:27123/open/ruta%2Fnota.md" -H "Authorization: Bearer c33f71c026877f5fd8f2a0588a7b94ca8f732eb68654d81a93ebe92064241d95"
```

Puerto HTTP: 27123 · Puerto HTTPS: 27124

## Sincronización con GitHub

Repo privado: `git@github.com:xino00/MIR-apuntes.git`

```bash
~/Obsidian/MIR/sync.sh   # commit + push con fecha automática
```

Cron configurado: sync automático cada día a las 22:00.

## Web pública (Quartz)

URL: **https://cuaderno-mir.netlify.app**

Cada `git push` lanza automáticamente GitHub Actions → construye Quartz → despliega en Netlify. No requiere ninguna acción manual.

Configuración en `.github/quartz.config.ts` (colores estilo Claude, locale es-ES).
El workflow está en `.github/workflows/deploy.yml`.
La homepage se genera copiando `90_MOCs/000_INICIO.md` como `index.md` antes del build.

Quartz se clona en `./quartz` (dentro del workspace del runner), no en `/tmp/quartz`, para que `actions/setup-node` pueda resolver el cache de npm con ruta relativa.

## Plantillas disponibles

| Plantilla | Uso |
|---|---|
| `TPL - Farmaco.md` | Nueva ficha de fármaco |
| `TPL - Patologia.md` | Nueva nota de patología |
| `TPL - Casos clinicos.md` | Caso clínico anónimo |
| `TPL - Guardia.md` | Registro de guardia |
| `TPL - PASE DE PLANTA.md` | Pase de planta |
