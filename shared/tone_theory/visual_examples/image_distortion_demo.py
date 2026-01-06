#!/usr/bin/env python3
"""
Image Distortion Demo: Applying Audio Distortion Effects to Images

This script demonstrates how overdrive, distortion, fuzz, and bitcrusher
effects work by applying them to a grayscale gradient image.

The pixel values (0-255) are treated as audio signal values, showing
how each distortion type affects the signal.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


# ============================================================
# Signal Processing Functions (from signal_processing_math_models.md)
# ============================================================

def normalize_image(img):
    """Normalize image to range [-1, 1] for processing"""
    return (img / 127.5) - 1.0


def denormalize_image(img):
    """Convert back from [-1, 1] to [0, 255]"""
    return ((img + 1.0) * 127.5).clip(0, 255).astype(np.uint8)


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
# Image Generation
# ============================================================

def create_gradient_image(width=512, height=512, direction='horizontal'):
    """
    Create a grayscale gradient image

    Args:
        width: Image width in pixels
        height: Image height in pixels
        direction: 'horizontal', 'vertical', 'radial', or 'diagonal'

    Returns:
        Grayscale image (numpy array, shape: (height, width), values: 0-255)
    """
    if direction == 'horizontal':
        # Left to right gradient
        gradient = np.linspace(0, 255, width, dtype=np.uint8)
        img = np.tile(gradient, (height, 1))

    elif direction == 'vertical':
        # Top to bottom gradient
        gradient = np.linspace(0, 255, height, dtype=np.uint8)
        img = np.tile(gradient[:, np.newaxis], (1, width))

    elif direction == 'diagonal':
        # Diagonal gradient
        x = np.linspace(0, 1, width)
        y = np.linspace(0, 1, height)
        xx, yy = np.meshgrid(x, y)
        img = ((xx + yy) / 2 * 255).astype(np.uint8)

    elif direction == 'radial':
        # Radial gradient from center
        y, x = np.ogrid[:height, :width]
        center_y, center_x = height // 2, width // 2

        # Calculate distance from center
        dist = np.sqrt((x - center_x)**2 + (y - center_y)**2)
        max_dist = np.sqrt(center_x**2 + center_y**2)

        # Normalize to 0-255
        img = (dist / max_dist * 255).clip(0, 255).astype(np.uint8)

    else:
        raise ValueError(f"Unknown direction: {direction}")

    return img


def create_test_pattern(width=512, height=512):
    """
    Create a test pattern with multiple gradients and shapes

    Returns:
        Grayscale image with various patterns
    """
    img = np.zeros((height, width), dtype=np.uint8)

    # Divide into 4 quadrants
    h2, w2 = height // 2, width // 2

    # Top-left: Horizontal gradient
    gradient_h = np.linspace(0, 255, w2, dtype=np.uint8)
    img[:h2, :w2] = np.tile(gradient_h, (h2, 1))

    # Top-right: Vertical gradient
    gradient_v = np.linspace(0, 255, h2, dtype=np.uint8)
    img[:h2, w2:] = np.tile(gradient_v[:, np.newaxis], (1, w2))

    # Bottom-left: Circular pattern
    y, x = np.ogrid[:h2, :w2]
    center_y, center_x = h2 // 2, w2 // 2
    dist = np.sqrt((x - center_x)**2 + (y - center_y)**2)
    max_dist = np.sqrt(center_x**2 + center_y**2)
    img[h2:, :w2] = (dist / max_dist * 255).clip(0, 255).astype(np.uint8)

    # Bottom-right: Sine wave pattern
    x = np.linspace(0, 4 * np.pi, w2)
    y = np.linspace(0, 4 * np.pi, h2)
    xx, yy = np.meshgrid(x, y)
    sine_pattern = ((np.sin(xx) + np.sin(yy)) / 2 + 1) / 2 * 255
    img[h2:, w2:] = sine_pattern.astype(np.uint8)

    return img


# ============================================================
# Image Processing
# ============================================================

def apply_effect_to_image(img, effect_func, **kwargs):
    """
    Apply audio effect to image

    Args:
        img: Input grayscale image (0-255)
        effect_func: Effect function to apply
        **kwargs: Parameters for effect function

    Returns:
        Processed image (0-255)
    """
    # Normalize to [-1, 1]
    img_norm = normalize_image(img.astype(np.float32))

    # Apply effect
    img_processed = effect_func(img_norm, **kwargs)

    # Denormalize back to [0, 255]
    return denormalize_image(img_processed)


# ============================================================
# Visualization
# ============================================================

def plot_transfer_functions():
    """Plot the transfer functions of each effect"""
    x = np.linspace(-1, 1, 1000)

    y_overdrive = overdrive_tanh(x, gain=5.0)
    y_distortion = distortion_hard_clip(x, gain=10.0, threshold=0.7)
    y_fuzz = fuzz_square_wave(x, gain=100.0)
    y_bitcrush = bitcrush_depth(x, n_bits=4)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Overdrive
    axes[0, 0].plot(x, x, 'k--', alpha=0.3, label='Linear (no effect)')
    axes[0, 0].plot(x, y_overdrive, 'b-', linewidth=2, label='Overdrive (tanh, g=5)')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xlabel('Input')
    axes[0, 0].set_ylabel('Output')
    axes[0, 0].set_title('Overdrive Transfer Function\n(Soft Clipping)')
    axes[0, 0].legend()
    axes[0, 0].set_xlim(-1, 1)
    axes[0, 0].set_ylim(-1, 1)

    # Distortion
    axes[0, 1].plot(x, x, 'k--', alpha=0.3, label='Linear')
    axes[0, 1].plot(x, y_distortion, 'r-', linewidth=2, label='Distortion (hard clip, g=10)')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_xlabel('Input')
    axes[0, 1].set_ylabel('Output')
    axes[0, 1].set_title('Distortion Transfer Function\n(Hard Clipping)')
    axes[0, 1].legend()
    axes[0, 1].set_xlim(-1, 1)
    axes[0, 1].set_ylim(-1, 1)

    # Fuzz
    axes[1, 0].plot(x, x, 'k--', alpha=0.3, label='Linear')
    axes[1, 0].plot(x, y_fuzz, 'purple', linewidth=2, label='Fuzz (tanh, g=100)')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_xlabel('Input')
    axes[1, 0].set_ylabel('Output')
    axes[1, 0].set_title('Fuzz Transfer Function\n(Square Wave Clipping)')
    axes[1, 0].legend()
    axes[1, 0].set_xlim(-1, 1)
    axes[1, 0].set_ylim(-1, 1)

    # Bitcrush
    axes[1, 1].plot(x, x, 'k--', alpha=0.3, label='Linear')
    axes[1, 1].plot(x, y_bitcrush, 'orange', linewidth=2, label='Bitcrush (4-bit)')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_xlabel('Input')
    axes[1, 1].set_ylabel('Output')
    axes[1, 1].set_title('Bitcrush Transfer Function\n(4-bit Quantization)')
    axes[1, 1].legend()
    axes[1, 1].set_xlim(-1, 1)
    axes[1, 1].set_ylim(-1, 1)

    plt.tight_layout()
    return fig


def visualize_effects(img, output_path='distortion_effects_visualization.png'):
    """
    Apply all effects and create comprehensive visualization

    Args:
        img: Input grayscale image
        output_path: Where to save the result
    """
    # Apply effects
    img_overdrive = apply_effect_to_image(img, overdrive_tanh, gain=5.0)
    img_distortion = apply_effect_to_image(img, distortion_hard_clip, gain=10.0, threshold=0.7)
    img_fuzz = apply_effect_to_image(img, fuzz_square_wave, gain=100.0)
    img_bitcrush = apply_effect_to_image(img, bitcrush_depth, n_bits=4)

    # Create figure
    fig = plt.figure(figsize=(16, 12))
    gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)

    # Original image (large, top-left)
    ax_original = fig.add_subplot(gs[0, :2])
    ax_original.imshow(img, cmap='gray', vmin=0, vmax=255)
    ax_original.set_title('Original Image (Grayscale Gradient)', fontsize=14, fontweight='bold')
    ax_original.axis('off')

    # Histogram of original
    ax_hist_orig = fig.add_subplot(gs[0, 2])
    ax_hist_orig.hist(img.flatten(), bins=50, color='black', alpha=0.7)
    ax_hist_orig.set_title('Original Histogram')
    ax_hist_orig.set_xlabel('Pixel Value')
    ax_hist_orig.set_ylabel('Count')
    ax_hist_orig.grid(True, alpha=0.3)

    # Overdrive
    ax_od = fig.add_subplot(gs[1, 0])
    ax_od.imshow(img_overdrive, cmap='gray', vmin=0, vmax=255)
    ax_od.set_title('Overdrive (Soft Clipping)\ngain=5.0', fontsize=12, fontweight='bold')
    ax_od.axis('off')

    # Distortion
    ax_dist = fig.add_subplot(gs[1, 1])
    ax_dist.imshow(img_distortion, cmap='gray', vmin=0, vmax=255)
    ax_dist.set_title('Distortion (Hard Clipping)\ngain=10.0, threshold=0.7', fontsize=12, fontweight='bold')
    ax_dist.axis('off')

    # Fuzz
    ax_fuzz = fig.add_subplot(gs[1, 2])
    ax_fuzz.imshow(img_fuzz, cmap='gray', vmin=0, vmax=255)
    ax_fuzz.set_title('Fuzz (Square Wave)\ngain=100.0', fontsize=12, fontweight='bold')
    ax_fuzz.axis('off')

    # Bitcrush
    ax_crush = fig.add_subplot(gs[2, 0])
    ax_crush.imshow(img_bitcrush, cmap='gray', vmin=0, vmax=255)
    ax_crush.set_title('Bitcrush (4-bit)\nQuantization', fontsize=12, fontweight='bold')
    ax_crush.axis('off')

    # Histogram comparison
    ax_hist = fig.add_subplot(gs[2, 1:])
    ax_hist.hist(img_overdrive.flatten(), bins=50, alpha=0.5, label='Overdrive', color='blue')
    ax_hist.hist(img_distortion.flatten(), bins=50, alpha=0.5, label='Distortion', color='red')
    ax_hist.hist(img_fuzz.flatten(), bins=50, alpha=0.5, label='Fuzz', color='purple')
    ax_hist.hist(img_bitcrush.flatten(), bins=50, alpha=0.5, label='Bitcrush', color='orange')
    ax_hist.set_title('Histogram Comparison of All Effects', fontsize=12, fontweight='bold')
    ax_hist.set_xlabel('Pixel Value (0-255)')
    ax_hist.set_ylabel('Count')
    ax_hist.legend()
    ax_hist.grid(True, alpha=0.3)

    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Visualization saved to: {output_path}")

    return fig


def analyze_gradient_response(output_path='gradient_response_analysis.png'):
    """
    Analyze how each effect transforms a simple gradient
    Shows input vs output relationship clearly
    """
    # Create simple horizontal gradient
    gradient = np.linspace(0, 255, 512, dtype=np.uint8)
    img = np.tile(gradient, (128, 1))

    # Apply effects
    img_overdrive = apply_effect_to_image(img, overdrive_tanh, gain=5.0)
    img_distortion = apply_effect_to_image(img, distortion_hard_clip, gain=10.0, threshold=0.7)
    img_fuzz = apply_effect_to_image(img, fuzz_square_wave, gain=100.0)
    img_bitcrush = apply_effect_to_image(img, bitcrush_depth, n_bits=4)

    # Plot
    fig, axes = plt.subplots(5, 2, figsize=(14, 12))

    images = [
        (img, 'Original'),
        (img_overdrive, 'Overdrive (gain=5)'),
        (img_distortion, 'Distortion (gain=10, thresh=0.7)'),
        (img_fuzz, 'Fuzz (gain=100)'),
        (img_bitcrush, 'Bitcrush (4-bit)')
    ]

    for i, (image, title) in enumerate(images):
        # Show image
        axes[i, 0].imshow(image, cmap='gray', vmin=0, vmax=255, aspect='auto')
        axes[i, 0].set_title(title, fontweight='bold')
        axes[i, 0].set_ylabel('Height')
        axes[i, 0].set_xlabel('Input Value (0→255)')

        # Show cross-section (middle row)
        middle_row = image[image.shape[0] // 2, :]
        axes[i, 1].plot(gradient, middle_row, linewidth=2)
        axes[i, 1].plot([0, 255], [0, 255], 'k--', alpha=0.3, label='Linear')
        axes[i, 1].set_xlabel('Input Pixel Value')
        axes[i, 1].set_ylabel('Output Pixel Value')
        axes[i, 1].set_title(f'{title} - Transfer Curve')
        axes[i, 1].grid(True, alpha=0.3)
        axes[i, 1].set_xlim(0, 255)
        axes[i, 1].set_ylim(0, 255)
        axes[i, 1].legend()

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Gradient analysis saved to: {output_path}")

    return fig


# ============================================================
# Main Execution
# ============================================================

def main():
    """Run all demonstrations"""

    print("=" * 60)
    print("Image Distortion Demo: Audio Effects Applied to Images")
    print("=" * 60)
    print()

    # 1. Plot transfer functions
    print("1. Generating transfer function plots...")
    fig_transfer = plot_transfer_functions()
    fig_transfer.savefig('transfer_functions.png', dpi=150, bbox_inches='tight')
    print("   Saved: transfer_functions.png")
    print()

    # 2. Test with horizontal gradient
    print("2. Creating horizontal gradient image...")
    img_horizontal = create_gradient_image(512, 512, direction='horizontal')
    visualize_effects(img_horizontal, 'horizontal_gradient_effects.png')
    print()

    # 3. Test with radial gradient
    print("3. Creating radial gradient image...")
    img_radial = create_gradient_image(512, 512, direction='radial')
    visualize_effects(img_radial, 'radial_gradient_effects.png')
    print()

    # 4. Test with complex pattern
    print("4. Creating test pattern with multiple gradients...")
    img_pattern = create_test_pattern(512, 512)
    visualize_effects(img_pattern, 'test_pattern_effects.png')
    print()

    # 5. Gradient response analysis
    print("5. Analyzing gradient response...")
    analyze_gradient_response('gradient_response_analysis.png')
    print()

    print("=" * 60)
    print("All demonstrations completed!")
    print("=" * 60)
    print()
    print("Generated files:")
    print("  - transfer_functions.png")
    print("  - horizontal_gradient_effects.png")
    print("  - radial_gradient_effects.png")
    print("  - test_pattern_effects.png")
    print("  - gradient_response_analysis.png")
    print()
    print("These images show how audio distortion effects")
    print("transform pixel values, making the math visible!")


if __name__ == "__main__":
    main()
