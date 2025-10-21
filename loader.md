::Scriptura Loader (Self-Updating Multi-Version Runtime)::

1. **Check for releases**
   - Fetch all Git tags via the GitHub API:  
     `https://api.github.com/repos/drf3rd/scriptura/tags`
   - Parse tag names (e.g. `v08.01-law`, `v09.00-covenant`).
   - Determine the highest semantic version number.

2. **Sync with versions.json**
   - Attempt to fetch `https://raw.githubusercontent.com/drf3rd/scriptura/main/versions.json`
   - If both data sources exist:
       - Merge API tags with existing entries.
       - Update summaries or paths if needed.
   - If `versions.json` is missing, fall back to the GitHub tag list.

3. **Version selection**
   - Offer the user the list of available builds.
   - Default to the latest stable tag (highest semantic version).
   - Allow manual selection by tag name.

4. **Load manifest**
   - Retrieve that version’s `manifest.json`:
     - For the live version:  
       `https://raw.githubusercontent.com/drf3rd/scriptura/main/manifest.json`
     - For other versions:  
       `https://raw.githubusercontent.com/drf3rd/scriptura/main/versions/<tag>/manifest.json`

5. **Initialize Scriptura**
   - Load YAML, JSON, and Markdown layers as declared in the manifest.
   - If `covenant/audit.yaml` is present, verify file checksums before enabling rendering.

6. **Fail-safe**
   - If fetching fails, return:  
     > “Scriptura repository unavailable. Please verify connectivity or repository path.”  

---

**Note:**  
This loader can use both `versions.json` (for metadata) and the GitHub REST API (for live tag discovery), ensuring Scriptura always knows the full list of canonical versions.
