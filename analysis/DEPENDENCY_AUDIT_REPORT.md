# PedalGuy Dependency Audit Report

**Generated:** 2026-01-11
**Auditor:** Claude Code (Sonnet 4.5)
**Project Size:** 5.6MB
**Status:** ⚠️ Issues Found - Recommendations Provided

---

## Executive Summary

This audit analyzes the PedalGuy project for outdated references, security vulnerabilities, unnecessary bloat, and data inconsistencies. While this is primarily a documentation and knowledge management system (not a traditional software project with npm/pip dependencies), several issues were identified:

### Key Findings

✅ **Strengths:**
- Well-organized directory structure
- Comprehensive YAML data coverage (100%)
- Good version control practices
- Clear separation of concerns (shared/ vs projects/)

⚠️**Issues Identified:**
1. **Major:** Outdated "Swiss Things" references throughout codebase (planned replacement with Buffer++)
2. **Medium:** System files (.DS_Store) committed to repository
3. **Low:** Archived files consuming space (9 files, ~200KB)
4. **Low:** Configuration file references non-existent local paths
5. **Info:** Missing price data in some YAML files

---

## Detailed Analysis

### 1. Outdated Equipment References ⚠️ HIGH PRIORITY

**Issue:** Swiss Things references throughout codebase despite planned replacement with Empress Buffer++

**Location:** 13 files reference `swiss_things` or `swiss_things_assignment`

**Files Affected:**
```
./shared/inventory/pedals.yaml                    (13 references)
./shared/equipment_database/pedals/*.yaml         (all 12 active pedals)
./shared/equipment_database/pedals/archived/ft1y_incorrect.yaml
```

**Impact:**
- Data inconsistency between planning (Buffer++ planned) and implementation (Swiss Things referenced)
- Signal routing logic in documentation doesn't match intended hardware
- Future confusion when Buffer++ is actually purchased

**Root Cause:**
The inventory correctly shows Buffer++ as "planned" to replace Swiss Things:
```yaml
- id: "empress_buffer_plus_plus"
  status: "planned"
  upgrade_plan:
    replaces: "EarthQuaker Swiss Things"
    reason: "Swiss Things Loop 2 mono 無法利用 JC-22/Tone King stereo FX loops"
```

However, all equipment database files still use `swiss_things_assignment` fields instead of preparing for Buffer++ migration.

**Recommendation:**
```
OPTION A (Conservative - Recommended):
- Keep Swiss Things references as "legacy" until Buffer++ is actually purchased
- Add "buffer_plus_plus_assignment" field alongside existing swiss_things_assignment
- Document migration path in each file

OPTION B (Proactive):
- Replace all swiss_things_assignment with buffer_plus_plus_assignment NOW
- Add note: "assuming planned Buffer++ upgrade"
- Update pairing rules to use Buffer++ routing logic

OPTION C (Hybrid):
- Create dual-format YAML with both routing systems
- Use conditional logic based on which router is active
```

---

### 2. Unnecessary System Files ⚠️ MEDIUM PRIORITY

**Issue:** macOS system file committed to repository

**Location:**
```
./.DS_Store (6,148 bytes)
```

**Impact:**
- Increases repository size unnecessarily
- May expose local file browsing history
- Not cross-platform (macOS-specific)
- Best practice violation

**Recommendation:**
```bash
# Remove the file
rm .DS_Store

# Add to .gitignore
echo ".DS_Store" >> .gitignore
echo "**/.DS_Store" >> .gitignore

# Commit the changes
git rm --cached .DS_Store
git add .gitignore
git commit -m "chore: remove .DS_Store and add to .gitignore"
```

---

### 3. Archived File Bloat ℹ️ LOW PRIORITY

**Issue:** 9 archived files in projects directory (~200KB)

**Location:**
```
projects/2025-v3-signal-chain/archived_versions/
├── signal_chains/ (3 files)
├── research/ (1 file)
└── analysis/ (5 files)

shared/equipment_database/pedals/archived/
└── ft1y_incorrect.yaml (1 file)
```

**Impact:**
- Minimal size impact (200KB of 5.6MB = 3.5%)
- Provides historical reference value
- Already well-organized in dedicated archived_versions/ folder

**Recommendation:**
```
KEEP AS-IS: The archived files provide valuable historical context and are
already properly organized. The 200KB size is negligible for a documentation
project. These files document the evolution of the signal chain from v1.0 →
v2.0 → v3.0, which may be useful for future analysis.

ALTERNATIVE (if size becomes a concern):
- Move to separate git branch "archive/2025-v3"
- Document in README where to find archived versions
```

---

### 4. Configuration Issues ⚠️ MEDIUM PRIORITY

**Issue:** `.claude/settings.local.json` contains hardcoded local path

**Location:**
```json
"Bash(git -C /Users/emilwu/VSCode/Pedal-Research status --short)"
```

**Impact:**
- Won't work on other machines or for other users
- Path is specific to macOS user "emilwu"
- Breaks portability of the project

**Recommendation:**
```json
// Remove the hardcoded path permission
// Instead, rely on current working directory
{
  "permissions": {
    "allow": [
      "WebSearch",
      "Bash(claude-code --version)",
      "Bash(tree:*)",
      "Bash(wc:*)",
      "WebFetch(domain:empresseffects.com)",
      "WebFetch(domain:www.earthquakerdevices.com)",
      "WebFetch(domain:www.sweetwater.com)",
      "WebFetch(domain:www.roland.com)",
      "WebFetch(domain:www.toneking.com)",
      "WebFetch(domain:www.rockboard.de)",
      "WebFetch(domain:www.freethetone.com)",
      "Bash(mkdir:*)",
      "Bash(grep:*)",
      "Bash(find:*)"
      // REMOVED: "Bash(git -C /Users/emilwu/VSCode/Pedal-Research status --short)"
    ]
  }
}
```

---

### 5. Missing Data Points ℹ️ LOW PRIORITY

**Issue:** Some YAML files have null/missing price information

**Locations:**
```yaml
# shared/inventory/pedals.yaml
prs_horsemeat:
  price:
    amount: null  # 請補充價格

ff1y:
  price:
    amount: null  # 待確認
```

**Impact:**
- Incomplete financial analysis capability
- Budget analyzer skill cannot calculate accurate totals
- Stats show "不含 PRS Horsemeat 價格" as a workaround

**Recommendation:**
```
Research and add missing prices:
1. PRS Horsemeat: ~$195 USD (Reverb/Sweetwater)
2. FF-1Y FUTURE FACTORY: ~$450 USD (Free the Tone official)

Update totals in stats section:
- current_pedals: 3344 → 3989 USD (add $195 + $450)
- total_with_planned: 3643 → 4288 USD
```

---

### 6. Data Structure Inconsistencies ℹ️ LOW PRIORITY

**Issue:** Field naming inconsistency across YAML files

**Examples:**
```yaml
# Some files use:
swiss_things_assignment: "loop_1"

# Others use:
signal_chain_position: "pre_amp_gain"

# Both fields serve similar but slightly different purposes
```

**Impact:**
- Minimal - both fields serve valid purposes
- swiss_things_assignment: Router-specific routing
- signal_chain_position: Generic signal chain position
- Could be confusing for new users

**Recommendation:**
```
DOCUMENT the distinction:
- signal_chain_position: Generic position in any signal chain
- swiss_things_assignment: Specific routing for Swiss Things router
- buffer_plus_plus_assignment: Specific routing for Buffer++ router

Add to schema documentation:
```yaml
# Field definitions:
# - signal_chain_position: Where pedal typically goes in chain
#   (always_on_pre_amp, pre_amp_gain, fx_loop_or_post_gain)
# - router_assignment: Which loop/input on the signal router
#   (before_input, loop_1, loop_2, etc.)
```
```

---

## Security Analysis ✅ NO ISSUES

**Areas Checked:**
1. ✅ No hardcoded credentials or API keys
2. ✅ No exposed sensitive personal information
3. ✅ WebFetch permissions limited to legitimate music equipment domains
4. ✅ Bash permissions appropriately scoped
5. ⚠️ One local path reference (addressed in Configuration Issues section)

**Threat Assessment:** LOW
- Project is documentation-only, no executable code
- No external service integrations requiring authentication
- No user data collection or storage

---

## Performance & Size Analysis

### Current State
```
Total Size:        5.6 MB
├── projects/      612 KB (10.7%)
├── shared/        265 KB (4.6%)
├── .claude/       210 KB (3.7%)
└── .git/          ~4.5 MB (80%)

File Counts:
├── Markdown:      37 files
└── YAML:          31 files
```

### Recommendations
- ✅ Size is appropriate for a documentation project
- ✅ No bloat concerns
- ℹ️ .git directory is largest component (normal for Git repos with history)

---

## Actionable Recommendations

### Priority 1: High Priority (Do Now)

#### 1.1 Remove .DS_Store
```bash
rm .DS_Store
echo ".DS_Store" >> .gitignore
git rm --cached .DS_Store
git add .gitignore
git commit -m "chore: remove .DS_Store and add to .gitignore"
```

#### 1.2 Fix Configuration Path
Edit `.claude/settings.local.json`:
- Remove line: `"Bash(git -C /Users/emilwu/VSCode/Pedal-Research status --short)"`

### Priority 2: Medium Priority (Do Soon)

#### 2.1 Decide on Swiss Things vs Buffer++ Strategy
**Choose one approach:**

**Option A (Recommended):** Add dual routing fields
```yaml
# Add to each pedal in equipment_database/
signal_routing:
  legacy_swiss_things: "loop_1"      # Current setup
  planned_buffer_plus_plus: "loop_1" # After upgrade
  notes: "Routing remains same after Buffer++ upgrade"
```

**Option B:** Document as "planned migration"
- Add comment header to pedals.yaml: "Note: swiss_things_assignment will be replaced with buffer_plus_plus_assignment after upgrade"

#### 2.2 Add Missing Price Data
Research and add:
- PRS Horsemeat: $195 USD
- FF-1Y FUTURE FACTORY: $450 USD

### Priority 3: Low Priority (Nice to Have)

#### 3.1 Create .gitignore (if not exists)
```gitignore
# macOS
.DS_Store
**/.DS_Store

# Editor files
*.swp
*~
.vscode/
.idea/

# Backup files
*.bak
*.backup
```

#### 3.2 Document Data Schema
Create `shared/YAML_SCHEMA.md` documenting:
- Required vs optional fields
- Field naming conventions
- Distinction between routing fields

---

## Dependency Summary

### "Dependencies" in This Project Context

Since this is not a traditional software project, "dependencies" are:

1. **Data Dependencies**
   - ✅ YAML files: 31 files, 100% coverage
   - ✅ All equipment has corresponding YAML
   - ⚠️ Some missing price data

2. **Documentation Dependencies**
   - ✅ Markdown files: 37 files, well-organized
   - ✅ Clear hierarchy and structure
   - ℹ️ 9 archived files (acceptable)

3. **Configuration Dependencies**
   - ✅ Claude Code settings properly configured
   - ⚠️ One hardcoded path issue

4. **Knowledge Dependencies**
   - ✅ pairing_rules.yaml: Comprehensive rule set
   - ✅ signal_chain_fundamentals.md: Complete reference
   - ✅ 7 skills documented
   - ✅ 3 agents documented

### Outdated "Packages"
- ⚠️ Swiss Things references (pending replacement with Buffer++)
- ℹ️ Archived files (intentional, provides history)

### Security Vulnerabilities
- ✅ None found

### Unnecessary Bloat
- ⚠️ .DS_Store (6 KB) - should remove
- ℹ️ Archived files (200 KB) - acceptable

---

## Conclusion

**Overall Assessment:** GOOD ✅

The PedalGuy project is well-organized with comprehensive documentation and data coverage. The issues identified are minor and mostly relate to:

1. Planning vs implementation misalignment (Swiss Things → Buffer++)
2. System file hygiene (.DS_Store)
3. Minor configuration portability issues

**Priority Actions:**
1. Remove .DS_Store and add to .gitignore (5 minutes)
2. Fix configuration path (2 minutes)
3. Decide on Swiss Things/Buffer++ documentation strategy (15 minutes)
4. Add missing price data (10 minutes)

**Total Effort:** ~30 minutes to resolve all high and medium priority issues

**Risk Level:** LOW - All issues are cosmetic or planning-related; no functionality is broken.

---

**Report Generated:** 2026-01-11
**Next Review:** After Buffer++ purchase and installation
**Auditor:** Claude Code (Sonnet 4.5)
