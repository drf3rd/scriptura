:: Scriptura Loader — v8.2 Arch (Unified, Lawful & Live) ::

---

## 0) Purpose
A single, authoritative **Loader** that merges the strengths of the earlier v8.x loader (lawful ordering, audit discipline) with the newer self‑updating design (live tag discovery, mode awareness, Lens integration). The Loader guarantees:

- **Ordered initialization**: Invocation → Path → Triune Witness Engine → Covenant → Closure
- **Mode awareness**: Default **Living Word**; user may switch to **Deterministic**
- **Triune witness** is **always on** (Rootseeker → Lightseeker → Rootlight)
- **Lens** is a **field**, queried by **Lightseeker** — not an engine, not a mode
- **Audit chain** and **continuity** bindings are honored when present
- **Live version discovery**: GitHub tags + `versions.json` reconciliation
- **Fail‑safe** messaging

---

## 1) Inputs & Sources
- **GitHub tags (live)**: `https://api.github.com/repos/drf3rd/scriptura/tags`
- **Version index**: `https://raw.githubusercontent.com/drf3rd/scriptura/main/versions.json`
- **Manifests**:
  - Live (default channel): `.../manifest.json`
  - Historical/alt: `.../versions/<tag>/manifest.json`

**Notes**
- If `versions.json` and the GitHub tag list disagree, the Loader **merges** them, preferring the **highest semantic version** that is **stable**.
- If `versions.json` is missing, **fallback** to the GitHub tag list.

---

## 2) Version Selection
1) Collect candidates from tags + `versions.json`.
2) Classify by **status**: stable > development > archived.
3) Default to **latest stable** (highest semver).
4) Present choices to the user; accept manual override by tag.

**Contract**
```json
{
  "selected_version": "v08.02-recombination",
  "source": "merged|tags|versions.json",
  "manifest_path": "manifest.json | versions/<tag>/manifest.json"
}
```

---

## 3) Manifest Retrieval & Validation
- Fetch the **selected** manifest.
- Validate schema keys (example for v08.02.1‑arch):
  - `version`, `repo`, `base_url`, `description`
  - `structure`: `core`, `modes`, `witness_engine`, `continuity`, `data`, `docs`
  - `governance`: `path_governs`, `mode_law`, `witness_sequence`, `covenant_binds`
  - `features`
- Ensure **governance paths** match **structure** paths.
- (Optional) Pre‑compute existence checks for referenced files; warn but do not fail unless audit requires.

---

## 4) Initialization (Lawful Ordered Sequence)
> **Order is law.** Do not parallelize. Do not eager‑load the Lens.  

```
Step 0 — Environment
  a) Create runtime context and empty state (mode := null, engines := inactive)
  b) Bind manifest metadata to context

Step 1 — Invocation (core.invocation)
  a) Load and execute ritual preamble
  b) Open motion and set run flags

Step 2 — Path (core.path)
  a) Resolve and set **Mode**
     - Default: **Living Word**
     - User may switch to **Deterministic** via Path directives or external input
  b) Authorize activation of Triune Witness Engine according to governance

Step 3 — Triune Witness Engine (witness_engine.*)
  a) Initialize **Rootseeker** (source candidate gathering)
  b) Initialize **Lightseeker** (illumination & ordering)
     - **On‑demand**: query **Lens** (data.lens) as a field for weighting
  c) Initialize **Rootlight** (synthesis & projection)
  d) Verify witness sequence aligns with governance.witness_sequence

Step 4 — Continuity (continuity.covenant)
  a) Bind continuity; record state transitions for audit

Step 5 — Closure (core.closure)
  a) Seal motion; finalize runtime state
```

**Invariant Rules**
- **Triune** is **not a mode**; it is the always‑on witness engine.
- **Lens** is not preloaded; it is read by Lightseeker when needed.
- **Mode** must be set **before** witness activation; the **Path** is authoritative.

---

## 5) Mode Semantics
- **Living Word**: dynamic recombination permitted within lawful bounds; Lens influence applied by Lightseeker.
- **Deterministic**: fixed, auditable rendering; Lens still applies for candidate ordering, but template expansion is restricted to canonical strata.

**Switching Modes**
- Allowed via Path directives or runtime instruction **before** witness activation.
- Mode change **mid‑witness** is disallowed; requires re‑invocation.

---

## 6) Lens Semantics (Field, not Engine)
- File: `data/lens_v4.0_arch.json`
- Role: **weighting/resonance field** consumed **only** by **Lightseeker**
- Scope: applies in both **Living Word** and **Deterministic** modes
- Read pattern: **on‑demand**, idempotent; no global mutable state kept by the Lens itself

**Loader Behavior**
- Do **not** preload or initialize Lens as an engine
- Provide a stable accessor for Lightseeker to query

---

## 7) Audit Chain & Continuity
If enabled by manifest (e.g., `audit_chain: true` **or** presence of `covenant/audit.yaml`):

1) Compile **expected chain** of paths (from manifest `structure` + `governance`).
2) Compute **SHA‑256** of each file and compare to declared checksums.
3) On mismatch: **fail closed** before Invocation; emit actionable diagnostics.
4) On success: continue; **Covenant** records chain artifacts and run metadata.

**Audit Output (example)**
```json
{
  "audit": {
    "enabled": true,
    "chain": [
      {"path": "rites/invocation_v_8_2.md", "sha256": "..."},
      {"path": "continuity/path_v_8_2.md", "sha256": "..."}
    ],
    "status": "verified"
  }
}
```

---

## 8) Fail‑Safe & Errors
- Network or repository error → return:
  > "Scriptura repository unavailable. Please verify connectivity or repository path."  
- Manifest schema error → return structured diagnostics and halt before Invocation.
- Missing governance alignment → error; require manifest correction.

---

## 9) Pseudocode (Reference Implementation)
```pseudo
function load_scriptura(request):
  tags    := try(fetch_github_tags()) else []
  index   := try(fetch_versions_json()) else null
  catalog := merge_catalog(tags, index)

  selected := select_version(request.preferred_tag, catalog)
  manifest := fetch_manifest(selected)
  assert validate_manifest(manifest)

  if audit_required(manifest):
    assert verify_audit_chain(manifest)

  ctx := new_context(manifest)

  // Ordered execution — no parallel loads
  invoke(load_file(manifest.structure.core.invocation), ctx)

  path_doc := load_file(manifest.structure.core.path)
  ctx.mode := resolve_mode(path_doc, default="Living Word", override=request.mode)
  ctx.engines := {rootseeker: inactive, lightseeker: inactive, rootlight: inactive}

  // Triune witness (always on)
  ctx.engines.rootseeker := init(load_file(manifest.structure.witness_engine.rootseeker), ctx)
  ctx.engines.lightseeker := init(load_file(manifest.structure.witness_engine.lightseeker), ctx,
                                  lens_accessor := () => read_json(manifest.structure.data.lens))
  ctx.engines.rootlight   := init(load_file(manifest.structure.witness_engine.rootlight), ctx)

  covenant := load_file(manifest.structure.continuity.covenant)
  bind_continuity(covenant, ctx)

  closure := load_file(manifest.structure.core.closure)
  seal(closure, ctx)

  return ctx.outcome
```

---

## 10) Minimal Compliance Checklist
- [ ] Uses GitHub tags **and** `versions.json`
- [ ] Defaults to **latest stable**
- [ ] Loads manifest and validates schema/governance
- [ ] Executes **Invocation → Path → Triune → Covenant → Closure** in order
- [ ] Mode set in **Path**, before witness activation
- [ ] **Lens queried on demand** by Lightseeker
- [ ] Optional **Audit Chain** verified when enabled
- [ ] Clear **fail‑safe** errors

---

## 11) Example Runtime Calls
- "Render Gen 1:1" → uses default **Living Word** mode, v08.02 if stable
- "Render Gen 1:1 using v08.01-law (Deterministic)" → overrides version + mode before Path

---

## 12) Changelog (Unified)
- **v8.2 Arch (Unified)**: Merge earlier lawful ordering & audit with live discovery and Lens field semantics. Clarified that **Triune is not a mode** and **Lens is always in effect**.
- **v8.x (Earlier)**: Strong audit & ordered init; no Lens, no explicit modes.
- **Self‑Updating Draft**: Added live tags and fail‑safe, but lacked ordered init; corrected here.

---

## 13) Closing Declaration
> Law orders motion. Path sets mode. Witness bears truth. Lens gives weight. Covenant remembers. Closure grants rest.  

