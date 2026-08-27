---
name: Academic Precision
colors:
  surface: '#e9fef3'
  surface-dim: '#cadfd4'
  surface-bright: '#e9fef3'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#e3f9ed'
  surface-container: '#def3e7'
  surface-container-high: '#d8ede2'
  surface-container-highest: '#d2e7dc'
  on-surface: '#0d1f18'
  on-surface-variant: '#414944'
  inverse-surface: '#22342d'
  inverse-on-surface: '#e0f6ea'
  outline: '#717973'
  outline-variant: '#c0c9c2'
  surface-tint: '#3a6753'
  primary: '#023625'
  on-primary: '#ffffff'
  primary-container: '#1f4d3a'
  on-primary-container: '#8dbda4'
  inverse-primary: '#a1d1b8'
  secondary: '#625e51'
  on-secondary: '#ffffff'
  secondary-container: '#e6dfcf'
  on-secondary-container: '#676255'
  tertiary: '#5d1200'
  on-tertiary: '#ffffff'
  tertiary-container: '#812307'
  on-tertiary-container: '#ff967a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bceed3'
  primary-fixed-dim: '#a1d1b8'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#214f3c'
  secondary-fixed: '#e9e2d2'
  secondary-fixed-dim: '#ccc6b6'
  on-secondary-fixed: '#1e1c12'
  on-secondary-fixed-variant: '#4a473b'
  tertiary-fixed: '#ffdbd1'
  tertiary-fixed-dim: '#ffb5a1'
  on-tertiary-fixed: '#3b0800'
  on-tertiary-fixed-variant: '#842509'
  background: '#e9fef3'
  on-background: '#0d1f18'
  surface-variant: '#d2e7dc'
typography:
  display-lg:
    fontFamily: Fraunces
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Fraunces
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-sm:
    fontFamily: Fraunces
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-sm-mobile:
    fontFamily: Fraunces
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: IBM Plex Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: IBM Plex Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: IBM Plex Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-mono:
    fontFamily: IBM Plex Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  status-mono:
    fontFamily: IBM Plex Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  rail-width: 320px
  pipeline-height: 80px
  gutter: 24px
  margin-page: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
---

## Brand & Style

This design system is built for a high-stakes, operations-focused environment where clarity, authority, and efficiency are paramount. The brand personality is academic yet modern—balancing the weight of traditional institutional history with the precision of a high-performance operating system.

The visual style is **Modern-Institutional**. It eschews decorative trends like gradients or glassmorphism in favor of structural integrity and high contrast. The aesthetic relies on crisp lines, archival-inspired color palettes, and a sophisticated typographic hierarchy to create a sense of focused intelligence.

**Core Principles:**
- **Calculated Restraint:** Use white space and hairlines to separate concerns rather than heavy shadows or fills.
- **Academic Authority:** Leverage serif typography for data points that carry weight, such as admission scores and institution names.
- **Operational Efficiency:** Use monospaced fonts for system statuses to evoke a sense of real-time processing and technical reliability.

## Colors

The palette is rooted in a "Scholar’s Cream" base, providing a warmer, more legible alternative to stark white for long-form data review. 

- **Primary (Forest Green):** Used for primary actions, success states, and indicating "active" pipeline steps.
- **Neutral (Deep Forest Ink):** The primary text color, ensuring maximum contrast against the cream background.
- **Secondary (Warm Gray):** Reserved for metadata, helper text, and inactive navigation states.
- **Warning (Terracotta-Rust):** A sophisticated, non-fluorescent red used for critical alerts, rejection statuses, or missing requirements.
- **Surface & Border:** Surfaces use pure white sparingly to elevate specific data cards above the cream canvas. Borders are kept to "hairline" weights (1px) using a muted clay tone to define structure without adding visual bulk.

## Typography

The typography system utilizes a tri-font strategy to differentiate between narrative, interface, and technical data.

1.  **Fraunces (Display):** Used for "high-value" data. This includes candidate names, admission scores (e.g., 1580 SAT), and large section headers. It brings a bespoke, editorial feel to the dashboard.
2.  **IBM Plex Sans (UI):** The workhorse for all interface labels, body copy, and input fields. It provides a neutral, highly legible foundation for complex operations.
3.  **IBM Plex Mono (System):** Used for timestamps, status tags, IDs, and tabular data values. This font signals "data-integrity" and makes vertical alignment in lists easier to scan.

## Layout & Spacing

The layout follows a highly structured, multi-pane approach designed for desktop-first operational workflows.

- **Fixed Left Rail:** A 320px sidebar that houses the primary candidate profile or input controls. It remains stationary to provide constant context.
- **Scrollable Center Grid:** A fluid area using a 12-column grid system for college cards and data visualizations. 
- **Docked "Railway" Pipeline:** A persistent horizontal strip at the bottom of the viewport. This tracks the admission journey chronologically from left to right.
- **Spacing Rhythm:** Use a 4px baseline grid. Standard component spacing is set at 16px (md), while high-density data views may drop to 8px (sm) to maximize information density without sacrificing legibility.

## Elevation & Depth

This system avoids shadows to maintain a "printed" aesthetic. Depth is communicated through color-blocking and borders.

- **Level 0 (Background):** The Cream (#F6F3EC) canvas.
- **Level 1 (Cards/Panels):** Pure White (#FFFFFF) surfaces with 1px Hairline Borders (#DCD6C7). Used for the main college grid items to make them pop against the cream.
- **Level 2 (Inlay):** Recessed areas within panels use a slightly darker tint of the background to indicate nested information or secondary groupings.
- **Dividers:** 1px solid lines are the primary tool for visual separation. No soft blurs or glows should be used.

## Shapes

The shape language is primarily **Sharp**. Architectural rigidity is used to reinforce the "OS" feel.

- **Standard UI Elements:** Buttons, input fields, and tags use 0px (sharp) corners.
- **Containers:** Only major data cards and the persistent rails may use a subtle Soft (0.25rem) radius to prevent the UI from feeling overly aggressive.
- **Interactive Elements:** Use 1px stroke borders for all interactive states rather than changing surface elevation.

## Components

- **Buttons:** Sharp corners. Primary buttons use Forest Green with Cream text. Secondary buttons use a Hairline border with Deep Forest Ink text. No icons in buttons unless strictly functional (e.g., "+" for add).
- **Status Chips:** Use IBM Plex Mono. Backgrounds are muted tints of the status color (e.g., pale rust for warning) with high-contrast text. No rounded ends; use sharp or slightly softened corners.
- **Input Fields:** Bottom-border only or full-framed with 1px #DCD6C7. Use IBM Plex Sans for input text. Labels should use the Mono font in uppercase for a "form-entry" feel.
- **College Cards:** White background, 1px border. The header of the card should feature the institution name in Fraunces. Data points within the card should be aligned to a strict internal grid.
- **The Railway (Pipeline):** A series of connected segments in the docked bottom bar. Active stages are filled with Forest Green; upcoming stages are outlined; completed stages use a checkmark icon with a muted gray fill.
- **Data Tables:** No vertical lines. Horizontal lines only in #DCD6C7. Alternate row striping is permitted using a very faint cream tint.