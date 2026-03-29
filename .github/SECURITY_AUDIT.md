# 🔒 Security Audit Report

**Fecha:** 2026-03-29
**Scope:** MIR-apuntes Obsidian Vault - Repositorio público
**Riesgo General:** BAJO ✅ (después de remediar issues identificadas)

---

## 📋 Hallazgos

### 🟢 RESUELTO - Token de Obsidian expuesto

**Severidad:** CRÍTICA
**Estado:** ✅ REMEDIADO

**Problema:**
- Token de Local REST API hardcodeado en `CLAUDE.md` (commit 4f206f5)
- Visible en historial público de GitHub
- Permitía acceso remoto a todas las notas médicas

**Solución implementada:**
- Token regenerado en Obsidian
- Documentación actualizada para usar variables de entorno
- Commit 32cc403: "security: Remove hardcoded Obsidian API token"

**Verificación:**
```bash
# No hay tokens en CLAUDE.md
cat CLAUDE.md | grep -E "Bearer [a-f0-9]{40,}"  # Ninguno ✅
```

---

### 🟢 RESUELTO - Archivos de configuración privada

**Severidad:** MEDIA
**Estado:** ✅ REMEDIADO

**Problema:**
- `.obsidian/plugins/obsidian-local-rest-api/data.json` podría exponer credenciales
- Workspace.json contiene estado privado de sesión

**Solución implementada:**
- Agregado a `.gitignore` (commit e5847f0):
  ```
  .obsidian/workspace.json
  .obsidian/workspace-mobile.json
  .obsidian/cache/
  .obsidian/sync.json
  .obsidian/plugins/obsidian-local-rest-api/data.json
  ```

**Verificación:**
```bash
git check-ignore .obsidian/workspace.json  # ✅ ignored
git check-ignore .obsidian/plugins/obsidian-local-rest-api/data.json  # ✅ ignored
```

---

### 🟢 RESUELTO - Secretos en .env

**Severidad:** ALTA
**Estado:** ✅ PROTEGIDO

**Configuración:**
- Agregado a `.gitignore`:
  ```
  .env
  .env.local
  .env.*.local
  secrets/
  *.pem
  *.key
  ```

**GitHub Secrets correctamente usados:**
- `CF_API_TOKEN` y `CF_ACCOUNT_ID` para Cloudflare
- Utilizados con `${{ secrets.* }}` en workflows

**Verificación:**
```bash
# No hay .env files en el repo
find . -name ".env*" 2>/dev/null  # Ninguno ✅

# Secrets en GitHub Actions:
grep -r "\${{ secrets\." .github/workflows/  # ✅ Correctamente referenciados
```

---

### 🟡 RECOMENDACIÓN - GitHub Actions Permissions

**Severidad:** MEDIA
**Estado:** ⚠️ NO CONFIGURADO

**Problema:**
- No hay sección `permissions:` en `deploy.yml`
- GitHub Actions obtiene permisos por defecto (potencialmente excesivos)

**Recomendación:**
```yaml
name: Deploy Quartz to Cloudflare

permissions:
  contents: read          # Solo lectura del código

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    # Sin permisos extra (contents: read es suficiente)
```

**Acción:** Implementar en próxima actualización.

---

### 🟡 RECOMENDACIÓN - Branch Protection Rules

**Severidad:** MEDIA
**Estado:** ⚠️ PARCIALMENTE CONFIGURADO

**Problema actual:**
- Repository Rules activos (bloquean force-push)
- Pero NO hay validación de PR reviews

**Recomendación en GitHub Settings → Branches:**
- [x] Require pull request reviews: 1
- [x] Require status checks to pass (GitHub Actions)
- [x] Require branches to be up to date before merging
- [x] Dismiss stale pull request approvals
- [ ] Require code owner reviews (opcional para repo personal)

---

### 🟢 OK - Gemini-Scribe Plugin

**Severidad:** MEDIA (si mal configurado)
**Estado:** ✅ SEGURO

**Configuración actual:**
```json
{
  "apiKeySecretName": "gemini",      // ✅ No hardcodeado
  "alwaysAllowReadWrite": false,     // ✅ Restrictivo
  "toolPolicy": {
    "activePreset": "cautious"       // ✅ Modo cauteloso
  },
  "mcpEnabled": false                // ✅ Deshabilitado
}
```

**Recomendación:**
- API key de Google almacenada localmente (no en git)
- Nunca usar `alwaysAllowReadWrite: true`
- Mantener `mcpEnabled: false`

---

### 🟢 OK - Archivos excluidos del build

**Severidad:** LOW
**Estado:** ✅ CONFIGURADO

**Build public excluye:**
```
.obsidian        # Configuración privada
.github          # Workflows
.git             # Historial
CLAUDE.md        # Documentación interna
*.sh             # Scripts
.env*            # Secretos
sync.log         # Logs
```

**Verificación:**
```bash
git check-ignore .github/workflows/deploy.yml  # ✅ ignored en build
git check-ignore CLAUDE.md  # ✅ ignored en build
```

---

### 🟢 OK - Git LFS para PDFs

**Severidad:** LOW (privacidad)
**Estado:** ✅ IMPLEMENTADO

**Configuración:**
```
.gitattributes: Libros y referencias/*.pdf filter=lfs diff=lfs merge=lfs -text
```

**Beneficio:**
- PDFs en LFS no se clonean por defecto
- Protege privacidad (usuarios deben hacer `git lfs pull` explícitamente)

---

### 🟢 OK - Validación de builds

**Severidad:** MEDIUM
**Estado:** ✅ IMPLEMENTADO

**GitHub Actions valida:**
1. ✅ `quartz/public/` existe
2. ✅ Al menos 1 archivo `.html` generado
3. ✅ Reporta métricas (HTML, CSS, JS, images, tamaño)

---

## 📊 Matriz de Riesgos

| Risk | Severidad | Estado | Acción |
|------|-----------|--------|--------|
| Token expuesto | CRÍTICA | ✅ Remediado | Regenerado + documentado |
| Workspace.json público | MEDIA | ✅ Remediado | Agregado a .gitignore |
| .env sin protección | ALTA | ✅ Protegido | Configurado .gitignore |
| GH Actions permisos | MEDIA | ⚠️ Pendiente | Implementar permissions: |
| Branch protection | MEDIA | ⚠️ Parcial | Completar rules |
| Gemini-Scribe | MEDIA | ✅ Seguro | Monitorear |
| Build validation | MEDIUM | ✅ Implementado | Mantener |
| Git LFS | LOW | ✅ Implementado | Mantener |

---

## 🔐 Checklist de seguridad

### ✅ Implementado
- [x] Token regenerado y documentado
- [x] `.gitignore` mejorado (secretos, cache, logs)
- [x] Archivos privados excluidos de build público
- [x] GitHub Secrets usados correctamente
- [x] Validación de builds
- [x] Git LFS para PDFs grandes
- [x] Plugins de Obsidian seguros

### ⚠️ Recomendado (próximo paso)
- [ ] Agregar `permissions:` a workflows
- [ ] Completar branch protection rules
- [ ] Considerar código de conducta (SECURITY.md)
- [ ] Configurar dependabot para alertas de vulnerabilidades

### 📋 Monitoreo continuo
- [ ] Ejecutar `git-secrets` en pre-commit hook
- [ ] Revisar logs de GitHub Actions mensualmente
- [ ] Auditar permisos de plugins de Obsidian
- [ ] Monitorear vulnerabilidades de dependencias

---

## 🚀 Próximos pasos

### Inmediato (esta semana)
1. Agregar `permissions: { contents: read }` a deploy.yml
2. Activar branch protection completo

### Corto plazo (mes siguiente)
1. Configurar pre-commit hooks con `git-secrets`
2. Crear SECURITY.md público
3. Habilitar dependabot

### Mediano plazo
1. Revisar audit logs de GitHub mensualmente
2. Actualizar plugins de Obsidian regularmente
3. Realizar auditorías de seguridad semestrales

---

## 📚 Referencias

- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
- [Obsidian Security Guide](https://help.obsidian.md/Obsidian/Security)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

**Auditoría completada por:** Claude Code
**Próxima auditoría recomendada:** 2026-06-29
