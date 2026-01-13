# Compression Theory & Application: Comprehensive Guide

**Document Type:** Tone Theory Research
**Version:** 1.0
**Created:** 2026-01-06
**Category:** Dynamic Processing Fundamentals
**Purpose:** Understanding compressor types, controls, signal chain placement, and practical application for guitar signal processing

---

## Table of Contents

1. [Compression Fundamentals](#compression-fundamentals)
2. [Compressor Types](#compressor-types)
3. [Control Parameters Deep Dive](#control-parameters-deep-dive)
4. [Signal Chain Positioning](#signal-chain-positioning)
5. [Compressor Applications by Genre](#compressor-applications-by-genre)
6. [Stacking with Gain Effects](#stacking-with-gain-effects)
7. [Common Mistakes and Solutions](#common-mistakes-and-solutions)
8. [Parallel Compression Technique](#parallel-compression-technique)
9. [Comparison Tables](#comparison-tables)
10. [Mathematical Models](#mathematical-models)

---

## Compression Fundamentals

### What is Compression?

**Compression** is a dynamic range processor that reduces the difference between the loudest and quietest parts of an audio signal. It automatically lowers the volume of loud sounds (peaks) that exceed a set threshold, creating a more consistent output level.

### Core Concept

```
Loud Signal Peak → [Compressor] → Reduced Peak (Compressed)
Quiet Signal     → [Compressor] → Unchanged or Slightly Boosted

Result: More consistent, controlled dynamic range
```

### Why Use Compression for Guitar?

1. **Sustain Enhancement**
   - Extends note decay
   - Creates singing lead tones
   - Improves legato playing

2. **Dynamic Control**
   - Evens out picking dynamics
   - Reduces volume spikes
   - Improves consistency in band mix

3. **Tone Shaping**
   - Adds warmth and character (colored compressors)
   - Enhances harmonics
   - Increases perceived thickness

4. **Clean Tone Definition**
   - Brings out articulation
   - Enhances fingerpicking clarity
   - Improves chord definition

5. **Gain Pedal Enhancement**
   - Controls input to overdrive pedals
   - Prevents flubby bass response
   - Smooths out gain transitions

### Basic Compression Behavior

**Input vs Output Relationship:**

```
Without Compression:
Input:  |-------|  |--|  |--------|  |---|
Output: |-------|  |--|  |--------|  |---|
        (loud)    (quiet)  (loud)    (quiet)

With Compression (4:1 ratio):
Input:  |-------|  |--|  |--------|  |---|
Output: |-----|    |--|  |------|    |---|
        (reduced)  (same) (reduced)  (same)

Result: More consistent output level
```

---

## Compressor Types

### 1. FET Compressor (Field-Effect Transistor)

**Circuit Type:** Solid-state FET transistor-based

**Technical Characteristics:**
- Very fast attack time (microseconds)
- Transparent to moderately colored
- Precise, punchy compression
- Solid-state circuitry

**Tone Character:**
- Modern, clean compression
- Fast transient response
- Can add subtle warmth (depending on design)
- Excellent for percussive playing

**Famous Units:**
- Studio: UREI 1176, Empirical Labs Distressor
- Pedals: Origin Effects Cali76 FET, Empress MKII, Keeley Compressor Plus

**Best For:**
- Clean guitar tones
- Funk rhythm (tight, fast attack)
- Percussive fingerpicking
- Jazz (transparent control)
- Neo Soul (when transparency is needed)

**Guitar Pedal Examples from Your Collection:**
- **Origin Effects Cali76 FET** - 1176-style with warmth, 10-LED meter
- **Empress MKII** - Ultra-transparent FET with Tilt EQ, Sidechain HPF

**Impedance Characteristics:**
- Not impedance-sensitive
- Can be placed anywhere in signal chain
- Usually buffered bypass

---

### 2. Optical Compressor (Opto)

**Circuit Type:** Photo-resistor and light source (LED/lamp)

**Technical Characteristics:**
- Slower attack time (natural lag)
- Very smooth, gentle compression
- Program-dependent behavior
- Analog optical circuit

**How it Works:**
```
Input Signal → LED brightness → Photo-resistor → Gain Reduction
(louder = brighter LED = lower resistance = more compression)
```

**Tone Character:**
- Smooth, musical, transparent
- Gentle, unobtrusive compression
- Natural-sounding dynamics
- "Invisible" compression

**Famous Units:**
- Studio: Teletronix LA-2A, LA-3A
- Pedals: Demeter Compulator, Diamond Compressor, JHS Pulp 'N' Peel

**Best For:**
- Vocals and bass (originally designed for)
- Smooth lead guitar
- Blues (natural feel)
- Country (gentle control)
- Ballads (transparent sustain)

**Attack/Release Behavior:**
- Attack: 10-60ms (naturally slow)
- Release: Program-dependent (automatically adjusts to signal)

**Impedance Characteristics:**
- Not impedance-sensitive
- Can be placed anywhere
- Usually true bypass or buffered

---

### 3. VCA Compressor (Voltage-Controlled Amplifier)

**Circuit Type:** Integrated circuit VCA chip

**Technical Characteristics:**
- Adjustable attack/release times
- Very flexible control
- Clean, precise compression
- Modern solid-state

**Tone Character:**
- Clean, transparent, versatile
- Precise control over dynamics
- Can be punchy or smooth (depending on settings)
- Neutral tonal character

**Famous Units:**
- Studio: SSL Bus Compressor, API 2500, DBX 160
- Pedals: Wampler Ego Compressor, MXR Dyna Comp (VCA-style)

**Best For:**
- Studio recording
- Versatile applications
- When you need precise control
- Modern production styles

**Impedance Characteristics:**
- Not impedance-sensitive
- Flexible placement

---

### 4. Tube Compressor (Valve)

**Circuit Type:** Vacuum tube-based

**Technical Characteristics:**
- Smooth, musical compression
- Natural harmonic saturation
- Warm, vintage character
- Requires tube maintenance

**Tone Character:**
- Warm, rich, colored
- Adds even-order harmonics
- Smooth saturation
- Vintage vibe

**Famous Units:**
- Studio: Fairchild 670, Manley Variable Mu
- Pedals: Effectrode PC-2A, Demeter HBC-1

**Best For:**
- Vintage tones
- Blues, jazz, classic rock
- When you want added warmth
- Colored compression character

**Impedance Characteristics:**
- May be impedance-sensitive (vintage designs)
- Check documentation

---

### 5. Multiband Compressor

**Circuit Type:** Splits signal into frequency bands, compresses separately

**Technical Characteristics:**
- Independent compression per frequency band
- Complex control
- Precise frequency-specific dynamics
- Usually digital

**Tone Character:**
- Very transparent (when set correctly)
- Prevents frequency masking
- Can fix specific frequency issues

**Best For:**
- Studio mixing
- Complex signal processing
- Bass guitar (control low-end separately)
- Advanced users

**Note:** Rarely used in guitar pedals (too complex for stage use)

---

## Control Parameters Deep Dive

### 1. Threshold

**Definition:** The signal level at which compression begins to engage.

**Range:** Typically measured in dB (e.g., -40dB to 0dB) or relative control (1-10)

**How it Works:**
```
Signal below threshold → No compression
Signal above threshold → Compression engages

Example (Threshold = -20dB):
-30dB signal → No compression
-10dB signal → Compressed (10dB over threshold)
```

**Practical Settings:**

| Setting | Effect | Use Case |
|---------|--------|----------|
| **High Threshold** (near 0dB) | Only compresses loudest peaks | Gentle, transparent control |
| **Medium Threshold** (-20 to -10dB) | Compresses normal playing | General purpose |
| **Low Threshold** (-40 to -30dB) | Compresses almost everything | Heavy sustain, leveling |

**Guitar Application:**
- **Clean tones:** Medium-high threshold (transparent)
- **Lead tones:** Lower threshold (more sustain)
- **Rhythm:** Medium threshold (consistency)

**Common Pedal Designs:**
- Some pedals have **fixed threshold** (e.g., Cali76 FET)
- Control compression amount via **INPUT knob** instead
- Higher input = more signal above threshold = more compression

---

### 2. Ratio

**Definition:** The amount of gain reduction applied to signals above the threshold.

**How it Works:**
```
Ratio = Input increase : Output increase (above threshold)

Example (4:1 ratio):
- Input increases by 4dB above threshold
- Output only increases by 1dB
- Result: 3dB of gain reduction
```

**Common Ratios:**

| Ratio | Type | Effect | Use Case |
|-------|------|--------|----------|
| **1:1** | No compression | No effect | Bypass |
| **2:1** | Gentle | Subtle leveling | Jazz, light control |
| **3:1** | Mild | Noticeable control | Blues, clean tones |
| **4:1** | Moderate | Clear compression | Rock, funk, general use |
| **6:1** | Heavy | Strong leveling | Lead guitar, heavy funk |
| **8:1** | Aggressive | Very compressed | Extreme sustain |
| **10:1+** | Limiting | Brick wall limiting | Peak protection |
| **∞:1** | Hard Limiting | Absolute ceiling | No signal exceeds threshold |

**Musical Examples:**

**Jazz Clean (2:1):**
- Transparent dynamic control
- Preserves playing nuance
- Prevents occasional loud notes

**Neo Soul Rhythm (4:1):**
- Balanced compression
- Evens out chord stabs
- Maintains groove consistency

**Funk Rhythm (6:1):**
- Tight, percussive compression
- Consistent chop rhythm
- Punchy attack

**Post Rock Lead (8:1+):**
- Massive sustain
- Singing lead tones
- Violin-like decay

---

### 3. Attack Time

**Definition:** How quickly the compressor reacts after the signal exceeds the threshold.

**Range:** Microseconds (μs) to hundreds of milliseconds (ms)

**How it Works:**
```
Signal Peak → [Attack Time] → Full Compression Engaged

Fast Attack (0.1-10ms):
Peak →|← [Compression hits immediately]

Slow Attack (50-200ms):
Peak →|         [Compression gradually engages]
```

**Attack Time Settings:**

| Attack | Effect | Tone Character | Use Case |
|--------|--------|----------------|----------|
| **Very Fast** (0.1-1ms) | Catches all transients | Squashed, tight | Funk rhythm, heavy leveling |
| **Fast** (1-10ms) | Catches most transients | Controlled, punchy | General purpose, clean tones |
| **Medium** (10-30ms) | Some transients pass | Natural feel | Blues, classic rock |
| **Slow** (30-100ms) | Initial pick attack passes | Transparent, dynamic | Jazz, fingerstyle, preserves attack |
| **Very Slow** (100ms+) | Almost all transient passes | Very natural | Light sustain, gentle leveling |

**Guitar Pick Attack Timing:**
- Guitar pick attack: ~5-20ms
- Fast attack (1ms): Completely controls pick attack
- Medium attack (10ms): Partial control
- Slow attack (50ms): Lets pick attack through

**Practical Examples:**

**Clean Jazz (Slow Attack - 30-50ms):**
```
Original: |▲------|  (sharp pick attack, natural decay)
Compressed: |▲------|  (pick attack preserved, tail sustained)
Effect: Natural attack, gentle sustain enhancement
```

**Funk Rhythm (Fast Attack - 1-5ms):**
```
Original: |▲--|  |▲--|  |▲--|  |▲--|
Compressed: |█-|  |█-|  |█-|  |█-|
Effect: Tight, percussive, consistent level
```

**Post Rock Lead (Medium Attack - 10-20ms):**
```
Original: |▲------------|  (strong attack, long decay)
Compressed: |▲========|  (slight attack, massive sustain)
Effect: Balanced attack, singing sustain
```

---

### 4. Release Time

**Definition:** How quickly the compressor stops compressing after the signal drops below the threshold.

**Range:** Milliseconds (ms) to seconds (s)

**How it Works:**
```
Signal drops below threshold → [Release Time] → Compression disengages

Fast Release (10-50ms):
Signal ↓ →|← [Compression releases quickly]

Slow Release (500ms-2s):
Signal ↓ →|                    [Compression slowly releases]
```

**Release Time Settings:**

| Release | Effect | Tone Character | Use Case |
|---------|--------|----------------|----------|
| **Very Fast** (10-50ms) | Quick recovery | Responsive, dynamic | Fast playing, funk chops |
| **Fast** (50-150ms) | Normal recovery | Natural feel | General purpose |
| **Medium** (150-500ms) | Gradual recovery | Smooth sustain | Blues, rock leads |
| **Slow** (500ms-1s) | Slow recovery | Long sustain | Ballads, post rock |
| **Very Slow** (1-3s) | Very slow recovery | Extreme sustain | Ambient, drone |
| **Auto** | Program-dependent | Adaptive | Versatile, musical |

**Release Time Interaction with Music:**

**Fast Release (50ms) - Funk Rhythm:**
```
Note: |▲-----|     |▲-----|     |▲-----|
Comp: |█---|       |█---|       |█---|
      ↑ Compression releases before next note
Effect: Each note compressed independently
```

**Slow Release (1s) - Post Rock:**
```
Note: |▲------------|               (single sustained note)
Comp: |▲===================|        (compression holds throughout)
      ↑ Compression maintains sustain
Effect: Long, singing sustain
```

**Medium Release (200ms) - Blues:**
```
Note: |▲--------|  |▲--------|
Comp: |▲======|    |▲======|
Effect: Natural feel, controlled sustain
```

---

### 5. Knee

**Definition:** The transition curve between uncompressed and compressed signal.

**Types:**

#### Hard Knee
```
         Compressed
        /
       /  ← Sharp transition
      /
-----+----------- Threshold
     Uncompressed
```

**Characteristics:**
- Sharp, abrupt transition
- Obvious compression effect
- More aggressive control
- Better for heavy compression

**Use Cases:**
- Funk rhythm (tight control)
- Limiting (peak protection)
- Heavy sustain

#### Soft Knee
```
         Compressed
        /
       /   ← Gradual curve
      /
-----)----------- Threshold
    Uncompressed
```

**Characteristics:**
- Smooth, gradual transition
- Subtle compression effect
- Musical, natural sound
- Less obvious compression

**Use Cases:**
- Jazz, blues (transparent)
- Vocals, acoustic guitar
- Gentle leveling

**Guitar Application:**
- Most guitar compressor pedals use **soft knee** (more musical)
- Some pedals offer switchable knee (e.g., Wampler Ego)

---

### 6. Makeup Gain / Output Level

**Definition:** Post-compression gain to restore or boost the overall output level.

**Why Needed:**
- Compression reduces signal level
- Makeup gain compensates for volume loss
- Allows comparison of bypassed vs compressed signal at equal volume

**Setting Makeup Gain:**

**Proper Method:**
1. Set compression parameters (Threshold, Ratio, Attack, Release)
2. Play guitar at normal intensity
3. Observe gain reduction meter (how many dB reduced)
4. Increase makeup gain to compensate
5. **Unity Gain:** Compressed signal = same volume as bypassed signal

**Unity Gain Formula:**
```
Makeup Gain (dB) ≈ Average Gain Reduction (dB)

Example:
- Compressor reduces signal by 6dB on average
- Set Makeup Gain to +6dB
- Result: Unity gain (bypassed = same volume as compressed)
```

**Beyond Unity Gain:**
- **Boost Mode:** Makeup Gain > Gain Reduction
- Use compressor as clean boost with compression
- Common in overdrive stacking (compressed signal pushes OD harder)

**Example Settings:**

**Transparent Control (Unity Gain):**
- Gain Reduction: 3dB
- Makeup Gain: +3dB
- Result: Same volume, controlled dynamics

**Boost Mode:**
- Gain Reduction: 3dB
- Makeup Gain: +6dB
- Result: +3dB boost with compression

---

### 7. Mix / Blend (Parallel Compression)

**Definition:** Blends compressed signal with uncompressed (dry) signal.

**How it Works:**
```
Input Signal → [Split] → [Compressor] → [Mix Control] → Output
                   ↓                           ↑
                   └──[Dry Signal]───────────┘

Mix = 100%: Fully compressed signal
Mix = 50%: Half compressed, half dry
Mix = 0%: Fully dry (bypass)
```

**Benefits of Parallel Compression:**
1. **Preserves Transients**
   - Dry signal retains pick attack
   - Compressed signal adds sustain
   - Result: Punchy attack + long sustain

2. **Natural Sound**
   - Less obvious compression effect
   - More dynamic than full compression
   - Best of both worlds

3. **Heavy Compression without Over-Squashing**
   - Can use aggressive compression (8:1 ratio)
   - Blend back dry signal for natural feel

**Practical Settings:**

**New York Style Compression (Heavy + Blend):**
- Ratio: 6:1 to 10:1 (aggressive)
- Attack: Fast (1-5ms)
- Release: Medium (200ms)
- **Mix: 30-50%** (blend heavily compressed with dry)
- Result: Massive sustain without losing attack

**Transparent Sustain:**
- Ratio: 4:1
- Attack: Medium (10ms)
- Release: Medium (200ms)
- **Mix: 60-80%**
- Result: Controlled but natural

**Pedal Examples with Mix Control:**
- **Origin Effects Cali76 FET** - DRY knob (parallel compression)
- **Empress MKII** - MIX knob
- **Keeley Compressor Plus** - Blend knob

---

### 8. Sidechain Filter (High-Pass Filter)

**Definition:** Applies a filter to the detection circuit (not the audio path), making the compressor less sensitive to low frequencies.

**How it Works:**
```
Input Signal → [Split] → [Audio Path] → Output
                   ↓
              [Sidechain HPF] → [Detection Circuit]
              (Filter out low freq)  (Trigger compression)
```

**Purpose:**
- Prevents bass frequencies from triggering excessive compression
- Maintains low-end punch
- Especially important for bass guitar

**Without Sidechain HPF:**
```
Low E string (82Hz) → Triggers heavy compression → Thin sound
High E string (330Hz) → Less compression → Uneven response
```

**With Sidechain HPF (120Hz):**
```
Low E string (82Hz) → Filtered out of detection → Punchy bass
High E string (330Hz) → Triggers compression → Even response
```

**Typical Settings:**
- **OFF:** Full-range compression (all frequencies trigger equally)
- **120Hz:** For 6-string guitar (filters out low E)
- **240Hz:** For bass guitar or very heavy low-tuned guitars

**Pedal Example:**
- **Empress MKII** - Sidechain HPF (OFF / 120Hz / 240Hz)

**Use Cases:**
- Bass-heavy guitar tones (low-tuned, humbuckers)
- Semi-hollow/hollow body guitars (prevent bass resonance from over-compressing)
- Bass guitar (essential for maintaining low-end punch)

---

### 9. Tilt EQ (Tone Shaping)

**Definition:** A single-control EQ that tilts the frequency response around a center frequency.

**How it Works:**
```
Center Frequency: 500Hz

Clockwise (Brighter):
    High Freq ↑
         /
        /
-------+-------- 500Hz
      /
Low Freq ↓

Counter-Clockwise (Warmer):
    High Freq ↓
         \
          \
-----------+---- 500Hz
            \
          Low Freq ↑
```

**Practical Application:**

**Brighten Dark Guitar:**
- Tilt: Clockwise (1-2 o'clock)
- Boosts highs, cuts lows
- Adds clarity and presence

**Warm Up Bright Guitar:**
- Tilt: Counter-clockwise (10-11 o'clock)
- Boosts lows, cuts highs
- Adds warmth and body

**Neutral:**
- Tilt: 12 o'clock (center detent)
- Flat response

**Pedal Example:**
- **Empress MKII** - Tilt Tone EQ (500Hz center)

---

## Signal Chain Positioning

### Compressor Placement Options

Compressor can be placed in multiple positions, each with different effects:

#### Position 1: Very First (After Guitar)

```
Guitar → Compressor → [Rest of Chain] → Amp
```

**Effect:**
- Controls raw guitar signal
- Most transparent compression
- Preserves guitar's natural tone

**Best For:**
- Clean tones
- Jazz, neo soul, fingerstyle
- When you want transparent control

**Considerations:**
- All downstream effects receive compressed signal
- May reduce effectiveness of touch-sensitive effects (wah, fuzz)

---

#### Position 2: After Wah/Filter (Before Gain)

```
Guitar → Wah → Compressor → Overdrive → [Rest] → Amp
```

**Effect:**
- Wah remains dynamic
- Compressor feeds consistent level to overdrive
- Better overdrive response

**Best For:**
- Blues, funk (wah + compression)
- Controlled overdrive input
- Dynamic wah + consistent OD

**Considerations:**
- Wah still has full dynamic range
- Overdrive receives compressed signal (more consistent)

---

#### Position 3: After Gain Pedals

```
Guitar → Overdrive → Distortion → Compressor → [Rest] → Amp
```

**Effect:**
- Compressor smooths out gain pedal output
- Evens out distortion dynamics
- Adds sustain to overdrive

**Best For:**
- Heavy gain tones
- Lead guitar (post-gain sustain)
- Taming aggressive distortion

**Considerations:**
- Gain pedals push compressor harder
- Can sound over-compressed if not careful
- May reduce gain pedal dynamics

---

#### Position 4: In Effects Loop (After Preamp)

```
Guitar → [Preamp Effects] → Amp Input
                              ↓
                         Amp Preamp
                              ↓
                         FX Send → Compressor → [Modulation] → [Delay] → [Reverb] → FX Return
```

**Effect:**
- Compressor after amp's preamp distortion
- Controls amp's output dynamics
- Adds sustain to amp-generated distortion

**Best For:**
- High-gain amp users
- When amp provides main distortion
- Studio-style compression on final tone

**Considerations:**
- Works well with modulation/delay/reverb
- Requires 4-Cable Method
- Both amps (Imperial MKII, JC-22) support this

---

### Position Strategy by Goal

**Goal: Transparent Clean Control**
```
Guitar → Compressor (Transparent FET) → EQ → [Rest] → Amp
Example: Empress MKII first
```

**Goal: Enhanced Overdrive Response**
```
Guitar → Compressor → Overdrive → [Rest] → Amp
Example: Light compression → Controlled OD input
```

**Goal: Maximum Sustain**
```
Guitar → Overdrive → Compressor (High Ratio) → [Rest] → Amp
Example: OD → Empress MKII or Cali76 (high ratio)
```

**Goal: Smooth High-Gain Tones**
```
Guitar → [Gain Pedals] → Compressor → Modulation → Delay → Reverb → Amp
Example: ODL-1-CS → Cali76 FET
```

**Goal: Funk Tightness**
```
Guitar → Compressor (Fast Attack) → Overdrive (Low Gain) → Amp
Example: Empress MKII (fast attack, 4:1) → From Yesterday (Yellow Clean)
```

---

### Your Specific Pedalboard Positioning

Based on your equipment and musical styles:

#### Recommendation 1: Empress MKII First (Jazz/Neo Soul/Funk)

```
Guitar → Empress MKII → PA-1QG → From Yesterday → Sweet Honey → Soul Food → Amp
         (transparent)   (EQ)     (transparent)    (warm)        (boost)
```

**Why:**
- Empress ultra-transparent for clean tones
- Controls dynamics before gain stages
- Preserves guitar's natural character
- Perfect for Jazz, Neo Soul, Funk

**Settings:**
- INPUT: Low (1-2 LED)
- RATIO: 2:1 or 4:1
- ATTACK: Medium to Slow
- RELEASE: Medium
- MIX: 80-100%
- TONE: 12 o'clock (flat)

---

#### Recommendation 2: Cali76 FET After Gain (Post Rock/Fusion)

```
Guitar → [Gain Pedals] → Cali76 FET → GE-7 → [Modulation] → [Delay/Reverb] → Amp
         (OD/Distortion)   (sustain)    (boost)
```

**Why:**
- Adds sustain to driven tones
- 1176-style warmth enhances gain
- Perfect for Post Rock singing leads
- Smooths out distortion dynamics

**Settings:**
- IN: Medium
- OUT: High (makeup gain + boost)
- ATTACK: Fast to Medium
- RELEASE: Medium to Slow
- RATIO: 4:1 or All (1176 style)
- DRY: 70-80% (parallel compression)

---

#### Recommendation 3: Dual Compressor Setup

```
Signal Chain 1 (Clean-focused):
Guitar → Empress MKII → PA-1QG → [Clean OD] → [Amp/Loop] → FT-1Y → Nucleo

Signal Chain 2 (Driven-focused):
Guitar → Cali76 FET → GE-7 → [Heavy Gain] → [Amp/Loop] → AASB → Nucleo
```

**Why:**
- Empress for clean tones (transparent)
- Cali76 for driven tones (colored, sustain)
- Each compressor optimized for different use case

**Switching:**
- Use Swiss Things or Lehle switcher
- Or manually swap pedals between chains

---

## Compressor Applications by Genre

### Jazz

**Compressor Type:** Transparent (Optical, FET)

**Goal:** Gentle dynamic control, preserve articulation

**Recommended Settings:**
- Ratio: **2:1 to 3:1** (gentle)
- Attack: **Slow** (30-50ms) - Preserve pick attack
- Release: **Medium** (200-400ms)
- Threshold: **High** (only compress peaks)
- Mix: **80-100%** (mostly compressed)

**Recommended Pedal:**
- **Empress MKII** (ultra-transparent)

**Signal Chain:**
```
Guitar (Throbber PAF) → Empress MKII → PA-1QG → Sweet Honey (low gain) → Imperial MKII
```

**Use Case:**
- Wes Montgomery-style warm jazz
- Comping (even chord levels)
- Lead lines (gentle sustain)

---

### Neo Soul

**Compressor Type:** Transparent to Lightly Colored (FET)

**Goal:** Smooth, controlled dynamics with warmth

**Recommended Settings:**
- Ratio: **4:1** (moderate)
- Attack: **Medium** (10-20ms)
- Release: **Medium** (150-300ms)
- Threshold: **Medium** (compress normal playing)
- Mix: **70-90%**
- Tilt EQ: Slight boost highs (clarity)

**Recommended Pedal:**
- **Empress MKII** with Tilt EQ

**Signal Chain:**
```
Guitar (Greco TE-500) → Empress MKII → PA-1QG → Sweet Honey → Soul Food → JC-22
```

**Use Case:**
- Smooth rhythm chords
- Controlled chord stabs
- D'Angelo/John Mayer-style tones

---

### Funk

**Compressor Type:** Fast FET

**Goal:** Tight, percussive, consistent level

**Recommended Settings:**
- Ratio: **4:1 to 6:1** (strong)
- Attack: **Fast** (1-5ms) - Catch all transients
- Release: **Fast** (50-100ms) - Quick recovery
- Threshold: **Low to Medium** (compress most of signal)
- Mix: **100%** (full compression)
- Sidechain HPF: **120Hz** (preserve bass punch)

**Recommended Pedal:**
- **Empress MKII** (fast attack, Sidechain HPF)

**Signal Chain:**
```
Guitar (Greco TE-500 Bridge) → Empress MKII → PA-1QG → From Yesterday (Clean) → JC-22
```

**Use Case:**
- Tight rhythm chops
- Nile Rodgers-style comping
- Percussive single-note lines

---

### Blues

**Compressor Type:** Optical or Light FET

**Goal:** Natural feel, gentle sustain enhancement

**Recommended Settings:**
- Ratio: **3:1 to 4:1** (moderate)
- Attack: **Medium to Slow** (20-40ms) - Natural attack
- Release: **Medium** (200-400ms)
- Threshold: **Medium** (subtle control)
- Mix: **70-90%**

**Recommended Pedal:**
- **Empress MKII** (transparent)
- Or Optical compressor (if available)

**Signal Chain:**
```
Guitar → Compressor → Overdrive (Bluesbreaker) → Amp
```

**Use Case:**
- SRV-style lead tones
- Controlled bend sustain
- Even rhythm playing

---

### Post Rock / Ambient

**Compressor Type:** Colored FET (sustain-focused)

**Goal:** Massive sustain, singing lead tones

**Recommended Settings:**
- Ratio: **6:1 to 10:1** (heavy)
- Attack: **Medium** (10-20ms) - Slight attack, then sustain
- Release: **Slow** (500ms-1s) - Long sustain
- Threshold: **Low** (compress everything)
- DRY Mix: **70-80%** (parallel compression for punch)

**Recommended Pedal:**
- **Cali76 FET** (1176-style, warmth, sustain)

**Signal Chain:**
```
Guitar (ESP EC-CTM) → Cali76 FET → Blacklon → Colosseum → [Amp] → AASB → Nucleo
```

**Use Case:**
- Explosions in the Sky-style leads
- Ambient swells
- Infinite sustain pads (with reverb)

---

### Fusion

**Compressor Type:** Transparent to Colored (depending on style)

**Goal:** Controlled dynamics for fast playing, smooth legato

**Recommended Settings:**
- Ratio: **4:1 to 6:1** (moderate to strong)
- Attack: **Fast to Medium** (5-15ms)
- Release: **Medium** (150-300ms)
- Threshold: **Medium**
- Mix: **80-100%**

**Recommended Pedal:**
- **Empress MKII** (Larry Carlton transparency)
- **Cali76 FET** (Robben Ford warmth)

**Signal Chain:**
```
Guitar → Compressor → Free the Tone ODL-1-CS (Dumble) → JC-22
```

**Use Case:**
- Fast alternate picking (even note levels)
- Smooth legato runs
- Larry Carlton / Robben Ford tones

---

### Classic Rock

**Compressor Type:** Optional (many classic rockers don't use compressor)

**Goal:** Slight sustain boost, control peaks

**Recommended Settings:**
- Ratio: **3:1 to 4:1** (gentle to moderate)
- Attack: **Medium** (15-30ms)
- Release: **Medium** (200-400ms)
- Threshold: **High** (only loud peaks)
- Mix: **60-80%** (blend for natural feel)

**Recommended Pedal:**
- **Cali76 FET** (warmth)

**Signal Chain:**
```
Guitar → Cali76 FET → Blacklon/Colosseum → Imperial MKII Lead
```

**Use Case:**
- Classic rock lead sustain (Page, Gilmour)
- Control tube amp dynamics
- Smooth out crunch tones

---

## Stacking with Gain Effects

### Compressor BEFORE Overdrive

**Signal Flow:**
```
Guitar → Compressor → Overdrive → Amp
```

**Effect:**
- Compressor feeds consistent level to overdrive
- Overdrive receives even dynamics (more predictable)
- Reduces input sensitivity of overdrive

**Pros:**
- Controlled, consistent overdrive response
- Prevents overdrive from farting out (low notes)
- Smooth, even distortion

**Cons:**
- May reduce touch sensitivity
- Less dynamic feel

**Best For:**
- Funk rhythm (consistent OD level)
- Clean boost into OD
- Controlled crunch

**Example:**
```
Greco TE-500 → Empress MKII → Soul Food (Boost) → From Yesterday (OD) → JC-22
```

---

### Compressor AFTER Overdrive

**Signal Flow:**
```
Guitar → Overdrive → Compressor → Amp
```

**Effect:**
- Overdrive has full dynamic range
- Compressor smooths out overdrive output
- Adds sustain to already-distorted signal

**Pros:**
- Maximum sustain
- Smooth out aggressive overdrive
- Singing lead tones

**Cons:**
- May sound over-compressed
- Can squash overdrive dynamics

**Best For:**
- Post rock leads (massive sustain)
- Smooth high-gain tones
- Singing solos

**Example:**
```
ESP EC-CTM → Blacklon → Colosseum → Cali76 FET → Amp
```

---

### Compressor BETWEEN Gain Stages

**Signal Flow:**
```
Guitar → Light Overdrive → Compressor → Heavy Overdrive → Amp
```

**Effect:**
- First OD adds some grit
- Compressor controls dynamics
- Second OD adds more saturation to compressed signal

**Pros:**
- Complex gain stacking
- Controlled but dynamic
- Versatile

**Cons:**
- Complex to dial in
- Many variables to manage

**Best For:**
- Advanced users
- Complex tone shaping
- Specific applications

**Example:**
```
Guitar → From Yesterday (Yellow Low Gain) → Empress MKII → Free the Tone ODL-1-CS (Drive) → Amp
```

---

### Parallel Compression with Gain (New York Style)

**Signal Flow:**
```
Guitar → Overdrive → Compressor (Heavy + Mix 30-50%) → Amp
                         ↓
                    [Heavy comp] + [Dry signal] = Punchy + Sustained
```

**Effect:**
- Heavily compressed signal (6:1 to 10:1)
- Blended with dry signal (MIX knob)
- Result: Punchy attack + massive sustain

**Pros:**
- Best of both worlds (punch + sustain)
- Heavy compression without squashing
- Very musical

**Cons:**
- Requires compressor with Mix/Blend control

**Best For:**
- Rock leads
- Post rock (Explosions in the Sky)
- Controlled but dynamic high-gain

**Example:**
```
ESP EC-CTM → Colosseum (Klon+BB) → Cali76 FET (Ratio:All, DRY:70%) → Amp
                                     (Heavy comp,  parallel mix)
```

---

### Double Compressor (Serial)

**Signal Flow:**
```
Guitar → Compressor 1 (Transparent) → Overdrive → Compressor 2 (Colored) → Amp
         (Empress MKII)                            (Cali76 FET)
```

**Effect:**
- First compressor controls input dynamics
- Second compressor adds sustain + warmth

**Pros:**
- Maximum control
- Separate functions (control vs sustain)
- Complex tone shaping

**Cons:**
- Two pedals (board space)
- Complex to dial in
- Risk of over-compression

**Best For:**
- Studio recording
- Advanced pedalboard users
- When you own both compressors (like you do!)

**Example:**
```
Guitar → Empress MKII (2:1, transparent) → Sweet Honey → Cali76 FET (4:1, warmth) → Amp
         (Clean control)                                 (Sustain + color)
```

---

## Common Mistakes and Solutions

### Mistake 1: Over-Compression (Squashed Sound)

**Symptoms:**
- Lifeless, flat tone
- No dynamic range
- "Pumping" or "breathing" effect
- Everything sounds the same volume

**Causes:**
- Ratio too high (10:1+)
- Threshold too low (compressing everything)
- Attack too fast + Ratio too high
- Makeup gain too high

**Solutions:**
1. **Reduce Ratio:** Start with 3:1 or 4:1, not 10:1
2. **Raise Threshold:** Only compress louder peaks, not everything
3. **Slow Down Attack:** Let transients through (20-30ms)
4. **Use Parallel Compression:** Mix dry signal back in (50-70%)

**Correct Settings:**
```
Instead of: Ratio 10:1, Threshold -40dB, Attack 0.1ms
Try:        Ratio 4:1,  Threshold -20dB, Attack 15ms, Mix 70%
```

---

### Mistake 2: Not Enough Compression (No Audible Effect)

**Symptoms:**
- Can't hear any difference when engaged
- No sustain increase
- Same dynamics as bypassed

**Causes:**
- Threshold too high
- Ratio too low (2:1 or less)
- Attack too slow
- Makeup gain not set (compressed signal quieter than bypass)

**Solutions:**
1. **Lower Threshold:** More signal triggers compression
2. **Increase Ratio:** 4:1 instead of 2:1
3. **Faster Attack:** Catch more transients
4. **Set Makeup Gain:** Match bypass volume (unity gain)

**Correct Settings:**
```
Instead of: Ratio 2:1, Threshold -10dB, Attack 50ms, Output Low
Try:        Ratio 4:1, Threshold -25dB, Attack 15ms, Output +6dB
```

---

### Mistake 3: Pumping / Breathing Effect

**Symptoms:**
- Volume swells up and down unnaturally
- Background noise rises after notes
- Sounds like compressor is "gasping"

**Causes:**
- **Release time too fast:** Compression releases too quickly, causing volume swells
- **Release time too slow:** Compression holds too long, causing pumping
- **Threshold too low + High Ratio:** Over-compression

**Solutions:**
1. **Adjust Release Time:**
   - Too fast pumping → Slow down release (200-400ms)
   - Too slow pumping → Speed up release (100-200ms)
2. **Use Auto Release:** If available (program-dependent)
3. **Reduce Compression Amount:** Lower ratio or raise threshold
4. **Parallel Compression:** Blend dry signal to mask pumping

**Finding Correct Release:**
- Play sustained notes and listen
- Release should be natural, not noticeable
- Typically 150-300ms for guitar

---

### Mistake 4: Loss of Pick Attack

**Symptoms:**
- Notes sound dull, soft
- No "snap" or "bite"
- All notes sound mushy

**Causes:**
- **Attack time too fast:** Compressor catches all transients
- **High Ratio + Fast Attack:** Squashing transients

**Solutions:**
1. **Slow Down Attack:** 20-50ms (let transients through)
2. **Use Parallel Compression:** Blend dry signal (preserves attack)
3. **Reduce Ratio:** 3:1 or 4:1 instead of 6:1+
4. **Check Knee Setting:** Soft knee is more natural

**Correct Settings for Preserving Attack:**
```
Ratio: 3:1 to 4:1 (moderate)
Attack: 20-40ms (slow, lets pick attack through)
Mix: 70% (blends dry signal with attack)
```

---

### Mistake 5: Frequency Imbalance (Thin/Boomy)

**Symptoms:**
- Bass-heavy notes sound thin (compressed too much)
- High notes sound normal (not compressed)
- Or vice versa (boomy bass, thin highs)

**Causes:**
- **Low frequencies trigger compression more** (higher amplitude)
- **No Sidechain HPF:** Bass triggers excessive compression
- **Tilt EQ set wrong:** Imbalanced frequency response

**Solutions:**
1. **Use Sidechain HPF:** Filter out bass from detection (e.g., 120Hz)
2. **Adjust Tilt EQ:** Brighten or darken as needed
3. **EQ Before Compressor:** Shape frequency balance before compression
4. **Multiband Compression:** (Advanced) Compress frequency bands separately

**Correct Setup:**
```
Guitar (Bass-heavy PAF) → PA-1QG (slight bass cut) → Empress MKII (Sidechain HPF: 120Hz)
                                                       (Bass doesn't trigger compression)
```

---

### Mistake 6: Noise Increase

**Symptoms:**
- Hiss increases when compressor is on
- Background noise louder during quiet parts
- Amp hum becomes audible

**Causes:**
- **Compressor raises noise floor:** Makeup gain amplifies noise
- **High compression ratio:** Brings up quiet noise
- **Gain staging issues:** Compressor after noisy pedals

**Solutions:**
1. **Lower Threshold:** Don't compress quiet parts (noise)
2. **Use Noise Gate:** After compressor (not ideal, but works)
3. **Fix Gain Staging:** Lower gain upstream, higher makeup gain downstream
4. **Better Quality Pedals:** Higher SNR (signal-to-noise ratio)
5. **Isolated Power Supply:** Reduce electrical noise

**Gain Staging Example:**
```
❌ Bad:  Guitar → High Gain Pedal (noisy) → Compressor (amplifies noise)
✅ Good: Guitar → Lower Gain Pedal (cleaner) → Compressor → Makeup Gain
```

---

### Mistake 7: Compressor Fighting Amp Compression

**Symptoms:**
- Tone sounds choked, lifeless
- Amp doesn't respond dynamically
- Too much compression overall

**Causes:**
- **Compressor + Natural Amp Compression:** Double compression
- **High-gain amp already compresses:** Additional compressor too much

**Solutions:**
1. **Reduce Pedal Compression:** Lower ratio, higher threshold
2. **Place in Effects Loop:** Compress after amp preamp (post-gain)
3. **Use Transparent Compressor:** Less added compression character
4. **Bypass Compressor for High-Gain:** Only use for clean/crunch

**Better Approach:**
```
Clean Amp (Low Compression):
✅ Guitar → Compressor → Overdrive → Clean Amp (works well)

High-Gain Amp (Heavy Compression):
✅ Guitar → Overdrive → High-Gain Amp (skip compressor)
Or: Guitar → [Preamp] → [FX Send] → Compressor → [FX Return] (4CM)
```

---

## Parallel Compression Technique

### What is Parallel Compression?

**Definition:** Blending heavily compressed signal with uncompressed (dry) signal.

**Also Known As:**
- New York Compression
- Wet/Dry Compression
- Blend Compression

### How It Works

**Signal Flow:**
```
Input Signal
    ↓
 [Split]
    ↓    ↓
    |    └──→ [Heavy Compression] → [Makeup Gain] ──┐
    |         (Ratio 6:1-10:1)                       |
    |                                             [Mix] → Output
    |                                                 |
    └──────→ [Dry Signal (Uncompressed)] ────────────┘
```

**Mix Control:**
- 100% = Fully compressed (traditional compression)
- 50% = Half compressed, half dry
- 0% = Fully dry (bypass)

### Benefits

**1. Preserve Transients While Adding Sustain**
```
Dry Signal:        |▲------|  (sharp attack, natural decay)
Compressed Signal: |█======|  (controlled, sustained)
Blended:           |▲=====|   (sharp attack + sustain) ← Best of both!
```

**2. Heavy Compression Without Squashing**
- Use aggressive compression (8:1, 10:1)
- Blend back dry signal (30-50%)
- Result: Massive sustain but still punchy

**3. More Natural Sound**
- Less obvious compression effect
- Maintains playing dynamics
- Adds sustain without killing attack

### Parallel Compression Settings

**Classic New York Style:**
- Ratio: **8:1 to 10:1** (very aggressive)
- Attack: **Fast** (1-5ms)
- Release: **Medium** (150-300ms)
- Threshold: **Low** (compress everything)
- Makeup Gain: **High** (+10 to +15dB)
- **Mix: 30-50%** (blend heavily compressed with dry)

**Effect:**
- Heavily compressed signal adds thickness and sustain
- Dry signal preserves attack and dynamics
- Combined: Punchy + thick + sustained

**Example:**
```
Guitar → Cali76 FET (IN: High, OUT: High, Ratio: All, DRY: 70%) → Amp
         (Aggressive compression, but 70% dry preserves punch)
```

### Your Pedals with Parallel Compression

**Origin Effects Cali76 FET:**
- **DRY Knob:** Parallel compression control
- Clockwise: More dry signal
- Counter-clockwise: Less dry signal (more compressed)

**Settings for New York Style:**
- IN: Medium-High (heavy compression)
- OUT: High (makeup gain)
- ATTACK: Fast (catch transients)
- RELEASE: Medium (200-300ms)
- RATIO: 4:1 or All (1176 style)
- **DRY: 70-80%** (blend back dry signal)

**Empress MKII:**
- **MIX Knob:** Parallel compression control
- Clockwise (100%): Fully compressed
- Counter-clockwise (0%): Fully dry

**Settings for New York Style:**
- INPUT: High (heavy compression)
- OUTPUT: High (makeup gain)
- ATTACK: Fast (1-5ms)
- RELEASE: Medium (200ms)
- RATIO: 10:1 (aggressive)
- **MIX: 40-60%** (blend)

### Practical Examples

#### Example 1: Post Rock Lead (Singing Sustain)

```
ESP EC-CTM → Colosseum (Klon+BB stacked) → Cali76 FET → Amp
                                             ↓
Settings:
- IN: High (strong compression)
- ATTACK: Medium (10ms) - Some attack
- RELEASE: Slow (400ms) - Long sustain
- RATIO: All (1176 all buttons)
- DRY: 75% (blend for punch)
```

**Result:**
- Massive sustain (compressed signal)
- Punchy attack (dry signal)
- Singing lead tone (Explosions in the Sky)

#### Example 2: Funk Rhythm (Tight + Punchy)

```
Greco TE-500 → Empress MKII → From Yesterday (Yellow Clean) → JC-22
                ↓
Settings:
- INPUT: Medium (moderate compression)
- ATTACK: Fast (2ms) - Tight
- RELEASE: Fast (100ms) - Quick recovery
- RATIO: 6:1 (strong)
- MIX: 60% (some dry for punch)
```

**Result:**
- Tight, consistent chops (compressed signal)
- Percussive attack (dry signal)
- Nile Rodgers-style funk

#### Example 3: Jazz Ballad (Transparent Sustain)

```
ESP Throbber (PAF) → Empress MKII → Sweet Honey (low gain) → Imperial MKII
                      ↓
Settings:
- INPUT: Low (gentle compression)
- ATTACK: Slow (40ms) - Natural attack
- RELEASE: Medium (250ms)
- RATIO: 3:1 (gentle)
- MIX: 80% (mostly compressed, some dry)
```

**Result:**
- Natural attack (dry signal + slow attack)
- Gentle sustain (compressed signal)
- Transparent jazz tone

---

## Comparison Tables

### Compressor Type Comparison

| Type | Attack Speed | Tone Character | Transparency | Best For | Example Pedals |
|------|--------------|----------------|--------------|----------|----------------|
| **FET** | Very Fast (μs) | Clean to Warm | High | Clean guitar, funk, jazz | Cali76 FET, Empress MKII |
| **Optical** | Slow (10-60ms) | Smooth, Musical | Very High | Blues, ballads, gentle control | Demeter Compulator |
| **VCA** | Adjustable | Clean, Precise | High | Studio, versatile | Wampler Ego |
| **Tube** | Medium | Warm, Colored | Low | Vintage tones, blues | Effectrode PC-2A |

### Your Compressors: Cali76 FET vs Empress MKII

| Feature | Cali76 FET | Empress MKII |
|---------|------------|--------------|
| **Type** | FET (1176-style) | FET (Modern) |
| **Transparency** | Lightly colored (warm) | Ultra-transparent |
| **Threshold** | Fixed (control via INPUT) | Fixed (control via INPUT) |
| **Ratio** | 1176-style (fixed ratios) | 2:1, 4:1, 10:1 (3 options) |
| **Attack** | Adjustable | Adjustable |
| **Release** | 69.5ms - 398ms | 50ms - 1 second |
| **Special Features** | 10-LED Meter, DRY (parallel) | Tilt Tone EQ, Sidechain HPF, MIX |
| **Tone Character** | Warm, slightly colored | Completely transparent |
| **Gain Meter** | 10-LED (dB scale) | Dual LED (Input + Reduction) |
| **Price** | $369 | $219 |
| **Best For** | Post Rock sustain, warm tones | Jazz, Neo Soul, transparent control |
| **Internal Voltage** | 9V → 24V (headroom) | 9V standard |

**Decision Matrix:**

**Use Empress MKII when:**
- You want ultra-transparent compression
- Playing Jazz, Neo Soul (clean tones)
- Need Tilt EQ for tone shaping
- Need Sidechain HPF (bass management)
- Want maximum flexibility (3 ratios)
- Budget-conscious ($219)

**Use Cali76 FET when:**
- You want 1176-style warmth
- Playing Post Rock, Fusion (driven tones)
- Want visual feedback (10-LED meter)
- Need parallel compression (DRY knob)
- Want classic studio compression character
- High-end budget ($369)

**Use Both (Dual Compressor Setup) when:**
- Empress first (clean control) + Cali76 after gain (sustain + warmth)
- Maximum flexibility across all genres
- Studio-quality pedalboard

---

### Parameter Settings by Genre

| Genre | Ratio | Attack | Release | Threshold | Mix | Pedal Choice |
|-------|-------|--------|---------|-----------|-----|--------------|
| **Jazz** | 2:1-3:1 | Slow (30-50ms) | Medium (250ms) | High (peaks only) | 80-100% | Empress MKII |
| **Neo Soul** | 4:1 | Medium (10-20ms) | Medium (200ms) | Medium | 70-90% | Empress MKII |
| **Funk** | 4:1-6:1 | Fast (1-5ms) | Fast (50-100ms) | Low-Medium | 100% | Empress MKII (Sidechain HPF ON) |
| **Blues** | 3:1-4:1 | Medium (20-40ms) | Medium (250ms) | Medium | 70-90% | Empress or Optical |
| **Post Rock** | 6:1-10:1 | Medium (10-20ms) | Slow (500ms-1s) | Low | 70-80% | Cali76 FET (DRY blend) |
| **Fusion** | 4:1-6:1 | Fast-Medium (5-15ms) | Medium (200ms) | Medium | 80-100% | Empress or Cali76 |
| **Classic Rock** | 3:1-4:1 | Medium (20-30ms) | Medium (250ms) | High | 60-80% | Cali76 FET |

---

## Mathematical Models

### Compression Transfer Function

**Basic Compression Formula:**

```
For signal above threshold:
  y_dB = T + (x_dB - T) / R

Where:
  y_dB = Output level (dB)
  x_dB = Input level (dB)
  T = Threshold (dB)
  R = Ratio (e.g., 4:1 → R = 4)
```

**Example (4:1 ratio, Threshold = -20dB):**

```
Input = -10dB (10dB above threshold)
Output = -20dB + (-10dB - (-20dB)) / 4
       = -20dB + (10dB) / 4
       = -20dB + 2.5dB
       = -17.5dB

Result: 10dB input increase → 2.5dB output increase (4:1 ratio)
```

### Gain Reduction Calculation

**Gain Reduction (GR):**

```
GR_dB = (x_dB - T) × (1 - 1/R)

Example (4:1 ratio):
Input = -10dB above threshold
GR = 10dB × (1 - 1/4)
   = 10dB × 0.75
   = 7.5dB of gain reduction
```

### Attack/Release Time Constants

**Exponential Attack Envelope:**

```
g(t) = 1 - e^(-t / τ_attack)

Where:
  g(t) = Gain reduction factor at time t (0 to 1)
  τ_attack = Attack time constant (seconds)
  t = Time since threshold exceeded
```

**Exponential Release Envelope:**

```
g(t) = e^(-t / τ_release)

Where:
  g(t) = Gain reduction factor at time t (1 to 0)
  τ_release = Release time constant (seconds)
  t = Time since signal dropped below threshold
```

**Example (Attack = 10ms):**
```
t = 0ms:   g(t) = 0% (no gain reduction yet)
t = 10ms:  g(t) = 63.2% (one time constant)
t = 20ms:  g(t) = 86.5% (two time constants)
t = 50ms:  g(t) = 99.3% (full gain reduction)
```

### Soft Knee Compression

**Hard Knee:**
```
         ⎧ x_dB                         if x_dB ≤ T
y_dB =   ⎨
         ⎩ T + (x_dB - T) / R          if x_dB > T
```

**Soft Knee (with knee width W):**

```
         ⎧ x_dB                                      if x_dB < (T - W/2)
         ⎪
y_dB =   ⎨ x_dB + [1/R - 1] × [(x_dB-T+W/2)^2] / (2W)  if (T-W/2) ≤ x_dB ≤ (T+W/2)
         ⎪
         ⎩ T + (x_dB - T) / R                      if x_dB > (T + W/2)

Where:
  W = Knee width (dB), typically 6-12dB
  T = Threshold (dB)
  R = Ratio
```

**Effect:**
- Hard knee: Abrupt transition at threshold
- Soft knee: Gradual transition over ±W/2 range

### Parallel Compression Mix

**Parallel Compression Output:**

```
y(t) = α × x(t) + (1-α) × compress(x(t))

Where:
  α = Dry mix (0 to 1)
  x(t) = Input signal
  compress(x(t)) = Compressed signal
  y(t) = Output signal

Example (Mix = 70% dry = α = 0.7):
  y(t) = 0.7 × x(t) + 0.3 × compress(x(t))
  (70% dry + 30% compressed)
```

### RMS vs Peak Detection

**RMS (Root Mean Square) Detection:**

```
RMS = sqrt(1/N × Σ(x[n]^2))

Where:
  N = Window size (samples)
  x[n] = Sample value

Result: Average signal level (more musical)
```

**Peak Detection:**

```
Peak = max(|x[n]|) over window

Result: Maximum signal level (more aggressive)
```

**Guitar Application:**
- **RMS:** More musical, responds to average signal (most guitar compressors)
- **Peak:** Fast response, prevents clipping (limiters)

---

## Practical Implementation Guide

### Step-by-Step Setup Process

#### Step 1: Set Bypass Reference

1. **Play guitar with compressor bypassed**
2. **Note the volume level and tone**
3. This is your reference point

#### Step 2: Set Threshold/Input

**For Fixed Threshold (Cali76, Empress):**
1. Start with **INPUT knob at minimum**
2. Play at normal intensity
3. **Gradually increase INPUT** until you see gain reduction (LED meter)
4. Target: **3-6dB gain reduction** on average playing

**Visual Feedback:**
- **Cali76 FET:** 10-LED meter (aim for 3-4 LEDs on average)
- **Empress MKII:** Gain Reduction LED (occasional flicker to constant glow)

#### Step 3: Set Ratio

1. Start with **4:1** (moderate, versatile)
2. Play and listen:
   - Too subtle? → Increase ratio (6:1)
   - Too squashed? → Decrease ratio (3:1 or 2:1)

**Rule of Thumb:**
- **Clean tones:** 2:1 to 4:1
- **Driven tones:** 4:1 to 6:1
- **Sustain tones:** 6:1 to 10:1

#### Step 4: Set Attack Time

1. Start with **Medium attack** (10-20ms)
2. Listen to pick attack:
   - **Too dull/soft?** → Slow down attack (30-50ms) - Let transients through
   - **Too dynamic/uncontrolled?** → Speed up attack (5-10ms) - Catch transients

**Test:**
- Play staccato notes (short, percussive)
- Should have clear attack but controlled tail

#### Step 5: Set Release Time

1. Start with **Medium release** (200-300ms)
2. Play sustained notes and listen:
   - **Pumping/breathing?** → Adjust release (faster or slower)
   - **Too obvious compression?** → Slower release or Auto (if available)

**Test:**
- Play sustained note, then stop abruptly
- Should return to natural level smoothly (not suddenly)

#### Step 6: Set Makeup Gain

1. **Play with compressor ON**
2. **Adjust OUTPUT/Makeup Gain** until volume matches bypass
3. This is **Unity Gain**

**Test:**
- Switch between bypass and compressed repeatedly
- Should be **same volume** (only dynamics change)

**Optional:**
- Set OUTPUT **higher than unity** for boost mode

#### Step 7: Fine-Tune with Mix/Dry (Parallel Compression)

**If your compressor has MIX/DRY/BLEND control:**

1. Start with **Mix = 100%** (fully compressed)
2. Listen to tone:
   - **Too squashed/lifeless?** → Reduce mix (blend dry signal)
   - **Good but could use more punch?** → Reduce mix to 70-80%

**Parallel Compression Sweet Spot:**
- **70-80% compressed:** Transparent sustain
- **50-60% compressed:** Punchy + sustained (New York style)
- **30-50% compressed:** Very punchy, heavy compression blended

#### Step 8: Optional Tone Shaping

**Empress MKII - Tilt EQ:**
1. Start at **12 o'clock** (flat)
2. Brighten if needed (clockwise) or warm if needed (counter-clockwise)

**Empress MKII - Sidechain HPF:**
1. **OFF:** Default (all frequencies trigger compression)
2. **120Hz:** For 6-string guitar (filters out low E from triggering)
3. **240Hz:** For bass or very bass-heavy guitars

#### Step 9: Verify in Context

1. **Play with band/backing track**
2. Ensure compression works in mix
3. Fine-tune as needed

---

### Signal Chain Integration

#### Integration with Your Specific Pedalboard

**Scenario 1: Jazz/Neo Soul Clean Tones**

```
Guitar (Throbber PAF / Greco TE-500)
  ↓
Empress MKII (Transparent control)
  Settings: INPUT Low (1-2 LED), Ratio 2:1, Attack Slow (30ms), Release Medium (250ms), MIX 80%
  ↓
PA-1QG (EQ for guitar voice)
  Preset 1: Greco TE-500
  Preset 2: Tokyo Thinline
  Preset 3: Throbber
  ↓
From Yesterday (KOT - Yellow Clean Mode)
  Clean Boost
  ↓
Mad Professor Sweet Honey Overdrive Deluxe
  Drive 11-12 o'clock (Neo Soul sweet spot)
  ↓
JC-22 or Imperial MKII Rhythm
  ↓
[FX Loop] → FT-1Y → Nucleo → [Return]
```

**Why This Works:**
- Empress first: Transparent dynamic control before any coloration
- PA-1QG: EQ shaping for each guitar
- Gain staging: Compressed signal → Clean Boost → Warm OD
- Result: Controlled, warm, Neo Soul tone

---

**Scenario 2: Post Rock / Ambient Sustain**

```
Guitar (ESP EC-CTM high output)
  ↓
Roshi Blacklon (Amp-in-a-Box - Blackface)
  6L6 + Drive Mode
  ↓
Cornerstone Colosseum (Klon → BB stacked)
  Clip Blender mixed
  ↓
Cali76 FET (Sustain + Warmth)
  Settings: IN Medium-High, OUT High, Ratio All, Attack Fast (5ms), Release Slow (400ms), DRY 75%
  ↓
GE-7 (Solo Boost - Optional)
  800Hz-3.2kHz boosted, LEVEL high
  ↓
Amp
  ↓
[FX Loop] → FT-1Y (Hold function) → AASB (Shimmer Both) → Nucleo Reactor → [Return]
```

**Why This Works:**
- Heavy gain → Cali76 (post-gain compression for sustain)
- DRY 75%: Parallel compression (punch + sustain)
- GE-7 optional solo boost
- Result: Massive sustain, singing lead tones (Explosions in the Sky)

---

**Scenario 3: Funk Rhythm Tightness**

```
Guitar (Greco TE-500 - Bridge pickup)
  ↓
Empress MKII (Tight, percussive control)
  Settings: INPUT Medium, Ratio 6:1, Attack Fast (2ms), Release Fast (100ms), Sidechain HPF 120Hz, MIX 100%
  ↓
PA-1QG (Frequency shaping for funk)
  Preset: Boost 800Hz-3.2kHz (mid-high punch)
  ↓
From Yesterday (Yellow Clean Mode)
  Transparent clean boost
  ↓
JC-22 (Bright ON, Chorus ON)
  ↓
[FX Loop] → FT-1Y (Short delay 100ms) → Nucleo Room (Low mix) → [Return]
```

**Why This Works:**
- Fast attack + Release: Tight, percussive compression
- Sidechain HPF 120Hz: Bass doesn't trigger compression (maintains punch)
- PA-1QG mid-high boost: Funk clarity
- Result: Nile Rodgers-style tight rhythm

---

## Conclusion

Compression is a powerful but nuanced tool for guitar signal processing. Key takeaways:

### Core Principles

1. **Compression is Subtle**
   - When done right, you shouldn't overtly "hear" it
   - You should feel more control and consistency
   - A/B bypass frequently to check

2. **Context Matters**
   - Clean tones: Transparent, gentle (2:1-4:1)
   - Driven tones: Moderate to heavy (4:1-6:1)
   - Sustain tones: Heavy (6:1-10:1)

3. **Placement is Flexible**
   - Before gain: Controls input dynamics
   - After gain: Adds sustain to driven signal
   - Both approaches valid (depends on goal)

4. **Parameters Interact**
   - Fast Attack + High Ratio = Squashed
   - Slow Attack + High Ratio = Punchy + Sustained
   - Experiment to find your sound

### Your Compressors Summary

**Empress MKII:**
- Use for: Jazz, Neo Soul, Funk, Clean tones
- Strength: Ultra-transparent, Tilt EQ, Sidechain HPF
- Placement: First in chain (before gain)

**Cali76 FET:**
- Use for: Post Rock, Fusion, Classic Rock, Driven tones
- Strength: 1176 warmth, parallel compression, sustain
- Placement: After gain (post-OD/Distortion)

**Both (Dual Compressor):**
- Empress first (clean control) + Cali76 after gain (sustain + warmth)
- Maximum flexibility across all genres
- Studio-quality pedalboard

### Final Advice

**For Beginners:**
1. Start with **moderate settings** (4:1 ratio, medium attack/release)
2. Use **visual feedback** (gain reduction meter)
3. Set **unity gain** (bypass = same volume as compressed)
4. **A/B frequently** (bypass vs compressed)

**For Advanced Users:**
1. Experiment with **parallel compression** (DRY/MIX control)
2. Try **dual compressor** setups (Empress + Cali76)
3. Use **Sidechain HPF** for bass-heavy guitars
4. Explore **extreme settings** (New York style, heavy compression + blend)

**Most Important:**
- **Use your ears**, not your eyes
- Compression should enhance your playing, not replace it
- When in doubt, less compression is more musical

---

**Document Version:** 1.0
**Last Updated:** 2026-01-06
**Category:** Tone Theory Research - Dynamic Processing
**Related Documents:**
- `gain_distortion_types.md` - Gain staging and distortion
- `signal_processing_math_models.md` - Mathematical signal processing
- Equipment-specific: `compressor_eq_spatial_effects_technical_data.md`

**References:**
- Origin Effects Cali76 FET Official Documentation
- Empress MKII Official Manual and Product Page
- Universal Audio 1176 Technical Documentation
- The Art of Mixing (David Gibson)
- Mixing Secrets for the Small Studio (Mike Senior)
- Sound on Sound: Compression Techniques
- Premier Guitar: Compressor Pedal Comparisons
- That Pedal Show: Compression Deep Dive

---

**祝演奏愉快！願這份 Compressor 理論文件幫助你掌握動態控制的藝術。** 🎸🎛️
