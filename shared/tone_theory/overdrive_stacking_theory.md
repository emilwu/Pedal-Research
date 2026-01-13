# Overdrive Stacking Theory & Pairing Strategies

**Document Type:** Tone Theory Research
**Version:** 1.0
**Created:** 2026-01-06
**Category:** Overdrive Signal Processing
**Purpose:** Understanding overdrive circuit types, stacking principles, and practical pairing strategies for building optimal gain chains

---

## Table of Contents

1. [Overdrive Circuit Families](#overdrive-circuit-families)
2. [Stacking Principles & Theory](#stacking-principles--theory)
3. [Frequency Interaction Analysis](#frequency-interaction-analysis)
4. [Gain Staging Mathematics](#gain-staging-mathematics)
5. [Two-Pedal Stacking Strategies](#two-pedal-stacking-strategies)
6. [Three-Pedal Stacking Strategies](#three-pedal-stacking-strategies)
7. [Common Mistakes & Solutions](#common-mistakes--solutions)
8. [Genre-Specific Recommendations](#genre-specific-recommendations)
9. [Signal Chain Positioning](#signal-chain-positioning)
10. [Practical Examples](#practical-examples)

---

## Overdrive Circuit Families

### Understanding Circuit Design Philosophy

Overdrive pedals fall into distinct circuit families, each with unique tonal characteristics and frequency responses. Understanding these families is crucial for effective stacking.

---

### 1. Bluesbreaker Family

**Original Circuit:** Marshall Bluesbreaker (1960s)

**Circuit Characteristics:**
- Op-amp based design (typically IC chip like JRC4558 or LM833)
- Symmetrical clipping (both positive and negative waveforms clipped equally)
- Open, transparent overdrive with minimal compression
- Frequency response: Balanced across spectrum
- No clipping diodes in some modern variants (for more volume and clarity)

**Tonal Signature:**
```
Low Freq:  Full but not excessive
Mid Freq:  Balanced, not scooped or boosted
High Freq: Open, clear, natural
Dynamic:   Very high touch sensitivity
Compression: Very low (amp-like response)
```

**Representative Pedals:**
- JHS Morning Glory V3 - Ultra-transparent Bluesbreaker
- Cornerstone Colosseum (BB side) - No clipping diodes variant
- Virtues Arca - BB-like with added grit

**Best For:**
- Jazz, Blues, Neo Soul
- Preserving guitar's natural character
- First stage in gain chain (transparent foundation)
- Stacking with colored overdrives

**Stacking Role:**
- **Primary:** Transparent boost or foundation layer
- **Stacking Position:** Usually first in chain
- **Pairs Well With:** Klon-style, TS-style, warm overdrives

---

### 2. Klon Family (Transparent Boost/OD)

**Original Circuit:** Klon Centaur (1994)

**Circuit Characteristics:**
- Dual-gang gain control (clean + distorted signal blending)
- Germanium or Silicon diodes (original used 1N34A Germanium)
- Internal 18V boost (9V input, doubled internally)
- Buffered bypass (high-quality buffer)
- Frequency response: Slight mid boost, enhanced high frequencies

**Tonal Signature:**
```
Low Freq:  Tight, controlled
Mid Freq:  Slightly enhanced (subtle, not aggressive like TS)
High Freq: Sparkle, shimmer, enhanced presence
Dynamic:   High touch sensitivity
Compression: Moderate (musical compression)
Harmonics: Rich even-order harmonics
```

**Representative Pedals:**
- EHX Soul Food - Budget Klon clone (Silicon diodes)
- PRS Horsemeat - Klon-inspired with Germanium, Voice control
- Cornerstone Colosseum (Klon side) - With Clip Blender (Ge + Si mix)

**Best For:**
- Clean boost applications
- Adding sparkle and presence
- Pushing other overdrives
- Blues, Rock, Country, Pop

**Stacking Role:**
- **Primary:** Clean boost or light overdrive
- **Stacking Position:** First or second in chain
- **Pairs Well With:** Bluesbreaker, warm overdrives

**Klon + BB Classic Combination:**
```
Klon (low gain, high volume) → Bluesbreaker (medium gain)
= Transparent mid boost → Open clear overdrive
= Classic Blues/Rock tone
```

---

### 3. Tube Screamer Family (Mid-Focused)

**Original Circuit:** Ibanez Tube Screamer TS808 (1979)

**Circuit Characteristics:**
- Op-amp based with diodes in feedback loop (asymmetrical soft clipping)
- Pronounced mid-frequency boost (720Hz-1kHz peak)
- Bass cut before gain stage
- Fixed EQ curve (signature mid hump)
- Designed to push tube amps into natural breakup

**Tonal Signature:**
```
Low Freq:  Reduced (tight, prevents flub)
Mid Freq:  Pronounced boost (800Hz-1.5kHz)
High Freq: Slightly reduced (smooth, not harsh)
Dynamic:   Good touch sensitivity
Compression: Moderate
Character: Vocal, singing, focused
```

**Representative Pedals:**
- TWA Source Code - TS Evolution with 18V, Bite control
- (Traditional TS808, TS9, Maxon OD808, etc.)

**Best For:**
- Rock, Classic Rock, Blues-Rock
- Cutting through band mix
- Tightening bass response
- Pushing tube amps

**Stacking Role:**
- **Primary:** Mid-range enhancement and definition
- **Stacking Position:** Second or third in chain (after transparent boost)
- **Pairs Well With:** Bluesbreaker (before TS), clean amps

**TS + Transparent OD Classic Combination:**
```
Transparent OD (boost) → Tube Screamer (mid focus)
= Clean foundation → Vocal, cutting tone
= Classic Rock tone (Stevie Ray Vaughan style)
```

**Critical Note:**
- TS mid-hump can clash with other mid-focused pedals
- Best paired with neutral or scooped frequency pedals
- May not suit Jazz or Neo Soul (mid hump too aggressive)

---

### 4. Dumble-Style Family (Amp-in-a-Box)

**Original Circuit:** Dumble Overdrive Special Amp (1970s-2000s)

**Circuit Characteristics:**
- Complex multi-stage gain structure
- No clipping diodes/LEDs (clean clipping from gain stages)
- Rich harmonic content even at clean settings
- Multiple voicing options (Rock/Jazz, EQ/Glass)
- High headroom design
- Voltage adjustable in some pedals (affects clipping point)

**Tonal Signature:**
```
Low Freq:  Rich, full (Jazz mode) or tight (Rock mode)
Mid Freq:  Complex, rich harmonics, three-dimensional
High Freq:  Adjustable (Glass = bright Blackface-like)
Dynamic:   Extremely high (amp-like response)
Compression: Dumble-style (musical, natural)
Harmonics: Extremely rich and complex
Character: Smooth, sophisticated, "alive"
```

**Representative Pedals:**
- Free the Tone ODL-1-CS - Dual channel, 10-19V adjustable (Custom Shop)

**Best For:**
- Fusion, Jazz, Blues (Larry Carlton, Robben Ford style)
- High-end, sophisticated tones
- When you want "amp in a pedal"
- Studio recording

**Stacking Role:**
- **Primary:** Final gain stage or standalone amp replacement
- **Stacking Position:** Usually last in gain chain
- **Pairs Well With:** Transparent boosts, Klon-style (to push Dumble into breakup)

**Transparent + Dumble Combination:**
```
Klon/BB (boost) → Dumble-style (final stage)
= Clean push → Rich harmonic saturation
= High-end Fusion tone
```

**Voltage Adjustment Strategy (ODL-1-CS):**
```
10-12V:  Earlier breakup, warmer saturation (vintage)
14V:     Standard balanced setting
16-19V:  Maximum headroom, cleaner, hi-fi (modern)
```

---

### 5. Amp-in-a-Box Family (Blackface/Tweed Simulation)

**Circuit Type:** Preamp simulation circuits

**Circuit Characteristics:**
- Simulates specific amplifier preamp circuits
- Multiple voicing switches (tube type, mode)
- Often includes EQ matching target amp
- Designed to give amp character to any rig

**Examples:**

#### Fender Blackface Simulation (Roshi Blacklon)

**Characteristics:**
- 6L6 vs 6V6 tube type selection
- Mellow vs Drive mode
- Blackface frequency response (scooped mids, extended highs/lows)

**Tonal Signature:**
```
Low Freq:  Extended, full (6L6) or warm (6V6)
Mid Freq:  Blackface characteristic (slightly scooped)
High Freq:  Clear, sparkly, separated
Dynamic:   Extremely high (amp-like)
Compression: Moderate, amp-like
Character: Clean to crunch Blackface tone
```

**Best For:**
- Neo Soul (6V6 + Mellow)
- Post Rock (6L6 + Drive)
- Adding tube amp character to solid-state amps (JC-22)
- Clean to crunch tones

**Stacking Role:**
- **Two Approaches:**
  1. **First Position:** As tone shaper (provides amp EQ foundation)
  2. **Last Position:** As final amp simulator (traditional amp-in-a-box use)

**Amp-in-a-Box Positioning:**
```
Approach 1 (Tone Shaper):
Blackface → Transparent OD → Other OD
= Amp EQ foundation → Overdrive layers

Approach 2 (Amp Simulator):
Transparent OD → Other OD → Blackface
= Gain layers → Final amp simulation
```

---

### 6. Vintage/Low-Medium Gain Family

**Philosophy:** Touch-sensitive, dynamic, warm overdrives

**Circuit Characteristics:**
- Lower gain range than modern pedals
- Emphasis on dynamic response
- Often include unique tone controls (Focus, Voice)
- Designed for "always-on" use

**Examples:**

#### Mad Professor Sweet Honey Overdrive Deluxe

**Characteristics:**
- Pre-gain Bass control (shapes low-end distortion)
- Post-gain Treble control (final tone shaping)
- Focus control (dynamic response + overall EQ)

**Tonal Signature:**
```
Low Freq:  Warm, full (adjustable pre-gain)
Mid Freq:  Warm, full, musical
High Freq:  Smooth (adjustable post-gain)
Dynamic:   Extremely high touch sensitivity
Compression: Moderate, adjustable via Focus
Harmonics: Rich even-order harmonics
Character: Warm, sweet, vintage
```

**Focus Control Effect:**
```
CCW (Counter-clockwise):
- Requires harder pick attack for breakup
- Softer, more gentle tone
- Best for: Jazz, Blues ballads

CW (Clockwise):
- Earlier breakup
- Slight high-frequency lift
- Best for: Classic Rock, driving styles
```

**Best For:**
- Jazz, Neo Soul, Post Rock, Blues
- Always-on tone foundation
- When you want warm coloration
- Pairing with transparent overdrives

**Stacking Role:**
- **Primary:** Core tone definition (warm character)
- **Stacking Position:** Second or third (after transparent boost)
- **Pairs Well With:** Transparent BB, Klon boost

---

## Stacking Principles & Theory

### Core Stacking Philosophy

Overdrive stacking is the art of combining multiple gain stages to create complex, harmonically rich tones that single pedals cannot achieve. Successful stacking requires understanding how pedals interact in terms of frequency response, gain staging, and dynamic behavior.

---

### Principle 1: Transparent + Colored Pairing

**Theory:**
Transparent overdrive preserves guitar/amp character, while colored overdrive adds specific tonal characteristics.

**Signal Flow:**
```
Transparent OD (foundation) → Colored OD (character)
```

**How It Works:**
1. **Transparent OD:**
   - Provides clean gain boost
   - Preserves guitar's natural frequency response
   - Maintains high dynamic response
   - Examples: Morning Glory, KOT Clean, Soul Food (low gain)

2. **Colored OD:**
   - Defines final tone character
   - Adds specific frequency shaping
   - Introduces harmonic coloration
   - Examples: Sweet Honey, TS-style, Dumble-style

**Frequency Interaction:**
```
Input Signal (full spectrum)
    ↓
Transparent OD (preserves spectrum, adds gain)
    ↓
Colored OD (shapes spectrum, adds character)
    ↓
Output (gain + character)
```

**Best Combinations:**
- **Morning Glory → Sweet Honey**
  - BB transparency → Warm coloration
  - Rating: 48/50

- **Soul Food → Morning Glory**
  - Klon boost → BB transparency
  - Rating: 47/50

- **KOT Clean → Sweet Honey**
  - Ultra-transparent → Warm character
  - Rating: 46/50

**Why This Works:**
- First pedal maintains instrument character
- Second pedal operates on preserved signal
- Combined effect is "your tone, but better"
- High dynamic range preserved throughout

---

### Principle 2: Low Gain + High Gain Stacking

**Theory:**
Low-gain pedal acts as boost, pushing high-gain pedal into its sweet spot.

**Signal Flow:**
```
Low Gain OD (Gain low, Volume high) → High Gain OD (Gain medium-high, Volume unity)
```

**How It Works:**

**Stage 1 - Low Gain Boost:**
```
Settings:
- Gain: 9-10 o'clock (minimal clipping)
- Volume: 1-3 o'clock (significant boost)
- Purpose: Increase signal strength without heavy distortion
```

**Stage 2 - High Gain Drive:**
```
Settings:
- Gain: 11-2 o'clock (receives boosted signal)
- Volume: 12 o'clock (unity or slight boost)
- Purpose: Provides main distortion character
```

**Gain Staging Math:**
```
Example:
- Pedal 1: +10dB boost (low gain, high volume)
- Pedal 2: +15dB gain at current input level
- Total: Pedal 2 receives 10dB hotter signal
- Result: Pedal 2 reaches optimal saturation point
```

**Best Combinations:**
- **Soul Food (boost) → ODL-1-CS (drive)**
  - Klon boost → Dumble saturation

- **Morning Glory (boost) → TWA Source Code (drive)**
  - BB boost → TS drive

- **Horsemeat (boost) → Sweet Honey (drive)**
  - Germanium boost → Warm overdrive

**Why This Works:**
- Boost pedal pushes drive pedal into "sweet spot"
- Drive pedal gets optimal input level
- More harmonic saturation without excessive gain
- Better sustain and compression control

**Critical Settings:**
```
Boost Pedal:
- Gain: Minimal (just slight edge of breakup)
- Volume: High (significant output boost)
- Tone: Neutral or slight adjustment

Drive Pedal:
- Gain: Set for desired distortion level
- Volume: Unity gain (matches bypass volume)
- Tone: Set for final tone shaping
```

---

### Principle 3: Complementary Frequency Stacking

**Theory:**
Pedals with different frequency responses combine to create fuller, more complete spectrum.

**Frequency Analysis:**

#### Frequency-Neutral Pedals
```
Morning Glory, KOT, Soul Food (mostly)
--------------------
Full spectrum preserved
```

#### Mid-Focused Pedals
```
Tube Screamer, TWA Source Code
       /\
      /  \     ← Mid boost (800Hz-1.5kHz)
_____/    \_____
```

#### Warm Pedals (Low-Mid Emphasis)
```
Sweet Honey, Horsemeat
    ___
   /   \___
  /        \___  ← Warm low-mid boost
_/            \
```

#### Bright Pedals (High Emphasis)
```
Soul Food, some Klon clones
            ___
         __/   ← High-freq sparkle
____----/
```

**Complementary Combinations:**

**Example 1: Neutral + Mid-Focused**
```
Morning Glory (neutral) → TWA Source Code (mid-focused)
= Balanced foundation → Vocal cutting tone
```

**Frequency Result:**
```
Morning Glory:  --------------------  (flat)
TWA Source:          /\               (mid boost)
Combined:       _____/\____           (enhanced mids, balanced elsewhere)
```

**Example 2: Warm + Bright**
```
Horsemeat (warm Germanium) → Soul Food (bright Klon)
= Warm low-mid foundation → Sparkly high-end
```

**Frequency Result:**
```
Horsemeat:   ___                     (warm lows)
            /   \___
Soul Food:          \___      ___    (bright highs)
                        \__--/
Combined:    ___            ___      (full spectrum)
            /   \___    __--/
```

**Example 3: Scooped + Mid-Focused**
```
Blackface amp-in-a-box (scooped) → TS-style (mid-focused)
= Scooped amp character → Fill the mid scoop
```

**Frequency Result:**
```
Blackface:   \        /             (scooped mids)
              \______/
TS-style:         /\                (mid boost)
                 /  \
Combined:    \   /\   /             (balanced spectrum)
              \_/  \_/
```

**Avoid: Similar Frequency Pedals**

**Bad Example: TWA Source Code → Virtues Arca**
```
TWA:            /\                  (mid boost)
               /  \
Virtues:        /\                  (BB mid fullness)
               /  \
Combined:       /\                  (excessive mids)
              _/  \_
= Muddy, unclear, frequency masking
```

**Bad Example: Sweet Honey → Horsemeat**
```
Sweet Honey: ___                    (warm)
            /   \___
Horsemeat:  ___                     (warm Germanium)
           /   \___
Combined:  ___                      (too warm, dark)
          /   \___
= Overly warm, lacking clarity
```

**Frequency Stacking Guidelines:**

1. **Pair Neutral with Colored:**
   - Morning Glory (neutral) + anything = usually works

2. **Pair Warm with Bright:**
   - Balance low-end warmth with high-end sparkle

3. **Pair Scooped with Mid-Focused:**
   - Blackface + TS = balanced frequency response

4. **Avoid Multiple Mid-Focused:**
   - TS + TS = excessive mid hump
   - TS + BB with thick mids = muddy

5. **Avoid Multiple Warm:**
   - Warm OD + Germanium OD = too dark
   - Unless your rig is very bright

---

### Principle 4: Same Circuit, Different Settings

**Theory:**
Two pedals of similar circuit with different settings create complex layering.

**Application: Dual Bluesbreaker**

**Example: Morning Glory → Virtues Arca**
```
Morning Glory (Layer 1):
- Gain: 10 o'clock (low)
- Volume: 1-2 o'clock (boost)
- Purpose: Transparent BB foundation

Virtues Arca (Layer 2):
- Gain: 12-1 o'clock (medium)
- Volume: 12 o'clock (unity)
- Purpose: BB with grit and character
```

**Harmonic Layering:**
```
Morning Glory: Simple harmonic structure (transparent)
Virtues Arca:  Complex harmonic structure (grit + thickness)
Combined:      Rich, layered BB tone
```

**Application: Dual Klon**

**Example: Soul Food → Horsemeat**
```
Soul Food (Layer 1):
- Drive: 9 o'clock (clean boost)
- Volume: 2 o'clock (significant boost)
- Diodes: Silicon (bright)

Horsemeat (Layer 2):
- Gain: 11-1 o'clock (medium)
- Volume: 12 o'clock (unity)
- Diodes: Germanium (warm)
- Voice: Adjust saturation character
```

**Tonal Combination:**
```
Soul Food:  Silicon clarity + Klon mid boost
Horsemeat:  Germanium warmth + saturated/glassy (Voice control)
Combined:   Bright + warm, complex Klon tone
```

**Application: Internal Dual Channel**

**Example: KOT (Dual Channel)**
```
Yellow Channel:
- Mode: Clean
- Gain: 10 o'clock
- Volume: 1 o'clock
- Purpose: Transparent boost

Red Channel:
- Mode: Overdrive
- Gain: 12 o'clock
- Volume: 12 o'clock
- Purpose: Medium overdrive
```

**Example: Cornerstone Colosseum (BB + Klon)**
```
BB Side:
- Gain: 10-11 o'clock (low)
- Clean Control: 10 o'clock (mix in clean signal)
- Purpose: Open BB foundation

Klon Side:
- Gain: 9-10 o'clock (boost)
- Clip Blender: Adjust Ge/Si mix
- Purpose: Klon push

Order Toggle: BB → Klon or Klon → BB
```

**Why This Works:**
- Same circuit family maintains tonal coherence
- Different settings create complexity without clash
- Gradual gain build-up feels natural
- Harmonic content remains musical

---

### Principle 5: Three-Layer Progressive Gain

**Theory:**
Build gain progressively across three stages for maximum complexity and control.

**Architecture:**
```
Layer 1: Transparent Boost
    ↓ (Gain: Minimal, Volume: High)
Layer 2: Core OD Character
    ↓ (Gain: Medium, Volume: Unity-Slight Boost)
Layer 3: Heavy Drive / Amp-like
    ↓ (Gain: Medium-High, Volume: Unity)
Final Output
```

**Best Practice Settings:**

**Layer 1 - Transparent Boost:**
```
Pedal Type: Klon, BB, KOT Clean
Gain:   9-10 o'clock (minimal clipping)
Volume: 1-3 o'clock (significant boost)
Tone:   Neutral or slight adjustment
Purpose: Push Layer 2 into sweet spot without adding character
```

**Layer 2 - Core OD:**
```
Pedal Type: BB, TS, Vintage OD
Gain:   11-1 o'clock (defines core tone)
Volume: 12-1 o'clock (unity or slight boost)
Tone:   Set for desired character
Purpose: Define the core overdrive character
```

**Layer 3 - Heavy Drive:**
```
Pedal Type: Dumble-style, Amp-in-a-Box, High-gain OD
Gain:   10-2 o'clock (receives two layers of push)
Volume: 12 o'clock (unity gain)
Tone:   Final tone shaping
Purpose: Final saturation and harmonic complexity
```

**Example: Soul Food → Morning Glory → ODL-1-CS**
```
Layer 1 (Soul Food):
- Drive: 9 o'clock
- Volume: 2-3 o'clock
- Treble: 11 o'clock
= Klon transparent boost

Layer 2 (Morning Glory):
- Gain: 11-12 o'clock (receives Klon boost)
- Volume: 12-1 o'clock
- Tone: 12 o'clock
- Bright Cut: OFF
= BB core OD character

Layer 3 (ODL-1-CS):
- Channel: Drive
- Voltage: 14-15V
- Drive: 11-1 o'clock (receives two layers)
- Mode: ROCK
= Dumble final saturation

Total: Klon boost → BB character → Dumble richness
Rating: 47/50
```

**Dynamic Preservation Strategy:**

**Problem:** Three layers can over-compress and kill dynamics

**Solution:**
1. At least one layer must be ultra-low compression
   - KOT Clean, Morning Glory, Soul Food (low gain)

2. Avoid three medium-compression pedals
   - Bad: Horsemeat → TWA Source Code → High-compression OD
   - Good: KOT Clean → Sweet Honey → ODL-1-CS

3. Use parallel compression if available
   - Cali76 FET DRY knob: 70-80% dry signal preserved

4. Total compression target: < 30%
   ```
   Layer 1: 5-10% compression
   Layer 2: 10-15% compression
   Layer 3: 10-15% compression
   Total:   25-40% (aim for < 30%)
   ```

**Usage Modes:**

Three-layer system provides multiple gain levels:

```
Mode 1: Clean/Edge Breakup
- Only Layer 1 active
- Transparent boost, minimal distortion

Mode 2: Medium OD
- Layer 1 + Layer 2 active
- Core overdrive tone

Mode 3: Heavy Drive
- All three layers active
- Maximum saturation and complexity
```

**Avoid Common Mistakes:**

**Mistake 1: All pedals set to medium-high gain**
```
❌ Bad:
Layer 1: Gain 2 o'clock
Layer 2: Gain 2 o'clock
Layer 3: Gain 2 o'clock
= Total gain excessive, muddy, over-compressed
```

**Correct:**
```
✅ Good:
Layer 1: Gain 9-10 o'clock
Layer 2: Gain 11-1 o'clock
Layer 3: Gain 12-2 o'clock
= Progressive gain, clear, dynamic
```

**Mistake 2: All similar frequency response**
```
❌ Bad:
Layer 1: TS-style (mid boost)
Layer 2: TS-style (mid boost)
Layer 3: Mid-focused OD
= Excessive mid hump, frequency masking
```

**Correct:**
```
✅ Good:
Layer 1: Neutral (Morning Glory)
Layer 2: Mid-focused (TWA Source Code)
Layer 3: Amp-like (ODL-1-CS)
= Balanced frequency spectrum
```

---

## Frequency Interaction Analysis

### Frequency Masking & Enhancement

When stacking overdrives, frequency interaction is critical. Pedals can either complement each other (enhancement) or conflict (masking).

---

### Frequency Masking (Avoid)

**What is Frequency Masking:**
When two pedals boost the same frequency range excessively, creating muddy, unclear tone.

**Example 1: Double Mid-Hump**
```
TS-style Pedal 1:       /\        (800Hz-1.5kHz boost)
                       /  \
TS-style Pedal 2:       /\        (800Hz-1.5kHz boost)
                       /  \
Combined Result:        /\        (excessive mid boost)
                    ___/  \___
                   /        \
= Muddy, honky, lacks clarity
```

**Example 2: Double Warmth**
```
Warm OD (Sweet Honey): ___       (low-mid emphasis)
                      /   \___
Germanium Klon:       ___        (warm low-mid)
                     /   \___
Combined:            ___         (too warm, dark)
                    /   \___
= Overly warm, lacking high-end clarity, dull
```

**Frequency Masking Pairs to Avoid:**
```
❌ TWA Source Code → Virtues Arca
   (TS mid boost → BB thick mids = excessive mids)

❌ Sweet Honey → Horsemeat
   (Warm OD → Warm Germanium = too warm)

❌ Multiple Tube Screamers in series
   (Mid hump x2 or x3 = honky, unnatural)
```

---

### Frequency Enhancement (Ideal)

**What is Frequency Enhancement:**
Pedals with complementary frequency responses fill different parts of spectrum, creating fuller tone.

**Example 1: Neutral + Mid-Focused**
```
Morning Glory (neutral):  ----------------  (flat response)

TWA Source Code (TS):          /\          (mid boost)
                              /  \

Combined Enhancement:     _____/\____      (enhanced mids, balanced)
= Clear lows/highs, punchy mids, vocal quality
```

**Example 2: Warm + Bright**
```
Horsemeat (warm):        ___              (warm low-mid)
                        /   \___

Soul Food (bright):              \___  ___  (sparkly highs)
                                     --

Combined Enhancement:    ___         ___    (full spectrum)
                        /   \___  __-
= Warm foundation + sparkly presence = balanced, full tone
```

**Example 3: Scooped + Mid-Filled**
```
Blackface Amp-in-a-Box: \        /         (scooped mids)
                         \______/

TS-style OD:                /\             (mid boost)
                           /  \

Combined Enhancement:    \ /\ /            (balanced response)
                         \/  \/
= Blackface clarity + TS vocal character = balanced, present
```

**Ideal Frequency Pairing Matrix:**

| First Pedal | Pairs Well With | Frequency Interaction |
|-------------|----------------|---------------------|
| **Neutral** (Morning Glory, KOT) | Almost anything | No frequency conflict |
| **Mid-Focused** (TS-style) | Neutral, Scooped | Fill spectrum |
| **Warm** (Sweet Honey, Horsemeat) | Bright (Soul Food) | Balance warmth + sparkle |
| **Bright** (Soul Food, some Klons) | Warm, Neutral | Add presence without harshness |
| **Scooped** (Blackface amp-in-a-box) | Mid-focused (TS) | Fill mid scoop |

---

### EQ Interaction with Tone Controls

**Tone Control Interaction:**

**Pre-Gain EQ (Sweet Honey Bass control):**
```
Input → [Pre-Gain EQ] → [Gain Stage] → [Post-Gain EQ] → Output
         (shapes what gets distorted)
```

**Effect:**
- Pre-gain Bass boost = More low-end distortion
- Pre-gain Bass cut = Tighter, less flubby distortion

**Post-Gain EQ (Sweet Honey Treble control):**
```
Input → [Gain Stage] → [Post-Gain EQ] → Output
                       (shapes final tone)
```

**Effect:**
- Post-gain Treble boost = Brighter final tone (without changing distortion character)
- Post-gain Treble cut = Warmer final tone

**Stacking with Different EQ Positions:**

**Example: Morning Glory → Sweet Honey**
```
Morning Glory:
- Tone control: Post-clipping (final tone shaping)
- Setting: 12 o'clock (neutral)

Sweet Honey:
- Bass control: Pre-gain (shapes low-end distortion)
- Treble control: Post-gain (final brightness)
- Bass: 11 o'clock (slight cut, avoid flub)
- Treble: 1 o'clock (add sparkle)

Result: Morning Glory passes balanced signal → Sweet Honey controls low-end distortion character + final brightness
```

**Advanced EQ Stacking:**

**Example: Using PA-1QG EQ Before Overdrive**
```
PA-1QG (10-band EQ) → Morning Glory → Sweet Honey
   ↓                      ↓               ↓
Shape input         Add transparent    Add warmth
frequency          OD character       & final saturation
```

**PA-1QG Settings for Different Guitars:**
```
Preset 1 (Tele with Wide Range Pickups):
- Slight boost: 800Hz-3.2kHz (add mid presence)
- Purpose: Make bright Tele cut through mix

Preset 2 (Humbucker guitar):
- Slight cut: 200-400Hz (reduce mud)
- Boost: 3.5kHz-7kHz (add clarity)
- Purpose: Prevent humbucker from sounding too thick

→ Both presets feed into same overdrive chain
→ Result: Consistent tone across different guitars
```

---

## Gain Staging Mathematics

### Understanding Gain Accumulation

When stacking overdrives, total gain is multiplicative, not additive. Understanding gain math helps prevent over-saturation and maintain clarity.

---

### Decibel (dB) Math Review

**Gain in dB:**
```
Gain (dB) = 20 × log10(Vout / Vin)

Example:
If Vout = 2 × Vin (doubling voltage)
Gain = 20 × log10(2) = 20 × 0.301 = 6.02 dB ≈ +6dB
```

**Rule of Thumb:**
- +6dB = Double the voltage
- +12dB = Quadruple the voltage
- +20dB = 10× the voltage

**Stacking Gain (dB is additive):**
```
Total Gain (dB) = Pedal 1 Gain + Pedal 2 Gain + ... + Pedal N Gain

Example:
Pedal 1: +6dB
Pedal 2: +12dB
Total:   +18dB
```

---

### Gain Staging Examples

**Example 1: Low Gain + Medium Gain**
```
Soul Food (boost mode):
- Gain: Low
- Output Gain: +10dB

Morning Glory:
- Gain: Medium
- At standard input: +8dB
- At boosted input (+10dB): +12dB (pushed into higher gain region)

Total: +10dB (boost) + +12dB (OD) = +22dB total gain
```

**Example 2: Three-Layer Stacking**
```
Soul Food (boost):
- Gain: Minimal
- Output: +8dB

Morning Glory (medium OD):
- Receives +8dB hotter signal
- Output: +10dB (at this input level)

ODL-1-CS (final drive):
- Receives +18dB hotter signal (Soul Food + Morning Glory)
- Output: +15dB (at this input level)

Total: +8dB + +10dB + +15dB = +33dB total gain
```

**Voltage Relationship:**
```
+33dB = 20 × log10(V) → V = 10^(33/20) ≈ 44.7×
The final output is about 45 times the input voltage!
```

---

### Compression & Dynamic Range Loss

**Problem:** As gain increases, dynamic range decreases (compression).

**Dynamic Range Calculation:**
```
Input Dynamic Range: 60dB (typical guitar signal)
After Compression: Depends on compressor ratio

Example with 4:1 compression:
- Input increases by 40dB (quiet to loud playing)
- Output increases by 10dB (40dB / 4)
- Dynamic range reduced to 10dB
```

**Stacking Compression Effects:**

**Each pedal adds compression:**
```
Input:    60dB dynamic range
  ↓
Pedal 1: 5% compression → 57dB dynamic range
  ↓
Pedal 2: 10% compression → 51.3dB dynamic range
  ↓
Pedal 3: 15% compression → 43.6dB dynamic range

Total compression: ~27% (60dB → 43.6dB)
```

**Target:** Keep total compression < 30% for dynamic playing

**Maintaining Dynamics:**

**Strategy 1: Use Low-Compression Pedals**
```
✅ Good:
Morning Glory (compression: very low, ~5%)
→ Sweet Honey (compression: moderate, ~10%)
→ Total: ~15% compression ← Still dynamic!
```

**Strategy 2: Avoid Multiple Moderate-Compression Pedals**
```
❌ Bad:
Horsemeat (compression: moderate, ~15%)
→ TWA Source Code (compression: moderate, ~10%)
→ High-compression OD (compression: ~20%)
→ Total: ~40% compression ← Over-compressed, lifeless
```

**Strategy 3: Parallel Compression**
```
Using Cali76 FET with DRY knob at 70%:

Compressed signal: Heavy compression (30%)
Dry signal: 0% compression

Mix (70% dry + 30% compressed):
Effective compression: ~9%

Result: Sustain + punch maintained!
```

---

### Optimal Gain Distribution

**For Two-Pedal Stack:**
```
Optimal Distribution:
Pedal 1: +6 to +10dB (boost/light OD)
Pedal 2: +8 to +15dB (main OD)
Total:   +14 to +25dB (sweet spot for most applications)
```

**For Three-Pedal Stack:**
```
Optimal Distribution:
Pedal 1: +6 to +8dB (transparent boost)
Pedal 2: +6 to +10dB (core OD)
Pedal 3: +10 to +15dB (final drive)
Total:   +22 to +33dB (high-gain applications)
```

**Avoid: Excessive Total Gain**
```
❌ Bad (all pedals set high):
Pedal 1: +15dB
Pedal 2: +18dB
Pedal 3: +20dB
Total:   +53dB (10^(53/20) ≈ 446× voltage!)

Result: Extreme saturation, loss of note definition, muddy
```

---

### Headroom Considerations

**What is Headroom:**
Headroom is the "space" between the normal operating level and the maximum level before clipping.

**High Headroom Benefits:**
- More dynamic range
- Cleaner tone at lower gain settings
- Better transient response

**Internal Voltage Boost:**

**Standard 9V Operation:**
```
Maximum peak-to-peak voltage: ~9V
Headroom: Moderate
```

**18V Internal Boost:**
```
Examples: TWA Source Code, KOT (optional 18V), Colosseum
Maximum peak-to-peak voltage: ~18V
Headroom: Double (additional 6dB)

Benefit:
- Cleaner boost tones
- More "air" in the tone
- Better bass response (doesn't clip early)
```

**Variable Voltage (ODL-1-CS Custom Shop):**
```
10V:   Lower headroom, earlier clipping, warmer saturation
14.5V: Standard balanced setting
19V:   Maximum headroom, ultra-clean, hi-fi character

Use case:
- Low voltage (10-12V): Vintage warm overdrive
- High voltage (16-19V): Transparent boost, Fusion tones
```

---

## Two-Pedal Stacking Strategies

### Strategy 1: Transparent Foundation + Warm Character

**Goal:** Preserve guitar's natural voice while adding warmth and sustain.

**Best Combinations:**

#### Morning Glory → Sweet Honey ⭐ Rating: 48/50

**Theory:**
- Morning Glory: Ultra-transparent BB (preserves guitar character)
- Sweet Honey: Warm vintage OD (adds sweet, musical coloration)
- Frequency: Complementary (neutral + warm)
- Dynamic: Both extremely touch-sensitive

**Settings:**
```
Morning Glory:
- Gain: 10-11 o'clock (low gain boost)
- Volume: 1-2 o'clock (push Sweet Honey)
- Tone: 12 o'clock (neutral)
- Bright Cut: OFF (for humbuckers) or ON (for single-coils)

Sweet Honey:
- Drive: 11-1 o'clock (receives Morning Glory boost)
- Focus: 1-2 o'clock (Neo Soul sweet spot)
- Volume: 12-1 o'clock (unity or slight boost)
- Bass: 12 o'clock (balanced)
- Treble: 12-1 o'clock (slight sparkle)
```

**Frequency Interaction:**
```
Morning Glory:  ------------------ (neutral, full spectrum preserved)
Sweet Honey:    ___                (warm low-mid emphasis)
               /   \___
Combined:      ___                 (warm but balanced)
              /   \----------
```

**Best For:**
- **Neo Soul:** Warm, sweet rhythm tones
- **Jazz:** Transparent with warmth
- **Post Rock:** Dynamic, warm sustain
- **Blues:** Open, musical overdrive

**Usage Modes:**
```
Mode 1: Morning Glory only
  = Transparent edge-of-breakup

Mode 2: Both active
  = Warm, sweet Neo Soul overdrive

Mode 3: Sweet Honey only
  = Warm core OD without boost
```

---

#### KOT Clean → Sweet Honey ⭐ Rating: 46/50

**Theory:**
- KOT Clean: Ultra-transparent, amp-like response (lowest compression)
- Sweet Honey: Warm character definition
- Dynamic: Both maintain exceptional touch sensitivity

**Settings:**
```
KOT Yellow Channel:
- Mode: Clean (via internal DIP switch)
- Gain: 9-10 o'clock (minimal clipping)
- Volume: 1-2 o'clock (clean boost)
- Tone: 12 o'clock

Sweet Honey:
- Drive: 11-1 o'clock
- Focus: 1-2 o'clock
- Volume: 12 o'clock
- Bass/Treble: 12 o'clock
```

**Why This Works:**
- KOT Clean is among the most transparent boosts available
- Zero coloration from KOT allows Sweet Honey's character to shine
- Combined result: "Your guitar tone, but warmer and with more sustain"
- Extremely amp-like response (guitar volume knob cleaning works perfectly)

**Best For:**
- **Jazz:** Ultra-transparent with subtle warmth
- **Neo Soul:** Clean foundation with sweet saturation
- **Blues:** Amp-like breakup feel
- **Post Rock:** Dynamic ambient swells

---

### Strategy 2: Klon Boost + Bluesbreaker

**Goal:** Classic gain-stacking combination - Klon mid-push into BB openness.

**Best Combinations:**

#### Soul Food → Morning Glory ⭐ Rating: 47/50

**Theory:**
- Soul Food: Klon-style transparent boost with slight mid lift
- Morning Glory: Ultra-transparent BB
- Classic combination validated by countless players

**Settings:**
```
Soul Food:
- Drive: 9-10 o'clock (clean boost mode)
- Volume: 2-3 o'clock (significant boost)
- Treble: 11-12 o'clock (avoid excessive brightness)

Morning Glory:
- Gain: 11-1 o'clock (receives Klon boost)
- Volume: 12 o'clock (unity gain)
- Tone: 12 o'clock
- Bright Cut: Adjust for guitar (OFF for humbuckers)
```

**Frequency Interaction:**
```
Soul Food:          /\__        (mid boost + high sparkle)
                   /    \___

Morning Glory:  ----------------  (neutral, preserves Soul Food character)

Combined:          /\__          (Klon character + BB openness)
                  /    \___------
```

**Why This Works:**
- Soul Food provides Klon's signature mid lift and sparkle
- Morning Glory preserves this character while adding BB openness
- Very low combined compression (both are low-compression pedals)
- Extremely versatile across genres

**Best For:**
- **Blues:** Classic Klon → BB combination
- **Classic Rock:** Mid punch for cutting through mix
- **Jazz:** Transparent with presence
- **Neo Soul:** Clean-to-OD versatility
- **Country:** Twangy, clear tones

**Usage Modes:**
```
Mode 1: Soul Food only
  = Klon-style clean boost with sparkle

Mode 2: Both active
  = Classic Blues/Rock overdrive

Mode 3: Morning Glory only
  = Pure BB transparency
```

---

### Strategy 3: Warm Germanium + Vintage OD

**Goal:** Double-warm combination for ultra-smooth, tube-like tones.

**Best Combinations:**

#### Horsemeat → Sweet Honey ⭐ Rating: 47/50

**Theory:**
- Horsemeat: Germanium Klon-inspired with Voice control
- Sweet Honey: Warm vintage OD
- Double-warm approach (only works if amp/guitar has brightness)

**Settings:**
```
Horsemeat:
- Gain: 9-10 o'clock (low gain boost)
- Volume: 2 o'clock (push Sweet Honey)
- Voice: 11-12 o'clock (adjust saturation character)
- Treble: 1-2 o'clock (compensate warmth)
- Bass: 11 o'clock (avoid excessive low-end)

Sweet Honey:
- Drive: 12-1 o'clock (receives Germanium boost)
- Focus: 1-2 o'clock
- Volume: 12 o'clock
- Bass: 11 o'clock (prevent mud)
- Treble: 1-2 o'clock (add sparkle)
```

**Frequency Interaction:**
```
Horsemeat:       ___             (warm Germanium low-mid)
                /   \___

Sweet Honey:    ___              (warm vintage OD)
               /   \___

Combined:       ___              (double warmth)
               /   \___

CRITICAL: Treble controls at 1-2 o'clock compensate
```

**Why This Works:**
- Germanium + vintage OD = tube-like warmth
- Voice control adds saturation versatility (saturated to glassy)
- Extremely smooth, musical compression
- Rich even-order harmonics from both pedals

**Best For:**
- **Neo Soul:** Ultra-warm smooth tones
- **Jazz:** Warm, round lead tones
- **Blues:** Smooth, singing sustain

**Caution:**
- May be too warm for dark amps or humbuckers into high-gain amps
- Requires bright guitar or amp to balance warmth
- Set Treble controls higher than usual (1-2 o'clock)

**Best Rig for This Combination:**
```
✅ Good:
- Bright guitar (Tele, Strat, P-90) + JC-22 (bright amp)
- Bridge pickup emphasis
- Treble controls at 1-2 o'clock

❌ Too Dark:
- Dark humbucker guitar + Marshall high-gain amp
- Neck pickup
- Treble controls at 12 o'clock or lower
```

---

### Strategy 4: Transparent + Mid-Focused

**Goal:** Balanced foundation with vocal, cutting mid-range.

**Best Combinations:**

#### Morning Glory → TWA Source Code ⭐ Rating: 45/50

**Theory:**
- Morning Glory: Neutral frequency response (preserves full spectrum)
- TWA Source Code: TS Evolution with Bite control
- Complementary frequencies (neutral + mid-focused)

**Settings:**
```
Morning Glory:
- Gain: 10-12 o'clock (low-medium)
- Volume: 12-1 o'clock (slight boost or unity)
- Tone: 12 o'clock
- Bright Cut: OFF (preserve brightness for TS)

TWA Source Code:
- Drive: 10-12 o'clock (receives Morning Glory)
- Tone: 12-1 o'clock
- Volume: 12 o'clock
- Bite: 12 o'clock (start neutral, adjust for harmonic balance)
  - CCW: More even-order harmonics (warmer)
  - CW: More odd-order harmonics (brighter, more aggressive)
```

**Frequency Interaction:**
```
Morning Glory:  ------------------  (neutral, full spectrum)

TWA Source:           /\            (TS mid boost 800Hz-1.5kHz)
                     /  \

Combined:       -----/  \-----      (balanced with vocal mids)
```

**Bite Control Effect:**
```
Bite CCW (counter-clockwise):
- More even-order harmonics (2nd, 4th)
- Warmer, rounder tone
- Smooth mid-range

Bite 12 o'clock (neutral):
- Balanced harmonic content
- Standard TS character

Bite CW (clockwise):
- More odd-order harmonics (3rd, 5th)
- Brighter, more aggressive
- Cutting mid-range
```

**Why This Works:**
- Morning Glory provides neutral foundation
- TWA Source Code adds vocal mid-range character
- Bite control allows harmonic fine-tuning
- 18V internal operation provides extra headroom
- Classic BB + TS pairing (updated versions)

**Best For:**
- **Classic Rock:** Vocal, cutting rhythm tones
- **Blues-Rock:** SRV-style overdrive
- **Fusion:** Singing lead tones with mid presence
- **Rock:** Cutting through band mix

**NOT Recommended For:**
- **Jazz:** TS mid-hump too aggressive
- **Neo Soul:** Mid-focus may clash with warm aesthetic (unless desired)

---

### Strategy 5: Amp-in-a-Box + Transparent OD

**Goal:** Amp simulation foundation, transparent OD pushes it into breakup.

**Best Combinations:**

#### Blacklon → Morning Glory ⭐ Rating: 45/50

**Theory:**
- Blacklon: Fender Blackface amp-in-a-box (provides amp EQ foundation)
- Morning Glory: Transparent BB (pushes Blacklon into natural breakup)
- Two Positioning Approaches: Blacklon first (tone shaper) or last (amp sim)

**Approach 1: Blacklon as Tone Shaper (First)**
```
Blacklon:
- Gain: 10-12 o'clock (moderate)
- Volume: 12 o'clock (unity)
- Tone: 12 o'clock
- 6L6/6V6: 6V6 (warmer for Neo Soul) or 6L6 (more headroom for Rock)
- Mellow/Drive: Mellow (receive boost from Morning Glory)
- Purpose: Provide Blackface EQ foundation

Morning Glory:
- Gain: 11-1 o'clock (push Blacklon)
- Volume: 1-2 o'clock (drive Blacklon into breakup)
- Tone: 12 o'clock
- Bright Cut: OFF
- Purpose: Drive Blacklon amp simulation

Result: Blackface EQ → Transparent OD push → Amp-like breakup
```

**Approach 2: Blacklon as Final Amp Simulator (Last)**
```
Morning Glory:
- Gain: 11-1 o'clock
- Volume: 1-2 o'clock (push Blacklon)
- Tone: 12 o'clock
- Purpose: Transparent gain staging

Blacklon:
- Gain: 11-1 o'clock (receives Morning Glory boost)
- Volume: 12 o'clock
- 6L6/6V6, Mellow/Drive: Adjust for final amp character
- Purpose: Final amp simulation

Result: Transparent OD → Amp-in-a-box final stage → Amp-like output
```

**Frequency Interaction:**
```
Blacklon:      \        /         (Blackface scooped mids)
                \______/
                (clean, sparkly)

Morning Glory: ------------------  (neutral, preserves Blackface character)

Combined:      \        /         (Blackface character with OD saturation)
                \__--__/
```

**Why This Works:**
- Blacklon provides Blackface amp character (scooped mids, sparkly highs)
- Morning Glory preserves this character while adding BB saturation
- Extremely amp-like dynamic response
- **Special Value:** Transforms solid-state amps (JC-22) into tube-like response

**Best For:**
- **Neo Soul:** 6V6 + Mellow mode for warm, clean tones
- **Post Rock:** 6L6 + Drive mode for headroom and breakup
- **Jazz:** Blackface clean character
- **Funk:** Sparkly clean with punch

**Special Application: JC-22 Users**
```
JC-22 (solid-state, clean platform)
  ↓
Blacklon (adds Blackface tube amp character)
  ↓
Morning Glory (pushes into natural tube-like breakup)
  ↓
Result: Tube amp response from solid-state amp
```

**Blacklon Mode Selection:**

**6L6 Mode:**
- More headroom
- Extended low-end
- Best for: Heavy riffs, Post Rock, clean headroom

**6V6 Mode:**
- Warmer, mellower
- Earlier breakup
- Best for: Neo Soul, Jazz, vintage tones

**Mellow vs Drive:**
- **Mellow:** Rich low-end, less distortion, gentle tone control
- **Drive:** Reduced low-end (prevents mud), more distortion, aggressive tone control

**Recommended Combinations:**
```
Neo Soul: 6V6 + Mellow
Post Rock: 6L6 + Drive
Jazz Clean: 6V6 + Mellow (low gain)
Funk Clean: 6L6 + Mellow (low gain)
```

---

## Three-Pedal Stacking Strategies

### Strategy 1: Ultimate Fusion Chain

**Goal:** High-end Fusion tone with maximum complexity and control.

#### Soul Food → Morning Glory → ODL-1-CS ⭐ Rating: 47/50

**Architecture:**
```
Layer 1: Klon Boost (transparent foundation)
Layer 2: BB Core OD (neutral character definition)
Layer 3: Dumble Drive (rich harmonic saturation)
```

**Settings:**
```
Soul Food (Layer 1 - Transparent Boost):
- Drive: 9 o'clock (minimal clipping)
- Volume: 2-3 o'clock (significant boost to push Morning Glory)
- Treble: 11 o'clock (slight reduction to avoid harshness)
- Purpose: Klon mid-boost foundation, push Morning Glory into sweet spot

Morning Glory (Layer 2 - Core OD):
- Gain: 11-12 o'clock (receives Soul Food boost)
- Volume: 12-1 o'clock (push ODL-1-CS or unity)
- Tone: 12 o'clock (neutral)
- Bright Cut: OFF (preserve brightness for final stage)
- Purpose: Define core BB overdrive character

ODL-1-CS (Layer 3 - Dumble Final Saturation):
- Channel: Drive Channel
- Voltage: 14-15V (Custom Shop - balanced setting)
- Drive: 11-1 o'clock (receives two layers of boost)
- Mode: ROCK (for modern attack) or JAZZ (for warmth)
- Glass/EQ: EQ ON (Dumble tone circuit active)
- Volume: 12 o'clock (unity gain)
- Purpose: Dumble harmonic richness and final saturation
```

**Frequency Layering:**
```
Soul Food (Layer 1):    /\__          (Klon mid-boost + sparkle)
                       /    \___

Morning Glory (L2):   ----------------  (neutral, preserves L1)

ODL-1-CS (Layer 3):   ___     ___      (Dumble rich harmonics)
                     /   \___/   \

Combined:            ___/\___/\___     (complex, full-spectrum)
= Klon mid-boost + BB neutrality + Dumble richness
```

**Gain Staging:**
```
Soul Food:      +8dB boost
Morning Glory:  +10dB (at boosted input level)
ODL-1-CS:       +15dB (at double-boosted input level)
Total:          +33dB (45× voltage amplification)

Compression:
Soul Food:      5% (very low)
Morning Glory:  5% (very low)
ODL-1-CS:       15% (Dumble-style)
Total:          ~22% (within ideal range < 30%)
```

**Why This Works:**
- Soul Food: Transparent Klon boost preserves guitar character
- Morning Glory: Ultra-transparent BB maintains Soul Food's mid-boost
- ODL-1-CS: Dumble adds rich harmonics without muddiness
- Total compression stays under 30% (maintains dynamics)
- All three pedals have high touch sensitivity
- Progressive gain build (not excessive at any stage)

**Usage Modes:**
```
Mode 1: Soul Food only
= Clean Klon boost with sparkle
Use for: Edge-of-breakup tones, pushing clean amp

Mode 2: Soul Food + Morning Glory
= Classic Klon → BB combination
Use for: Medium overdrive, Blues, Rock

Mode 3: All three active
= Full Fusion tone
Use for: Lead lines, complex rhythm, Larry Carlton / Robben Ford style
```

**Best For:**
- **Fusion:** Larry Carlton, Robben Ford, Scott Henderson style
- **Blues:** Complex, rich overdrive
- **Jazz:** Transparent with harmonic richness
- **Rock:** Sophisticated, non-aggressive overdrive

**Reference Artists:**
- Larry Carlton (Dumble + transparent boost)
- Robben Ford (Dumble-style tones)
- Eric Johnson (complex gain staging)
- John Mayer (Klon + Dumble approach)

---

### Strategy 2: Warm Neo Soul Stack

**Goal:** Ultra-warm, tube-like Neo Soul tone optimized for solid-state amps.

#### Horsemeat → Sweet Honey → Blacklon ⭐ Rating: 46/50

**Architecture:**
```
Layer 1: Germanium Klon Boost (warm foundation)
Layer 2: Vintage OD (sweet character)
Layer 3: Blackface Amp-in-a-Box (tube amp simulation)
```

**Settings:**
```
Horsemeat (Layer 1 - Germanium Boost):
- Gain: 9 o'clock (low gain, warm boost)
- Volume: 2 o'clock (push Sweet Honey)
- Voice: 11-12 o'clock (saturated to glassy balance)
- Treble: 1-2 o'clock (compensate double warmth)
- Bass: 11 o'clock (avoid excessive low-end)
- Purpose: Germanium warm foundation

Sweet Honey (Layer 2 - Core Warm OD):
- Drive: 11-12 o'clock (receives Germanium boost)
- Focus: 1-2 o'clock (Neo Soul sweet spot)
- Volume: 12-1 o'clock (push Blacklon)
- Bass: 11 o'clock (prevent mud from triple warmth)
- Treble: 1-2 o'clock (add sparkle to balance warmth)
- Purpose: Sweet Neo Soul overdrive character

Blacklon (Layer 3 - Blackface Amp Simulation):
- Gain: 11-1 o'clock (receives two warm layers)
- Volume: 12 o'clock (unity)
- Tone: 12-1 o'clock
- 6L6/6V6: 6V6 (warm Neo Soul character)
- Mellow/Drive: Mellow (receive two layers of drive)
- Purpose: Final Blackface amp tube simulation
```

**Frequency Layering:**
```
Horsemeat (L1):     ___              (warm Germanium low-mid)
                   /   \___

Sweet Honey (L2):  ___               (warm vintage OD)
                  /   \___

Blacklon (L3):   \        /          (Blackface scooped mids, bright highs)
                  \______/

Combined:        ___      ___        (warm lows + sparkly highs)
                /   \____/   \
= Warm but not dark (Blacklon adds high-end sparkle)
```

**Why This Works:**
- Horsemeat: Germanium warmth without being dark
- Sweet Honey: Vintage OD sweetness
- Blacklon: Adds Blackface sparkle to balance warmth
- All three maintain excellent touch sensitivity
- Blacklon's scooped-mid Blackface character prevents mid-range mud

**Critical EQ Strategy:**
```
Triple-warm pedal stack requires careful EQ:

Horsemeat Treble: 1-2 o'clock (higher than usual)
Sweet Honey Treble: 1-2 o'clock (higher than usual)
Blacklon Tone: 12-1 o'clock (Blackface natural brightness)

Bass controls: All at 11 o'clock or lower (prevent low-end buildup)

Result: Warm but clear, not dark or muddy
```

**Best For:**
- **Neo Soul:** Ultra-warm, smooth tones (D'Angelo, John Mayer style)
- **Jazz:** Rich, warm lead tones
- **Blues:** Smooth, singing sustain
- **Post Rock:** Warm ambient swells

**Special Application: JC-22 Users**
```
JC-22 (solid-state, bright, clean)
  ↓
Horsemeat (Germanium warmth)
  ↓
Sweet Honey (vintage OD sweetness)
  ↓
Blacklon (tube amp simulation)
  ↓
Result: Warm tube amp response from solid-state amp
```

**Caution:**
```
❌ Too Dark For:
- Dark humbucker guitars (especially neck pickup)
- Dark/warm amplifiers (Marshall, vintage Fender)
- Low-treble settings

✅ Works Best With:
- Bright guitars (Tele, Strat, P-90)
- Solid-state amps (JC-22, Roland, Fender Frontman)
- Bridge pickup emphasis
- Treble controls set higher (1-2 o'clock)
```

**Usage Modes:**
```
Mode 1: Horsemeat only
= Warm Germanium clean boost

Mode 2: Horsemeat + Sweet Honey
= Warm Neo Soul overdrive (without amp sim)

Mode 3: All three active
= Full tube-like Neo Soul tone with Blackface character
```

---

### Strategy 3: Classic Rock Power Trio

**Goal:** Balanced, cutting Classic Rock tone with vocal mids.

#### Morning Glory → TWA Source Code → ODL-1-CS ⭐ Rating: 45/50

**Architecture:**
```
Layer 1: Transparent BB (foundation)
Layer 2: TS Evolution (vocal mids)
Layer 3: Dumble Drive (final richness)
```

**Settings:**
```
Morning Glory (Layer 1 - Transparent Foundation):
- Gain: 10-11 o'clock (low gain boost)
- Volume: 1-2 o'clock (push TWA Source Code)
- Tone: 12 o'clock
- Bright Cut: OFF (preserve brightness)
- Purpose: Transparent BB foundation

TWA Source Code (Layer 2 - Mid-Focused Core):
- Drive: 10-12 o'clock (receives Morning Glory boost)
- Tone: 12-1 o'clock
- Volume: 12 o'clock (push ODL-1-CS or unity)
- Bite: 12 o'clock (start neutral)
  - Adjust CW for more aggressive (odd harmonics)
  - Adjust CCW for warmer (even harmonics)
- Purpose: TS-style mid-range definition

ODL-1-CS (Layer 3 - Dumble Final Saturation):
- Channel: Drive
- Voltage: 15-16V (higher for more headroom with TS mids)
- Drive: 11-1 o'clock (receives two layers)
- Mode: ROCK (for punch and attack)
- Volume: 12 o'clock
- Purpose: Dumble richness and final saturation
```

**Frequency Layering:**
```
Morning Glory (L1): ----------------  (neutral foundation)

TWA Source (L2):        /\            (TS mid-boost 800Hz-1.5kHz)
                       /  \

ODL-1-CS (L3):     ___      ___       (Dumble harmonics)
                  /   \____/   \

Combined:         ___/\___/\___       (vocal mids + full harmonics)
```

**Bite Control Application:**
```
For Classic Rock:

Bite at 12-1 o'clock (neutral to slight CW):
- Balanced to slightly aggressive
- Cutting mid-range
- Classic Rock punch

For Blues-Rock:

Bite at 11-12 o'clock (slight CCW to neutral):
- Warmer, rounder mids
- Smooth sustain
- SRV-style warmth
```

**Why This Works:**
- Morning Glory: Transparent foundation preserves guitar character
- TWA Source Code: Adds TS vocal mid-range (cutting through mix)
- ODL-1-CS: Dumble richness prevents TS from being thin
- Bite control allows fine-tuning harmonic character
- 18V internal (TWA) + voltage-adjustable (ODL-1-CS) = massive headroom

**Best For:**
- **Classic Rock:** Cutting, vocal rhythm tones
- **Blues-Rock:** SRV-style overdrive with richness
- **Fusion:** Vocal lead tones
- **Rock:** Punchy rhythm with mid presence

**NOT Recommended For:**
- **Jazz:** TS mid-boost too aggressive
- **Neo Soul:** May lack warmth if Bite set too aggressive

**Usage Modes:**
```
Mode 1: Morning Glory only
= Transparent BB boost

Mode 2: Morning Glory + TWA Source Code
= BB + TS classic rock combination

Mode 3: All three active
= Full complex Classic Rock / Fusion tone
```

---

## Common Mistakes & Solutions

### Mistake 1: Over-Compression (Squashed Tone)

**Symptoms:**
- Lifeless, flat tone
- No dynamic range (all notes same volume)
- "Pumping" or "breathing" effect
- Guitar volume knob has no effect
- Sounds like a limiter, not an overdrive

**Causes:**
```
❌ Problem Setup:
Cali76 FET (high compression)
→ Horsemeat (moderate compression)
→ TWA Source Code (moderate compression)
→ Another medium-compression OD

Total compression: 40-50% ← WAY too much!
```

**Solutions:**

**Solution 1: Replace with Low-Compression Pedals**
```
✅ Fixed Setup:
Empress MKII (ultra-transparent, low compression)
→ Morning Glory (ultra-low compression)
→ ODL-1-CS (moderate Dumble compression)

Total compression: 20-25% ← Healthy range!
```

**Solution 2: Use Parallel Compression**
```
✅ Using Cali76 FET:
- IN: Medium (moderate compression trigger)
- OUT: High (makeup gain)
- RATIO: 4:1 or All
- DRY: 70-80% (blend 70-80% dry signal back in)

Result: Heavy compression + preserved transients
```

**Solution 3: Remove One Pedal**
```
If using three ODs and tone sounds squashed:
→ Bypass one pedal (usually the middle one)
→ Test which two-pedal combination sounds best
→ Keep only those two pedals active
```

**Compression Test:**
```
Play with your hands:
1. Play very softly
2. Play very hard

If soft and hard playing sound nearly identical in volume:
→ Over-compressed! Reduce compression.

If soft and hard playing have clear volume difference:
→ Good! Dynamics preserved.
```

---

### Mistake 2: Frequency Masking (Muddy Tone)

**Symptoms:**
- Muddy, unclear tone
- Individual notes don't stand out
- Sounds "honky" or "boxy"
- High-end or low-end lacking

**Causes:**
```
❌ Problem: Double Mid-Hump
TWA Source Code (TS mid-boost)
→ Virtues Arca (BB thick mids + grit)

Result: Excessive mid-range buildup, frequency masking
```

**Solutions:**

**Solution 1: Pair Mid-Focused with Neutral**
```
✅ Fixed:
Morning Glory (neutral frequency)
→ TWA Source Code (mid-focused)

Result: Balanced spectrum, vocal mids without mud
```

**Solution 2: Use EQ to Compensate**
```
If stuck with two mid-focused pedals:

Add PA-1QG before both:
- Cut 400-800Hz by 2-3dB (reduce mid buildup)
- Boost 3.5kHz-7kHz by 2dB (add clarity)

Result: Compensated frequency response
```

**Solution 3: Change Pedal Order**
```
Sometimes changing order helps:

Try: Virtues Arca → TWA Source Code
vs:  TWA Source Code → Virtues Arca

One order may sound clearer than the other.
```

**Frequency Masking Test:**
```
A/B Test:
1. Play both pedals together
2. Turn off second pedal
3. Listen to how much clarity returns

If clarity dramatically improves when second pedal off:
→ Frequency masking! Change pedals or order.
```

---

### Mistake 3: Wrong Pedal Order

**Symptoms:**
- Tone sounds "wrong" but can't identify why
- Less dynamic than expected
- One pedal doesn't seem to be doing anything

**Common Order Mistakes:**

#### Mistake 3A: Amp-in-a-Box in Wrong Position

**❌ Wrong (usually):**
```
Blacklon (amp-in-a-box) → Morning Glory → TWA Source Code
```

**Problem:**
- Amp-in-a-box usually should be LAST (receives all the drive)
- Placing it first misses the point of "amp simulation"

**✅ Correct (traditional):**
```
Morning Glory → TWA Source Code → Blacklon (amp-in-a-box)
```

**However, there are TWO valid approaches:**

**Approach 1: Amp-in-a-Box as Tone Shaper (First)**
```
Blacklon → Morning Glory → TWA Source Code
= Provides Blackface EQ foundation → ODs layer on top
Use case: Solid-state amp (JC-22) needs tube EQ character
```

**Approach 2: Amp-in-a-Box as Amp Simulator (Last)**
```
Morning Glory → TWA Source Code → Blacklon
= OD layers → Final amp-like saturation
Use case: Traditional amp-in-a-box use, tube amp users
```

#### Mistake 3B: Colored Before Transparent

**❌ Wrong:**
```
Sweet Honey (warm colored) → Morning Glory (transparent)
```

**Problem:**
- Transparent pedal after colored pedal can't "restore" transparency
- Order negates Morning Glory's transparent character

**✅ Correct:**
```
Morning Glory (transparent) → Sweet Honey (warm colored)
= Preserve guitar character → Add warmth
```

**Principle:** Transparent pedals go FIRST to preserve character.

#### Mistake 3C: High Gain Before Low Gain

**❌ Wrong:**
```
ODL-1-CS (Drive Channel, high gain) → Soul Food (clean boost)
```

**Problem:**
- Boost after heavy drive doesn't push drive harder
- Just makes loud, already-saturated signal louder
- Misses benefit of boosting drive into sweet spot

**✅ Correct:**
```
Soul Food (clean boost) → ODL-1-CS (Drive Channel)
= Boost pushes drive into optimal saturation point
```

**Principle:** Boost pedals go BEFORE drive pedals.

---

### Mistake 4: All Pedals Set to Medium-High Gain

**Symptoms:**
- Extremely saturated, fuzzy tone (but you want overdrive)
- Loss of note definition
- Muddy, indistinct tone
- Can't hear individual notes in chords

**Causes:**
```
❌ Problem Setup:
Morning Glory (Gain at 2 o'clock)
→ TWA Source Code (Drive at 2 o'clock)
→ ODL-1-CS (Drive at 2 o'clock)

Total gain: Excessive! Each pedal adds high gain.
```

**Solutions:**

**Solution: Progressive Gain Staging**
```
✅ Fixed:
Morning Glory (Gain at 10 o'clock) ← Low gain boost
→ TWA Source Code (Drive at 12 o'clock) ← Medium gain
→ ODL-1-CS (Drive at 1 o'clock) ← Higher gain (receives boost)

Result: Progressive, controlled gain buildup
```

**Gain Staging Guidelines:**
```
Layer 1 (Boost):        Gain 9-10 o'clock
Layer 2 (Core OD):      Gain 11-1 o'clock
Layer 3 (Final Drive):  Gain 12-2 o'clock (receives boost from L1+L2)
```

**Test Method:**
```
1. Set all pedals to minimum gain
2. Turn on Layer 1, increase gain until slight edge-of-breakup
3. Turn on Layer 2, increase gain to desired OD level
4. Turn on Layer 3, increase gain to final saturation

Result: Optimal gain distribution
```

---

### Mistake 5: Ignoring Guitar Volume Knob Interaction

**Symptoms:**
- Guitar volume knob doesn't clean up tone
- Tone sounds the same from 5 to 10 on guitar volume
- Can't achieve clean-to-OD gradient with volume knob

**Causes:**
- Using pedals with high compression
- Excessive gain staging
- Using multiple medium-compression pedals

**Solutions:**

**Solution 1: Use Low-Compression Pedals**
```
High Volume Knob Sensitivity:
- KOT (extreme sensitivity)
- Morning Glory (extreme sensitivity)
- Soul Food (high sensitivity)
- Sweet Honey (high sensitivity, adjustable via Focus)

Low Volume Knob Sensitivity:
- High-compression ODs
- Multiple pedals stacked with medium gain
```

**Solution 2: Reduce Overall Gain**
```
If guitar volume knob not working:
→ Reduce gain on all pedals by 10-20%
→ Test volume knob response again

Lower gain = more dynamic = better volume knob response
```

**Solution 3: Use Focus Control (Sweet Honey)**
```
Sweet Honey Focus Control:
- CCW (counter-clockwise): Requires harder attack for breakup
  → More volume knob sensitivity

- CW (clockwise): Earlier breakup, less sensitivity
  → Less volume knob sensitivity

For volume knob clean-up: Set Focus more CCW
```

**Test Method:**
```
1. Guitar volume at 10 (full)
2. Pedals on, set gain for desired OD tone
3. Reduce guitar volume to 5
4. If tone cleans up significantly: ✅ Good!
5. If tone stays same: ❌ Too compressed, adjust pedals
```

---

## Genre-Specific Recommendations

### Jazz Clean to Edge-of-Breakup

**Goal:** Ultra-transparent, amp-like response with minimal coloration.

**Best Combinations:**

#### Option 1: KOT Clean → Sweet Honey (Focus CCW)
```
KOT Yellow Channel:
- Mode: Clean
- Gain: 9-10 o'clock
- Volume: 1 o'clock (slight boost)
- Tone: 12 o'clock

Sweet Honey:
- Drive: 10-11 o'clock (subtle overdrive)
- Focus: 10-11 o'clock (CCW - requires harder pick attack)
- Volume: 12 o'clock
- Bass: 12 o'clock
- Treble: 12 o'clock

Character: Transparent, touch-sensitive, cleans up with guitar volume
Best Guitar: ESP Throbber (PAF humbuckers) or hollowbody
Best Amp: Tone King Imperial MKII (tube warmth)
```

#### Option 2: Morning Glory → ODL-1-CS (JAZZ mode)
```
Morning Glory:
- Gain: 9-10 o'clock
- Volume: 12 o'clock
- Tone: 12 o'clock
- Bright Cut: OFF

ODL-1-CS:
- Channel: Normal (not Drive)
- Voltage: 14-16V (higher headroom for Jazz)
- Mode: JAZZ (emphasizes low-frequency richness)
- Gain: 9-10 o'clock
- Glass/EQ: GLASS (Blackface bright switch for clarity)

Character: Transparent with Dumble richness, extremely amp-like
Best Guitar: Hollowbody with humbuckers (Throbber, L-5, ES-335)
Best Amp: Clean amp with headroom
```

#### Option 3: Horsemeat (Low Gain, Germanium Boost)
```
Horsemeat (standalone):
- Gain: 9 o'clock (minimal clipping)
- Volume: 1-2 o'clock (clean boost with warmth)
- Voice: 11 o'clock (slightly saturated)
- Treble: 12 o'clock
- Bass: 12 o'clock

Character: Warm Germanium clean boost, subtle coloration
Best Guitar: Bright guitar (Tele, Strat, P-90)
Best Amp: JC-22 or clean solid-state (adds warmth)
```

**Jazz Settings Philosophy:**
- Gain: Very low (9-11 o'clock)
- Volume: Unity to slight boost
- Compression: Minimal (use low-compression pedals)
- Touch sensitivity: Maximum (test with guitar volume knob)

---

### Neo Soul Smooth Rhythm

**Goal:** Warm, sweet, smooth overdrive with excellent chord clarity.

**Best Combinations:**

#### Option 1: Horsemeat → Sweet Honey ⭐ (Top Choice)
```
Horsemeat:
- Gain: 9-10 o'clock
- Volume: 2 o'clock (push Sweet Honey)
- Voice: 11-12 o'clock (warm saturation)
- Treble: 1 o'clock (compensate warmth)
- Bass: 11 o'clock

Sweet Honey:
- Drive: 11-1 o'clock (receives Germanium boost)
- Focus: 1-2 o'clock (Neo Soul sweet spot)
- Volume: 12 o'clock
- Bass: 11 o'clock (avoid mud)
- Treble: 1-2 o'clock (sparkle)

Character: Ultra-warm, Germanium + vintage OD, smooth
Best Guitar: Greco TE-500 (Wide Range) or Tokyo Thinline (P-90)
Best Amp: JC-22 (solid-state needs warmth)

Reference: D'Angelo, John Mayer (warm Neo Soul tones)
```

#### Option 2: Morning Glory → Sweet Honey
```
Morning Glory:
- Gain: 10 o'clock
- Volume: 1 o'clock
- Tone: 12 o'clock
- Bright Cut: Adjust for guitar

Sweet Honey:
- Drive: 12 o'clock
- Focus: 1-2 o'clock
- Volume: 12 o'clock
- Bass/Treble: 12 o'clock

Character: Transparent warmth, balanced
Best Guitar: Any (Morning Glory is neutral)
Best Amp: Any

Note: Less warm than Horsemeat version, more transparent
```

#### Option 3: Blacklon (6V6 + Mellow) Standalone
```
Blacklon:
- Gain: 11-1 o'clock (moderate Neo Soul drive)
- Volume: 12 o'clock
- Tone: 12 o'clock
- 6L6/6V6: 6V6 (warm, mellow)
- Mellow/Drive: Mellow (rich low-end, less distortion)

Character: Blackface mellow warmth, Neo Soul characteristic
Best Guitar: P-90 (Fender Tokyo Thinline), Wide Range (Greco TE-500)
Best Amp: JC-22 (adds tube character)

Reference: Neo Soul characteristic "mellow Fender" tone
```

**Neo Soul Settings Philosophy:**
- Focus Control: 1-2 o'clock (sweet spot)
- Treble: Slightly higher (1-2 o'clock) to balance warmth
- Bass: Slightly lower (11 o'clock) to prevent mud
- Compression: Moderate (sustain without killing dynamics)
- Warmth: Priority (Germanium, vintage OD)

---

### Blues Lead with Bite

**Goal:** Vocal, singing lead tone with sustain and harmonic richness.

**Best Combinations:**

#### Option 1: Soul Food → Morning Glory ⭐
```
Soul Food:
- Drive: 10 o'clock (clean boost)
- Volume: 2-3 o'clock (significant boost)
- Treble: 11-12 o'clock

Morning Glory:
- Gain: 12-1 o'clock (receives Klon boost)
- Volume: 12 o'clock (unity)
- Tone: 12 o'clock
- Bright Cut: OFF (preserve brightness)

Character: Classic Klon + BB, transparent with bite
Best Guitar: Strat, Tele, Les Paul (versatile)
Best Amp: Clean to edge-of-breakup amp

Reference: Classic Blues tone (many players use this combo)
```

#### Option 2: Soul Food → Virtues Arca (Gritty Blues)
```
Soul Food:
- Drive: 10 o'clock
- Volume: 2 o'clock
- Treble: 12 o'clock

Virtues Arca:
- Gain: 12-1 o'clock (receives Klon boost)
- Volume: 12 o'clock
- Treble: 12 o'clock
- Bass: 12 o'clock

Character: Klon + BB with grit, more aggressive than Morning Glory
Best Guitar: Humbucker guitars (Les Paul, SG)
Best Amp: Fender, Marshall

Note: More "grit" and texture than standard Klon+BB combo
```

#### Option 3: Horsemeat → Colosseum BB (Warm Blues)
```
Horsemeat:
- Gain: 10 o'clock
- Volume: 2 o'clock
- Voice: 12 o'clock
- Treble: 1 o'clock
- Bass: 12 o'clock

Cornerstone Colosseum (BB Side):
- Gain: 12 o'clock
- Volume: 12 o'clock
- Tone: 12 o'clock
- Clean Control: 10 o'clock (mix in clean signal)

Character: Warm Germanium + open BB, vintage Blues
Best Guitar: Les Paul, SG, hollowbody
Best Amp: Fender, vintage amp

Reference: Vintage warm Blues (Eric Clapton "Bluesbreaker" era)
```

**Blues Settings Philosophy:**
- Gain: Medium (12-1 o'clock on final stage)
- Sustain: Important (moderate compression okay)
- Bite: Klon mid-boost or TS-style adds vocal quality
- Touch sensitivity: High (blues requires dynamics)

---

### Funk Tight Rhythm

**Goal:** Tight, percussive, consistent level with sparkle.

**Best For Funk:**
- Compressor FIRST (tight, percussive attack)
- Transparent or Klon-style OD (maintain clarity)
- Bright tone (sparkle and presence)

#### Recommended Setup:
```
Empress MKII Compressor (tight, fast attack)
  ↓
PA-1QG (boost 800Hz-3.2kHz for Funk punch)
  ↓
From Yesterday (KOT) Yellow Clean Mode
  ↓
JC-22 (bright, clean, Chorus ON)
```

**Settings:**
```
Empress MKII:
- INPUT: Medium (3-4 LED) - significant compression
- RATIO: 4:1 or 6:1 (tight control)
- ATTACK: Fast (1-5ms) - catch all transients
- RELEASE: Fast (50-100ms) - quick recovery
- MIX: 100% (full compression for Funk)
- Sidechain HPF: 120Hz (preserve bass punch)
- TONE: Slight CW (add brightness)

PA-1QG:
- Preset: Funk EQ
  - Boost 800Hz: +2dB
  - Boost 1.6kHz: +3dB
  - Boost 3.2kHz: +2dB
- LEVEL: Unity or +3dB

From Yesterday (KOT Yellow):
- Mode: Clean (via internal DIP switch)
- Gain: 10 o'clock (slight edge-of-breakup)
- Volume: 12 o'clock (unity)
- Tone: 1 o'clock (bright)

JC-22:
- Volume: 5-6
- Bright Switch: ON
- Chorus: Speed 3-4, Depth 4-5
```

**Character:** Tight, percussive, sparkly, consistent level
**Best Guitar:** Greco TE-500 Bridge pickup (Wide Range), bright Strat
**Reference:** Nile Rodgers (Chic), Cory Wong

**Alternative (Without Compressor):**
```
PA-1QG (Funk EQ)
→ Soul Food (Drive low, Volume high - Klon boost)
→ Morning Glory (Gain low, Bright Cut OFF)
→ JC-22

Less compressed, more dynamic, but still clear and punchy
```

**Funk Settings Philosophy:**
- Compression: Important (Empress MKII fast attack)
- EQ: Boost high-mids (800Hz-3.2kHz) for Funk spank
- Tone: Bright (preserve sparkle)
- Overdrive: Minimal (edge-of-breakup or clean boost)
- Guitar: Bridge pickup (tight bass, bright treble)

---

### Post Rock Ambient

**Goal:** Long sustain, warm, dynamic swells, reverb-friendly.

**Best Combinations:**

#### Option 1: Morning Glory → Sweet Honey ⭐
```
Morning Glory:
- Gain: 10 o'clock (low gain boost)
- Volume: 1 o'clock (push Sweet Honey)
- Tone: 12 o'clock
- Bright Cut: OFF

Sweet Honey:
- Drive: 11-12 o'clock (moderate drive)
- Focus: 1 o'clock (Post Rock sweet spot)
- Volume: 12 o'clock
- Bass: 12 o'clock
- Treble: 12 o'clock

→ Imperial MKII or JC-22
→ [FX Loop] → AASB (Shimmer) → Nucleo (Reactor) → [Return]

Character: Transparent warmth, long sustain, reverb-friendly
Best Guitar: ESP EC-CTM (high-output humbuckers), Greco TE-500
Best Amp: Imperial MKII (tube warmth) or JC-22 (clean platform)

Reference: Explosions in the Sky, This Will Destroy You
```

#### Option 2: KOT Clean → Sweet Honey → Blacklon
```
KOT Yellow:
- Mode: Clean
- Gain: 9 o'clock
- Volume: 1 o'clock

Sweet Honey:
- Drive: 11 o'clock
- Focus: 1 o'clock
- Volume: 12 o'clock

Blacklon:
- Gain: 11 o'clock
- 6L6/6V6: 6L6 (headroom for swells)
- Mellow/Drive: Drive
- Volume: 12 o'clock

→ Amp → [Loop] → Ambient effects

Character: Three-layer transparent warmth, maximum dynamic control
```

#### Option 3: Sweet Honey → Blacklon (6L6 + Drive)
```
Sweet Honey:
- Drive: 11 o'clock
- Focus: 1 o'clock
- Volume: 12 o'clock

Blacklon:
- Gain: 12-1 o'clock
- 6L6/6V6: 6L6 (maximum headroom for swells)
- Mellow/Drive: Drive
- Volume: 12 o'clock

→ Amp → [Loop] → Delay (FT-1Y Hold) → AASB → Nucleo

Character: Warm OD + Blackface headroom, perfect for ambient swells
```

**Post Rock Settings Philosophy:**
- Dynamics: Critical (use low-compression pedals)
- Gain: Low to medium (preserve clean-to-OD gradient)
- Sustain: Important (but not over-compressed)
- Warmth: Desired (pairs well with ambient reverb)
- Guitar Volume Knob: Must work (clean-to-drive swells)

**Post Rock Pedal Priority:**
```
Most Important for Post Rock:
1. Low compression (preserve dynamics)
2. Guitar volume knob sensitivity (swells)
3. Reverb/Delay quality (more important than OD)
4. Warm but not dark tone (pairs with reverb)

Post Rock OD Use:
- Often used at LOW gain (edge-of-breakup)
- Dynamic swells from clean to OD using guitar volume
- Sustain without killing transients
```

---

## Signal Chain Positioning

### Complete Signal Chain Architecture

#### Full Signal Chain (4-Cable Method):
```
Guitar
  ↓
[Pre-Amp Chain - Before Amp Input]
  ↓
Compressor (optional - Cali76 FET or Empress MKII)
  ↓
EQ (optional - PA-1QG)
  ↓
Overdrive Layer 1 (transparent boost or low gain)
  ↓
Overdrive Layer 2 (core OD character)
  ↓
Overdrive Layer 3 (final drive or amp-in-a-box)
  ↓
Amp Input
  ↓
[Amp Pre-amp Stage]
  ↓
FX Send
  ↓
[Effects Loop Chain]
  ↓
Modulation (Chorus, Flanger, Phaser)
  ↓
Delay (FT-1Y)
  ↓
Reverb (Nucleo, AASB)
  ↓
FX Return
  ↓
[Amp Power Amp Stage]
  ↓
Speaker Output
```

---

### Pre-Amp Chain Positioning Rules

#### Rule 1: Compressor First (If Using)
```
Compressor → [Overdrive Chain]

Why: Compressor controls dynamics before gain stages
```

**Compressor Positioning Options:**

**Option A: Compressor First (Most Common)**
```
Empress MKII (transparent control)
→ PA-1QG (EQ)
→ Morning Glory
→ Sweet Honey
→ Amp

Use case: Jazz, Neo Soul, Funk (control dynamics before OD)
```

**Option B: Compressor After OD (Post Rock, Sustain)**
```
Morning Glory
→ Sweet Honey
→ Cali76 FET (sustain + warmth)
→ Amp

Use case: Post Rock, Ambient (add sustain to driven signal)
```

#### Rule 2: EQ Positioning (Multiple Options)

**Option A: EQ Before OD (Tone Shaping)**
```
PA-1QG (shape input tone)
→ Morning Glory
→ Sweet Honey
→ Amp

Use case: Shape frequency before distortion (different guitars, tonal correction)
```

**Option B: EQ After OD (Boost/Solo)**
```
Morning Glory
→ Sweet Honey
→ GE-7 (LEVEL up for solo boost, EQ for final tone)
→ Amp

Use case: Solo boost, final tone shaping after OD
```

**Option C: EQ Both Before and After**
```
PA-1QG (guitar-specific EQ)
→ Morning Glory
→ Sweet Honey
→ GE-7 (solo boost)
→ Amp

Use case: Maximum control (EQ input tone + final solo boost)
```

#### Rule 3: Overdrive Chain Order

**Standard Order: Transparent → Colored**
```
Morning Glory (transparent foundation)
→ Sweet Honey (warm coloration)
→ Amp

Why: Preserve guitar character first, add coloration second
```

**Boost → OD Order:**
```
Soul Food (low gain, high volume - boost)
→ Morning Glory (medium gain - core OD)
→ Amp

Why: Boost pushes OD into sweet spot
```

**Amp-in-a-Box Positioning:**

**Approach 1: First (Tone Shaper)**
```
Blacklon (Blackface EQ foundation)
→ Morning Glory (transparent OD)
→ TWA Source Code (TS mid-focus)
→ Amp

Use case: Solid-state amp (JC-22) needs tube EQ character
```

**Approach 2: Last (Amp Simulator)**
```
Morning Glory (transparent OD)
→ TWA Source Code (TS mid-focus)
→ Blacklon (final amp simulation)
→ Amp

Use case: Traditional amp-in-a-box, tube amp users
```

---

### Effects Loop Positioning

**Standard FX Loop Order:**
```
FX Send
  ↓
[Modulation] - Chorus, Flanger, Phaser (optional)
  ↓
[Delay] - FT-1Y
  ↓
[Reverb 1] - AASB (Shimmer/special effects)
  ↓
[Reverb 2] - Nucleo (main stereo reverb)
  ↓
FX Return
```

**Why This Order:**
- Modulation before delay (modulate dry signal, not delayed)
- Delay before reverb (reverb creates space for delayed notes)
- Special reverb (AASB) before main reverb (Nucleo adds final space)
- Nucleo last for stereo output (if amp supports stereo return like JC-22)

---

### Two-Loop System (Advanced)

**Your V3.0 Setup: Loop 1 + Loop 2**

#### Loop 1 (Jazz/Neo Soul/Funk):
```
Guitar
  ↓
Empress MKII (transparent control)
  ↓
PA-1QG (guitar-specific EQ presets)
  ↓
Sweet Honey (warm Neo Soul OD)
  ↓
Horsemeat (Germanium Klon, optional layer)
  ↓
JC-22 Input
  ↓
[FX Loop] → FT-1Y → Nucleo → [Return]
```

**Character:** Transparent, warm, Neo Soul, Jazz, Funk
**Usage:** Clean-focused styles, low to medium gain

#### Loop 2 (Post Rock/Fusion/Rock):
```
Guitar
  ↓
Cali76 FET (sustain + warmth)
  ↓
PA-1QG (EQ)
  ↓
Blacklon (Blackface foundation or Amp-in-a-box)
  ↓
Morning Glory (transparent BB)
  ↓
TWA Source Code (TS mid-focus)
  ↓
ODL-1-CS (Dumble final drive)
  ↓
Imperial MKII or JC-22
  ↓
[FX Loop] → FT-1Y → AASB → Nucleo → [Return]
```

**Character:** Post Rock, Fusion, Classic Rock, heavier gain
**Usage:** Driven tones, complex gain staging

---

## Practical Examples

### Example 1: Jazz Clean Setup (Transparent Foundation)

**Goal:** Preserve hollowbody's natural woody tone with subtle edge-of-breakup.

**Gear:**
- Guitar: ESP Throbber-CTM (APH-1 PAF humbuckers)
- Amp: Tone King Imperial MKII (Rhythm Channel)

**Signal Chain:**
```
ESP Throbber (neck pickup)
  ↓
Empress MKII Compressor
  Settings:
  - INPUT: Low (1-2 LED flicker) - gentle compression
  - RATIO: 2:1 (gentle control)
  - ATTACK: Slow (30-50ms) - preserve pick attack
  - RELEASE: Medium (250ms)
  - MIX: 80-100% (mostly compressed)
  - TONE: 12 o'clock (flat)
  - Sidechain HPF: OFF (full-range compression)
  ↓
PA-1QG EQ
  Preset 3: Throbber-specific EQ
  - Slight boost: 800Hz (+1dB), 1.5kHz (+2dB) - add presence
  - LEVEL: Unity (100)
  ↓
From Yesterday (KOT Clone) - Yellow Channel
  Settings:
  - Mode: Clean (via internal DIP switch)
  - Gain: 9 o'clock (minimal clipping)
  - Volume: 1 o'clock (slight boost)
  - Tone: 12 o'clock
  ↓
Mad Professor Sweet Honey Overdrive Deluxe
  Settings:
  - Drive: 10-11 o'clock (subtle overdrive)
  - Focus: 10 o'clock (CCW - requires harder pick attack)
  - Volume: 12 o'clock (unity)
  - Bass: 12 o'clock
  - Treble: 12 o'clock
  ↓
Tone King Imperial MKII Input
  Amp Settings:
  - Channel: Rhythm
  - Volume: 4-5 (lower volume for Jazz)
  - Treble: 6
  - Mid: 5
  - Bass: 5
  - Reverb: 4 (built-in reverb)
  ↓
[FX Loop]
  ↓
Free the Tone FT-1Y Delay
  - Delay Time: 400ms (quarter note at 150 BPM)
  - Feedback: 2 repeats
  - Mix: 20% (subtle)
  ↓
Cornerstone Nucleo Reverb (Stereo)
  - Mode: Hall
  - Blend: 25-30% (subtle room)
  - Decay: Short-medium
  ↓
[FX Return]
  ↓
Imperial MKII Output → Speaker
```

**Playing Technique:**
- Guitar Volume: 7-8 (slight reduction for clean Jazz)
- Pickup: Neck (warm, round jazz tone)
- Playing: Fingerstyle or pick (gentle attack)

**Sound Character:**
- Ultra-transparent with woody hollowbody character
- Subtle compression evens out dynamics
- Sweet Honey adds gentle warmth and sustain
- Guitar volume at 7-8 keeps tone clean
- Volume at 10 pushes into edge-of-breakup
- Extremely touch-sensitive (Focus at CCW)

**Usage Modes:**
```
Mode 1: Guitar volume 7 + only Empress MKII active
= Pure clean compressed tone

Mode 2: Guitar volume 8-9 + KOT Clean active
= Clean with slight edge

Mode 3: Guitar volume 9-10 + both KOT + Sweet Honey active
= Gentle Jazz overdrive, Wes Montgomery-style warmth
```

---

### Example 2: Neo Soul Rhythm Setup (Warm Smooth)

**Goal:** Smooth, warm, sweet Neo Soul chord tones with excellent clarity.

**Gear:**
- Guitar: Greco TE-500 (Lindy Fralin Wide Range humbuckers)
- Amp: Roland JC-22

**Signal Chain:**
```
Greco TE-500 (neck pickup)
  ↓
Empress MKII Compressor
  Settings:
  - INPUT: Medium (2-3 LED) - moderate compression
  - RATIO: 4:1 (clear control)
  - ATTACK: Medium (10-20ms) - slight transient control
  - RELEASE: Medium (200ms)
  - MIX: 70-90% (blend some dry for punch)
  - TONE: Slight CW (add brightness to balance warmth)
  - Sidechain HPF: OFF
  ↓
PA-1QG EQ
  Preset 1: Greco TE-500 specific
  - Boost: 800Hz (+2dB), 1.6kHz (+3dB), 3.2kHz (+2dB)
  - Purpose: Neo Soul sparkle and presence
  - LEVEL: Unity or +3dB
  ↓
Mad Professor Sweet Honey Overdrive Deluxe
  Settings:
  - Drive: 11-12 o'clock (Neo Soul sweet spot)
  - Focus: 1-2 o'clock (earlier breakup, slight high-freq lift)
  - Volume: 12 o'clock
  - Bass: 11 o'clock (avoid excessive warmth)
  - Treble: 1 o'clock (add sparkle)
  ↓
PRS Horsemeat
  Settings:
  - Gain: 10-11 o'clock (light additional saturation)
  - Volume: 12 o'clock
  - Voice: 11-12 o'clock (warm saturation)
  - Treble: 1-2 o'clock (balance double warmth)
  - Bass: 11 o'clock (avoid mud)
  ↓
Roland JC-22 Input
  Amp Settings:
  - Volume: 5-6
  - Bright Switch: ON (balance warmth from pedals)
  - Chorus: Speed 3-4, Depth 4-5 (moderate chorus)
  ↓
[FX Loop Stereo]
  ↓
Free the Tone FT-1Y Delay
  - Delay Time: Realtime BPM Analyzer (follow tempo)
  - Feedback: 3 repeats
  - Mix: 25-35% (noticeable but not overwhelming)
  ↓
Cornerstone Nucleo Reverb (Stereo Out)
  - Mode: Room
  - Blend: 35-50%
  - Decay: Medium
  - Voicing: Normal
  - Stereo: Both L+R outputs to JC-22 Return L+R
  ↓
[FX Return Stereo]
  ↓
JC-22 Stereo Output → Speakers (L+R)
```

**Playing Technique:**
- Guitar Volume: 9-10 (full volume for Neo Soul drive)
- Pickup: Neck or middle position (warmth)
- Playing: Chord stabs, fingerstyle, smooth lines

**Sound Character:**
- Warm, sweet, smooth Neo Soul tone
- Germanium (Horsemeat) + Vintage OD (Sweet Honey) = double warmth
- Stereo Chorus from JC-22 adds dimension
- Stereo Reverb (Nucleo) creates space
- D'Angelo / John Mayer style warm rhythm tones

**Critical Settings:**
- Treble controls at 1-2 o'clock (compensate double warmth)
- Bass controls at 11 o'clock (prevent mud)
- JC-22 Bright ON (balance pedal warmth)
- Stereo reverb for wide Neo Soul soundstage

**Usage Modes:**
```
Mode 1: Only Sweet Honey active
= Core Neo Soul warm OD

Mode 2: Sweet Honey + Horsemeat active
= Full warm Germanium + vintage OD
= D'Angelo-style thick rhythm tone

Mode 3: Bypass Horsemeat if too warm
= Sweet Honey only for lighter Neo Soul tone
```

---

### Example 3: Fusion Lead Setup (Complex Gain)

**Goal:** Rich, singing lead tone with maximum harmonic complexity and sustain.

**Gear:**
- Guitar: Fender Tokyo Thinline (Seymour Duncan SP90-1 P-90 pickups)
- Amp: Roland JC-22 or Tone King Imperial MKII

**Signal Chain:**
```
Fender Tokyo Thinline (bridge pickup)
  ↓
[NO compressor for maximum dynamics]
  ↓
PA-1QG EQ
  Preset 2: Tokyo Thinline specific
  - Slight cut: 200Hz (-1dB) - prevent P-90 thickness
  - Boost: 1.5kHz (+2dB), 3.5kHz (+3dB), 7kHz (+2dB) - clarity
  - LEVEL: Unity
  ↓
EHX Soul Food (Layer 1 - Klon Boost)
  Settings:
  - Drive: 9 o'clock (minimal clipping)
  - Volume: 2-3 o'clock (significant boost)
  - Treble: 11 o'clock (slight reduction)
  Purpose: Transparent Klon boost with mid-lift
  ↓
JHS Morning Glory V3 (Layer 2 - BB Core OD)
  Settings:
  - Gain: 11-12 o'clock (receives Soul Food boost)
  - Volume: 12-1 o'clock (push ODL-1-CS)
  - Tone: 12 o'clock
  - Bright Cut: OFF (preserve brightness)
  Purpose: Transparent BB core overdrive character
  ↓
Free the Tone ODL-1-CS (Layer 3 - Dumble Final Drive)
  Settings:
  - Channel: Drive Channel
  - Voltage: 14-15V (Custom Shop - balanced)
  - Drive: 11-1 o'clock (receives two layers of boost)
  - Mode: ROCK (for attack and punch)
  - Glass/EQ: EQ ON (Dumble tone circuit active)
  - Volume: 12 o'clock (unity)
  Purpose: Dumble harmonic richness and final saturation
  ↓
Amp Input (JC-22 or Imperial MKII)
  ↓
[FX Loop]
  ↓
Free the Tone FT-1Y Delay
  - Delay Time: Realtime BPM Analyzer
  - Feedback: 4-5 repeats
  - Mix: 30-40% (noticeable delay)
  ↓
Cornerstone Nucleo Reverb
  - Mode: Hall
  - Blend: 40-50%
  - Decay: Medium-long
  ↓
[FX Return]
  ↓
Amp Output
```

**Playing Technique:**
- Guitar Volume: Start at 7-8 (clean-ish)
- Dynamic playing: Use guitar volume for clean-to-lead gradient
- Pickup: Bridge (bright P-90 for cutting lead)

**Sound Character:**
- Complex three-layer gain structure
- Klon mid-boost → BB transparency → Dumble richness
- Maximum harmonic complexity
- Singing sustain with clarity
- Larry Carlton / Robben Ford style Fusion tone

**Gain Staging Analysis:**
```
Soul Food:      +8dB (Klon boost)
Morning Glory:  +10dB (receives +8dB, pushed harder)
ODL-1-CS:       +15dB (receives +18dB, massive push into Dumble sweet spot)
Total Gain:     +33dB (controlled, progressive)

Compression:
Soul Food:      5% (very low)
Morning Glory:  5% (very low)
ODL-1-CS:       15% (Dumble-style)
Total:          ~23% (healthy range, maintains dynamics)
```

**Usage Modes:**
```
Mode 1: Guitar vol 7 + only Soul Food active
= Clean Klon boost with sparkle

Mode 2: Guitar vol 8 + Soul Food + Morning Glory active
= Classic Klon → BB medium overdrive

Mode 3: Guitar vol 9-10 + all three active
= Full Fusion lead tone
= Maximum harmonic complexity and sustain

Dynamic swells:
- Start: Guitar vol 5 (clean)
- Swell: Increase guitar vol to 10 (full saturation)
- Result: Smooth clean-to-lead gradient
```

**ODL-1-CS Voltage Experiment:**
```
Try different voltages for different lead characters:

14V (Standard):
- Balanced, warm Dumble tone
- Good for most Fusion applications

15-16V (Higher):
- More headroom, cleaner
- Hi-fi Fusion tone (Scott Henderson style)

12-13V (Lower):
- Earlier breakup, more saturated
- Vintage Dumble character (Larry Carlton style)
```

---

## Conclusion

### Key Takeaways

**1. Understand Circuit Families:**
- Bluesbreaker = Transparent, open
- Klon = Mid-boost, sparkle
- Tube Screamer = Mid-focused, vocal
- Dumble = Rich harmonics, complex
- Amp-in-a-Box = Amp simulation

**2. Follow Stacking Principles:**
- Transparent + Colored = Best pairing
- Low Gain + High Gain = Optimal push
- Complementary Frequencies = Full spectrum
- Progressive Gain Staging = Controlled saturation
- Maintain Dynamics = <30% total compression

**3. Frequency Matters:**
- Pair neutral with colored pedals
- Avoid double mid-hump (TS + BB thick mids)
- Avoid double warmth (unless rig is bright)
- Use EQ to compensate frequency issues

**4. Order Matters:**
- Transparent before colored
- Boost before drive
- Amp-in-a-box: First (tone shaper) or Last (amp sim)

**5. Genre-Specific Optimization:**
- Jazz: Ultra-transparent, low compression
- Neo Soul: Warm, smooth, Focus control
- Funk: Compressed, bright, mid-boost
- Blues: Vocal, Klon+BB classic
- Fusion: Complex three-layer gain
- Post Rock: Dynamic, warm, sustain

**6. Common Mistakes to Avoid:**
- Over-compression (>30%)
- Frequency masking (double mid-hump)
- Wrong pedal order
- All pedals at medium-high gain
- Ignoring guitar volume knob interaction

**7. Your Specific Pedals (Best Combinations):**

**Two-Pedal:**
1. Morning Glory → Sweet Honey (48/50) - Neo Soul, Jazz
2. Soul Food → Morning Glory (47/50) - Blues, Rock
3. Horsemeat → Sweet Honey (47/50) - Warm Neo Soul
4. Morning Glory → TWA Source Code (45/50) - Classic Rock

**Three-Pedal:**
1. Soul Food → Morning Glory → ODL-1-CS (47/50) - Fusion
2. Horsemeat → Sweet Honey → Blacklon (46/50) - Neo Soul
3. Morning Glory → TWA → ODL-1-CS (45/50) - Rock/Fusion

**8. V3.0 Configuration Assessment:**

**Loop 1:** Sweet Honey → Horsemeat ⭐⭐⭐⭐⭐ (47/50)
- Perfect for Jazz/Neo Soul/Funk
- Warm, smooth, dynamic

**Loop 2:** Morning Glory → TWA → ODL-1-CS ⭐⭐⭐⭐⭐ (45/50)
- Perfect for Post Rock/Fusion/Classic Rock
- Complex, versatile, punchy

---

### Experimentation Encouragement

These principles provide a strong foundation, but **experimentation is key:**

1. **Try Different Orders:** Sometimes "wrong" order sounds right for your rig
2. **Adjust for Your Gear:** Guitar/amp combination affects ideal settings
3. **Use Your Ears:** Theory guides, but your ears decide
4. **Document Your Settings:** Write down settings that work
5. **Revisit Periodically:** Your preferences may change over time

**Trust Your Ears Above All Theory.**

---

**Document Version:** 1.0
**Last Updated:** 2026-01-06
**Category:** Tone Theory Research - Overdrive Stacking
**Related Documents:**
- `gain_distortion_types.md` - Gain types overview (OD vs Dist vs Fuzz)
- `compression_theory_and_application.md` - Compressor theory
- `signal_processing_math_models.md` - DSP mathematics

**Source Material:**
- `overdrive_pedals_technical_data.md` - 10 pedal technical database
- `overdrive_stacking_analysis.md` - Combination analysis report

**References:**
- Premier Guitar: Pedal stacking techniques
- That Pedal Show: Gain stacking episodes
- JHS Show: Overdrive history and circuits
- The Gear Page: Community knowledge base
- Professional guitar tech interviews
- Equipment manufacturer technical documentation

---

**願這份理論文件幫助你建立完美的 Overdrive 疊加組合！** 🎸🎛️
