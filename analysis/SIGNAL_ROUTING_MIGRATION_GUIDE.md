# Signal Routing Migration Guide

**Created:** 2026-01-11
**Status:** ✅ Migration Complete
**Version:** 2.1

---

## Overview

This document explains the signal routing migration from the legacy Swiss Things-only system to a dual-routing system that supports both Swiss Things (current) and Empress Buffer++ (planned).

### What Changed

**Before (Version 2.0):**
```yaml
signal_chain_position: "pre_amp_gain"
swiss_things_assignment: "loop_1"
```

**After (Version 2.1):**
```yaml
signal_chain_position: "pre_amp_gain"

signal_routing:
  current_router: "swiss_things"
  legacy_swiss_things: "loop_1"
  planned_buffer_plus_plus: "loop_1"
  migration_notes: "Routing remains same (loop_1 on both routers)"
```

---

## Why This Change?

### Problem Identified
The audit revealed that while the inventory correctly shows Empress Buffer++ as "planned" to replace Swiss Things, all equipment database files still only referenced Swiss Things routing. This created:

1. **Data inconsistency** between planning and implementation
2. **Migration blindness** - no clear path from current to planned state
3. **Lost context** - future readers wouldn't understand the routing evolution

### Solution Implemented
Dual routing fields that maintain both:
- **Legacy context** - Swiss Things routing (current hardware)
- **Migration readiness** - Buffer++ routing (planned upgrade)
- **Transparency** - Clear status of which router is active

---

## Routing Mappings

### Swiss Things → Buffer++ Translation

| Swiss Things Position | Buffer++ Position | Pedal Types | Notes |
|----------------------|-------------------|-------------|-------|
| `before_input` | `before_router` | Compressors, EQ | Always-on pedals |
| `loop_1` | `loop_1` | Gain/Overdrive | Switchable gain pedals |
| `loop_2` | `loop_2` | Delay, Reverb | **STEREO UPGRADE!** |

### Key Difference: Loop 2 Stereo Capability

**Swiss Things Loop 2:** Mono only
- FF-1Y, Nucleo, AASB forced to mono mode
- Cannot utilize JC-22/Tone King stereo FX loops
- Stereo imaging lost

**Buffer++ Loop 2:** Full stereo
- FF-1Y, Nucleo, AASB can run in stereo mode
- Full utilization of amp stereo FX loops
- Preserved stereo imaging
- **This is the primary reason for the upgrade**

---

## Files Updated

### 1. Inventory File (1 file)
**Location:** `shared/inventory/pedals.yaml`

**Changes:**
- Version bumped: 2.0 → 2.1
- All 12 active pedals updated with `signal_routing` section
- Stats section updated with dual routing information
- Added `current_status: "swiss_things"` indicator

**Example:**
```yaml
- id: "empress_mkii"
  signal_routing:
    current_router: "swiss_things"
    legacy_swiss_things: "before_input"
    planned_buffer_plus_plus: "before_router"
    notes: "Always-on compressor before signal router"
```

### 2. Equipment Database (12 files)
**Location:** `shared/equipment_database/pedals/*.yaml`

**Updated Files:**
1. `cali76_fet.yaml` - Compressor (before_input → before_router)
2. `pa1qg.yaml` - EQ (before_input → before_router)
3. `sweet_honey.yaml` - Overdrive (loop_1 → loop_1)
4. `prs_horsemeat.yaml` - Overdrive (loop_1 → loop_1)
5. `morning_glory.yaml` - Overdrive (loop_1 → loop_1)
6. `roshi_blacklon.yaml` - Overdrive (loop_1 → loop_1)
7. `twa_source_code.yaml` - Overdrive (loop_1 → loop_1)
8. `odl1cs.yaml` - Overdrive (loop_1 → loop_1)
9. `ff1y.yaml` - Delay (loop_2 → loop_2, STEREO UPGRADE)
10. `nucleo.yaml` - Reverb (loop_2 → loop_2, STEREO UPGRADE)
11. `aasb.yaml` - Reverb (loop_2 → loop_2, STEREO UPGRADE)
12. `cornerstone_colosseum.yaml` - Archived (n/a, removed in V3.0)

**Example:**
```yaml
signal_chain:
  position: "fx_loop_or_post_gain"

  signal_routing:
    current_router: "swiss_things"
    legacy_swiss_things: "loop_2"
    planned_buffer_plus_plus: "loop_2"
    migration_notes: "STEREO UPGRADE: Buffer++ Loop 2 is stereo (Swiss Things Loop 2 is mono)"

  notes: "兩條訊號鏈共用，Stereo 主 Reverb"
```

---

## Current System State

### Active Router
**Swiss Things** (until Buffer++ is purchased)

### Signal Flow

```
Guitar → [Before Router] → Router → [Loop 1] → [Loop 2] → Amp
            ↓                          ↓           ↓
         Compressors              Overdrives   Delay/Reverb
         EQ                                    (mono only!)
```

**Before Router (3 pedals):**
- Empress MKII (compressor)
- Cali76 FET (compressor)
- PA-1QG (EQ)

**Loop 1 (6 pedals):**
- Sweet Honey
- PRS Horsemeat
- Morning Glory V3
- Roshi Blacklon
- TWA Source Code
- ODL-1-CS

**Loop 2 (3 pedals - mono mode):**
- FF-1Y (delay)
- Nucleo (reverb)
- AASB (reverb)

---

## Planned System State

### Planned Router
**Empress Buffer++** (status: planned purchase)

### Signal Flow

```
Guitar → [Before Router] → Buffer++ → [Loop 1] → [Loop 2] → Amp
            ↓                            ↓           ↓
         Compressors                Overdrives   Delay/Reverb
         EQ                                      (STEREO!)
```

**Before Router (3 pedals):** Same as current

**Loop 1 (6 pedals):** Same as current

**Loop 2 (3 pedals - STEREO mode!):**
- FF-1Y (delay, stereo enabled)
- Nucleo (reverb, stereo enabled)
- AASB (reverb, stereo enabled)

### Key Improvements
1. **Stereo FX Loop:** Full stereo capability for time-based effects
2. **2 Inputs:** Quick guitar switching
3. **Input Metering:** Prevents EMG active pickup clipping
4. **12 Routing Modes:** More flexible than Swiss Things
5. **30dB Boost:** Built-in boost capability
6. **Transformer Isolation (Output B):** Reduces noise

---

## Migration Checklist

### When Buffer++ is Purchased

- [ ] **Physical Setup**
  - [ ] Uninstall Swiss Things from pedalboard
  - [ ] Install Empress Buffer++
  - [ ] Rewire according to Buffer++ manual

- [ ] **Cable Upgrade (Critical for Stereo)**
  - [ ] Confirm Loop 2 pedals (FF-1Y, Nucleo, AASB) support TRS stereo
  - [ ] Acquire TRS stereo cables for Loop 2
  - [ ] Test stereo signal path

- [ ] **Pedal Configuration**
  - [ ] Configure FF-1Y for stereo input/output
  - [ ] Configure Nucleo for stereo operation
  - [ ] Configure AASB for stereo operation

- [ ] **Documentation Update**
  - [ ] Update `shared/inventory/pedals.yaml`:
    - Change `current_router: "swiss_things"` to `"buffer_plus_plus"`
    - Update stats section to reflect active router
  - [ ] Update all equipment database files if needed
  - [ ] Update any signal chain diagrams in projects/

- [ ] **Testing**
  - [ ] Test all routing modes
  - [ ] Verify stereo signal path through Loop 2
  - [ ] Test with both JC-22 and Tone King stereo FX loops
  - [ ] Verify no ground loops or noise issues

- [ ] **Swiss Things Disposition**
  - [ ] List for sale (expected: $200-250 USD used)
  - [ ] Document sale in changelog
  - [ ] Calculate net upgrade cost

---

## Field Definitions

### `signal_routing` Section

```yaml
signal_routing:
  current_router: string        # "swiss_things" | "buffer_plus_plus"
  legacy_swiss_things: string   # Swiss Things assignment
  planned_buffer_plus_plus: string  # Buffer++ assignment
  migration_notes: string       # Human-readable migration context
```

### Valid Values

**current_router:**
- `"swiss_things"` - Swiss Things is currently active
- `"buffer_plus_plus"` - Buffer++ is currently active
- `"n/a"` - Pedal not in active use

**Routing positions:**
- `"before_input"` / `"before_router"` - Before the signal router
- `"loop_1"` - Router Loop 1 (gain pedals)
- `"loop_2"` - Router Loop 2 (time-based effects)
- `"n/a"` - Not applicable

---

## Benefits of Dual Routing System

### 1. Migration Readiness
✅ Clear path from current to planned state
✅ No ambiguity about routing changes
✅ Easy to identify which pedals benefit from upgrade

### 2. Historical Context
✅ Future readers understand evolution
✅ Archived pedals maintain routing history
✅ Version control shows decision points

### 3. Upgrade Justification
✅ Stereo upgrade clearly documented
✅ Loop 2 limitations visible
✅ Buffer++ advantages explicit

### 4. Flexibility
✅ Can revert to Swiss Things if needed
✅ Can run A/B comparison
✅ Can maintain both routers temporarily

---

## Compatibility Notes

### Backward Compatibility
✅ Old tools/scripts should ignore unknown fields
✅ `position` field still exists for generic routing
✅ No breaking changes to existing integrations

### Forward Compatibility
✅ Easy to add new routers (e.g., "gigrig_g3")
✅ Routing logic can evolve without breaking data
✅ Migration notes provide context for any routing

---

## Related Documents

- **Audit Report:** `analysis/DEPENDENCY_AUDIT_REPORT.md`
- **Inventory:** `shared/inventory/pedals.yaml`
- **Equipment Database:** `shared/equipment_database/pedals/*.yaml`
- **Pairing Rules:** `.claude/knowledge/pairing_rules.yaml`

---

## Version History

### Version 2.1 (2026-01-11)
- ✅ Added dual routing system
- ✅ Updated all 12 active pedals
- ✅ Updated 1 archived pedal (Colosseum)
- ✅ Documented migration path
- ✅ Preserved historical context

### Version 2.0 (2026-01-02)
- Added Empress Buffer++ as "planned"
- Swiss Things routing only

---

**Status:** ✅ Ready for Buffer++ upgrade
**Next Action:** Purchase and install Empress Buffer++
**Estimated Net Cost:** $50-100 (after selling Swiss Things)

---

**Document Author:** Claude Code (Sonnet 4.5)
**Last Updated:** 2026-01-11
