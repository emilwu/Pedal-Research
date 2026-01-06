#!/usr/bin/env python3
"""
Sine Wave Distortion Demo

This script demonstrates how overdrive, distortion, fuzz, and bitcrusher
effects transform a pure sine wave, showing both time-domain waveforms
and frequency-domain spectrum (harmonics).
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy import signal


# ============================================================
# Signal Processing Functions
# ============================================================

def overdrive_tanh(x, gain=5.0):
    """Soft clipping overdrive using tanh"""
    return np.tanh(gain * x)


def distortion_hard_clip(x, gain=10.0, threshold=0.7):
    """Hard clipping distortion"""
    x_gained = gain * x
    return np.clip(x_gained, -threshold, threshold)


def fuzz_square_wave(x, gain=100.0):
    """Extreme fuzz (square wave approximation)"""
    return np.tanh(gain * x)


def bitcrush_depth(x, n_bits=4):
    """Bit depth reduction"""
    n_levels = 2 ** n_bits
    return np.round(x * n_levels) / n_levels


# ============================================================
# Signal Generation
# ============================================================

def generate_sine_wave(frequency=440, duration=0.01, sample_rate=44100, amplitude=0.5):
    """
    Generate a sine wave

    Args:
        frequency: Frequency in Hz (default: 440 Hz = A4)
        duration: Duration in seconds
        sample_rate: Sample rate in Hz
        amplitude: Amplitude (0.0 to 1.0)

    Returns:
        t: Time array
        x: Sine wave signal
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    x = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, x


# ============================================================
# Frequency Analysis
# ============================================================

def compute_spectrum(x, sample_rate=44100, window='hann'):
    """
    Compute frequency spectrum using FFT

    Args:
        x: Input signal
        sample_rate: Sample rate in Hz
        window: Window function ('hann', 'hamming', None)

    Returns:
        freqs: Frequency array (Hz)
        magnitude: Magnitude spectrum (dB)
    """
    # Apply window
    if window == 'hann':
        x_windowed = x * np.hanning(len(x))
    elif window == 'hamming':
        x_windowed = x * np.hamming(len(x))
    else:
        x_windowed = x

    # Compute FFT
    fft = np.fft.rfft(x_windowed)
    freqs = np.fft.rfftfreq(len(x), 1/sample_rate)

    # Magnitude in dB
    magnitude = 20 * np.log10(np.abs(fft) + 1e-10)

    return freqs, magnitude


def find_harmonics(freqs, magnitude, fundamental_freq, num_harmonics=10, tolerance=20):
    """
    Find harmonic peaks in spectrum

    Args:
        freqs: Frequency array
        magnitude: Magnitude spectrum
        fundamental_freq: Fundamental frequency (Hz)
        num_harmonics: Number of harmonics to find
        tolerance: Frequency tolerance (Hz)

    Returns:
        harmonic_freqs: List of harmonic frequencies
        harmonic_mags: List of harmonic magnitudes
    """
    harmonic_freqs = []
    harmonic_mags = []

    for n in range(1, num_harmonics + 1):
        target_freq = n * fundamental_freq

        # Find closest frequency bin
        idx_range = np.where((freqs >= target_freq - tolerance) &
                             (freqs <= target_freq + tolerance))[0]

        if len(idx_range) > 0:
            # Find peak in range
            idx_peak = idx_range[np.argmax(magnitude[idx_range])]
            harmonic_freqs.append(freqs[idx_peak])
            harmonic_mags.append(magnitude[idx_peak])
        else:
            harmonic_freqs.append(np.nan)
            harmonic_mags.append(np.nan)

    return harmonic_freqs, harmonic_mags


# ============================================================
# Visualization
# ============================================================

def plot_waveform_comparison(frequency=440, duration=0.01, sample_rate=44100):
    """
    Plot waveform comparison of all effects
    """
    # Generate sine wave
    t, x = generate_sine_wave(frequency, duration, sample_rate, amplitude=0.8)

    # Apply effects
    y_overdrive = overdrive_tanh(x, gain=5.0)
    y_distortion = distortion_hard_clip(x, gain=10.0, threshold=0.7)
    y_fuzz = fuzz_square_wave(x, gain=100.0)
    y_bitcrush = bitcrush_depth(x, n_bits=4)

    # Create figure
    fig, axes = plt.subplots(5, 1, figsize=(14, 12))

    # Time range to display (show a few cycles)
    num_cycles = 3
    t_max = num_cycles / frequency
    mask = t <= t_max

    # Original
    axes[0].plot(t[mask] * 1000, x[mask], 'k-', linewidth=2)
    axes[0].set_ylabel('Amplitude')
    axes[0].set_title(f'Original Sine Wave ({frequency} Hz)', fontweight='bold', fontsize=12)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_ylim(-1.1, 1.1)
    axes[0].axhline(0, color='gray', linestyle='--', linewidth=0.5)

    # Overdrive
    axes[1].plot(t[mask] * 1000, y_overdrive[mask], 'b-', linewidth=2)
    axes[1].set_ylabel('Amplitude')
    axes[1].set_title('Overdrive (Soft Clipping, gain=5)', fontweight='bold', fontsize=12)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_ylim(-1.1, 1.1)
    axes[1].axhline(0, color='gray', linestyle='--', linewidth=0.5)

    # Distortion
    axes[2].plot(t[mask] * 1000, y_distortion[mask], 'r-', linewidth=2)
    axes[2].set_ylabel('Amplitude')
    axes[2].set_title('Distortion (Hard Clipping, gain=10, threshold=0.7)', fontweight='bold', fontsize=12)
    axes[2].grid(True, alpha=0.3)
    axes[2].set_ylim(-1.1, 1.1)
    axes[2].axhline(0, color='gray', linestyle='--', linewidth=0.5)

    # Fuzz
    axes[3].plot(t[mask] * 1000, y_fuzz[mask], color='purple', linewidth=2)
    axes[3].set_ylabel('Amplitude')
    axes[3].set_title('Fuzz (Square Wave, gain=100)', fontweight='bold', fontsize=12)
    axes[3].grid(True, alpha=0.3)
    axes[3].set_ylim(-1.1, 1.1)
    axes[3].axhline(0, color='gray', linestyle='--', linewidth=0.5)

    # Bitcrush
    axes[4].plot(t[mask] * 1000, y_bitcrush[mask], color='orange', linewidth=2)
    axes[4].set_ylabel('Amplitude')
    axes[4].set_xlabel('Time (ms)')
    axes[4].set_title('Bitcrush (4-bit Quantization)', fontweight='bold', fontsize=12)
    axes[4].grid(True, alpha=0.3)
    axes[4].set_ylim(-1.1, 1.1)
    axes[4].axhline(0, color='gray', linestyle='--', linewidth=0.5)

    plt.tight_layout()
    return fig


def plot_spectrum_comparison(frequency=440, duration=0.1, sample_rate=44100):
    """
    Plot frequency spectrum comparison of all effects
    Shows harmonic generation
    """
    # Generate sine wave (longer duration for better frequency resolution)
    t, x = generate_sine_wave(frequency, duration, sample_rate, amplitude=0.8)

    # Apply effects
    y_overdrive = overdrive_tanh(x, gain=5.0)
    y_distortion = distortion_hard_clip(x, gain=10.0, threshold=0.7)
    y_fuzz = fuzz_square_wave(x, gain=100.0)
    y_bitcrush = bitcrush_depth(x, n_bits=4)

    # Compute spectra
    freqs_orig, mag_orig = compute_spectrum(x, sample_rate)
    freqs_od, mag_od = compute_spectrum(y_overdrive, sample_rate)
    freqs_dist, mag_dist = compute_spectrum(y_distortion, sample_rate)
    freqs_fuzz, mag_fuzz = compute_spectrum(y_fuzz, sample_rate)
    freqs_crush, mag_crush = compute_spectrum(y_bitcrush, sample_rate)

    # Create figure
    fig, axes = plt.subplots(5, 1, figsize=(14, 12))

    # Frequency range to display (show up to 10th harmonic)
    f_max = frequency * 12

    # Original
    mask = freqs_orig <= f_max
    axes[0].plot(freqs_orig[mask], mag_orig[mask], 'k-', linewidth=1.5)
    axes[0].set_ylabel('Magnitude (dB)')
    axes[0].set_title(f'Original Sine Wave - Spectrum (Pure {frequency} Hz)', fontweight='bold', fontsize=12)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_ylim(-100, 20)
    # Mark fundamental
    axes[0].axvline(frequency, color='red', linestyle='--', alpha=0.5, linewidth=1)
    axes[0].text(frequency, 10, 'f₀', fontsize=10, ha='center')

    # Overdrive
    mask = freqs_od <= f_max
    axes[1].plot(freqs_od[mask], mag_od[mask], 'b-', linewidth=1.5)
    axes[1].set_ylabel('Magnitude (dB)')
    axes[1].set_title('Overdrive - Spectrum (Odd Harmonics: 3f, 5f, 7f...)', fontweight='bold', fontsize=12)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_ylim(-100, 20)
    # Mark harmonics
    for n in [1, 3, 5, 7, 9]:
        axes[1].axvline(n * frequency, color='red', linestyle='--', alpha=0.3, linewidth=1)
        if n == 1:
            axes[1].text(n * frequency, 10, 'f₀', fontsize=9, ha='center')
        else:
            axes[1].text(n * frequency, 10, f'{n}f', fontsize=9, ha='center')

    # Distortion
    mask = freqs_dist <= f_max
    axes[2].plot(freqs_dist[mask], mag_dist[mask], 'r-', linewidth=1.5)
    axes[2].set_ylabel('Magnitude (dB)')
    axes[2].set_title('Distortion - Spectrum (Even + Odd Harmonics)', fontweight='bold', fontsize=12)
    axes[2].grid(True, alpha=0.3)
    axes[2].set_ylim(-100, 20)
    # Mark harmonics
    for n in [1, 2, 3, 4, 5, 6, 7, 8]:
        axes[2].axvline(n * frequency, color='red', linestyle='--', alpha=0.3, linewidth=1)
        if n == 1:
            axes[2].text(n * frequency, 10, 'f₀', fontsize=9, ha='center')
        else:
            axes[2].text(n * frequency, 10, f'{n}f', fontsize=9, ha='center')

    # Fuzz
    mask = freqs_fuzz <= f_max
    axes[3].plot(freqs_fuzz[mask], mag_fuzz[mask], color='purple', linewidth=1.5)
    axes[3].set_ylabel('Magnitude (dB)')
    axes[3].set_title('Fuzz - Spectrum (Very Strong Odd Harmonics)', fontweight='bold', fontsize=12)
    axes[3].grid(True, alpha=0.3)
    axes[3].set_ylim(-100, 20)
    # Mark harmonics
    for n in [1, 3, 5, 7, 9, 11]:
        axes[3].axvline(n * frequency, color='red', linestyle='--', alpha=0.3, linewidth=1)
        if n == 1:
            axes[3].text(n * frequency, 10, 'f₀', fontsize=9, ha='center')
        else:
            axes[3].text(n * frequency, 10, f'{n}f', fontsize=9, ha='center')

    # Bitcrush
    mask = freqs_crush <= f_max
    axes[4].plot(freqs_crush[mask], mag_crush[mask], color='orange', linewidth=1.5)
    axes[4].set_ylabel('Magnitude (dB)')
    axes[4].set_xlabel('Frequency (Hz)')
    axes[4].set_title('Bitcrush - Spectrum (Inharmonic/Aliasing Content)', fontweight='bold', fontsize=12)
    axes[4].grid(True, alpha=0.3)
    axes[4].set_ylim(-100, 20)
    # Mark fundamental
    axes[4].axvline(frequency, color='red', linestyle='--', alpha=0.5, linewidth=1)
    axes[4].text(frequency, 10, 'f₀', fontsize=10, ha='center')

    plt.tight_layout()
    return fig


def plot_comprehensive_analysis(frequency=440, duration=0.1, sample_rate=44100):
    """
    Comprehensive analysis: waveform + spectrum for each effect
    """
    # Generate sine wave
    t, x = generate_sine_wave(frequency, duration, sample_rate, amplitude=0.8)

    # Apply effects
    effects = {
        'Original': x,
        'Overdrive (gain=5)': overdrive_tanh(x, gain=5.0),
        'Distortion (gain=10)': distortion_hard_clip(x, gain=10.0, threshold=0.7),
        'Fuzz (gain=100)': fuzz_square_wave(x, gain=100.0),
        'Bitcrush (4-bit)': bitcrush_depth(x, n_bits=4)
    }

    colors = ['black', 'blue', 'red', 'purple', 'orange']

    # Create figure with GridSpec
    fig = plt.figure(figsize=(18, 12))
    gs = GridSpec(5, 2, figure=fig, hspace=0.35, wspace=0.3)

    # Time range for waveform (show 3 cycles)
    num_cycles = 3
    t_max = num_cycles / frequency
    mask_time = t <= t_max

    # Frequency range for spectrum
    f_max = frequency * 12

    for i, (name, y) in enumerate(effects.items()):
        color = colors[i]

        # Waveform (left column)
        ax_wave = fig.add_subplot(gs[i, 0])
        ax_wave.plot(t[mask_time] * 1000, y[mask_time], color=color, linewidth=2)
        ax_wave.set_ylabel('Amplitude')
        ax_wave.set_title(f'{name} - Waveform', fontweight='bold', fontsize=11)
        ax_wave.grid(True, alpha=0.3)
        ax_wave.set_ylim(-1.1, 1.1)
        ax_wave.axhline(0, color='gray', linestyle='--', linewidth=0.5)
        if i == 4:
            ax_wave.set_xlabel('Time (ms)')

        # Spectrum (right column)
        ax_spec = fig.add_subplot(gs[i, 1])
        freqs, magnitude = compute_spectrum(y, sample_rate)
        mask_freq = freqs <= f_max
        ax_spec.plot(freqs[mask_freq], magnitude[mask_freq], color=color, linewidth=1.5)
        ax_spec.set_ylabel('Magnitude (dB)')
        ax_spec.set_title(f'{name} - Spectrum', fontweight='bold', fontsize=11)
        ax_spec.grid(True, alpha=0.3)
        ax_spec.set_ylim(-100, 20)

        # Mark harmonics
        for n in range(1, 11):
            ax_spec.axvline(n * frequency, color='gray', linestyle='--', alpha=0.2, linewidth=0.5)

        if i == 4:
            ax_spec.set_xlabel('Frequency (Hz)')

    plt.savefig('sine_wave_comprehensive_analysis.png', dpi=150, bbox_inches='tight')
    print("Comprehensive analysis saved to: sine_wave_comprehensive_analysis.png")

    return fig


def plot_harmonic_analysis(frequency=440, duration=0.1, sample_rate=44100):
    """
    Analyze and compare harmonic content
    """
    # Generate sine wave
    t, x = generate_sine_wave(frequency, duration, sample_rate, amplitude=0.8)

    # Apply effects
    y_overdrive = overdrive_tanh(x, gain=5.0)
    y_distortion = distortion_hard_clip(x, gain=10.0, threshold=0.7)
    y_fuzz = fuzz_square_wave(x, gain=100.0)
    y_bitcrush = bitcrush_depth(x, n_bits=4)

    # Compute spectra
    freqs_od, mag_od = compute_spectrum(y_overdrive, sample_rate)
    freqs_dist, mag_dist = compute_spectrum(y_distortion, sample_rate)
    freqs_fuzz, mag_fuzz = compute_spectrum(y_fuzz, sample_rate)
    freqs_crush, mag_crush = compute_spectrum(y_bitcrush, sample_rate)

    # Find harmonics
    h_freqs_od, h_mags_od = find_harmonics(freqs_od, mag_od, frequency, num_harmonics=10)
    h_freqs_dist, h_mags_dist = find_harmonics(freqs_dist, mag_dist, frequency, num_harmonics=10)
    h_freqs_fuzz, h_mags_fuzz = find_harmonics(freqs_fuzz, mag_fuzz, frequency, num_harmonics=10)
    h_freqs_crush, h_mags_crush = find_harmonics(freqs_crush, mag_crush, frequency, num_harmonics=10)

    # Plot
    fig, axes = plt.subplots(2, 1, figsize=(14, 10))

    # Bar chart of harmonic magnitudes
    harmonics = np.arange(1, 11)
    width = 0.2

    axes[0].bar(harmonics - 1.5*width, h_mags_od, width, label='Overdrive', color='blue', alpha=0.7)
    axes[0].bar(harmonics - 0.5*width, h_mags_dist, width, label='Distortion', color='red', alpha=0.7)
    axes[0].bar(harmonics + 0.5*width, h_mags_fuzz, width, label='Fuzz', color='purple', alpha=0.7)
    axes[0].bar(harmonics + 1.5*width, h_mags_crush, width, label='Bitcrush', color='orange', alpha=0.7)

    axes[0].set_xlabel('Harmonic Number')
    axes[0].set_ylabel('Magnitude (dB)')
    axes[0].set_title('Harmonic Content Comparison', fontweight='bold', fontsize=14)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3, axis='y')
    axes[0].set_xticks(harmonics)
    axes[0].set_xticklabels([f'{n}f₀' for n in harmonics])

    # Line plot for clarity
    axes[1].plot(harmonics, h_mags_od, 'o-', linewidth=2, markersize=8, label='Overdrive', color='blue')
    axes[1].plot(harmonics, h_mags_dist, 's-', linewidth=2, markersize=8, label='Distortion', color='red')
    axes[1].plot(harmonics, h_mags_fuzz, '^-', linewidth=2, markersize=8, label='Fuzz', color='purple')
    axes[1].plot(harmonics, h_mags_crush, 'd-', linewidth=2, markersize=8, label='Bitcrush', color='orange')

    axes[1].set_xlabel('Harmonic Number')
    axes[1].set_ylabel('Magnitude (dB)')
    axes[1].set_title('Harmonic Content - Line Plot', fontweight='bold', fontsize=14)
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    axes[1].set_xticks(harmonics)
    axes[1].set_xticklabels([f'{n}f₀' for n in harmonics])

    plt.tight_layout()
    plt.savefig('harmonic_analysis.png', dpi=150, bbox_inches='tight')
    print("Harmonic analysis saved to: harmonic_analysis.png")

    return fig


# ============================================================
# Main Execution
# ============================================================

def main():
    """Run all demonstrations"""

    print("=" * 70)
    print("Sine Wave Distortion Analysis")
    print("=" * 70)
    print()

    # Parameters
    frequency = 440  # A4
    duration_short = 0.01  # 10ms for waveform visualization
    duration_long = 0.1    # 100ms for spectrum analysis
    sample_rate = 44100

    print(f"Frequency: {frequency} Hz (A4)")
    print(f"Sample Rate: {sample_rate} Hz")
    print()

    # 1. Waveform comparison
    print("1. Generating waveform comparison...")
    fig1 = plot_waveform_comparison(frequency, duration_short, sample_rate)
    fig1.savefig('sine_wave_waveforms.png', dpi=150, bbox_inches='tight')
    print("   Saved: sine_wave_waveforms.png")
    print()

    # 2. Spectrum comparison
    print("2. Generating spectrum comparison...")
    fig2 = plot_spectrum_comparison(frequency, duration_long, sample_rate)
    fig2.savefig('sine_wave_spectra.png', dpi=150, bbox_inches='tight')
    print("   Saved: sine_wave_spectra.png")
    print()

    # 3. Comprehensive analysis
    print("3. Generating comprehensive analysis (waveform + spectrum)...")
    plot_comprehensive_analysis(frequency, duration_long, sample_rate)
    print()

    # 4. Harmonic analysis
    print("4. Generating harmonic analysis...")
    plot_harmonic_analysis(frequency, duration_long, sample_rate)
    print()

    print("=" * 70)
    print("All analyses completed!")
    print("=" * 70)
    print()
    print("Generated files:")
    print("  - sine_wave_waveforms.png          (Time domain)")
    print("  - sine_wave_spectra.png            (Frequency domain)")
    print("  - sine_wave_comprehensive_analysis.png  (Both)")
    print("  - harmonic_analysis.png            (Harmonic comparison)")
    print()
    print("Key Observations:")
    print("  • Overdrive: Generates odd harmonics (3f, 5f, 7f...)")
    print("  • Distortion: Generates both even and odd harmonics")
    print("  • Fuzz: Very strong odd harmonics (square wave-like)")
    print("  • Bitcrush: Inharmonic content due to quantization")


if __name__ == "__main__":
    main()
