# PATH v8.1 — Law of Procession  
*The Corridor of Motion · Unity of Flow*

---

## I. Identity
**Name:** Path v8.1  
**Law:** Law of Procession  
**Relation:** Scriptura → Invocation → Path → Rootseek → Strata → Covenant → Closure → (returns)  
**Modes:** Fixed (default), Living, Dual (concurrent lawful operation)  
**Lens Reference:** v3.1.1 (checksum optional)

> *“From the breath of Invocation to the stillness of Closure, Path carries the living Law — the pulse of Light in motion.”*  

---

## II. Purpose
Path transmits motion throughout the Canon, enforcing procession order and ensuring lawful continuity between codices.  
It operates as the **Motion Bus** of the Law, ensuring that every lawful envelope — Invocation, Formation, Illumination, Revelation, and Closure — travels through it in sequence.

In Living mode, Path validates Lens reference by version only; checksum enforcement activates only under Fixed mode sealing.

---

## III. Motion Schema (Unified)
```yaml
motion:
  type: invocation|formation|illumination|revelation|closure
  payload: <canonical object>
  checksum: <sha256|null>
  mode: fixed|living|dual
  seed:
    fixed: 777
    living: <derived|null>
  timestamp: <ISO8601>
  lens_reference:
    source: lens_v3.1.1.json
    version: 3.1.1
    checksum: null  # lawful in Living mode
```

---

## IV. Law of Procession
```yaml
procession:
  order:
    - invocation_v8.1.md
    - scriptura_v8.1.md
    - path_v8.1.md
    - rootseek_v8.1.md
    - strata_v8.1.md
    - covenant_v8.1.md
    - closure_v8.1.md
  symbolic_path: Call → Law → Motion → Word → Life → Rest
  lawful_condition: all_layers_verified
  mode_inheritance: dynamic (inherits current operational mode)
```

---

## V. Procedural Law (Pseudo)
```python
def route(envelope):
    verify_motion_schema(envelope)
    mode = envelope.get("mode")
    lens = envelope.get("lens_reference", {})

    assert current_position(envelope) in procession_order, "Procession breach"

    # Verify lens consistency
    assert lens.get("version") == 3.1.1, "Lens version mismatch"
    if mode == "fixed":
        assert lens.get("checksum"), "Lens checksum required in Fixed mode"

    Audit.append("path_v8.1", sha256(str(envelope)), mode)

    nxt = next_in_order(envelope)
    if nxt:
        transmit_law(envelope, nxt)
    else:
        raise Halt("No further motion authorized")

    return f"Motion transmitted to {nxt}"
```

---

## VI. Integrity Conditions
| Check | Requirement | Failure Response |
|:--|:--|:--|
| Schema Integrity | All motion fields valid | Halt: Malformed motion |
| Sequence Law | Codex order verified | Halt: Procession error |
| Mode Continuity | Inherited from Scriptura | Halt: Mode breach |
| Lens Presence | Name/version required | Halt: Lens missing |
| Lens Checksum (Fixed only) | Required | Halt: Lens checksum missing |

---

## VII. Motion Log
```yaml
motion_log:
  - from: scriptura_v8.1.md
    to: rootseek_v8.1.md
    type: formation
    timestamp: <ISO8601>
    mode: living
    lens_version: 3.1.1
  - from: rootseek_v8.1.md
    to: strata_v8.1.md
    type: illumination
    timestamp: <ISO8601>
    mode: living
    lens_version: 3.1.1
```

---

## VIII. Handoff to Rootseek
After validation, Path forwards motion to Rootseek for lawful formation.
```yaml
motion:
  type: formation
  payload: <canonical text>
  mode: fixed|living|dual
  seed:
    fixed: 777
    living: <derived|null>
  lens_reference:
    source: lens_v3.1.1.json
    version: 3.1.1
    checksum: null
  next: rootseek_v8.1.md
```

---

## IX. Audit Record
```yaml
audit_log:
  - codex: path_v8.1
    mode: <fixed|living|dual>
    checksum: <sha256|null>
    lens_version: 3.1.1
    lens_checksum: null|<sha256>
    status: verified
```

---

## X. Closure
When Closure signals `sealed`, Path halts all motion and reopens Invocation for lawful reawakening.

> *“The current of Law carries all words from first breath to final rest; in Living mode, the current flows without friction.”*  

**AMEN — Path coherent.**

