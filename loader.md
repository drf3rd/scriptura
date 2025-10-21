:: Scriptura Loader — Multi-Version Runtime (v8.x) ::

---

## 1. Overview  
The **Scriptura Loader** is the lawful initialization sequence that activates any version of the Scriptura codex from GitHub.  
It reads `versions.json`, allows selection (or defaults to the stable version), then loads the corresponding `manifest.json`.  
All other layers — Lawgiver, Path, Rootseek, Strata, and Covenant — are initialized from the manifest paths.  

---

## 2. Version Index  
**Source:**  
```
https://raw.githubusercontent.com/drf3rd/scriptura/main/versions.json
```

This file defines:  
- `default_version` → the stable release (`v08.01-law`)  
- `available_versions` → current builds (stable and development)  
- `archived_versions` → legacy lineage (`v07.05-law`)  

The loader reads this index, then offers:  
- **[1] v08.01-law** — *Law in Motion (stable)*  
- **[2] v08.00-covenant** — *The Covenant Build (development)*  
- **[3] v07.05-law** — *Lawgiver Archive (read-only)*  

If no input is provided within a short timeout, the loader defaults to the stable version.  

---

## 3. Manifest Retrieval  
Once a version is selected, the loader performs the following:  
`FETCH versions.json → parse chosen_version.manifest → FETCH manifest.json`  

From the manifest, Scriptura loads:  

| Domain | Files | Function |
|:--|:--|:--|
| **Prompt** | `scriptura_v_8.1.md` | The Lawgiver (identity). |
| **Rites** | `invocation_v_8.1.md`, `closure_v_8.1.md` | Declare and seal motion. |
| **Continuity** | `path_v_8_1.md`, `covenant_v_8.1.md` | Govern and bind motion. |
| **Motion** | `rootseek_v_8.1.md`, `strata_v_8.1.md` | Form and reveal the Word. |
| **Layers** | `token_layer.md`, `verse_layer.md`, `range_layer.md` | Rendering strata for visible output. |
| **Docs** | `canonical_map_v_8_1.md` | Lawful schema and audit notes. |

---

## 4. Initialization Sequence  
```
1. Read versions.json
2. Select version (default: v08.01-law)
3. Load manifest.json for chosen version
4. Verify manifest structure and checksums (if audit enabled)
5. Initialize Scriptura:
   a. Invocation (open call)
   b. Path (lawful motion)
   c. Rootseek (formation)
   d. Strata (revelation)
   e. Covenant (record)
   f. Closure (rest)
6. Render Genesis 1:1 (or declared range)
```

---

## 5. Audit & Continuity  
If the manifest specifies `"audit_chain": true`,  
Scriptura verifies all declared paths under `"expected_chain"` using SHA-256 checksums.  

When complete:  
```
Covenant sealed → Audit confirmed → Continuity maintained
```

---

## 6. Extensibility  
To add a new version:  
1. Create a new folder under `/versions/` or `/archive/`  
2. Copy a manifest template into it  
3. Update `versions.json` with:  
   ```json
   "v08.02-name": {
     "path": "versions/v08.02-name/",
     "status": "development",
     "summary": "Describe the focus of the new build.",
     "manifest": "versions/v08.02-name/manifest.json"
   }
   ```  
4. Commit and push to GitHub.  

The loader will automatically detect and display the new version.  

---

## 7. Invocation Example  
To initialize Scriptura (in ChatGPT or runtime):  
```
Render Gen 1:1
```  
or explicitly:  
```
Render Gen 1:1 using v08.01-law
```

---

## 8. Lawful Summary  
>**Scriptura is Law.  
>
> **Invocation** opens the motion.  
>  
> **Path** governs it.  
>  
> **Rootseek** forms the Word.  
>  
> **Strata** reveals the Word.  
>  
> **Covenant** seals the Path.  
>  
> **Closure** recrods the motion.  

---

## 9. Closing Declaration  
> “Law breathes through motion; Covenant remembers through rest.  
> Invocation calls; Closure fulfills.  
> Thus Continuity is kept.”  
